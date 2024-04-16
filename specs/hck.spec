%global debug_package %{nil}

Name:           hck
Version:        0.10.0
Release:        3%{?dist}
Summary:        A sharp cut(1) clone

License:        MIT OR Unlicense
URL:            https://github.com/sstadick/hck
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  cmake3 gcc

%description
hck is a shortening of hack, a rougher form of cut.

A close to drop in replacement for cut that can use a regex delimiter instead
of a fixed string. Additionally this tool allows for specification of the order
of the output columns using the same column selection syntax as cut (see below
for examples).

No single feature of hck on its own makes it stand out over awk, cut, xsv or
other such tools. Where hck excels is making common things easy, such as
reordering output fields, or splitting records on a weird delimiter. It is
meant to be simple and easy to use while exploring datasets. Think of this as
filling a gap between cut and awk.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env

# On EL7 `cmake` links to cmake2
CMAKE=cmake3 cargo +stable build --release

%check
source ~/.cargo/env
CMAKE=cmake3 cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE-MIT UNLICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Tue Apr 16 2024 cyqsimon - 0.10.0-3
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Tue Apr 16 2024 cyqsimon - 0.10.0-2
- Fix cmake config for EL7

* Tue Apr 16 2024 cyqsimon - 0.10.0-1
- Release 0.10.0

* Thu Apr 13 2023 cyqsimon - 0.9.2-1
- Release 0.9.2

* Sat Mar 18 2023 cyqsimon - 0.9.1-2
- Run tests in debug mode

* Wed Feb 15 2023 cyqsimon - 0.9.1-1
- Release 0.9.1
