%global debug_package %{nil}

Name:           procs
Version:        0.14.6
Release:        1%{?dist}
Summary:        A modern replacement for ps written in Rust

License:        MIT
URL:            https://github.com/dalance/procs
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
procs is a replacement for ps written in Rust.

Features:
- Colored and human-readable output
  - Automatic theme detection based on terminal background
- Multi-column keyword search
- Some additional information which are not supported by ps
  - TCP/UDP port
  -  Read/Write throughput
  -  Docker container name
  -  More memory information
- Pager support
- Watch mode (like top)
- Tree view

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

target/release/%{name} --gen-completion bash
target/release/%{name} --gen-completion fish
target/release/%{name} --gen-completion zsh

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Jul 30 2024 cyqsimon - 0.14.6-1
- Release 0.14.6

* Tue Apr 16 2024 cyqsimon - 0.14.5-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Thu Mar 07 2024 cyqsimon - 0.14.5-1
- Release 0.14.5

* Fri Nov 24 2023 cyqsimon - 0.14.4-1
- Release 0.14.4

* Fri Oct 20 2023 cyqsimon - 0.14.3-1
- Release 0.14.3

* Wed Oct 18 2023 cyqsimon - 0.14.2-1
- Release 0.14.2

* Fri Oct 06 2023 cyqsimon - 0.14.1-1
- Release 0.14.1

* Sat Mar 18 2023 cyqsimon - 0.14.0-2
- Run tests in debug mode

* Tue Mar 07 2023 cyqsimon - 0.14.0-1
- Release 0.14.0

* Tue Jan 31 2023 cyqsimon - 0.13.4-1
- Release 0.13.4

* Tue Oct 18 2022 cyqsimon - 0.13.3-1
- Release 0.13.3

* Wed Oct 05 2022 cyqsimon - 0.13.2-1
- Release 0.13.2

* Wed Sep 21 2022 cyqsimon - 0.13.1-1
- Release 0.13.1

* Fri Jul 29 2022 cyqsimon - 0.13.0-1
- Release 0.13.0

* Sun Jul 17 2022 cyqsimon - 0.12.3-2
- Always prefer toolchain from rustup

* Sat Jul 16 2022 cyqsimon - 0.12.3-1
- Release 0.12.3
