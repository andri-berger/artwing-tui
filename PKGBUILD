pkgrel=1
pkgver=0.1.0
arch=('any')
pkgname=artwing-tui
license=('GPL-3.0-only')
pkgdesc='Flexible FilterFX Layer in TUI format'
url="https://github.com/andri-berger/${pkgname}"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/andri-berger/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('b0bb10dd319361adcc82a672130731814733e430704f82627ef8775f640da9a8')
makedepends=(
    'python-hatchling'
    'python-installer'
    'python-build'
    'python-wheel')
depends=(
    'python-textual-image'
    'python-platformdirs'
    'ptyhon-imagesize'
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

