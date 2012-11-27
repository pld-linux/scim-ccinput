Summary:	SCIM IMEngine module for CCInput method
Summary(pl.UTF-8):	Moduł silnika IM platformy SCIM dla metody CCInput
Name:		scim-ccinput
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.bz2
# Source0-md5:	8859f934d874852ec13e47d6e67ed144
Patch0:		%{name}-sh.patch
Patch1:		%{name}-gettext.patch
Patch2:		%{name}-gtk3.patch
URL:		http://www.scim-im.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.2.0
Requires:	scim >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM IMEngine module for CCInput method.

%description -l pl.UTF-8
Moduł silnika IM platformy SCIM dla metody CCInput.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang ccinput

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ccinput.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/ccin.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/ccin-imengine-setup.so
%{_datadir}/scim/ccinput
%{_datadir}/scim/icons/ccinput.png
%{_datadir}/scim/icons/sp_ls.png
%{_datadir}/scim/icons/sp_ms.png
%{_datadir}/scim/icons/sp_st.png
%{_datadir}/scim/icons/sp_zg.png
%{_datadir}/scim/icons/sp_zn.png
%{_datadir}/scim/icons/sp_zr.png
