#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simplejson
Version  : 3.10.0
Release  : 29
URL      : https://github.com/simplejson/simplejson/archive/v3.10.0.tar.gz
Source0  : https://github.com/simplejson/simplejson/archive/v3.10.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AFL-2.1
Requires: simplejson-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
simplejson
----------
.. image:: https://travis-ci.org/simplejson/simplejson.svg?branch=master
:target: https://travis-ci.org/simplejson/simplejson

%package python
Summary: python components for the simplejson package.
Group: Default

%description python
python components for the simplejson package.


%prep
%setup -q -n simplejson-3.10.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
