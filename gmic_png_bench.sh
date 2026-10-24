#!/bin/bash
# Temporary: is gmic's png writer the bottleneck here too?
# usage: bash gmic_png_bench.sh [image]   (default: a 12 MP test image)
# Delete this file after the run, it is not part of the app.
D=$(mktemp -d); trap 'rm -rf "$D"' EXIT
IMG=${1:-$D/in.png}
[ -f "$IMG" ] || gmic 4000,3000,1,3 noise 60 plasma 1 blur 1 -o "$IMG" >/dev/null 2>&1
V=$(gmic -version 2>&1 | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+' | head -1)
echo "gmic $V"
# gmic 3 renamed uchar to uint8
T=uint8; [ "${V%%.*}" -lt 3 ] && T=uchar
TIMEFORMAT='%Rs'
echo -n "png (before): "; time gmic "$IMG" -keep[0] -o "$D/out.png" >/dev/null 2>&1
echo -n "tif ($T):   "; time gmic "$IMG" -keep[0] -o "$D/out.tif,$T,none" >"$D/err" 2>&1
grep -a '\*\*\*' "$D/err" | sed 's/\x1b\[[0-9;]*m//g'
python3 - "$D/out.tif" <<'PY' 2>&1 || true
import sys
try:
    from PIL import Image
    im = Image.open(sys.argv[1]); im.load()
    print("tif readable:", im.mode, im.size)
except ImportError:
    import os
    if os.path.exists(sys.argv[1]):
        print("tif written:", os.path.getsize(sys.argv[1]), "bytes")
    else:
        print("tif NOT written")
except Exception as e:
    print("tif NOT readable:", e)
PY
