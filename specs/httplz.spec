%global debug_package %{nil}
%global _prj_name http

Name:           httplz
Version:        1.12.5
Release:        2%{?dist}
Summary:        A basic HTTP server for hosting a folder fast and simply

License:        MIT
URL:            https://github.com/thecoshman/http
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       bzip2-libs openssl
BuildRequires:  gcc pkgconfig(bzip2) pkgconfig(openssl)
# for some inexplicable reason, EL9 doesn't have pandoc
# so we need to grab the statically-linked binary
%if ! 0%{?el9}
BuildRequires:  pandoc
%endif

%description
A simple-binary server that can be used via CLI to quickly take
the current directory and serve it. Everything has sensible defaults
such that you do not have to pass parameters like what port to use.

%prep
%autosetup -n %{_prj_name}-%{version}

# use latest stable version from rustup
curl -Lfo "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
# only build and install the `httplz` binary
RUSTFLAGS="-C strip=symbols" cargo build --release --bin %{name}

# rename man page markdown
mv %{_prj_name}.md %{name}.md
# patch man page markdown
## rename all instances of `http` to `httplz`
sed -Ei 's/%{_prj_name}\(1\)/%{name}(1)/g' %{name}.md
sed -Ei 's/`%{_prj_name}`/`%{name}`/g' %{name}.md
sed -Ei 's/`%{_prj_name} /`%{name} /g' %{name}.md
## remove opening header
sed -Ei '/={3,}$/d' %{name}.md
## add header in a format acceptable to pandoc
sed -Ei '1i % %{name}(1) v%{version}\n\n## NAME\n' %{name}.md

# if EL9, get the static binary and add its directory to PATH
%if 0%{?el9}
    _PD_VER="2.18"
    _PD_PKG="pandoc-${_PD_VER}"
    %ifarch x86_64
        _ARCH=amd64
    %elifarch aarch64
        _ARCH=arm64
    %else
        echo "Unsupported architecture!"
        exit 1
    %endif
    _PD_URL="https://github.com/jgm/pandoc/releases/download/${_PD_VER}/${_PD_PKG}-linux-${_ARCH}.tar.gz"

    curl -Lfo "${_PD_PKG}.tar.gz" "${_PD_URL}"
    tar -xf "${_PD_PKG}.tar.gz"

    _PD_BIN_DIR=$(realpath "${_PD_PKG}/bin")
    export PATH="${_PD_BIN_DIR}:${PATH}"
%endif

# generate man page to ./httplz.1
pandoc --standalone --from markdown --to man %{name}.md > %{name}.1

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jul 17 2022 cyqsimon - 1.12.5-2
- Always prefer toolchain from rustup

* Fri Jul 15 2022 cyqsimon - 1.12.5-1
- Release 1.12.5
