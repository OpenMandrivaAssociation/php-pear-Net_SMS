%define		_class		Net
%define		_subclass	SMS
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.2.0
Release:	3
Summary:	SMS functionality
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_SMS/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package provides SMS functionality and access to SMS gateways.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdv2012.0
+ Revision: 741799
- fix major breakage by careless packager

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1
+ Revision: 735175
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-8
+ Revision: 667631
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-7mdv2011.0
+ Revision: 607125
- rebuild

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-6mdv2010.1
+ Revision: 468720
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.0-5mdv2010.0
+ Revision: 426662
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdv2009.1
+ Revision: 321886
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-3mdv2009.0
+ Revision: 224839
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdv2008.1
+ Revision: 178530
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdv2007.0
+ Revision: 82411
- Import php-pear-Net_SMS

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdk
- 0.1.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-1mdk
- initial Mandriva package (PLD import)

