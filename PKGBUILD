# Script generated with Bloom
pkgdesc="ROS - The pythonwifi package is available through pypi, but not through a deb package. This is copy of the package suitable for use through the ROS ecosystem."
url='http://pythonwifi.wikispot.org/'

pkgname='ros-kinetic-rocon-python-wifi'
pkgver='0.3.2_2'
pkgrel=1
arch=('any')
license=('GPLv2'
)

makedepends=('python2-catkin_pkg'
'ros-kinetic-catkin'
)

depends=()

conflicts=()
replaces=()

_dir=rocon_python_wifi
source=()
md5sums=()

prepare() {
    cp -R $startdir/rocon_python_wifi $srcdir/rocon_python_wifi
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

