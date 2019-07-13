#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bandit
Version  : 1.6.2
Release  : 38
URL      : https://files.pythonhosted.org/packages/05/51/cbfd4b5a383d51a73a9e8cbf152037a212e0058ee8b329d4501f74cdddef/bandit-1.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/51/cbfd4b5a383d51a73a9e8cbf152037a212e0058ee8b329d4501f74cdddef/bandit-1.6.2.tar.gz
Summary  : Python security linter from OpenStack Security
Group    : Development/Tools
License  : Apache-2.0
Requires: bandit-bin = %{version}-%{release}
Requires: bandit-license = %{version}-%{release}
Requires: bandit-python = %{version}-%{release}
Requires: bandit-python3 = %{version}-%{release}
Requires: GitPython
Requires: PyYAML
Requires: colorama
Requires: six
Requires: stevedore
BuildRequires : GitPython
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : pbr
BuildRequires : six
BuildRequires : stevedore

%description
.. image:: https://github.com/PyCQA/bandit/blob/master/logo/logotype-sm.png
:alt: Bandit

%package bin
Summary: bin components for the bandit package.
Group: Binaries
Requires: bandit-license = %{version}-%{release}

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
Requires: bandit-python3 = %{version}-%{release}

%description python
python components for the bandit package.


%package python3
Summary: python3 components for the bandit package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bandit package.


%prep
%setup -q -n bandit-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562029450
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bandit
cp LICENSE %{buildroot}/usr/share/package-licenses/bandit/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bandit/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
