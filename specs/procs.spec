%global debug_package %{nil}

Name:           procs
Version:        0.12.3
Release:        2%{?dist}
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
curl -Lfo "rustup.sh" "https://sh.rustup.rs"
chmod +x "rustup.sh"
./rustup.sh --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

target/release/%{name} --completion bash
target/release/%{name} --completion fish
target/release/%{name} --completion zsh

%check
source ~/.cargo/env
cargo test --release

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
* Sun Jul 17 2022 cyqsimon - 0.12.3-2
- Always prefer toolchain from rustup

* Sat Jul 16 2022 cyqsimon - 0.12.3-1
- Release 0.12.3
