%define debug_package %{nil}
Name:           tor-static
Version:        1718029021.6ccf94f
Release:        0
Summary:        Tor static compiled library
License:        GPL
Url:            https://github.com/cretz/tor-static
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: bash
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libcap-static
BuildRequires: glibc-static
BuildRequires: libzstd-static
BuildRequires: asciidoc
BuildRequires: libcap-devel
BuildRequires: libzstd-devel
BuildRequires: glibc-devel
BuildRequires: po4a
BuildRequires: golang
BuildRequires: perl
BuildRequires: perl(FindBin)
BuildRequires: gettext-devel

%description
%{summary}.

%prep
%autosetup

%build
env -i HOME=$HOME PATH=$PATH go run build.go --verbose build-all

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cp tor/libtor.a %{buildroot}%{_libdir}/libtor.a
cp tor/src/feature/api/tor_api.h %{buildroot}%{_includedir}/tor_api.h

%files
%{_includedir}/tor_api.h
%{_libdir}/libtor.a
%doc README.md
%license LICENSE
