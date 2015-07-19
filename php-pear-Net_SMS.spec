%define	_class	Net
%define	_subclass	SMS
%define	modname	%{_class}_%{_subclass}

Summary:	SMS functionality

Name:		php-pear-%{modname}
Version:	0.2.1
Release:	4
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_SMS/
Source0:	http://download.pear.php.net/package/Net_SMS-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This package provides SMS functionality and access to SMS gateways.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml
%{php_pear_dir}/data/Net_SMS/README


