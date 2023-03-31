# Created by pyp2rpm-3.3.5
%global pypi_name identify

Name:		python-%{pypi_name}
Version:	1.5.12
Release:	3
Summary:	File identification library for Python
Group:		Development/Python
License:	MIT
URL:		https://github.com/pre-commit/identify
Source0:	%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%description
[![Build Status]( [![Azure DevOps coverage]( [![pre-commit.ci status]( [![PyPI
version](

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%license LICENSE identify/vendor/licenses.py
%doc README.md
%{_bindir}/identify-cli
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
