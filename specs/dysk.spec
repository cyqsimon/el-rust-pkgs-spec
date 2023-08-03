%global debug_package %{nil}

Name:           dysk
Version:        2.7.2
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
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# compatibility symlink
ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/lfs

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
