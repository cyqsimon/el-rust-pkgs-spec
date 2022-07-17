%global debug_package %{nil}

Name:           garbage
Version:        0.3.3
Release:        2%{?dist}
Summary:        Soft-deletion CLI tool with FreeDesktop Trash compatibility

License:        GPLv3
URL:            https://git.sr.ht/~mzhang/garbage
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc git

%description
Soft-deletion CLI tool with FreeDesktop Trash compatibility.

Rust version of 'trash-cli'.

%prep
%autosetup -n %{name}-v%{version}

# use latest stable version from rustup
curl -Lfo "rustup.sh" "https://sh.rustup.rs"
chmod +x "rustup.sh"
./rustup.sh --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 0.3.3-2
- Always prefer toolchain from rustup

* Sun Jul 17 2022 cyqsimon - 0.3.3-1
- Release 0.3.3
