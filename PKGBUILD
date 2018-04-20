# Script generated with Bloom
pkgdesc="ROS - Utilities and tools developed for rocon, but usable beyond the boundaries of rocon."
url='http://www.ros.org/wiki/rocon_tools'

pkgname='ros-kinetic-rocon-tools'
pkgver='0.3.2_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-rocon-console'
'ros-kinetic-rocon-ebnf'
'ros-kinetic-rocon-interactions'
'ros-kinetic-rocon-launch'
'ros-kinetic-rocon-master-info'
'ros-kinetic-rocon-python-comms'
'ros-kinetic-rocon-python-redis'
'ros-kinetic-rocon-python-utils'
'ros-kinetic-rocon-python-wifi'
'ros-kinetic-rocon-semantic-version'
'ros-kinetic-rocon-uri'
)

conflicts=()
replaces=()

_dir=rocon_tools
source=()
md5sums=()

prepare() {
    cp -R $startdir/rocon_tools $srcdir/rocon_tools
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

