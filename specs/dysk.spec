%global debug_package %{nil}

Name:           dysk
Version:        2.10.1
Release:        1%{?dist}
Summary:        A linux utility listing your filesystems (previously lfs)
Provides:       lfs = %{version}-%{release}
Obsoletes:      lfs <= 2.6.0

License:        MIT
URL:            https://github.com/Canop/dysk
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
A linux utility to get information on filesystems, like df but better.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

# create compatibility script
cat >lfs <<"EOF"
#!/usr/bin/env bash
set -e
NC='\033[0m'; YELLOW='\033[0;33m'
echo -e "${YELLOW}[WARN]${NC} \"lfs\" is the deprecated old name for this binary and will be removed in the future. Use \"dysk\" instead."
/usr/bin/dysk "$@"
EOF

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# compatibility script
install -Dpm 755 lfs %{buildroot}%{_bindir}/lfs

# manpage
install -Dpm 644 target/release/build/%{name}-*/out/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 target/release/build/%{name}-*/out/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 target/release/build/%{name}-*/out/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 target/release/build/%{name}-*/out/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Wed May 14 2025 cyqsimon - 2.10.1-1
- Release 2.10.1

* Sun Dec 22 2024 cyqsimon - 2.10.0-1
- Release 2.10.0

* Mon Sep 09 2024 cyqsimon - 2.9.1-1
- Release 2.9.1

* Tue Jun 04 2024 cyqsimon - 2.9.0-1
- Release 2.9.0

* Tue Apr 16 2024 cyqsimon - 2.8.2-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Tue Oct 17 2023 cyqsimon - 2.8.2-1
- Release 2.8.2

* Tue Oct 10 2023 cyqsimon - 2.8.1-1
- Release 2.8.1

* Thu Aug 24 2023 cyqsimon - 2.8.0-3
- Fix `lfs` script

* Thu Aug 24 2023 cyqsimon - 2.8.0-2
- Use compatibility script instead of symlink for `lfs` executable
- Add deprecation warning in `lfs` executable

* Tue Aug 22 2023 cyqsimon - 2.8.0-1
- Release 2.8.0

* Fri Aug 04 2023 cyqsimon - 2.7.2-1
- Release 2.7.2

* Tue Jul 18 2023 cyqsimon - 2.7.1-1
- Relaese 2.7.1
- Install man page && shell completion

* Tue Jul 04 2023 cyqsimon - 2.6.1-1
- Release 2.6.1
- Project renamed from `lfs` to `dysk`
- Create compatibility symlink from `lfs` to `dysk`

* Sat Mar 18 2023 cyqsimon - 2.6.0-2
- Run tests in debug mode

* Thu Dec 08 2022 cyqsimon - 2.6.0-1
- Release 2.6.0
