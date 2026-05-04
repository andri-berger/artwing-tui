pkgname=filterx-tui
pkgver=0.0.1
pkgrel=1
arch=('x86_64')
license=('GPL-3.0-only')
provides=('filterx-tui')
conflicts=('filterx-tui')
pkgdesc="Flexible Filter Generator in TUI format"
url="https://github.com/andri-berger/filterx-tui"
source=("https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('95cda2e85ef7c9aa8f5eea4e3551ac8d6da7baac1a11fab668917d0adcd71eef')
makedepends=('python-build' 'python-installer' 'python-wheel')
depends=(
    'python-numpy'
    'python-pillow'
    'python-playwright'
    'python-platformdirs'
    'python-textual-fspicker'
    'python-textual-image'
    'python-textual'
    'python-vtracer'
    'opencv-python'
    'opencv'
    'resvg'
    'gmic'
)

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

  # post_install() {
  #   echo ""
  #   echo "==> artwork-tui requires Playwright's Chromium browser."
  #   echo "==> If not already installed, run as your normal user:"
  #   echo ""
  #   echo "    playwright install chromium --with-deps"
  #   echo ""
  #   if ! find ~/.cache/ms-playwright -name 'chrome' 2>/dev/null | grep -q .; then
  #       echo "==> WARNING: Chromium not detected — app will fail without it."
  #   fi
  # }

  # post_install() {
  #   echo ""
  #   echo "╔════════════════════════════════════════════════╗"
  #   echo "║           filterx-tui — post install           ║"
  #   echo "╚════════════════════════════════════════════════╝"
  #   echo ""
  #   echo " Chromium is required but must be installed as"
  #   echo " your normal user (not root). Run:"
  #   echo ""
  #   echo "   playwright install chromium --with-deps"
  #   echo ""
  #   echo " filterx-tui will not function without this step."
  #   echo ""
  # }

  # post_upgrade() {
  #   post_install
  # }
