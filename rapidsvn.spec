Summary:	Cross-platform GUI front-end for the Subversion revision system
Summary(pl):	Wieloplatformowy graficzny interfejs do systemu kontroli wersji Subversion
Name:		rapidsvn
Version:	0.4.0
Release:	1
License:	Apache
Group:		Development/Version Control
Source0:	http://rapidsvn.tigris.org/files/documents/341/8734/%{name}-%{version}.tar.gz
# Source0-md5:	d8943ea719303e96180f79eb265f9059
URL:		http://rapidsvn.tigris.org/
BuildRequires:	apr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	neon-devel
BuildRequires:	subversion-devel >= 0.28.0
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-platform GUI front-end for the Subversion revision system.

%description -l pl
Wieloplatformowy graficzny interfejs u¿ytkownika do systemu kontroli
wersji Subversion.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-svn-include=%{_includedir} \
	--with-svn-lib=%{_libdir} \
	--with-wx-config=%{_bindir}/wxgtk2-2.4-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.so.*
%{_mandir}/man1/*
