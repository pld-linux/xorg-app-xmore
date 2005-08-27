Summary:	xmore application
Summary(pl):	Aplikacja xmore
Name:		xorg-app-xmore
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xmore-%{version}.tar.bz2
# Source0-md5:	510128a91a6e26b55e6efb00bfa3eb42
Patch0:		xmore-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmore application.

%description -l pl
Aplikacja xmore.

%prep
%setup -q -n xmore-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
