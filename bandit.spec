#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : bandit
Version  : 1.4.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/45/b2/f5a4adb1e7773e6d631481b784ad49e6ec56aa81e9fdafcabf0fe3e0241a/bandit-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/b2/f5a4adb1e7773e6d631481b784ad49e6ec56aa81e9fdafcabf0fe3e0241a/bandit-1.4.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/45/b2/f5a4adb1e7773e6d631481b784ad49e6ec56aa81e9fdafcabf0fe3e0241a/bandit-1.4.0.tar.gz.asc
Summary  : Security oriented static analyser for python code.
Group    : Development/Tools
License  : Apache-2.0
Requires: bandit-bin
Requires: bandit-python3
Requires: bandit-license
Requires: bandit-python
Requires: GitPython
Requires: PyYAML
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
======

%package bin
Summary: bin components for the bandit package.
Group: Binaries
Requires: bandit-license

%description bin
bin components for the bandit package.


%package license
Summary: license components for the bandit package.
Group: Default

%description license
license components for the bandit package.


%package python
Summary: python components for the bandit package.
Group: Default
Requires: bandit-python3

%description python
python components for the bandit package.


%package python3
Summary: python3 components for the bandit package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bandit package.


%prep
%setup -q -n bandit-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532377627
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/bandit
cp LICENSE %{buildroot}/usr/share/doc/bandit/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bandit
/usr/bin/bandit-baseline
/usr/bin/bandit-config-generator

%files license
%defattr(-,root,root,-)
/usr/share/doc/bandit/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
