# NOTE:
# [DEPRECATED] This repository only exists for BC compatibility with old
# versions of Symfony. Recent versions comes with ICU data.

%define		pearname	Icu
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Icu Component
Name:		php-symfony2-Icu
Version:	1.2.2
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	7679e2d3b1235c4cdc343bd2f1213de9
URL:		https://github.com/symfony/Icu
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	libicu >= 4.4
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php-symfony2-Intl >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains the data of the ICU library in a specific version. Use it
through the API of the Intl component.

%prep
%setup -q -n icu-%{version}

mv Resources/data/*.txt .

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{pearname}
cp -a Icu*.php Resources $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md *.txt
%dir %{php_data_dir}/Symfony/Component/Icu
%{php_data_dir}/Symfony/Component/Icu/IcuCurrencyBundle.php
%{php_data_dir}/Symfony/Component/Icu/IcuData.php
%{php_data_dir}/Symfony/Component/Icu/IcuLanguageBundle.php
%{php_data_dir}/Symfony/Component/Icu/IcuLocaleBundle.php
%{php_data_dir}/Symfony/Component/Icu/IcuRegionBundle.php

%dir %{php_data_dir}/Symfony/Component/Icu/Resources
%dir %{php_data_dir}/Symfony/Component/Icu/Resources/data
%dir %{php_data_dir}/Symfony/Component/Icu/Resources/data/curr
%dir %{php_data_dir}/Symfony/Component/Icu/Resources/data/lang
%dir %{php_data_dir}/Symfony/Component/Icu/Resources/data/locales
%dir %{php_data_dir}/Symfony/Component/Icu/Resources/data/region

# TODO: lang tags
%{php_data_dir}/Symfony/Component/Icu/Resources/data/curr/*.res
%{php_data_dir}/Symfony/Component/Icu/Resources/data/lang/*.res
%{php_data_dir}/Symfony/Component/Icu/Resources/data/locales/*.res
%{php_data_dir}/Symfony/Component/Icu/Resources/data/region/*.res
