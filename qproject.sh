#!/usr/bin/env sh

# Descriptive / functional:
# filterx-tui – A terminal-based creative filter engine wrapping G'MIC effects in a spreadsheet-driven interface
# gmic-sheet – Spreadsheet-driven G'MIC filter sequencer for the terminal
# tui-fx – A dawless-inspired creative filter machine for images, built on G'MIC and the terminal

# More conceptual / evocative:
# patina – A terminal image processing workbench powered by G'MIC
# darkroom-tui – A non-destructive creative filter environment for images, operated from the terminal
# grainfield – Terminal-native creative image processing via G'MIC

# Leaning into the novelty:
# gmic-rack – A modular effects rack for images, operated entirely from the terminal
# cellfx – Cell-driven creative image filter sequencer powered by G'MIC
# filterpress – Batch creative image processing via a terminal spreadsheet interface


INTERVAL=2
OUTPUT_DIR="$HOME/screenshots"
mkdir -p "$OUTPUT_DIR"

i=0
while true; do
    hyprshot -m output -f "$OUTPUT_DIR/frame_$(printf '%04d' $i).png"
    i=$((i+1))
    sleep "$INTERVAL"
done

# Then stitch into APNG with ffmpeg:
ffmpeg -framerate 0.5 -i "$OUTPUT_DIR/frame_%04d.png" -plays 0 output.apng

# Or if you prefer GIF:
ffmpeg -framerate 0.5 -i "$OUTPUT_DIR/frame_%04d.png" output.gif


