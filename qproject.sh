#!/usr/bin/env sh

# filterx-tui is a terminal-native creative filter engine wrapping G'MIC's extensive library of image effects into a comfortable spreadsheet-driven interface. Think of it as an effects rack for images, operated entirely from the terminal – a creative filter machine with no GUI overhead, no cloud dependency, no subscription. The motivation was equally simple: G'MIC is one of the most powerful and underappreciated image processing tools in existence, yet its full potential remains largely inaccessible to anyone unwilling to memorize its command syntax or navigate its GIMP plugin interface. filterx-tui bridges that gap, exposing G'MIC's creative filter library through a structured, navigable interface that rewards exploration without demanding expertise. It is the sibling project of artwork-tui, operating under the same GitHub umbrella and complementing it naturally: where artwork-tui generates, filterx-tui processes.

# filterx-tui – A terminal-based creative filter engine wrapping G'MIC effects in a spreadsheet-driven interface
# gmic-sheet – Spreadsheet-driven G'MIC filter sequencer for the terminal
# tui-fx – A dawless-inspired creative filter machine for images, built on G'MIC and the terminal

# patina – A terminal image processing workbench powered by G'MIC
# darkroom-tui – A non-destructive creative filter environment for images, operated from the terminal
# grainfield – Terminal-native creative image processing via G'MIC

# gmic-rack – A modular effects rack for images, operated entirely from the terminal
# cellfx – Cell-driven creative image filter sequencer powered by G'MIC
# filterpress – Batch creative image processing via a terminal spreadsheet interface

# apngasm output.apng frame1.png frame2.png frame3.png -d 100  # 100ms per frame
# apngasm output.apng frame1.png 1/2 frame2.png 1/4 frame3.png 1/1
# apngasm output.apng frames/*.png -d 10  # 10ms per frame
# apngasm output.apng frame*.png 1 10

INTERVAL=2
OUTPUT_DIR="$HOME/screenshots"
mkdir -p "$OUTPUT_DIR"

i=0
while true; do
    grim "$OUTPUT_DIR/frame_$(printf '%04d' $i).png"
    i=$((i+1))
    sleep "$INTERVAL"
done

