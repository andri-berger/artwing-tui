pkgrel=1
pkgver=0.1.1
arch=('any')
pkgname=artwing-tui
license=('GPL-3.0-only')
pkgdesc='Flexible FilterFX Layer in TUI format'
url="https://github.com/andri-berger/${pkgname}"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/andri-berger/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('70220ec3bc80f07d554b76868454782ea41409d790f2b4fd2121b10c7ab14825')
makedepends=(
    'python-hatchling'
    'python-installer'
    'python-build'
    'python-wheel')
depends=(
    'python>=3.14'
    'python-textual-image'
    'python-platformdirs'
    'python-imagesize'
    'python-textual'
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

