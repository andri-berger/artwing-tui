class Tap < Formula
  include Language::Python::Virtualenv

  license "GPL-3.0-only"
  desc "Flexible Filterx Generator in TUI format"
  homepage "https://github.com/andri-berger/filterx-tui"
  url "https://github.com/andri-berger/filterx-tui/archive/v0.0.1.tar.gz"
  sha256 "10790e80a965d21087a53c40286817f7f7835356d917c2bce1c152dc004edcab"
  depends_on "python@3.14"
  depends_on "gmic"

  resource "imagesize" do
    url "https://files.pythonhosted.org/packages/6c/e6/7bf14eeb8f8b7251141944835abd42eb20a658d89084b7e1f3e5fe394090/imagesize-2.0.0.tar.gz"
    sha256 "8e8358c4a05c304f1fccf7ff96f036e7243a189e9e42e90851993c558cfe9ee3"
  end

  resource "textual-image" do
    url "https://files.pythonhosted.org/packages/c2/e7/c82ea0604874b6d51d5717a0911061ae5810e36dad2e4d2b11fa7d54cdaa/textual_image-0.12.0.tar.gz"
    sha256 "fdd0b5ff9c8a99740bc360a99ce014d563fa97d07a5b49b472470809f57c0a74"
  end

  resource "textual" do
    url "https://files.pythonhosted.org/packages/62/1e/1eedc5bac184d00aaa5f9a99095f7e266af3ec46fa926c1051be5d358da1/textual-8.2.5.tar.gz"
    sha256 "6c894e65a879dadb4f6cf46ddcfedb0173ff7e0cb1fe605ff7b357a597bdbc90"
  end

  test do
    system "#{bin}/filterx-tui", "--version"
  end
end
