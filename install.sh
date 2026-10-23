#!/usr/bin/env sh
# artwing-tui installer: uv + G'MIC + artwing-tui (isolated uv tool env)
# usage: curl -fsSL https://raw.githubusercontent.com/andri-berger/artwing-tui/main/install.sh | sh
set -eu

# REF is rewritten by release.sh on every release
REF="v0.1.1"
URL="https://github.com/andri-berger/artwing-tui/archive/refs/tags/${REF}.tar.gz"

say() { printf '%s\n' "$*"; }
die() { printf 'error: %s\n' "$*" >&2; exit 1; }
has() { command -v "$1" >/dev/null 2>&1; }

if [ "$(id -u)" -eq 0 ]; then
    SUDO=""
elif has sudo; then
    SUDO="sudo"
else
    SUDO=""
fi

has curl || die "curl is required"

# 1. uv (brings its own Python 3.14 if the system has none)
export PATH="$HOME/.local/bin:$PATH"
if has uv; then
    say "uv already installed, skipping"
else
    say "installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    has uv || die "uv installation failed, see https://docs.astral.sh/uv/"
fi

# 2. G'MIC
if has gmic; then
    say "gmic already installed, skipping"
elif has pacman; then
    $SUDO pacman -S --needed --noconfirm gmic
elif has apt-get; then
    $SUDO apt-get update
    $SUDO apt-get install -y gmic
elif has dnf; then
    $SUDO dnf install -y gmic
elif has zypper; then
    $SUDO zypper --non-interactive install gmic
elif has brew; then
    brew install gmic
else
    die "could not install gmic automatically, please install it manually: https://gmic.eu/download.html"
fi
has gmic || die "gmic installation failed, please install it manually: https://gmic.eu/download.html"

# several filters need G'MIC 3.x (Debian/Ubuntu still ship 2.9)
GMIC_VERSION=$(gmic -version 2>&1 | sed 's/\x1b\[[0-9;]*m//g' \
    | grep -o '[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*' | head -n 1 || true)
case "$GMIC_VERSION" in
    "" | [3-9].* | [1-9][0-9]*.*) ;;
    *)
        say "warning: gmic $GMIC_VERSION found, some filters need gmic 3.x"
        say "         newer builds: https://gmic.eu/download.html"
        ;;
esac

# 3. artwing-tui
say "installing artwing-tui ${REF}..."
uv tool install --force --python ">=3.14" "artwing-tui @ ${URL}" --quiet

if has artwing-tui; then
    say "done, run: artwing-tui"
else
    say "done, but artwing-tui is not on your PATH yet"
    say "add to your shell config: export PATH=\"\$HOME/.local/bin:\$PATH\""
fi
