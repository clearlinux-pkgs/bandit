#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bandit
Version  : 0.13.2
Release  : 3
URL      : https://pypi.python.org/packages/source/b/bandit/bandit-0.13.2.tar.gz
Source0  : https://pypi.python.org/packages/source/b/bandit/bandit-0.13.2.tar.gz
Summary  : Security oriented static analyser for python code.
Group    : Development/Tools
License  : Apache-2.0
Requires: bandit-bin
Requires: bandit-python
Requires: bandit-data
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : appdirs-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : fixtures-python
BuildRequires : hacking
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2-python
BuildRequires : unittest2-python
Patch1: 0001-use-our-hacking-version.patch

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
Requires: PyYAML-python
Requires: appdirs-python
Requires: stevedore

%description python
python components for the bandit package.


%prep
%setup -q -n bandit-0.13.2
%patch1 -p1

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

%files data
%defattr(-,root,root,-)
/usr/share/bandit/wordlist/default-passwords
/usr/share/defaults/bandit/bandit.yaml

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
