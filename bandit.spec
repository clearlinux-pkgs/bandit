#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bandit
Version  : 0.17.3
Release  : 9
URL      : http://tarballs.openstack.org/bandit/bandit-0.17.3.tar.gz
Source0  : http://tarballs.openstack.org/bandit/bandit-0.17.3.tar.gz
Summary  : Security oriented static analyser for python code.
Group    : Development/Tools
License  : Apache-2.0
Requires: bandit-bin
Requires: bandit-python
Requires: bandit-data
BuildRequires : PyYAML
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : funcsigs-python
BuildRequires : git-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyrsistent-python
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
A security linter from OpenStack Security
* Free software: Apache license
* Documentation: https://wiki.openstack.org/wiki/Security/Projects/Bandit
* Source: https://git.openstack.org/cgit/openstack/bandit
* Bugs: https://bugs.launchpad.net/bandit

%package bin
Summary: bin components for the bandit package.
Group: Binaries
Requires: bandit-data

%description bin
bin components for the bandit package.


%package data
Summary: data components for the bandit package.
Group: Data

%description data
data components for the bandit package.


%package python
Summary: python components for the bandit package.
Group: Default
Requires: six-python
Requires: stevedore

%description python
python components for the bandit package.


%prep
%setup -q -n bandit-0.17.3

%build
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
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/bandit
mv %{buildroot}/usr/etc/bandit/* %{buildroot}/usr/share/defaults/bandit
rm -rf %{buildroot}/usr/etc
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bandit
/usr/bin/bandit-baseline
/usr/bin/bandit-config-generator

%files data
%defattr(-,root,root,-)
/usr/share/bandit/wordlist/default-passwords
/usr/share/defaults/bandit/bandit.yaml

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
