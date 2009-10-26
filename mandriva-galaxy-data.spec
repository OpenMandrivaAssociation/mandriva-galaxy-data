%define source_date 20091026

Name: mandriva-galaxy-data
Summary: Mandriva Galaxy data files
Version: 2010.0
Release: %mkrel 1
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/mandriva-galaxy-kde4
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

cp -a html/*.html %{buildroot}/%{_datadir}/mdk/mandrivagalaxy
cp -a style %{buildroot}/%{_datadir}/mdk/mandrivagalaxy
cp -a mandrivagalaxy.png %{buildroot}/%{_datadir}/mdk/mandrivagalaxy

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/mdk/mandrivagalaxy
%{_datadir}/mdk/mandrivagalaxy/*
