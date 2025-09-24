%global debug_package %{nil}
%global _bin_name evcxr

Name:           evcxr-repl
Version:        0.21.1
Release:        2%{?dist}
Summary:        A Rust REPL

License:        MIT AND Apache-2.0
URL:            https://github.com/evcxr/evcxr
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       rust-src
BuildRequires:  gcc

%description
A Rust REPL.

%prep
%autosetup -n %{_bin_name}-%{version}

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

%check
source ~/.cargo/env
cargo +stable test -- --test-threads 1

%install
# bin
install -Dpm 755 -t %{buildroot}%{_bindir} target/release/%{_bin_name}

%files
%license LICENSE
%doc COMMON.md README.md RELEASE_NOTES.md
%{_bindir}/%{_bin_name}

%changelog
* Wed Sep 24 2025 cyqsimon - 0.21.1-2
- Run tests single-threaded for now
  - See https://github.com/evcxr/evcxr/issues/425

* Wed Sep 24 2025 cyqsimon - 0.21.1-1
- Release 0.21.1

* Wed Sep 24 2025 cyqsimon - 0.17.0-2
- Mass rebuild

* Wed Sep 18 2024 cyqsimon - 0.17.0-1
- Release 0.17.0
