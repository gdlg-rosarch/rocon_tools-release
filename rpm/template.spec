Name:           ros-indigo-rocon-python-utils
Version:        0.1.16
Release:        0%{?dist}
Summary:        ROS rocon_python_utils package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rocon_python_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       python-catkin_pkg
Requires:       python-rospkg
Requires:       ros-indigo-rocon-std-msgs
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rosunit

%description
Python system and ros utilities.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 02 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.16-0
- Autogenerated by Bloom

* Sat Feb 28 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.15-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.14-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.13-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Daniel Stonier <d.stonier@gmail.com> - 0.1.12-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.11-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.10-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.9-0
- Autogenerated by Bloom

