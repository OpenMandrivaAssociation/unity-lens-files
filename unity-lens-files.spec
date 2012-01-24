Summary:	Files lens for the Unity Desktop
Name:		unity-lens-files
Version:	0.6.12
Release:	1
License:	GPLv3
Url:		https://launchpad.net/unity-lens-files
Group:		Graphical desktop/Other
Source:		%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	pkgconfig(zeitgeist-daemon)
BuildRequires:	pkgconfig(dee-1.0)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(unity)
BuildRequires:	pkgconfig(zeitgeist-1.0)
BuildRequires:	vala-devel

Requires:	zeitgeist

%description
This package contains the "files" place which can be used into Unity
to browse files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING
%dir %{_datadir}/unity
%dir %{_datadir}/unity/themes
%{_libexecdir}/unity-files-daemon
%{_datadir}/dbus-1/services/unity-lens-files.service
%{_datadir}/unity/lenses/
%{_datadir}/unity/themes/files.png


