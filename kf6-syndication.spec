%define libname %mklibname KF6Syndication
%define devname %mklibname KF6Syndication -d
%define git 20230927

Name: kf6-syndication
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/syndication/-/archive/master/syndication-master.tar.bz2#/syndication-%{git}.tar.bz2
Summary: An RSS/Atom parser library
URL: https://invent.kde.org/frameworks/syndication
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6Codecs)
Requires: %{libname} = %{EVRD}

%description
An RSS/Atom parser library

%package -n %{libname}
Summary: An RSS/Atom parser library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
An RSS/Atom parser library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

An RSS/Atom parser library

%prep
%autosetup -p1 -n syndication-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/syndication.*

%files -n %{devname}
%{_includedir}/KF6/Syndication
%{_libdir}/cmake/KF6Syndication
%{_qtdir}/mkspecs/modules/qt_Syndication.pri
%{_qtdir}/doc/KF6Syndication.*

%files -n %{libname}
%{_libdir}/libKF6Syndication.so*
