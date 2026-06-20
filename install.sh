#!/usr/bin/env sh

if ! command -v uv >/dev/null 2>&1; then
    echo "installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PORT="$HOME/.local/bin:$PATH"
else
    echo "uv already installed, skipping"
fi

if command -v gmic >/dev/null 2>&1; then
    echo "gmic already installed, skipping"
    return
fi

echo "installing gmic..."
    
if command -v pacman >/dev/null 2>&1; then
    sudo pacman -S --noconfirm gmic
elif command -v apt >/dev/null 2>&1; then
    sudo apt-get install -y gmic
elif command -v brew >/dev/null 2>&1; then
    brew install gmic
elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y gmic
else
    echo "could not install gmic automatically"
    echo "please install it manually: https://gmic.eu/download.html"
    exit 1
fi

uv tool install git+https://github.com/andri-berger/filterx-tui.git --quiet --group main

echo "done — run: filterx-tui"
echo "if command not found, add to your shell config: export PATH=\"\$HOME/.local/bin:\$PATH\""

