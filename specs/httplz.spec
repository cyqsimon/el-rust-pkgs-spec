%global debug_package %{nil}

Name:    httplz
Version: 1.12.5
Release: 1%{?dist}
Summary: A basic HTTP server for hosting a folder fast and simply

License: MIT
URL: https://github.com/thecoshman/http
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cargo rust
# install ronn-ng from source using gem due to its
# different availability on EL7/8/9
BuildRequires: gcc ruby ruby-devel rubygems

%description
A simple-binary server that can be used via CLI to quickly take
the current directory and serve it. Everything has sensible defaults
such that you do not have to pass parameters like what port to use.

%prep
# install ronn-ng
gem install ronn-ng

%autosetup
# rename man page
mv http.md %{name}.md

%build
# only build and install the `httplz` binary
RUSTFLAGS="-C strip=symbols" cargo build --release --bin %{name}

# generate man page to ./httplz.1
ronn --organization="http developers" "${pkgname}.md" --output-dir .

%check
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jul 15 2022 cyqsimon - 1.12.5-1
- Release 1.12.5
