#!/usr/bin/env sh

## LIBHUNT:: awesome-cli-app:: awesome-tui(s)::
## REDDIT:: r/commandline r/tui - I wrapped G'MIC's 600+ filters in a terminal spreadsheet because the CLI syntax was killing me - G'MIC is genuinely one of the most powerful open-source image processing tools out there. It's also, frankly, a pain to use raw — the CLI syntax is dense, the GIMP plugin is clunky, and most people bounce off it before discovering what it can actually do. filterx-tui puts a spreadsheet-driven TUI in front of it. Browse filters, tweak parameters inline, chain effects, iterate. No flags to memorize, no GUI, no cloud, no subscription. Runs entirely in the terminal via Textual (Python). Built it as a side project after using G'MIC in a SaaS context and realizing the friction wasn't the tool — it was the interface. This is the interface it deserved. WIP but functional. GPL-3, AUR package available, Homebrew tap in progress.
## HACKERNEWS:: filterx-tui – spreadsheet-driven G'MIC filter interface for the terminal - G'MIC has ~600 image filters, rivals commercial tools in raw capability, and almost nobody uses it — because the CLI syntax is arcane and the GIMP plugin is a UX dead end. filterx-tui wraps it in a terminal-native spreadsheet interface. You navigate filters, tweak parameters inline, chain effects — no memorized flags, no GUI, no cloud, no subscription tier that unlocks the good stuff. The interface is intentionally boring: a TUI table. The interesting part is what's underneath.
## TERMINALTROVE:: A terminal interface for G'MIC, browsing and chaining 600+ image filters via a spreadsheet view. - 600+ image filters, no GUI — a spreadsheet-driven front end for G'MIC. - filterx-tui wraps G'MIC's extensive filter library in a terminal-native, spreadsheet-driven interface built with Textual. Browse filters, tweak parameters inline, and chain effects without memorizing G'MIC's CLI syntax or fighting the GIMP plugin. No GUI overhead, no cloud, no subscription — just a structured terminal view over one of the most powerful open-source image processing engines available.
## PRODUCTHUNT:: filterx-tui — A terminal interface for G'MIC's creative filter library - 600+ image filters. No app. No cloud. Just your terminal. - filterx-tui brings G'MIC's massive image filter library into a navigable, spreadsheet-driven terminal interface — so you can explore, tweak, and chain effects without memorizing a single flag. G'MIC is the image processing engine that quietly powers serious creative work across photography, generative art, and print. filterx-tui makes it approachable: browse filters, adjust parameters inline, see what sticks. What you get: * 600+ G'MIC filters, navigable from the terminal * Spreadsheet interface — no learning curve, just explore * Chain effects, tweak parameters, iterate fast * No subscription, no account, no GUI overhead * Works on any Unix system, same experience everywhere * If Lightroom's pricing frustrates you, or you've tried G'MIC and bounced off the CLI — this is the middle ground that's been missing.
## GITHUB:: filterx-tui is a terminal-native creative filter engine wrapping G'MIC's extensive library of image effects into a comfortable spreadsheet-driven interface. Think of it as an effects rack for images, operated entirely from the terminal – a creative filter machine with no GUI overhead, no cloud dependency, no subscription. The motivation was equally simple: G'MIC is one of the most powerful and underappreciated image processing tools in existence, yet its full potential remains largely inaccessible to anyone unwilling to memorize its command syntax or navigate its GIMP plugin interface. filterx-tui bridges that gap, exposing G'MIC's creative filter library through a structured, navigable interface that rewards exploration without demanding expertise. It is the sibling project of artwork-tui, operating under the same GitHub umbrella and complementing it naturally: where artwork-tui generates, filterx-tui processes.

# GITHUB:: Fully customizable, creative filter fx environment for images, operated from the terminal, spreadsheet based.
# GITHUB:: filterx-tui – terminal-based creative filter engine wrapping G'MIC effects in a spreadsheet-driven interface
# GITHUB:: darkroom-tui – non-destructive creative filter environment for images, operated from the terminal
# GITHUB:: tui-fx – A dawless-inspired creative filter machine for images, built on G'MIC and the terminal
# GITHUB:: gmic-rack – A modular effects rack for images, operated entirely from the terminal
# GITHUB:: filterpress – Batch creative image processing via a terminal spreadsheet interface
# GITHUB:: gmic-sheet – Spreadsheet-driven G'MIC filter sequencer for the terminal
# GITHUB:: cellfx – Cell-driven creative image filter sequencer powered by G'MIC
# GITHUB:: grainfield – Terminal-native creative image processing via G'MIC
# GITHUB:: patina – A terminal image processing workbench powered by G'MIC

# apngasm -o output.png frame/*.png -d 2000
# apngasm -o output.png frame/*.png -d 1600
# apngasm -o output.png frame/*.png -d 1300
# apngasm -o output.png frame/*.png 1.3 1
# apngasm -o output.png frame/*.png 1.6 1
# apngasm -o output.png frame/*.png 2 1


OUTPUT_DIRS="$HOME/screenshots"
mkdir -p "$OUTPUT_DIRS"
INTERVAL=2
i=0

while true; do
    grim "$OUTPUT_DIRS/frame_$(printf '%04d' $i).png"
    i=$((i+1))
    sleep "$INTERVAL"
done
