%global debug_package %{nil}

Name:           ouch
Version:        0.3.1
Release:        1%{?dist}
Summary:        Painless compression and decompression for your terminal

License:        MIT
URL:            https://github.com/ouch-org/ouch
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  pkgconfig(bzip2) pkgconfig(libzstd) pkgconfig(xz) pkgconfig(zlib)
BuildRequires:  gcc
# See https://github.com/ouch-org/ouch/issues/256
%if 0%{?el8}
BuildRequires:  gcc-toolset-11
%endif

%description
ouch stands for Obvious Unified Compression Helper and is a CLI tool
to help you compress and decompress files of several formats.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

# remove toolchain override (use stable)
rm -f rust-toolchain

%build
%if 0%{?el8}
    source /opt/rh/gcc-toolset-11/enable
%endif

source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" GEN_COMPLETIONS=1 cargo build --release

%check
%if 0%{?el8}
    source /opt/rh/gcc-toolset-11/enable
%endif

source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# completions
install -Dpm 644 target/release/build/%{name}-*/out/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 target/release/build/%{name}-*/out/completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 target/release/build/%{name}-*/out/completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Mon Aug 15 2022 cyqsimon - 0.3.1-1
- Release 0.3.1
