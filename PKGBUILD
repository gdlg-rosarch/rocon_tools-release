# Script generated with Bloom
pkgdesc="ROS - Module for working with rocon uri strings."
url='http://ros.org/wiki/rocon_uri'

pkgname='ros-kinetic-rocon-uri'
pkgver='0.3.2_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-rosunit'
)

depends=('python2-rospkg'
'ros-kinetic-rocon-console'
'ros-kinetic-rocon-ebnf'
'ros-kinetic-rocon-python-utils'
'ros-kinetic-rospy'
)

conflicts=()
replaces=()

_dir=rocon_uri
source=()
md5sums=()

prepare() {
    cp -R $startdir/rocon_uri $srcdir/rocon_uri
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

