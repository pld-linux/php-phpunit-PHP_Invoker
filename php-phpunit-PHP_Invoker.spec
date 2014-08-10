%define		status		stable
%define		pearname	PHP_Invoker
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Utility class for invoking callables with a timeout
Name:		php-phpunit-PHP_Invoker
Version:	1.1.3
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	b2bd440322f98b21b87c1b8b5288e4ad
URL:		http://pear.phpunit.de/package/PHP_Invoker/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(pcntl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-PHP_Timer >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility class for invoking callables with a timeout.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/PHP_Invoker/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PHP/Invoker.php
%{php_pear_dir}/PHP/Invoker
