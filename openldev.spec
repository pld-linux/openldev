Summary:	Graphical front-end to gcc/g++
Summary(pl):	Graficzna nak³adka na gcc/g++
Name:		openldev
Version:	1.0
%define	_rc	rc1
Release:	0.%{_rc}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/openldev/%{name}-%{version}%{_rc}.tar.bz2
# Source0-md5:	64cd3b4c6324cc2a1673f66e6a3cd264
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-makefile.patch
URL:		http://www.openldev.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	gtksourceview-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	vte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Linux Developer is a environment based on the GTK+2 libraries
that provides a graphical front-end to gcc/g++. It includes the basic
essentials needed by a C/C++ programmer.

%description -l pl
Open Linux Developer jest ¶rodowiskiem opartym o bibliotekê GTK+2,
bêd±cym graficzn± nak³adk± na gcc/g++. Zawiera podstawowe sk³adniki
porzebne dla programisty C/C++.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1

# workaround for hardcoded paths
sed -i -e 's|/lib/openldev|/%{_lib}/openldev|' openldev/openldev-plugin-engine.cc

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-template-all \
	--disable-static

%{__make} \
	CXXFLAGS='%{rpmcflags}'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_pixmapsdir}/openldev/openldev48.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/openldev.png
	
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang OpenLDev

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f OpenLDev.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libopenldev.so*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.plugin
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
%{_mandir}/man1/*.1*
