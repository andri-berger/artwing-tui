# <img src="readme.png" width="50" valign="middle" alt="logo"> Artwing-TUI
Artwork-TUI is a terminal-native creative filter engine wrapping G'MIC's extensive library of image effects into a comfortable spreadsheet-driven interface. Think of it as an effects rack for images, operated entirely from the terminal – a creative filter machine with no GUI overhead, no cloud dependency, no subscription. 

The motivation was equally simple: G'MIC is one of the most powerful and underappreciated image processing tools in existence, yet its full potential remains largely inaccessible to anyone unwilling to memorize its command syntax or navigate its GIMP plugin interface. artwing-tui bridges that gap, exposing G'MIC's creative filter library through a structured, navigable interface that rewards exploration without demanding expertise. It is the sibling project of artwork-tui, operating under the same GitHub umbrella and complementing it naturally: where artwork-tui generates, artwing-tui processes.

[Installation](#installation) / 
[Configuration](#configuration) / 
[API Reference](#reference) / 
[API Credit](#credit) / 
[Gallery](#gallery)


<img src="artwing/Backend/modules/710000000.png" width="100%">
<table>
  </tr>
    <tr>
        <td><a href="artwing/Backend/modules/710000000.png">
        <img src="artwing/Backend/modules/710000000.png"></a></td>
        <td><a href="artwing/Backend/modules/710000001.png">
        <img src="artwing/Backend/modules/710000001.png"></a></td>
        <td><a href="artwing/Backend/modules/710000001.png">
        <img src="artwing/Backend/modules/710000001.png"></a></td>
        <td><a href="artwing/Backend/modules/710000002.png">
        <img src="artwing/Backend/modules/710000002.png"></a></td>
        <td><a href="artwing/Backend/modules/710000002.png">
        <img src="artwing/Backend/modules/710000002.png"></a></td>
    </tr>
  </tr>
</table>


## Installation
Artwing-TUI has no Electron, no npm, no 200 MB runtime surprise — just a Python TUI and G'MIC under the hood. Pick whichever method matches your setup below.

### Generic Install (Native)
Pulls the install script directly from the repo and wires everything up.
Requires Python 3.11+ and G'MIC to be present on your system. The script uses
uv under the hood, so installation lands in an isolated environment and never
touches your system Python. If piping curl into sh makes you twitch — good
instinct — read the script first; it is short and does exactly what it says.

```bash
curl -fsSL https://raw.githubusercontent.com/\
andri-berger/artwing-tui/main/install.sh | sh
```

### macOS (Homebrew)
Tap the formula and let Homebrew handle dependencies. G'MIC gets pulled in
automatically via the formula's dependency spec. First install may take a
moment while G'MIC builds its filter collection — subsequent updates via
`brew upgrade` are quick. Additional, user-generated files are stored in the following directory => ~/Library/Application Support/artwing-tui

```bash
brew tap andri-berger/artwing-tui \
https://github.com/andri-berger/artwing-tui
brew install artwing-tui #install from tap
```

### Arch Linux (AUR)
Use your AUR helper of choice — the PKGBUILD handles the rest, including the
G'MIC dependency. If you prefer doing it by hand, `git clone` the AUR repo
and run `makepkg -si`; there is nothing exotic in the build. You run Arch,
so you knew that already. Additional, user-generated files are stored in the following directories => ~/.local/share/artwing-tui and ~/.local/state/artwing-tui

```bash
yay -S artwing-tui 
# paru -S artwing-tui
```

## Configuration
The interface is built from a small set of panels and buttons, each described
below. Most buttons have a function-key twin from the API Reference above —
pressing F8, for instance, does nothing more than programmatically press the
Create button, so the two tables describe one surface from two angles: the
keybindings are the fast path, the buttons the discoverable one. Screenshots
in the Docs column show each element in context.

A note on terminal support: the app renders image previews inline, which
requires a terminal implementing a graphics protocol — hence the current list
of kitty, ghostty, and wezterm. On anything else the TUI itself will run, but
you would be filtering images blind, which defeats the purpose.

The three file trees on the left feed the pipeline, the FX rack in the center
is where the actual work happens, and the button row drives generation and
export. A typical session reads left to right: pick a base image, stack and
tune filters, generate, export.

```bash
artwing-tui #Launches the TUI
# kitty, ghostty, wezterm are currently supported
```

<table>
    <tr>
        <th width="20">Docs</th>
        <th align="left">Element</th>
        <th align="left">Description</th>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Global Filetree</kbd></td>
        <td>Choose either png (for the base image) or json (for your project-files). Mirror of your unrestricted / full filesystem, hence the name global. </td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Local Filetree</kbd></td>
        <td>Choose either png (for the base image) or json (for your project-files). Local Filesystem only hosting all files copied over via Button Create (see below), hence the name local. </td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>FX Filetree</kbd></td>
        <td>Browse the catalogue of available filter effects. Selecting an entry loads
it into the Grid FX Rack, where its parameters become editable.</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Grid FX Rack</kbd></td>
        <td>The heart of the app — a spreadsheet-style grid where selected effects are
stacked like modules in a rack. Each row holds one effect with its parameters
as editable cells; the stack is applied to the base image in order.</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Button X</kbd></td>
        <td>Clear currently active/selected FX Parameters. Resets the grid to a blank state so you can start a new composition — exported files on disk are not touched.</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Button Afs</kbd></td>
        <td>Set previous Theme (there are 19 Themes in total to choose from).</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Button Bfs</kbd></td>
        <td>Set next Theme (there are 19 Themes in total to choose from).</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Button Cfs</kbd></td>
        <td>Copy/Export existing file to the local file directory, that can be used as base for further FX processing.</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Button Create</kbd></td>
        <td>The heart of the app — a spreadsheet-style grid where selected effects are
stacked like modules in a rack. Each row holds one effect with its parameters
as editable cells; the stack is applied to the base image in order.</td>
    </tr>
    <tr>
        <td><a href="artwing/Backend/modules/700000038.png">
        <img src="artwing/Backend/modules/1700000038.png"></a></td>
        <td><kbd>Button Export</kbd></td>
        <td>Export both generated (png) and project file (json) into the directory from where the app was executed / started.</td>
    </tr>
</table>


## API Reference
The entire application is driven from the keyboard — there is no mouse layer,
and that is a feature, not a gap. The function keys F1 through F9 form the
actual API surface of the app: clipboard operations, seed control, generation,
and export. What makes them worth learning is that they behave consistently
across contexts — F1/F2/F3 work the same whether you are copying a cell inside
the grid or moving a png/json file between the directory trees, so the muscle
memory you build in one panel carries over to the other.

The remaining bindings follow the conventions you already know from any
terminal application: Tab cycles focus, arrow keys move through the grid,
Del clears, Ctrl-Q leaves. A deliberate design choice runs through all of it —
every action is deterministic and inspectable. Seeds (F5–F7) pin down the
random generator per element group, so an artwork you like is never a happy
accident you cannot reproduce; the exported json (F9) is the full recipe,
the png merely its rendering.

<table>
    <tr>
        <td><kbd>
        F1</kbd></td>
        <td>Copy</td>
        <td>Copy table cell, also applies to the first 2 directories, you can copy png/json files therein without leaving the app. Think of it as Ctrl-C in setting outside of TUI. </td>
    </tr>
    <tr>
        <td><kbd>
        F2</kbd></td>
        <td>Cut</td>
        <td>Cut table cell, also applies to the first 2 file directories, you can cut png/json files without leaving the app. Think of it as Ctrl-X in setting outside of TUI. </td>
    </tr>
    <tr>
        <td><kbd>
        F3</kbd></td>
        <td>Paste</td>
        <td>Paste table cell, also applies to first 2 file directories, you can paste png/json files without leaving the app. Think of it as Ctrl-V in setting outside of TUI. </td>
    </tr>
    <tr>
        <td><kbd>
        F4</kbd></td>
        <td>Clear</td>
        <td>Clear currently active/selected FX Parameters. Resets the grid to a blank state so you can start a new composition — exported files on disk are not touched.</td>
    </tr>
    <tr>
        <td><kbd>
        F5</kbd></td>
        <td>Afs</td>
        <td>Set previous Theme (there are 19 Themes in total to choose from).</td>
    </tr>
    <tr>
        <td><kbd>
        F6</kbd></td>
        <td>Bfs</td>
        <td>Set next Theme (there are 19 Themes in total to choose from).</td>
    </tr>
    <tr>
        <td><kbd>
        F7</kbd></td>
        <td>Cfs</td>
        <td>Set Seed for C00-C99. Completes the per-group seed control; with all three seeds set, an artwork is fully deterministic.</td>
    </tr>
    <tr>
        <td><kbd>
        F8</kbd></td>
        <td>Create</td>
        <td>Generate Artwork via Random Generator. Uses the seeds set via F5-F7 where given, otherwise draws fresh ones.</td>
    </tr>
    <tr>
        <td><kbd>
        Tab</kbd></td>
        <td>Navigate</td>
        <td>Cycle forward through all navigational UI elements — grid, directory trees, and panels — in a fixed, predictable order.</td>
    </tr>
    <tr>
        <td><kbd>
        Arrow-keys</kbd></td>
        <td>Navigation</td>
        <td>Navigate table/grid cells in all directions: left, right, up, down. Within the directory trees, up/down move through entries.</td>
    </tr>
    <tr>
        <td><kbd>
        BackSpace</kbd></td>
        <td>Navigation</td>
        <td>Step back one level — collapses the current node in the directory tree, or leaves cell editing without applying changes.</td>
    </tr>
    <tr>
        <td><kbd>
        Space</kbd></td>
        <td>Navigation</td>
        <td>Toggle the element under the cursor — expands or collapses a directory node without changing focus.</td>
    </tr>
    <tr>
        <td><kbd>
        Enter</kbd></td>
        <td>Navigation</td>
        <td>Confirm the current selection — activates the focused cell or opens the highlighted file entry.</td>
    </tr>
    <tr>
        <td><kbd>
        Ctrl-Q</kbd></td>
        <td>System</td>
        <td>Exit the app. Unexported work in the grid is discarded, so run F9 first if you want to keep the current state.</td>
    </tr>
</table>


## API Credit
This tool stands on other people's work, and the table below is meant as more
than a dependency list. Entries are grouped by layer: **Build** covers what
produces the README assets and keeps the JavaScript side honest, **Utility**
the Python toolchain, **Framework** the TUI foundation this app is written
against, and **Processing** the actual image engine — G'MIC does the heavy
lifting behind every filter, invoked as a subprocess rather than vendored, so
all credit for the visual results belongs upstream.

The **Inspiration** entries deserve a special word: none of their source code
appears in this repo, but they shaped it more than some of the code that does.
Fred Weinhaus' ImageMagick scripts demonstrated what a disciplined collection
of composable image effects can look like; vtracer and Wand each informed how
this tool thinks about wrapping a powerful engine behind a humane interface.
If you like what this project does, follow the links — the ideas started there.

<table width="100%">
    <tr>
        <th align="left">Layer</th>
        <th align="left">Name</th>
        <th align="left">Link</th>
    </tr>
        <tr><td><kbd>
        Build</kbd></td>
        <td>Apng</td><td>
        <a href="//github.com/apngasm/apngasm">
        https://github.com/apngasm/apng</a></td>
    </tr>
    </tr>
        <tr><td><kbd>
        Build</kbd></td>
        <td>Grim</td><td>
        <a href="//github.com/emersion/grim">
        https://github.com/emersion/grim</a></td>
    </tr>
    <tr>
        <td><kbd>
        Build</kbd></td>
        <td>Biome</td><td>
        <a href="//github.com/biomejs/biome">
        https://github.com/biomejs/biome</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utility</kbd></td>
        <td>Ruff</td><td>
        <a href="//github.com/astral-sh/ruff">
        https://github.com/astral-sh/ruff</a></td>
    </tr>
    <tr>
        <td><kbd>
        Utility</kbd></td>
        <td>Pip Uv</td><td>
        <a href="//github.com/astral-sh/uv">
        https://github.com/astral-sh/uv</a></td>
    </tr>
    <tr>
        <td><kbd>
        Framework</kbd></td>
        <td>Platform</td><td>
        <a href="//github.com/tox-dev/platformdirs">
        https://github.com/tox-dev/platform</a></td>
    </tr>
    <tr>
        <td><kbd>
        Framework</kbd></td>
        <td>Textual</td><td>
        <a href="//github.com/Textualize/textual">
        https://github.com/Textualize/textual</a></td>
    </tr>
    <tr>
        <td><kbd>
        Framework</kbd></td>
        <td>Textual Img</td><td>
        <a href="//github.com/lnqs/textual-image">
        https://github.com/lnqs/textual-image</a></td>
    </tr>
    <tr align="left">
        <td><kbd>
        Processing</kbd></td>
        <td>Resize Img</td><td>
        <a href="//github.com/shibukawa/imagesize_py">
        https://github.com/shibukawa/imsize</a></td>
    </tr>
    <tr>
        <td><kbd>
        Processing</kbd></td>
        <td>FX Gmic</td><td>
        <a href="//github.com/GreycLab/gmic">
        https://github.com/GreycLab/gmic</a></td>
    </tr>
    <tr>
        <td><kbd>
        Inspiration</kbd></td>
        <td>FX Script</td><td>
        <a href="//www.fmwconcepts.com">
        https://www.fmwconcepts.com</a></td>
    </tr>
    <tr>
        <td><kbd>
        Inspiration</kbd></td>
        <td>FX Tracer</td><td>
        <a href="//visioncortex.org/vtracer">
        https://visioncortex.org/vtracer</a></td>
    </tr>
    <tr>
        <td><kbd>
        Inspiration</kbd></td>
        <td>FX Wand</td><td>
        <a href="//docs.wand-py.org/en/0.7.2/">
        https://docs.wand-py.org/en</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    </tr>
</table>


## PI Gallery
Twenty-five takes on a single source image. Every variation below was produced
with the filters shipped in this repo — same input file, different filter
effect per render, no manual retouching in between. The gallery exists to give
you a feel for the expressive range before you install anything: from subtle
tonal shifts to renders where the original is barely recognizable. Filenames are the Unix timestamps of their render runs, left untouched as a
quiet proof of process — these are batch outputs, not hand-picked compositions.
Click any thumbnail for full resolution, then pick the effects you want to
reproduce and feed them your own images.

<table>
<tr>
    <td><a href="artwing/Backend/module/1780150638.png">
    <img src="artwing/Backend/module/1780150638.png"></a></td>
    <td><a href="artwing/Backend/module/1780150643.png">
    <img src="artwing/Backend/module/1780150643.png"></a></td>
    <td><a href="artwing/Backend/module/1780150675.png">
    <img src="artwing/Backend/module/1780150675.png"></a></td>
    <td><a href="artwing/Backend/module/1780150689.png">
    <img src="artwing/Backend/module/1780150689.png"></a></td>
    <td><a href="artwing/Backend/module/1780150715.png">
    <img src="artwing/Backend/module/1780150715.png"></a></td>
</tr>
<tr>
    <td><a href="artwing/Backend/module/1780150731.png">
    <img src="artwing/Backend/module/1780150731.png"></a></td>
    <td><a href="artwing/Backend/module/1780150740.png">
    <img src="artwing/Backend/module/1780150740.png"></a></td>
    <td><a href="artwing/Backend/module/1780150748.png">
    <img src="artwing/Backend/module/1780150748.png"></a></td>  
    <td><a href="artwing/Backend/module/1780151480.png">
    <img src="artwing/Backend/module/1780151480.png"></a></td>  
    <td><a href="artwing/Backend/module/1780151501.png">
    <img src="artwing/Backend/module/1780151501.png"></a></td>
</tr>
<tr>
    <td><a href="artwing/Backend/module/1780151522.png">
    <img src="artwing/Backend/module/1780151522.png"></a></td>
    <td><a href="artwing/Backend/module/1780159196.png">
    <img src="artwing/Backend/module/1780159196.png"></a></td>
    <td><a href="artwing/Backend/module/1780159214.png">
    <img src="artwing/Backend/module/1780159214.png"></a></td>
    <td><a href="artwing/Backend/module/1780159226.png">
    <img src="artwing/Backend/module/1780159226.png"></a></td>
    <td><a href="artwing/Backend/module/1780159230.png">
    <img src="artwing/Backend/module/1780159230.png"></a></td>  
</tr>
<tr>
    <td><a href="artwing/Backend/module/1780159311.png">
    <img src="artwing/Backend/module/1780159311.png"></a></td>
    <td><a href="artwing/Backend/module/1780159326.png">
    <img src="artwing/Backend/module/1780159326.png"></a></td>
    <td><a href="artwing/Backend/module/1780159589.png">
    <img src="artwing/Backend/module/1780159589.png"></a></td>
    <td><a href="artwing/Backend/module/1780159608.png">
    <img src="artwing/Backend/module/1780159608.png"></a></td>
    <td><a href="artwing/Backend/module/1780159627.png">
    <img src="artwing/Backend/module/1780159627.png"></a></td>
</tr>
<tr>
    <td><a href="artwing/Backend/module/1780159636.png">
    <img src="artwing/Backend/module/1780159636.png"></a></td>
    <td><a href="artwing/Backend/module/1780159664.png">
    <img src="artwing/Backend/module/1780159664.png"></a></td>
    <td><a href="artwing/Backend/module/1780159667.png">
    <img src="artwing/Backend/module/1780159667.png"></a></td>
    <td><a href="artwing/Backend/module/1780159675.png">
    <img src="artwing/Backend/module/1780159675.png"></a></td>
    <td><a href="artwing/Backend/module/1780159679.png">
    <img src="artwing/Backend/module/1780159679.png"></a></td>
</tr>
</table>
<br>
