Summary:	Cross-platform GUI front-end for the Subversion revision system
Summary(pl.UTF-8):	Wieloplatformowy graficzny interfejs do systemu kontroli wersji Subversion
Name:		rapidsvn
Version:	0.9.8
Release:	1
License:	GPL v3
Group:		Development/Version Control
Source0:	http://www.rapidsvn.org/download/release/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1b49d893027ae83dbcff3d7508b3f42f
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
BuildRequires:	wxGTK2-unicode-devel >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-platform GUI front-end for the Subversion revision system.

%description -l pl.UTF-8
Wieloplatformowy graficzny interfejs użytkownika do systemu kontroli
wersji Subversion.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-svn-include=%{_includedir} \
	--with-svn-lib=%{_libdir} \
	--with-wx-config=%{_bindir}/wx-gtk2-unicode-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-apr-config=%{_bindir}/apr-1-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for -devel ?
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/libsvncpp.{a,la,so}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libsvncpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsvncpp.so.2
