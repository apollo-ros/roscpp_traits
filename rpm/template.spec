Name:           ros-jade-cpp-common
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS cpp_common package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/cpp_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       console-bridge-devel
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  ros-jade-catkin

%description
cpp_common contains C++ code for doing things that are not necessarily ROS
related, but are useful for multiple packages. This includes things like the
ROS_DEPRECATED and ROS_FORCE_INLINE macros, as well as code for getting
backtraces. This package is a component of roscpp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Mar 09 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.7-0
- Autogenerated by Bloom

* Wed May 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.6-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.5-0
- Autogenerated by Bloom

