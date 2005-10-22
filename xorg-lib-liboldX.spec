Summary:	oldX library
Summary(pl):	Biblioteka oldX
Name:		xorg-lib-liboldX
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/liboldX-%{version}.tar.bz2
# Source0-md5:	9185c9f553c73a4f59ceb2d917258164
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oldX library.

%description -l pl
Biblioteka oldX.

%package devel
Summary:	Header files liboldX development
Summary(pl):	Pliki nagłówkowe do biblioteki liboldX
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description devel
oldX library.

This package contains the header files needed to develop programs that
use these liboldX.

%description devel -l pl
Biblioteka oldX.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki liboldX.

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

Pakiet zawiera statyczną bibliotekę liboldX.

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
