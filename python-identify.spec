%define module identify

Name:		python-identify
Version:	2.6.19
Release:	1
Summary:	File identification library for Python
Group:		Development/Python
License:	MIT
URL:		https://github.com/pre-commit/identify
Source0:	https://files.pythonhosted.org/packages/source/i/identify/identify-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)

%description
File identification library for Python.

Given a file (or some information about a file), return a set of
standardized tags identifying what the file is.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE
%{_bindir}/identify-cli
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
