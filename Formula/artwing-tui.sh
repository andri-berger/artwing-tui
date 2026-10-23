#!/usr/bin/env sh
# artwing-tui.sh — run from the artwing-tui repo root after tag+push
# usage: sh Formula/artwing-tui.sh [vX.Y.Z]
#
# updates all three distribution paths to the tag:
#   install.sh (curl), Formula/artwing-tui.rb (brew tap), PKGBUILD (AUR)

# linuxbrew setup (only needed for the optional brew steps below)
# NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv zsh)"' >> ~/.zshrc
set -eu

FORMULA="Formula/artwing-tui.rb"
DEV_TAP="andri-berger/dev"

# 0. tag: explicit argument wins; otherwise newest version tag (NOT git describe)
TAG=${1:-$(git tag --list 'v*' --sort=-version:refname | head -n 1)}
[ -n "$TAG" ] || { echo "no version tag found" >&2; exit 1; }
VERSION=${TAG#v}

# the tag must carry the same version as pyproject.toml
TAGGED=$(git show "${TAG}:pyproject.toml" | sed -n 's/^version = "\(.*\)"/\1/p')
[ "$TAGGED" = "$VERSION" ] || {
    echo "pyproject.toml in ${TAG} says ${TAGGED}, expected ${VERSION}" >&2; exit 1; }

# 1. sha of the tag tarball — -f makes a 404 (tag not pushed) abort instead of hashing an error page
SHA=$(curl -fsL "https://github.com/andri-berger/artwing-tui/archive/refs/tags/${TAG}.tar.gz" \
      | sha256sum | cut -d' ' -f1)
[ "$SHA" != "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" ] || {
    echo "empty download, is ${TAG} pushed?" >&2; exit 1; }

# 2. curl installer
sed -i "s|^REF=\"v[0-9.]*\"|REF=\"${TAG}\"|" install.sh
grep -q "^REF=\"${TAG}\"" install.sh || { echo "install.sh ref not updated" >&2; exit 1; }

# 3. brew formula: only the sha256 right below the main url, not the resources
sed -i \
    -e "s|archive/refs/tags/v[0-9.]*\.tar\.gz|archive/refs/tags/${TAG}.tar.gz|" \
    -e "/archive\/refs\/tags\//{n;s/sha256 \"[a-f0-9]*\"/sha256 \"${SHA}\"/;}" \
    "$FORMULA"
grep -q "sha256 \"${SHA}\"" "$FORMULA" || { echo "formula sha not updated" >&2; exit 1; }

# 4. AUR
sed -i \
    -e "s/^pkgver=.*/pkgver=${VERSION}/" \
    -e "s/^pkgrel=.*/pkgrel=1/" \
    -e "s/^sha256sums=.*/sha256sums=('${SHA}')/" \
    PKGBUILD
if command -v makepkg >/dev/null 2>&1; then
    makepkg --printsrcinfo > .SRCINFO
else
    echo "makepkg not found, regenerate .SRCINFO on Arch: makepkg --printsrcinfo > .SRCINFO"
fi

# 5. optional brew checks (linuxbrew is enough, no Mac needed)
if command -v brew >/dev/null 2>&1; then
    DEV_TAP_DIR="$(brew --repository)/Library/Taps/andri-berger/homebrew-dev"
    brew tap | grep -qx "$DEV_TAP" || brew tap-new "$DEV_TAP"
    [ -e "$DEV_TAP_DIR/Formula/artwing-tui.rb" ] || \
        ln -s "$PWD/$FORMULA" "$DEV_TAP_DIR/Formula/artwing-tui.rb"
    [ -L "$DEV_TAP_DIR/Formula/artwing-tui.rb" ] || {
        echo "tap copy is a real file, not a symlink — two truths!" >&2; exit 1; }
    brew update-python-resources --exclude-packages pillow artwing-tui
else
    echo "brew not found, skipped resource refresh (resources mirror uv.lock)"
fi

# 6. review gate
git diff --stat install.sh "$FORMULA" PKGBUILD
echo "review with: git diff — then commit & push"
