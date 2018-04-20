# Script generated with Bloom
pkgdesc="ROS - Interaction management for human interactive agents in the concert."
url='http://ros.org/wiki/rocon_interactions'

pkgname='ros-kinetic-rocon-interactions'
pkgver='0.3.2_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-catkin_pkg'
'ros-kinetic-catkin'
'ros-kinetic-roslint'
'ros-kinetic-rostest'
'ros-kinetic-rosunit'
)

depends=('python2-rospkg'
'ros-kinetic-genpy'
'ros-kinetic-rocon-app-manager-msgs'
'ros-kinetic-rocon-bubble-icons'
'ros-kinetic-rocon-console'
'ros-kinetic-rocon-icons'
'ros-kinetic-rocon-interaction-msgs'
'ros-kinetic-rocon-python-comms'
'ros-kinetic-rocon-python-utils'
'ros-kinetic-rocon-std-msgs'
'ros-kinetic-rocon-uri'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-unique-id'
)

conflicts=()
replaces=()

_dir=rocon_interactions
source=()
md5sums=()

prepare() {
    cp -R $startdir/rocon_interactions $srcdir/rocon_interactions
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

