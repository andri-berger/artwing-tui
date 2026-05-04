  class Filterx-Tui < Formula
    include Language::Python::Virtualenv

    license "GPL-3.0-only"
    desc "Flexible Filter Generator in TUI format"
    homepage "https://github.com/andri-berger/filterx-tui"
    url "https://github.com/andri-berger/filterx-tui/archive/v0.0.1.tar.gz"
    sha256 "95cda2e85ef7c9aa8f5eea4e3551ac8d6da7baac1a11fab668917d0adcd71eef"
    # depends_on cask: "ungoogled-chromium"
    depends_on "python@3.14"
    depends_on "gmic"


    resource "platformdirs" do
      url "https://files.pythonhosted.org/packages/9f/4a/0883b8e3802965322523f0b200ecf33d31f10991d0401162f4b23c698b42/platformdirs-4.9.6.tar.gz"
      sha256 "3bfa75b0ad0db84096ae777218481852c0ebc6c727b3168c1b9e0118e458cf0a"
    end
    
    resource "textual-fspicker" do
      url "https://files.pythonhosted.org/packages/e8/fd/dc3160123af550838d50a4fa7f62e357d7ad2fc9b4220ead9160661bcd1b/textual_fspicker-1.0.0.tar.gz"
      sha256 "462608dbe6a14edff679fc6116addcf288f4a79f8e4fffd240f9ce2caaf9e655"
    end

    resource "textual-image" do
      url "https://files.pythonhosted.org/packages/c2/e7/c82ea0604874b6d51d5717a0911061ae5810e36dad2e4d2b11fa7d54cdaa/textual_image-0.12.0.tar.gz"
      sha256 "fdd0b5ff9c8a99740bc360a99ce014d563fa97d07a5b49b472470809f57c0a74"
    end
    
    resource "textual" do
      url "https://files.pythonhosted.org/packages/62/1e/1eedc5bac184d00aaa5f9a99095f7e266af3ec46fa926c1051be5d358da1/textual-8.2.5.tar.gz"
      sha256 "6c894e65a879dadb4f6cf46ddcfedb0173ff7e0cb1fe605ff7b357a597bdbc90"
    end

    on_arm do
      resource "vtracer" do
        url "https://files.pythonhosted.org/packages/ca/c6/22c009b147de23fb8d1b18587ec303ab99fe4af423802185a2991a0a5bc4/vtracer-0.6.15-cp314-cp314-macosx_11_0_arm64.whl"
        sha256 "a845d023d5704eb4edf017cb4e57cad2c7dec36d80160b7f6eab744ca8121e68"
      end
    end

    on_intel do
      resource "vtracer" do
        url "https://files.pythonhosted.org/packages/58/84/8b269b73dd0b0f662dc11b6f9ae695ce98b98103cb9248c097e4c1d406f0/vtracer-0.6.15-cp314-cp314-macosx_10_12_x86_64.whl"
        sha256 "51b9069e87ea022249352f585a2774a07db7434743b8ddae5e49761c33412ceb"
      end
    end
    
    on_arm do
      resource "playwright" do
        url "https://files.pythonhosted.org/packages/08/71/5e4d98b2ce3641b4343623c6450ff33b9de1c979d12a957505e392338b07/playwright-1.59.0-py3-none-macosx_11_0_arm64.whl"
        sha256 "af068143a0c045ec11608b67d6c42e58db7e9cf65a742dd21fddedc1a9802c47"
      end
    end

    on_intel do
      resource "playwright" do
        url "https://files.pythonhosted.org/packages/5b/48/abab23f40643b4de8f2665816f0a1bf0994eeecda39d6d62f0f292b2ad01/playwright-1.59.0-py3-none-macosx_10_13_x86_64.whl"
        sha256 "bfc6940100b57423175c819ce2422ec5880d55fa2769987f62ab7a1f5fe6783e"
      end
    end
   
    on_arm do
      resource "opencv-contrib-python-headless" do
        url "https://files.pythonhosted.org/packages/70/b5/9af5b81d9279e9982e21dad52f8a6aec10f7c891ae1e3d3d1b3ce111f8e7/opencv_contrib_python_headless-4.13.0.92-cp37-abi3-macosx_13_0_arm64.whl"
        sha256 "b0467988c2d56c283b00fb808e0b57f5db2e3ca7743164a3b3efc733bfa03d3a"
      end
    end

    on_intel do
      resource "opencv-contrib-python-headless" do
        url "https://files.pythonhosted.org/packages/c5/42/f0aef27baf1f376007b018b00f6c304c42c20d31aa8491633c53b18912cb/opencv_contrib_python_headless-4.13.0.92-cp37-abi3-macosx_14_0_x86_64.whl"  
        sha256 "79e503b77880d806a1b106ff8182c6f898347ccfd1db58ffc9a6369acc236c4c"
      end
    end

    on_arm do
      resource "pillow" do
        url "https://files.pythonhosted.org/packages/19/1e/dce46f371be2438eecfee2a1960ee2a243bbe5e961890146d2dee1ff0f12/pillow-12.2.0-cp314-cp314t-macosx_11_0_arm64.whl"
        sha256 "d5d38f1411c0ed9f97bcb49b7bd59b6b7c314e0e27420e34d99d844b9ce3b6f3"
      end
    end

    on_intel do
      resource "pillow" do
        url "https://files.pythonhosted.org/packages/b6/ab/1b426a3974cb0e7da5c29ccff4807871d48110933a57207b5a676cccc155/pillow-12.2.0-cp314-cp314t-macosx_10_15_x86_64.whl"
        sha256 "57850958fe9c751670e49b2cecf6294acc99e562531f4bd317fa5ddee2068463"
      end
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

    # def install
    #   inreplace "pyproject.toml", /\[project\.dependencies\][^\[]*/m, ""
    #   virtualenv_install_with_resources
    # end

    def post_install
      ohai "Installing Chromium via Playwright..."
      system libexec/"bin/playwright", "install", "chromium"
    end

    def caveats
      <<~EOS
      Chromium is managed by Playwright and installed separately.
      If Chromium is missing or broken, reinstall it manually:
         #{libexec}/bin/playwright install chromium

         On Linux, system dependencies may also be needed:
         #{libexec}/bin/playwright install chromium --with-deps
         EOS
    end
 
    test do
      system "#{bin}/filterx-tui", "--version"
    end

  end
