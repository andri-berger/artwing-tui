#!/usr/bin/env sh
# artwing-tui.sh — run from the artwing-tui repo root after tag+push

# sudo chown -R admin /opt/brew
# sudo rm -rf /opt/brew
#NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"   # replace the /opt/brew line in your rc
#echo >> /home/admin/.zshrc
#echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv zsh)"' >> /home/admin/.zshrc
#eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv zsh)"
set -e

FORMULA="Formula/artwing-tui.rb"
DEV_TAP="andri-berger/dev"
DEV_TAP_DIR="$(brew --repository)/Library/Taps/andri-berger/homebrew-dev"

# 00 AUR Preparation
# updpkgsums && makepkg --printsrcinfo > .SRCINFO

# 0. tag: explicit argument wins; otherwise newest version tag (NOT git describe)
TAG=${1:-$(git tag --list 'v*' --sort=-version:refname | head -1)}
[ -n "$TAG" ] || { echo "no version tag found" >&2; exit 1; }

sed -i "s|\.git@v[0-9.]*|.git@${TAG}|" install.sh
grep -q "@${TAG}" install.sh || { echo "install.sh ref not updated" >&2; exit 1; }
# 1. url + sha derived from the tag — -f makes a 404 abort instead of hashing an error page
SHA=$(curl -fsL "https://github.com/andri-berger/artwing-tui/archive/${TAG}.tar.gz" \
      | sha256sum | cut -d' ' -f1)
sed -i "s|archive/v[0-9.]*\.tar\.gz|archive/${TAG}.tar.gz|" "$FORMULA"
sed -i "s/^\(\s*sha256 \)\"[a-f0-9]*\"/\1\"${SHA}\"/" "$FORMULA"

# 2. scratch-tap dev harness (idempotent)
brew tap | grep -qx "$DEV_TAP" || brew tap-new "$DEV_TAP"
[ -e "$DEV_TAP_DIR/Formula/artwing-tui.rb" ] || \
    ln -s "$PWD/$FORMULA" "$DEV_TAP_DIR/Formula/artwing-tui.rb"
[ -L "$DEV_TAP_DIR/Formula/artwing-tui.rb" ] || {
    echo "tap copy is a real file, not a symlink — two truths!" >&2; exit 1; }

# 3. regenerate resources
brew update-python-resources --exclude-packages pillow artwing-tui

# 4. review gate
git diff --stat "$FORMULA"
echo "review with: git diff Formula/ — then commit & push"
