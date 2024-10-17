%define source_date 20110211

Name: mandriva-galaxy-data
Summary: Mandriva Galaxy data files
Version: 2011.0
Release: 8
URL: https://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/mandriva-galaxy-kde4
Group: System/Configuration/Other
BuildRoot: %{_tmppath}/%{name}-%{version}.%{source_date}-buildroot
Source0: %{name}-%{version}.%{source_date}.tar.bz2
License: GPL
BuildArch: noarch
BuildRequires: intltool
Requires: mandriva-galaxy

Conflicts: mandriva-galaxy < 2:2009.0

%description
This package groups all Mandriva Galaxy data files (html files show at startup)

%prep
%setup -q -n mandriva-galaxy-data

%build
./create_galaxy_index.sh

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_datadir}/mdk/mandrivagalaxy

# do not package .xcf file
rm -f style/images/BDO-GALAXY.xcf

cp -a html/*.html %{buildroot}/%{_datadir}/mdk/mandrivagalaxy
cp -a style %{buildroot}/%{_datadir}/mdk/mandrivagalaxy
cp -a mandrivagalaxy.png %{buildroot}/%{_datadir}/mdk/mandrivagalaxy

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/mdk/mandrivagalaxy
%{_datadir}/mdk/mandrivagalaxy/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2011.0-2mdv2011.0
+ Revision: 666383
- mass rebuild

* Fri Feb 11 2011 Eugeni Dodonov <eugeni@mandriva.com> 2011.0-1
+ Revision: 637337
- Updated for 2011 alpha.

* Mon Jun 07 2010 Anne Nicolas <ennael@mandriva.org> 2010.1-6mdv2010.1
+ Revision: 547203
- updates po files

* Wed May 26 2010 Anne Nicolas <ennael@mandriva.org> 2010.1-5mdv2010.1
+ Revision: 546315
- update translations

* Tue May 25 2010 Anne Nicolas <ennael@mandriva.org> 2010.1-4mdv2010.1
+ Revision: 545906
- more translation updates

* Fri May 21 2010 Anne Nicolas <ennael@mandriva.org> 2010.1-3mdv2010.1
+ Revision: 545587
- first update for 2010 Spring text

* Tue May 04 2010 Anne Nicolas <ennael@mandriva.org> 2010.1-2mdv2010.1
+ Revision: 541985
- update more images

* Sun May 02 2010 Anne Nicolas <ennael@mandriva.org> 2010.1-1mdv2010.1
+ Revision: 541681
- update for 2010 Spring

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-4mdv2010.1
+ Revision: 523267
- rebuilt for 2010.1

* Fri Oct 30 2009 Anne Nicolas <ennael@mandriva.org> 2010.0-3mdv2010.0
+ Revision: 460233
- fix localisation

* Thu Oct 29 2009 Anne Nicolas <ennael@mandriva.org> 2010.0-2mdv2010.0
+ Revision: 459947
- update images for 2010

* Mon Oct 26 2009 Anne Nicolas <ennael@mandriva.org> 2010.0-1mdv2010.0
+ Revision: 459364
- first update for 2010 (text only)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.1-13mdv2010.0
+ Revision: 426073
- rebuild

  + Arthur Renato Mello <arthur@mandriva.com>
    - Update translation files

* Mon Apr 20 2009 Arthur Renato Mello <arthur@mandriva.com> 2009.1-11mdv2009.1
+ Revision: 368460
- Adding updated translation files

* Thu Apr 16 2009 Arthur Renato Mello <arthur@mandriva.com> 2009.1-10mdv2009.1
+ Revision: 367737
- Add BuildRequires for intltool
  Change from 2009.0 to 2009.1
- Update package with new translation files
- Add support to new index.html translation using po files

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-7mdv2009.1
+ Revision: 351564
- rebuild

* Thu Oct 02 2008 Anne Nicolas <ennael@mandriva.org> 2009.0-6mdv2009.0
+ Revision: 290876
- bump release
- fix typo in text

* Thu Oct 02 2008 Anne Nicolas <ennael@mandriva.org> 2009.0-5mdv2009.0
+ Revision: 290802
- update mandriva-alaxy for 2009

* Wed Sep 10 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-4mdv2009.0
+ Revision: 283524
- New snapshot, improved screen captures

* Tue Aug 26 2008 Anne Nicolas <ennael@mandriva.org> 2009.0-3mdv2009.0
+ Revision: 276211
- bump release
- Update images for 2009

* Sat Aug 16 2008 Anne Nicolas <ennael@mandriva.org> 2009.0-2mdv2009.0
+ Revision: 272663
- bump release
- add require

* Fri Aug 15 2008 Arthur Renato Mello <arthur@mandriva.com> 2009.0-1mdv2009.0
+ Revision: 272381
- import mandriva-galaxy-data


