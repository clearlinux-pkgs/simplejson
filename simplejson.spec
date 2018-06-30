#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simplejson
Version  : 3.13.2
Release  : 50
URL      : https://github.com/simplejson/simplejson/archive/v3.13.2.tar.gz
Source0  : https://github.com/simplejson/simplejson/archive/v3.13.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AFL-2.1
Requires: simplejson-python3
Requires: simplejson-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools

%description
simplejson
----------
.. image:: https://travis-ci.org/simplejson/simplejson.svg?branch=master
:target: https://travis-ci.org/simplejson/simplejson

%package legacypython
Summary: legacypython components for the simplejson package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the simplejson package.


%package python
Summary: python components for the simplejson package.
Group: Default
Requires: simplejson-python3

%description python
python components for the simplejson package.


%package python3
Summary: python3 components for the simplejson package.
Group: Default
Requires: python3-core

%description python3
python3 components for the simplejson package.


%prep
%setup -q -n simplejson-3.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528573765
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python setup.py test
%install
export SOURCE_DATE_EPOCH=1528573765
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
