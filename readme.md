
![Readme](./readme.png)
# Filterx-TUI (WIP)
Generative design tool with a terminal UI — compose layouts, render to canvas, export to SVG/PDF. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

[Installation](#installation) / 
[Configuration](#configuration) / 
[API Reference](#reference) / 
[API Credit](#credit) / 
[Gallery](#gallery)


(Drag Video in here). Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.


## Installation
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

### Generic Install (Native)
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua

```bash
curl -fsSL https://raw.githubusercontent.com/\
andri-berger/filterx-tui/main/install.sh | sh
```

### macOS (Homebrew)
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua

```bash
brew tap andri-berger/filterx-tui
brew install andri-berger/filterx-tui/build
```
```bash
brew install filterx-tui
```

### Arch Linux (AUR)
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua

```bash
pacman -S filterx-tui
```
```bash
paru -S filterx-tui
yay -S filterx-tui
```

## Configuration
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.
```bash
filterx-tui
```
Launches the TUI. Keyboard-driven, no mouse. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

## API Reference
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

<table>
    <tr>
        <th align="left">Cell</th>
        <th align="left">Resource</th>
        <th align="left">Default</th>
        <th align="left">Description</th>
    </tr>
    <tr>
        <td>A0</td>
        <td>boolean</td>
        <td>nil</td>
        <td>Enable centering in typing-mode. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.</td>
    </tr>
    <tr>
        <td>A1</td>
        <td>boolean</td>
        <td>nil</td>
        <td>Enable anchoring in navigation-mode. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>A2</td>
        <td>boolean</td>
        <td>nil</td>
        <td>Enable anchoring in org-mode. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>A3</td>
        <td>boolean</td>
        <td>nil</td>
        <td>LTR vs RTL Alignment. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>A4</td>
        <td>boolean </td>
        <td>nil</td>
        <td>Centering horizontally. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>A5</td>
        <td>integer</td>
        <td>50</td>
        <td>Max-width in chars. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>A6</td>
        <td>integer</td>
        <td>0</td>
        <td>Left fringe width in px. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B0</td>
        <td>integer</td>
        <td>0</td>
        <td>Vertical gap at the edge in px. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B1</td>
        <td>integer</td>
        <td>0</td>
        <td>Vertical gap fringe left in px. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B2</td>
        <td>select 0-3</td>
        <td>0</td>
        <td>Line-styles. 
        <br>0 = Lorem ipsum dolor sit amet. 
        <br>1 = Lorem ipsum dolor sit amet. 
        <br>2 = Lorem ipsum dolor sit amet. 
        <br>3 = Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B3</td>
        <td>select 0-3</td>
        <td>0</td>
        <td>Hierarchy treshold. 
        <br>0 = Lorem ipsum dolor sit amet. 
        <br>1 = Lorem ipsum dolor sit amet. 
        <br>2 = Lorem ipsum dolor sit amet. 
        <br>3 = Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B4</td>
        <td>select 0-3</td>
        <td>0</td>
        <td>Lines config header. 
        <br>0 = Lorem ipsum dolor sit amet. 
        <br>1 = Lorem ipsum dolor sit amet. 
        <br>2 = Lorem ipsum dolor sit amet. 
        <br>3 = Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B5</td>
        <td>select 0-3</td>
        <td>0</td>
        <td>Lines config mode. 
        <br>0 = Lorem ipsum dolor sit amet. 
        <br>1 = Lorem ipsum dolor sit amet. 
        <br>2 = Lorem ipsum dolor sit amet. 
        <br>3 = Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>B6</td>
        <td>select 0-3</td>
        <td>0</td>
        <td>Char/line/word header. 
        <br>0 = Lorem ipsum dolor sit amet. 
        <br>1 = Lorem ipsum dolor sit amet. 
        <br>2 = Lorem ipsum dolor sit amet. 
        <br>3 = Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>C0</td>
        <td>select 0-3</td>
        <td>0</td>
        <td>Char/line/word mode. 
        <br>0 = Lorem ipsum dolor sit amet. 
        <br>1 = Lorem ipsum dolor sit amet. 
        <br>2 = Lorem ipsum dolor sit amet. 
        <br>3 = Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>C1</td>
        <td>string</td>
        <td>"/"</td>
        <td>First Separator header / mode. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>C2</td>
        <td>string</td>
        <td>" // "</td>
        <td>Second separator header / mode. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>C3</td>
        <td>string</td>
        <td>"writer"</td>
        <td>Fallback text if no org-parent. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>C4</td>
        <td>value</td>
        <td>'unspecified</td>
        <td>Faces inherit header mode line. Lorem ipsum dolor sit amet.</td>
    </tr>
    <tr>
        <td>C5</td>
        <td>value</td>
        <td>'unspecified</td>
        <td>Custom face of vertical line. Lorem ipsum dolor sit amet.</td>
    </tr>
</table>


## API Credit
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

<table width="100%">
    <tr>
        <th align="left">Layer</th>
        <th align="left">Name</th>
        <th align="left">
        Link <img width="560"></th>
    </tr>
    <tr>
        <td>Assets</td>
        <td>Flags</td><td>
        <a href="https://github.com/lipis/flag-icons">
        https://github.com/lipis/flag-icons</a></td>
    </tr>
    <tr>
        <td>Assets</td>
        <td>Maps</td><td>
        <a href="//github.com/djaiss/mapsicon">
        https://github.com/djaiss/mapsicon</a></td>
    </tr>
    <tr>
        <td>Build</td>
        <td>Grip</td><td>
        <a href="//github.com/chrishrb/go-grip">
        https://github.com/chrishrb/go-grip</a></td>
    </tr>
    <tr>
        <td>Build</td>
        <td>Biome</td><td>
        <a href="//github.com/biomejs/biome">
        https://github.com/biomejs/biome</a></td>
    </tr>
        <tr>
        <td>Build</td>
        <td>Pyright</td><td>
        <a href="//github.com/microsoft/pyright">
        https://github.com/microsoft/pyright</a></td>
    </tr>
    <tr>
        <td>Build</td>
        <td>Ruff</td>
        <td><a href="//github.com/astral-sh/ruff">
        https://github.com/astral-sh/ruff</a></td>
    </tr>
    <tr>
        <td>Build</td>
        <td>UV</td><td>
        <a href="//github.com/astral-sh/uv">
        https://github.com/astral-sh/uv</a></td>
    </tr>
    <tr>
        <td>Utilities</td>
        <td>Numpy</td><td>
        <a href="//github.com/numpy/numpy">
        https://github.com/numpy/numpy</a></td>
    </tr>
    <tr>
        <td>Utilities</td>
        <td>Platform</td><td>
        <a href="https://github.com/tox-dev/platformdirs">
        https://github.com/tox-dev/platformdirs</a></td>
    </tr>
    <tr>
        <td>Framework</td>
        <td>Textual Dev</td><td>
        <a href="//github.com/Textualize/textual-dev">
        https://github.com/Textualize/textual-dev</a></td>
    </tr>
    <tr>
        <td>Framework</td>
        <td>Textual Img</td><td>
        <a href="//github.com/lnqs/textual-image">
        https://github.com/lnqs/textual-image</a></td>
    </tr>
    <tr>
        <td>Framework</td>
        <td>Textual Fs</td><td>
        <a href="//github.com/davep/textual-fspicker">
        https://github.com/davep/textual-fspicker</a></td>
    </tr>
    <tr>
        <td>Processing</td>
        <td>Playwright</td><td>
        <a href="https://github.com/microsoft/playwright">
        https://github.com/microsoft/playwright</a></td>
    </tr>
    <tr>
        <td>Processing</td>
        <td>GMic</td><td>
        <a href="https://github.com/GreycLab/gmic">
        https://github.com/GreycLab/gmic</a></td>
    </tr>
    <tr>
        <td>Processing</td>
        <td>Pillow</td><td>
        <a href="//github.com/python-pillow/Pillow">
        https://github.com/python-pillow/Pillow</a></td>
    </tr>
    <tr>
        <td>Processing</td>
        <td>Pixi Filters</td><td>
        <a href="//github.com/pixijs/filters">
        https://github.com/pixijs/filters</a></td>
    </tr>
    <tr>
        <td>Processing</td>
        <td>OpenCV</td><td>
        <a href="https://github.com/opencv/opencv">
        https://github.com/opencv/opencv</a></td>
    </tr>
    <tr>
        <td>Conversion</td>
        <td>VTracer</td><td>
        <a href="//github.com/visioncortex/vtracer">
        https://github.com/visioncortex/vtracer</a></td>
    </tr>
    <tr>
        <td>Conversion</td>
        <td>ReSVG</td><td>
        <a href="//github.com/linebender/resvg">
        https://github.com/linebender/resvg</a></td>
    </tr>
</table>


## Gallery
<table>
  <tr>
    <td><a href="assets/file-png/1744168392.png">
    <img src="assets/file-png/1744168392.png"></a></td>
    <td><a href="assets/file-png/1744168389.png">
    <img src="assets/file-png/1744168389.png"></a></td>
    <td><a href="assets/file-png/1744168387.png">
    <img src="assets/file-png/1744168387.png"></a></td>
    <td><a href="assets/file-png/1744168383.png">
    <img src="assets/file-png/1744168383.png"></a></td>
    <td><a href="assets/file-png/1744168379.png">
    <img src="assets/file-png/1744168379.png"></a></td>
    <td><a href="assets/file-png/1744168364.png">
    <img src="assets/file-png/1744168364.png"></a></td>
  </tr>
  <tr>
    <td><a href="assets/file-png/1744168360.png">
    <img src="assets/file-png/1744168360.png"></a></td>
    <td><a href="assets/file-png/1744168357.png">
    <img src="assets/file-png/1744168357.png"></a></td>
    <td><a href="assets/file-png/1744168352.png">
    <img src="assets/file-png/1744168352.png"></a></td>
    <td><a href="assets/file-png/1744168350.png">
    <img src="assets/file-png/1744168350.png"></a></td>
    <td><a href="assets/file-png/1744168323.png">
    <img src="assets/file-png/1744168323.png"></a></td>
    <td><a href="assets/file-png/1744168321.png">
    <img src="assets/file-png/1744168321.png"></a></td>
  </tr>
  <tr>
    <td><a href="assets/file-png/1744168314.png">
    <img src="assets/file-png/1744168314.png"></a></td>
    <td><a href="assets/file-png/1744168305.png">
    <img src="assets/file-png/1744168305.png"></a></td>
    <td><a href="assets/file-png/1744168298.png">
    <img src="assets/file-png/1744168298.png"></a></td>
    <td><a href="assets/file-png/1744168282.png">
    <img src="assets/file-png/1744168282.png"></a></td>
    <td><a href="assets/file-png/1744168280.png">
    <img src="assets/file-png/1744168280.png"></a></td>
    <td><a href="assets/file-png/1744168271.png">
    <img src="assets/file-png/1744168271.png"></a></td>
  </tr>
  <tr>
    <td><a href="assets/file-png/1744168261.png">
    <img src="assets/file-png/1744168261.png"></a></td>
    <td><a href="assets/file-png/1744168246.png">
    <img src="assets/file-png/1744168246.png"></a></td>
    <td><a href="assets/file-png/1744168243.png">
    <img src="assets/file-png/1744168243.png"></a></td>
    <td><a href="assets/file-png/1744168233.png">
    <img src="assets/file-png/1744168233.png"></a></td>
    <td><a href="assets/file-png/1744168209.png">
    <img src="assets/file-png/1744168209.png"></a></td>
    <td><a href="assets/file-png/1744168199.png">
    <img src="assets/file-png/1744168199.png"></a></td>
  </tr>
  <tr>
    <td><a href="assets/file-png/1744168196.png">
    <img src="assets/file-png/1744168196.png"></a></td>
    <td><a href="assets/file-png/1744168190.png">
    <img src="assets/file-png/1744168190.png"></a></td>
    <td><a href="assets/file-png/1744168164.png">
    <img src="assets/file-png/1744168164.png"></a></td>
    <td><a href="assets/file-png/1744168146.png">
    <img src="assets/file-png/1744168146.png"></a></td>
    <td><a href="assets/file-png/1744168006.png">
    <img src="assets/file-png/1744168006.png"></a></td>
    <td><a href="assets/file-png/1744167993.png">
    <img src="assets/file-png/1744167993.png"></a></td>
  </tr>
  <tr>
    <td><a href="assets/file-png/1744167990.png">
    <img src="assets/file-png/1744167990.png"></a></td>
    <td><a href="assets/file-png/1744167985.png">
    <img src="assets/file-png/1744167985.png"></a></td>
    <td><a href="assets/file-png/1744167983.png">
    <img src="assets/file-png/1744167983.png"></a></td>
    <td><a href="assets/file-png/1744167978.png">
    <img src="assets/file-png/1744167978.png"></a></td>
    <td><a href="assets/file-png/1744167972.png">
    <img src="assets/file-png/1744167972.png"></a></td>
    <td><a href="assets/file-png/1744167951.png">
    <img src="assets/file-png/1744167951.png"></a></td>
  </tr>
</table>

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.

<br>
<br>
<br>

