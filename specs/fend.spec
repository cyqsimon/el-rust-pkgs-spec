%global debug_package %{nil}

Name:           fend
Version:        1.2.0
Release:        1%{?dist}
Summary:        Arbitrary-precision unit-aware calculator

License:        MIT
URL:            https://github.com/printfn/fend
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pandoc

%description
fend is an arbitrary-precision unit-aware calculator.

Unique features:

- Arbitrary-precision arithmetic using rational numbers
- Full support for complex numbers
- D&D-style dice rolls
- Variables
- Binary, octal, hexadecimal and all other bases between 2 and 36
- Keep track of units, with support for SI, US and UK customary and many historical units
- Emacs-style CLI shortcuts
- Trigonometric functions
- Lambda calculus

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release --package %{name}

documentation/build.sh

%check
source ~/.cargo/env
cargo test --package %{name} --package %{name}-core

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 documentation/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jul 20 2023 cyqsimon - 1.2.0-1
- Relaese 1.2.0

