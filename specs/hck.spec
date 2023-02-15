%global debug_package %{nil}

Name:           hck
Version:        0.9.1
Release:        1%{?dist}
Summary:        A sharp cut(1) clone

License:        MIT OR Unlicense
URL:            https://github.com/sstadick/hck
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc
%if 0%{?rhel} >= 8
BuildRequires:  cmake
%else
BuildRequires:  cmake3
%endif

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

%if 0%{?rhel} < 8
# symlink cmake3 to cmake
mkdir -p "$HOME/.local/bin"
ln -s "/usr/bin/cmake3" "$HOME/.local/bin/cmake"
%endif

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE-MIT UNLICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Feb 15 2023 cyqsimon - 0.9.1-1
- Release 0.9.1
