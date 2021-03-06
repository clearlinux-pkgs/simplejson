#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simplejson
Version  : 3.16.1
Release  : 75
URL      : https://github.com/simplejson/simplejson/archive/v3.16.1/simplejson-3.16.1.tar.gz
Source0  : https://github.com/simplejson/simplejson/archive/v3.16.1/simplejson-3.16.1.tar.gz
Summary  : Simple, fast, extensible JSON encoder/decoder for Python
Group    : Development/Tools
License  : AFL-2.1
Requires: simplejson-license = %{version}-%{release}
Requires: simplejson-python = %{version}-%{release}
Requires: simplejson-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : py
BuildRequires : pytest

%description
simplejson
----------
.. image:: https://travis-ci.org/simplejson/simplejson.svg?branch=master
:target: https://travis-ci.org/simplejson/simplejson

%package license
Summary: license components for the simplejson package.
Group: Default

%description license
license components for the simplejson package.


%package python
Summary: python components for the simplejson package.
Group: Default
Requires: simplejson-python3 = %{version}-%{release}

%description python
python components for the simplejson package.


%package python3
Summary: python3 components for the simplejson package.
Group: Default
Requires: python3-core
Provides: pypi(simplejson)

%description python3
python3 components for the simplejson package.


%prep
%setup -q -n simplejson-3.16.1
cd %{_builddir}/simplejson-3.16.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603404403
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/simplejson
cp %{_builddir}/simplejson-3.16.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/simplejson/e0d52aebcf1a0f2270f61d29aebbaf29f8c91e2c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/simplejson/e0d52aebcf1a0f2270f61d29aebbaf29f8c91e2c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
