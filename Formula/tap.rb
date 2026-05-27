class Tap < Formula
  include Language::Python::Virtualenv

  license "GPL-3.0-only"
  desc "Flexible Filterx Generator in TUI format"
  homepage "https://github.com/andri-berger/artwork-tui"
  url "https://github.com/andri-berger/artwork-tui/archive/v0.0.1.tar.gz"
  sha256 "10790e80a965d21087a53c40286817f7f7835356d917c2bce1c152dc004edcab"
  depends_on "python@3.14"
  depends_on "gmic"

  
  resource "textual-image" do
    url "https://files.pythonhosted.org/packages/c2/e7/c82ea0604874b6d51d5717a0911061ae5810e36dad2e4d2b11fa7d54cdaa/textual_image-0.12.0.tar.gz"
    sha256 "fdd0b5ff9c8a99740bc360a99ce014d563fa97d07a5b49b472470809f57c0a74"
  end

  resource "textual" do
    url "https://files.pythonhosted.org/packages/62/1e/1eedc5bac184d00aaa5f9a99095f7e266af3ec46fa926c1051be5d358da1/textual-8.2.5.tar.gz"
    sha256 "6c894e65a879dadb4f6cf46ddcfedb0173ff7e0cb1fe605ff7b357a597bdbc90"
  end
      
  on_arm do
    resource "numpy" do
      url "https://files.pythonhosted.org/packages/05/1a/d8007a5138c179c2bf33ef44503e83d70434d2642877ee8fbb230e7c0548/numpy-2.4.4-cp314-cp314t-macosx_14_0_arm64.whl"
      sha256 "42c16925aa5a02362f986765f9ebabf20de75cdefdca827d14315c568dcab113"
    end
  end

  on_intel do
    resource "numpy" do
      url "https://files.pythonhosted.org/packages/99/64/ffb99ac6ae93faf117bcbd5c7ba48a7f45364a33e8e458545d3633615dda/numpy-2.4.4-cp314-cp314t-macosx_14_0_x86_64.whl"
      sha256 "874f200b2a981c647340f841730fc3a2b54c9d940566a3c4149099591e2c4c3d"
    end
  end

  test do
    system "#{bin}/filterx-tui", "--version"
  end
end
