Summary:	Cross-platform GUI front-end for the Subversion revision system
Summary(pl):	Wieloplatformowy graficzny interfejs do systemu kontroli wersji Subversion
Name:		rapidsvn
Version:	0.7.2
Release:	0.1
License:	Apache
Group:		Development/Version Control
Source0:	http://www.rapidsvn.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	e2c16a506b2bc20f4532ce40ce1a117c
Patch0:		%{name}-ac_flags.patch
Patch1:		%{name}-apr-1.patch
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
BuildRequires:	subversion-devel >= 1.0.0
BuildRequires:	wxGTK2-devel >= 2.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-platform GUI front-end for the Subversion revision system.

%description -l pl
Wieloplatformowy graficzny interfejs u¿ytkownika do systemu kontroli
wersji Subversion.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-svn-include=%{_includedir} \
	--with-svn-lib=%{_libdir} \
	--with-wx-config=%{_bindir}/wxgtk2-2.4-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-apr-config=%{_bindir}/apr-1-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*
