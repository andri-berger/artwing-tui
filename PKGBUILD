pkgname=filterx-tui
pkgver=1.0.0
pkgrel=1
arch=('any')
pkgdesc="Flexible Filter Generator in TUI format"
url="https://github.com/you/layout-tui"
makedepends=('python-build' 'python-pip')
license=('GPL-3.0-only')
depends=('python' 'uv')
  source=("${pkgname}-${pkgver}.tar.gz::https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('abc123...')

  build() {
      cd "$srcdir/${pkgname}-${pkgver}"
      uv build --wheel
  }

  package() {
      cd "$srcdir/${pkgname}-${pkgver}"
      pip install \
          --root="$pkgdir" \
          --prefix=/usr \
          --no-deps \
          dist/*.whl
  }
