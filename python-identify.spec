%global pypi_name identify

Name:		python-%{pypi_name}
Version:	2.6.15
Release:	1
Summary:	File identification library for Python
Group:		Development/Python
License:	MIT
URL:		https://github.com/pre-commit/identify
Source0:	https://files.pythonhosted.org/packages/source/i/identify/identify-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)

%description
File identification library for Python.

Given a file (or some information about a file), return a set of
standardized tags identifying what the file is.

%files -n python-%{pypi_name}
%license LICENSE identify/vendor/licenses.py
%doc README.md
%{_bindir}/identify-cli
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py%{pyver}.egg-info
