# <img src="artwing/build.png" width="50" valign="middle" alt="logo"> Artwing-TUI
Artwing-TUI is a terminal-native creative filter engine wrapping G'MIC's extensive library of image effects into a comfortable spreadsheet-driven interface. Think of it as an effects rack for images, operated entirely from the terminal – a creative filter machine with no GUI overhead, no cloud dependency, no subscription. 

The motivation was equally simple: G'MIC is one of the most powerful and underappreciated image processing tools in existence, yet its full potential remains largely inaccessible to anyone unwilling to memorize its command syntax or navigate its GIMP plugin interface. artwing-tui bridges that gap, exposing G'MIC's creative filter library through a structured, navigable interface that rewards exploration without demanding expertise. It is the sibling project of artwork-tui, operating under the same GitHub umbrella and complementing it naturally: where artwork-tui generates, artwing-tui processes.

[Installation](#installation) / 
[Configuration](#configuration) / 
[API Reference](#reference) / 
[API Credit](#credit) / 
[Gallery](#gallery)


<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="demos/01_apply_effect.png"><img src="demos/01_apply_effect.png" width="100%" alt="Apply an effect and tweak it"></a>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="demos/02_open_images.png"><img src="demos/02_open_images.png" width="100%" alt="Open images from anywhere"></a>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="demos/03_effect_tour.png"><img src="demos/03_effect_tour.png" width="100%" alt="Tour the effect categories"></a>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="demos/04_realtime.png"><img src="demos/04_realtime.png" width="100%" alt="Realtime FX on every picked image"></a>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="demos/05_stack.png"><img src="demos/05_stack.png" width="100%" alt="Stack effects with CREATE"></a>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="demos/06_save.png"><img src="demos/06_save.png" width="100%" alt="CREATE and EXPORT"></a>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="demos/07_load_project.png"><img src="demos/07_load_project.png" width="100%" alt="Load a saved project"></a>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="demos/08_restore.png"><img src="demos/08_restore.png" width="100%" alt="Pick up where you left off"></a>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="demos/09_resets.png"><img src="demos/09_resets.png" width="100%" alt="Reset parameters, effect or image"></a>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top">
      <a href="demos/10_themes.png"><img src="demos/10_themes.png" width="100%" alt="Themes"></a>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="demos/11_grid.png"><img src="demos/11_grid.png" width="100%" alt="Edit parameters in the grid"></a>
    </td>
    <td width="33%" align="center" valign="top">
      <a href="demos/12_files.png"><img src="demos/12_files.png" width="100%" alt="Copy, move and delete files"></a>
    </td>
  </tr>
</table>

## Installation
Artwing-TUI has no Electron, no npm, no 200 MB runtime surprise — just a Python TUI and G'MIC under the hood. One install script, one path, every Unix system.

Pulls the install script directly from the repo and wires everything up.
The script installs uv and G'MIC if they are missing (G'MIC 3.x recommended,
some filters are missing in 2.9). uv brings its own Python 3.14 when your
system has none, so installation lands in an isolated environment and never
touches your system Python. If piping curl into sh makes you twitch — good
instinct — read the script first; it is short and does exactly what it says.

```bash
curl -fsSL https://raw.githubusercontent.com/\
andri-berger/artwing-tui/main/install.sh | sh
```

To update, run the same command again. To remove it, run
`uv tool uninstall artwing-tui`. User-generated files are not removed with it,
see below.

### Where your files end up
Artwing keeps two folders per user, a share (data) folder and a state folder.
`$XDG_DATA_HOME` and `$XDG_STATE_HOME` override the defaults on both systems.

| | Linux | macOS |
|---|---|---|
| Share | `~/.local/share/artwing-tui` | `~/Library/Application Support/artwing-tui` |
| State | `~/.local/state/artwing-tui` | `~/Library/Application Support/artwing-tui` |
| Share, XDG set | `$XDG_DATA_HOME/artwing-tui` | `$XDG_DATA_HOME/artwing-tui` |
| State, XDG set | `$XDG_STATE_HOME/artwing-tui` | `$XDG_STATE_HOME/artwing-tui` |

- **Export (F9)** writes the png and its json project file into the share
  folder, named by timestamp, e.g. `1792780000.png` and `792780000.json`.
- **Create (F8)** writes the png into the state folder, under the category of
  the active effect, e.g. `filter/blur_all.png` (`blur_all_0.png` and so on
  if it already exists), and its json under the same name into `yamljson/`,
  e.g. `yamljson/blur_all.json`. An image without effect goes to the top of
  the state folder under its own name. These are the files the local tree in
  the middle shows; its cursor jumps to the new png, so you can pick it as
  the next source and stack another effect on top.
- Both only save a finished render. While gmic is still running, or after
  it failed, they save nothing and say so.
- The share folder also holds the working copies `1700000000.tif` (current
  preview) and `700000000.json` (current state), which are overwritten as you
  work.

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
        <th align="left">Element</th>
        <th align="left">Description</th>
    </tr>
    <tr>
        <td><kbd>Global Filetree</kbd></td>
        <td>Choose either an image (png, jpg, bmp, gif, tif, webp, ppm/pgm/pnm or tga as base image) or json (for your project-files). Mirror of your unrestricted / full filesystem, hence the name global. </td>
    </tr>
    <tr>
        <td><kbd>Local Filetree</kbd></td>
        <td>Choose either an image (png, jpg, bmp, gif, tif, webp, ppm/pgm/pnm or tga as base image) or json (for your project-files). Local Filesystem only hosting all files copied over via Button Create (see below), hence the name local. </td>
    </tr>
    <tr>
        <td><kbd>FX Filetree</kbd></td>
        <td>Browse the catalogue of available filter effects. Selecting an entry loads
it into the Grid FX Rack, where its parameters become editable.</td>
    </tr>
    <tr>
        <td><kbd>Grid FX Rack</kbd></td>
        <td>The heart of the app — a spreadsheet-style grid where selected effects are
stacked like modules in a rack. Each row holds one effect with its parameters
as editable cells; the stack is applied to the base image in order.</td>
    </tr>
    <tr>
        <td><kbd>Button X</kbd></td>
        <td>Clear the parameters of the active effect, so it runs with its defaults again. Files on disk are not touched.</td>
    </tr>
    <tr>
        <td><kbd>Button AS</kbd></td>
        <td>Toggle whether picking a new image re-applies the active effect. Off (default): every picked image gets the effect. On: picked images show raw.</td>
    </tr>
    <tr>
        <td><kbd>Button BSS</kbd></td>
        <td>Step to the previous theme of the built-in list.</td>
    </tr>
    <tr>
        <td><kbd>Button CSS</kbd></td>
        <td>Step to the next theme of the built-in list.</td>
    </tr>
    <tr>
        <td><kbd>Button Create</kbd></td>
        <td>Save the current result (png plus json named after it) into the local file directory in the middle, the cursor lands on it, so you can pick it as the next source and stack another effect on top. See Where your files end up.</td>
    </tr>
    <tr>
        <td><kbd>Button Export</kbd></td>
        <td>Export both generated (png) and project file (json) into the share folder, see Where your files end up.</td>
    </tr>
</table>


## API Reference
The entire application is driven from the keyboard. Del and F1 to F9 follow
the button row from left to right: Del, cut, copy, paste, then X, AS, BSS,
CSS, Create and Export. Del and F1 to F3 work on whatever has the focus:
in the grid they act on the cell under the cursor, in a file tree on the
file under the cursor. Files can be cut or copied in the global and the
local tree, and are always pasted into the local tree in the middle, which
makes it the place to collect sources for further FX.

The remaining bindings follow the conventions you already know from any
terminal application: Tab cycles focus, arrow keys move through the grid,
Ctrl-Q leaves. The exported json (F9) is the full recipe, the png merely its
rendering.

<table>
    <tr>
        <td><kbd>
        Del</kbd></td>
        <td>Delete</td>
        <td>Grid: clear the cell (inside the cell editor Del just deletes a character). Local file tree: delete the file under the cursor from disk.</td>
    </tr>
    <tr>
        <td><kbd>
        F1</kbd></td>
        <td>Cut</td>
        <td>Grid: cut the cell (copy it, then clear it). Global or local file tree: cut the png/json file, F3 moves it into the local tree. Think of it as Ctrl-X.</td>
    </tr>
    <tr>
        <td><kbd>
        F2</kbd></td>
        <td>Copy</td>
        <td>Grid: copy the cell. Global or local file tree: copy the png/json file, F3 pastes a copy into the local tree. Think of it as Ctrl-C.</td>
    </tr>
    <tr>
        <td><kbd>
        F3</kbd></td>
        <td>Paste</td>
        <td>Grid: paste into the cell. Local file tree: paste the cut or copied file into the folder under the cursor (a name that is taken gets _0, _1, ...). Think of it as Ctrl-V.</td>
    </tr>
    <tr>
        <td><kbd>
        F4</kbd></td>
        <td>X</td>
        <td>Press Button X (clear the effect parameters).</td>
    </tr>
    <tr>
        <td><kbd>
        F5</kbd></td>
        <td>AS</td>
        <td>Press Button AS (toggle re-applying the effect to picked images).</td>
    </tr>
    <tr>
        <td><kbd>
        F6</kbd></td>
        <td>BSS</td>
        <td>Press Button BSS (previous theme).</td>
    </tr>
    <tr>
        <td><kbd>
        F7</kbd></td>
        <td>CSS</td>
        <td>Press Button CSS (next theme).</td>
    </tr>
    <tr>
        <td><kbd>
        F8</kbd></td>
        <td>Create</td>
        <td>Press Button Create (save the result into the local file tree).</td>
    </tr>
    <tr>
        <td><kbd>
        F9</kbd></td>
        <td>Export</td>
        <td>Press Button Export (png plus json into the share folder).</td>
    </tr>
    <tr>
        <td><kbd>
        Tab</kbd></td>
        <td>Navigate</td>
        <td>Cycle forward through grid, file trees and buttons in a fixed order; Shift-Tab goes back. In a cell editor, Tab applies the value.</td>
    </tr>
    <tr>
        <td><kbd>
        Arrow-keys</kbd></td>
        <td>Navigation</td>
        <td>Move through grid cells in all directions; in the file trees, up/down move through entries.</td>
    </tr>
    <tr>
        <td><kbd>
        Space</kbd></td>
        <td>Navigation</td>
        <td>File trees: pick the entry under the cursor (open a folder, choose an image, json or effect). Grid: edit the cell, like Enter.</td>
    </tr>
    <tr>
        <td><kbd>
        Enter / BackSpace</kbd></td>
        <td>Edit</td>
        <td>Grid: edit the cell, starting from its current value, or from the default when the cell is empty. Typing a character or - starts editing with it.</td>
    </tr>
    <tr>
        <td><kbd>
        Escape</kbd></td>
        <td>Edit</td>
        <td>Leave the cell editor without applying the change.</td>
    </tr>
    <tr>
        <td><kbd>
        Ctrl-Q</kbd></td>
        <td>System</td>
        <td>Exit the app. Work is kept for the next start; run F9 to keep a copy of the current state.</td>
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
        <td>Pillow Img</td><td>
        <a href="//github.com/python-pillow/Pillow">
        https://github.com/python-pillow/Pillow</a></td>
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
