#!/usr/bin/env sh
# release.sh — run from the artwing-tui repo root after tag+push
# usage: sh release.sh [vX.Y.Z]
#
# points the curl installer (install.sh) at the tag
set -eu

# 0. tag: explicit argument wins; otherwise newest version tag (NOT git describe)
TAG=${1:-$(git tag --list 'v*' --sort=-version:refname | head -n 1)}
[ -n "$TAG" ] || { echo "no version tag found" >&2; exit 1; }
VERSION=${TAG#v}

# the tag must carry the same version as pyproject.toml
TAGGED=$(git show "${TAG}:pyproject.toml" | sed -n 's/^version = "\(.*\)"/\1/p')
[ "$TAGGED" = "$VERSION" ] || {
    echo "pyproject.toml in ${TAG} says ${TAGGED}, expected ${VERSION}" >&2; exit 1; }

# 1. the tag tarball must be downloadable, otherwise install.sh would point at a 404
curl -fsIL "https://github.com/andri-berger/artwing-tui/archive/refs/tags/${TAG}.tar.gz" \
    >/dev/null || { echo "${TAG} tarball not found, is the tag pushed?" >&2; exit 1; }

# 2. curl installer
sed -i "s|^REF=\"v[0-9.]*\"|REF=\"${TAG}\"|" install.sh
grep -q "^REF=\"${TAG}\"" install.sh || { echo "install.sh ref not updated" >&2; exit 1; }

# 3. review gate
git diff --stat install.sh
echo "review with: git diff install.sh — then commit & push"
