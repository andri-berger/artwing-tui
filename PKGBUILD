pkgname=filterx-tui
pkgver=0.0.1
pkgrel=1
arch=('x86_64')
license=('GPL-3.0-only')
provides=('filterx-tui')
conflicts=('filterx-tui')
pkgdesc="Flexible FilterFX Layer in TUI format"
url="https://github.com/andri-berger/filterx-tui"  source=("https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('10790e80a965d21087a53c40286817f7f7835356d917c2bce1c152dc004edcab')
makedepends=('python-build' 'python-installer' 'python-wheel')
depends=(
    'gmic'
    'python-numpy'
    'python-textual-image'
    'python-textual'
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


