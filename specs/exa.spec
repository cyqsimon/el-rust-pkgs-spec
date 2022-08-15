%global debug_package %{nil}

Name:           exa
Version:        0.10.1
Release:        3%{?dist}
Summary:        A modern replacement for ‘ls’

License:        MIT
URL:            https://github.com/ogham/exa
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc
# for some inexplicable reason, EL9 doesn't have pandoc
# so we need to grab the statically-linked binary
%if ! 0%{?el9}
BuildRequires:  pandoc
%endif

%description
exa is a modern replacement for the venerable file-listing command-line
program ls that ships with Unix and Linux operating systems,
giving it more features and better defaults.

It uses colours to distinguish file types and metadata.
It knows about symlinks, extended attributes, and Git.
And it’s small, fast, and just one single binary.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

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
pandoc --standalone -f markdown -t man man/%{name}.1.md > %{name}.1
pandoc --standalone -f markdown -t man man/exa_colors.5.md > exa_colors.5

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 644 exa_colors.5 %{buildroot}%{_mandir}/man5/exa_colors.5

# doc
install -Dpm 644 LICEN?E %{buildroot}%{_docdir}/%{name}/LICENSE

# completions
install -Dpm 644 completions/completions.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 completions/completions.fish  %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 completions/completions.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/exa_colors.5*
%{_docdir}/%{name}/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 0.10.1-3
- Always prefer toolchain from rustup

* Sat Jul 16 2022 cyqsimon - 0.10.1-2
- Follow Zsh completion conventions

* Wed Jul 13 2022 cyqsimon - 0.10.1-1
- Release 0.10.1
