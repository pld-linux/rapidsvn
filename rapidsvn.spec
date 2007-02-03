Summary:	Cross-platform GUI front-end for the Subversion revision system
Summary(pl):	Wieloplatformowy graficzny interfejs do systemu kontroli wersji Subversion
Name:		rapidsvn
Version:	0.9.6
%define		_rel	20070203
Release:	0.%{_rel}
License:	Apache
Group:		Development/Version Control
#Source0:	http://rapidsvn.org/download/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_rel}.tar.bz2
# Source0-md5:	3fc40c7452d81fe793ed8e561962f92e
Patch0:		%{name}-link.patch
URL:		http://rapidsvn.tigris.org/
BuildRequires:	apr-devel >= 1:1.0
BuildRequires:	apr-util-devel >= 1:1.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	neon-devel
BuildRequires:	subversion-devel >= 1.1.0
BuildRequires:	libuuid-devel
BuildRequires:	wxGTK2-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-platform GUI front-end for the Subversion revision system.

%description -l pl
Wieloplatformowy graficzny interfejs u¿ytkownika do systemu kontroli
wersji Subversion.

%prep
%setup -q -n %{name}-%{_rel}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-svn-include=%{_includedir} \
	--with-svn-lib=%{_libdir} \
	--with-wx-config=%{_bindir}/wx-gtk2-ansi-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-apr-config=%{_bindir}/apr-1-config 

%{__make}
cd doc/manpage
%{__make} manpage

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/manpage/rapidsvn.1 $RPM_BUILD_ROOT%{_mandir}/man1/

rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/libsvncpp.{a,la}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*
