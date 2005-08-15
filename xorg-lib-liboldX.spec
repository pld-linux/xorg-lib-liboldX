# $Rev: 3326 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	oldX library
Summary(pl):	Biblioteka oldX
Name:		xorg-lib-liboldX
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/liboldX-%{version}.tar.bz2
# Source0-md5:	543d19f961d0137af59ecd11fd3398c4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/liboldX-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
oldX library.

%description -l pl
Biblioteka oldX.


%package devel
Summary:	Header files liboldX development
Summary(pl):	Pliki nag³ówkowe do biblioteki liboldX
Group:		X11/Development/Libraries
Requires:	xorg-lib-liboldX = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
oldX library.

This package contains the header files needed to develop programs that
use these liboldX.

%description devel -l pl
Biblioteka oldX.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki liboldX.


%package static
Summary:	Static liboldX libraries
Summary(pl):	Biblioteki statyczne liboldX
Group:		Development/Libraries
Requires:	xorg-lib-liboldX-devel = %{version}-%{release}

%description static
oldX library.

This package contains the static liboldX library.

%description static -l pl
Biblioteka oldX.

Pakiet zawiera statyczn± bibliotekê liboldX.


%prep
%setup -q -n liboldX-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_libdir}/liboldX.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/X10.h
%{_libdir}/liboldX.la
%attr(755,root,wheel) %{_libdir}/liboldX.so
%{_pkgconfigdir}/oldx.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/liboldX.a
