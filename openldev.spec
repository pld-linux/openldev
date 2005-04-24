Summary:	Graphical front-end to gcc/g++
Summary(pl):	Graficzna nak³adka na gcc/g++
Name:		openldev
Version:	0.3.8
Release:	1
License:	GPL v.2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/openldev/%{name}-%{version}.tar.gz
# Source0-md5:	155ba92644921ac9b47dc9700d815cfd
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-makefile.patch
URL:		http://www.openldev.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm >= 2.6.0
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Linux Developer is a environment based on the Gtkmm libraries
that provides a graphical front-end to gcc/g++. It includes the basic
essentials needed by a c/c++ programmer.

%description -l pl
Open Linux Developer jest ¶rodowiskiem opartym o bibliotekê Gtkmm,
bêd±cym graficzn± nak³adk± na gcc/g++. Zawiera podstawowe sk³adniki
porzebne dla programisty c/c++.

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
%configure
%{__make}

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
#%%doc nothing to add, empty files
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}
%{_pixmapsdir}/*.png
