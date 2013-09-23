%define		pearname	Icu
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Icu Component
Name:		php-symfony2-Icu
Version:	1.2.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/Icu/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	c8f4620029e716602d3c0699a0ae2569
URL:		https://github.com/symfony/Icu
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	libicu >= 4.4
Requires:	php(core) >= %{php_min_version}
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-Intl >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains the data of the ICU library in a specific version. Use it
through the API of the Intl component.

%prep
%setup -q -n %{pearname}-%{version}

mv Resources/data/*.txt .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/Icu
cp -a Icu*.php Resources $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/Icu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md *.txt
%dir %{php_pear_dir}/Symfony/Component/Icu
%{php_pear_dir}/Symfony/Component/Icu/IcuCurrencyBundle.php
%{php_pear_dir}/Symfony/Component/Icu/IcuData.php
%{php_pear_dir}/Symfony/Component/Icu/IcuLanguageBundle.php
%{php_pear_dir}/Symfony/Component/Icu/IcuLocaleBundle.php
%{php_pear_dir}/Symfony/Component/Icu/IcuRegionBundle.php

%dir %{php_pear_dir}/Symfony/Component/Icu/Resources
%dir %{php_pear_dir}/Symfony/Component/Icu/Resources/data
%dir %{php_pear_dir}/Symfony/Component/Icu/Resources/data/curr
%dir %{php_pear_dir}/Symfony/Component/Icu/Resources/data/lang
%dir %{php_pear_dir}/Symfony/Component/Icu/Resources/data/locales
%dir %{php_pear_dir}/Symfony/Component/Icu/Resources/data/region

# TODO: lang tags
%{php_pear_dir}/Symfony/Component/Icu/Resources/data/curr/*.res
%{php_pear_dir}/Symfony/Component/Icu/Resources/data/lang/*.res
%{php_pear_dir}/Symfony/Component/Icu/Resources/data/locales/*.res
%{php_pear_dir}/Symfony/Component/Icu/Resources/data/region/*.res
