%global debug_package %{nil}

Name:           ouch
Version:        0.3.1
Release:        1%{?dist}
Summary:        Painless compression and decompression for your terminal

License:        MIT
URL:            https://github.com/ouch-org/ouch
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

# See https://github.com/ouch-org/ouch/issues/256
%if 0%{?el8}
BuildRequires:  gcc-toolset-11
%else
BuildRequires:  gcc
%endif

BuildRequires:  pkgconfig(liblzma) pkgconfig(libzstd) pkgconfig(zlib)
# EL7's bzip2-devel does not include bzip2.pc
%if 0%{?rhel} >= 8
BuildRequires:  pkgconfig(bzip2)
%else
BuildRequires:  bzip2-devel
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
# CHANGELOG.md created after v0.3.1
#%doc CHANGELOG.md README.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Mon Aug 15 2022 cyqsimon - 0.3.1-1
- Release 0.3.1
