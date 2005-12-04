Summary:	oldX library
Summary(pl):	Biblioteka oldX
Name:		xorg-lib-liboldX
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/liboldX-%{version}.tar.bz2
# Source0-md5:	cf3faee62f1682f3e305d3834bcde343
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oldX library.

%description -l pl
Biblioteka oldX.

%package devel
Summary:	Header files for liboldX library
Summary(pl):	Pliki nag³ówkowe biblioteki liboldX
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
oldX library.

This package contains the header files needed to develop programs that
use liboldX.

%description devel -l pl
Biblioteka oldX.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki liboldX.

%package static
Summary:	Static liboldX library
Summary(pl):	Biblioteka statyczna liboldX
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%doc ChangeLog
%attr(755,root,root) %{_libdir}/liboldX.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboldX.so
%{_libdir}/liboldX.la
%{_includedir}/X11/X10.h
%{_pkgconfigdir}/oldx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liboldX.a
