# README demos

Animated PNGs of artwing-tui, one feature each, recorded headless from the
real app with real G'MIC. Regenerate after UI changes with
`tool/make.sh` (all) or `make.sh demos/03_effect_tour.py` (one).

How it works: `tool/record.py` drives the app through Textual's pilot in a
throw-away XDG state and saves an SVG screenshot per step
(`snap(hold, caption)`); `tool/render.py` paints the real preview image where
a kitty/sixel terminal shows it (headless textual-image only draws half
cells), renders the frames in headless Chromium and writes one APNG:
1000 px wide, one shared 256-colour palette, identical frames merged, each
frame held as long as its step needs.

A new demo is a short script in `tool/demos`: `setup(s)` prepares the saved
session and files, `run(r)` presses keys and snaps frames.

Every demo uses the company image: `tool/samples.sh` turns `qproject.png`
from the repo root into the same picture as bmp, jpg, png, tif and webp
(1600 px, so gmic stays fast), so steps that pick another file still have
one to pick. Nothing is downloaded, and every run gives the same frames
(apart from effects that use randomness, such as warhol's colours).
