#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bandit
Version  : 1.1.0
Release  : 20
URL      : http://tarballs.openstack.org/bandit/bandit-1.1.0.tar.gz
Source0  : http://tarballs.openstack.org/bandit/bandit-1.1.0.tar.gz
Summary  : Security oriented static analyser for python code.
Group    : Development/Tools
License  : Apache-2.0
Requires: bandit-bin
Requires: bandit-python
BuildRequires : PyYAML
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testtools
BuildRequires : testtools-python

%description
Bandit
======
.. image:: https://img.shields.io/pypi/v/bandit.svg
:target: https://pypi.python.org/pypi/bandit/
:alt: Latest Version

%package bin
Summary: bin components for the bandit package.
Group: Binaries

%description bin
bin components for the bandit package.


%package python
Summary: python components for the bandit package.
Group: Default
Requires: six-python
Requires: stevedore

%description python
python components for the bandit package.


%prep
%setup -q -n bandit-1.1.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bandit
/usr/bin/bandit-baseline
/usr/bin/bandit-config-generator

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
