%global debug_package %{nil}
%global artifact_dir artifacts
# disable `unrar` feature due to non-compliant license
%global feature_flag --no-default-features --features=use_zlib,use_zstd_thin,bzip3

Name:           ouch
Version:        0.8.2
Release:        1%{?dist}
Summary:        Painless compression and decompression for your terminal

License:        MIT
URL:            https://github.com/ouch-org/ouch
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  clang pkgconfig(bzip2) pkgconfig(bzip3) pkgconfig(liblzma) pkgconfig(libzstd) pkgconfig(zlib)
# Git required for some tests
BuildRequires:  git

%description
ouch stands for Obvious Unified Compression Helper and is a CLI tool
to help you compress and decompress files of several formats.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
OUCH_ARTIFACTS_FOLDER=%{artifact_dir} cargo +stable build --release %{feature_flag}

%check
source ~/.cargo/env
cargo +stable test %{feature_flag}

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

cd %{artifact_dir}

# man pages
mkdir -pm 755 %{buildroot}%{_mandir}/man1
install -Dpm 644 -t %{buildroot}%{_mandir}/man1 %{name}{,-compress,-decompress,-list}.1

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Sep 01 2026 cyqsimon - 0.8.2-1
- Release 0.8.2
- Remove GCC12 workaround for EL8: no longer appears necessary

* Wed Sep 24 2025 cyqsimon - 0.4.2-3
- Mass rebuild

* Tue Aug 13 2024 cyqsimon - 0.4.2-2
- Remove provisions for EL7

* Tue Apr 16 2024 cyqsimon - 0.4.2-1
- Release 0.4.2
- Fix artifact generation

* Tue Apr 16 2024 cyqsimon - 0.4.1-3
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Sat Mar 18 2023 cyqsimon - 0.4.1-2
- Run tests in debug mode

* Fri Jan 06 2023 cyqsimon - 0.4.1-1
- Release 0.4.1

* Fri Nov 25 2022 cyqsimon - 0.4.0-1
- Release 0.4.0
- Use GCC12 on EL8
- Install man pages

* Mon Aug 15 2022 cyqsimon - 0.3.1-1
- Release 0.3.1
