%define debug_package %{nil}
Name:           tor-static
Version:        1743937280.ac0367b
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
for i in *
do
 if test -d "$i"
 then
  pushd "${i}"
  mkdir dist/lib64 -p
  ln lib64 dist/lib -s
#  rm -rfv test || :
#  rm -rfv tests || :
  popd
 fi
done

go run build.go --verbose build-all

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
