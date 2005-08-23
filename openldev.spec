Summary:	Graphical front-end to gcc/g++
Summary(pl):	Graficzna nak³adka na gcc/g++
Name:		openldev
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/openldev/%{name}-%{version}.tar.gz
# Source0-md5:	9883643f1939f00f7c54318030d7b460
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-template-all
%{__make} \
	OPTFLAGS='%{rpmcflags}'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_pixmapsdir}/openldev/openldev48.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/openldev.png
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
