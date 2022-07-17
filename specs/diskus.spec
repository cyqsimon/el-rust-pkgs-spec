%global debug_package %{nil}

Name:           diskus
Version:        0.7.0
Release:        2%{?dist}
Summary:        A minimal, fast alternative to 'du -sh'

License:        Apache-2.0 or MIT
URL:            https://github.com/sharkdp/diskus
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
diskus is a very simple program that computes the total size
of the current directory. It is a parallelized version of du -sh.

On an 8-core laptop, it is about ten times faster than du with a
cold disk cache and more than three times faster with a warm disk cache.

%prep
%autosetup

# use latest stable version from rustup
curl -Lfo "rustup.sh" "https://sh.rustup.rs"
chmod +x "rustup.sh"
./rustup.sh --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jul 17 2022 cyqsimon - 0.7.0-2
- Always prefer toolchain from rustup

* Sun Jul 17 2022 cyqsimon - 0.7.0-1
- Release 0.7.0
