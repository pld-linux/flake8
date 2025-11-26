#
# Conditional build:
%bcond_with	tests	# pytest tests (not in sdist)

Summary:	The modular source code checker: pycodestyle, pyflakes and co.
Summary(pl.UTF-8):	Modularne narzędzie do sprawdzania kodu źródłowego: pycodestyle, pyflakes itp.
Name:		flake8
Version:	7.3.0
Release:	1
License:	MIT
Group:		Development/Tools
#Source0Download: https://pypi.org/simple/flake8/
Source0:	https://files.pythonhosted.org/packages/source/f/flake8/%{name}-%{version}.tar.gz
# Source0-md5:	c32beb4d9f5afb1390586468f455471f
URL:		https://gitlab.com/pycqa/flake8
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:30
%if %{with tests}
BuildRequires:	python3-mccabe >= 0.7.0
BuildRequires:	python3-mccabe < 0.8.0
BuildRequires:	python3-pycodestyle >= 2.14.0
BuildRequires:	python3-pycodestyle < 2.15.0
BuildRequires:	python3-pyflakes >= 3.4.0
BuildRequires:	python3-pyflakes < 3.5.0
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
Requires:	python3-flake8 = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The modular source code checker. It is a wrapper around these tools:
- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

%description -l pl.UTF-8
Modularne narzędzie do sprawdzania kodu źródłowego. Jest to opakowanie
dla narzędzi:
- PyFlakes
- pycodestyle
- skrypt McCabe autorstwa Neda Batcheldera

%package -n python3-flake8
Summary:	The modular source code checker: pycodestyle, pyflakes and co
Summary(pl.UTF-8):	Modularne narzędzie do sprawdzania kodu źródłowego: pycodestyle, pyflakes itp.
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.9

%description -n python3-flake8
The modular source code checker. It is a wrapper around these tools:
- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

%description -n python3-flake8 -l pl.UTF-8
Modularne narzędzie do sprawdzania kodu źródłowego. Jest to opakowanie
dla narzędzi:
- PyFlakes
- pycodestyle
- skrypt McCabe autorstwa Neda Batcheldera

%prep
%setup -q

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest -rw tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/flake8{,-3}
ln -s flake-3 $RPM_BUILD_ROOT%{_bindir}/flake8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/flake8

%files -n python3-flake8
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/flake8-3
%{py3_sitescriptdir}/flake8
%{py3_sitescriptdir}/flake8-%{version}-py*.egg-info
