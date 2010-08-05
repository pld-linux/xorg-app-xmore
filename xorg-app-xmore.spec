Summary:	xmore - plain text display program for the X Window System
Summary(pl.UTF-8):	xmore - program do wyświetlania czystego tekstu dla systemu X Window
Name:		xorg-app-xmore
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xmore-%{version}.tar.bz2
# Source0-md5:	e66f16684e92d3ca035c27003157cdbd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmore application - plain text display program for the X Window
System.

%description -l pl.UTF-8
Aplikacja xmore - program do wyświetlania czystego tekstu dla systemu
X Window.

%prep
%setup -q -n xmore-%{version}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xmore
%{_datadir}/X11/app-defaults/XMore
%{_mandir}/man1/xmore.1x*
