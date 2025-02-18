%global debug_package %{nil}

Name:           xh
Version:        0.24.0
Release:        1%{?dist}
Summary:        Friendly and fast tool for sending HTTP requests

License:        MIT
URL:            https://github.com/ducaale/xh
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
xh is a friendly and fast tool for sending HTTP requests.
It reimplements as much as possible of HTTPie's excellent design,
with a focus on improved performance.

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

# symlink
# `xh` will default to HTTPS scheme if the binary name is one of `xhs`, `https`, or `xhttps`
ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}s

# manpage
install -Dpm 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Feb 18 2025 cyqsimon - 0.24.0-1
- Release 0.24.0

* Fri Jan 03 2025 cyqsimon - 0.23.1-1
- Release 0.23.1

* Sun Oct 13 2024 cyqsimon - 0.23.0-1
- Release 0.23.0

* Tue Jul 09 2024 cyqsimon - 0.22.2-1
- Release 0.22.2

* Tue Apr 16 2024 cyqsimon - 0.22.0-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Sun Apr 14 2024 cyqsimon - 0.22.0-1
- Release 0.22.0

* Mon Jan 29 2024 cyqsimon - 0.21.0-1
- Release 0.21.0

* Mon Nov 20 2023 cyqsimon - 0.20.1-1
- Release 0.20.1

* Mon Oct 23 2023 cyqsimon - 0.19.4-1
- Release 0.19.4

* Sun Oct 22 2023 cyqsimon - 0.19.2-1
- Release 0.19.2
