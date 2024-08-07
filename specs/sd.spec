%global debug_package %{nil}

Name:           sd
Version:        1.0.0
Release:        2%{?dist}
Summary:        Intuitive find & replace CLI (sed alternative)

License:        MIT
URL:            https://github.com/chmln/sd
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
sd is an intuitive find & replace CLI written in Rust that makes
find and replace using regular expressions fast and easy.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 gen/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 gen/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 gen/completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 gen/completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Apr 16 2024 cyqsimon - 1.0.0-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Wed Nov 08 2023 cyqsimon - 1.0.0-1
- Release 1.0.0 🎉

* Sat Mar 18 2023 cyqsimon - 0.7.6-4
- Run tests in debug mode

* Sun Jul 17 2022 cyqsimon - 0.7.6-3
- Always prefer toolchain from rustup

* Thu Jul 14 2022 cyqsimon - 0.7.6-2
- Move Zsh completions to site-functions dir

* Wed Jul 13 2022 cyqsimon - 0.7.6-1
- Release 0.7.6
