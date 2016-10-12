Name:           ros-kinetic-rocon-python-utils
Version:        0.3.2
Release:        1%{?dist}
Summary:        ROS rocon_python_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rocon_python_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       python-catkin_pkg
Requires:       python-rospkg
Requires:       ros-kinetic-rocon-std-msgs
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rosunit

%description
Python system and ros utilities.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Oct 12 2016 Daniel Stonier <d.stonier@gmail.com> - 0.3.2-1
- Autogenerated by Bloom

* Wed May 11 2016 Daniel Stonier <d.stonier@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

