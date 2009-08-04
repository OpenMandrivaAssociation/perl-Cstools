%define	upstream_name    Cstools
%define	upstream_version 3.42

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Tools for dealing with Czech and Slovak texts in Perl
License:    GPL
Group:      Development/Perl
Url:        http://www.fi.muni.cz/~adelton/perl/
Source0:    %{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This package includes modules that are useful when dealing with Czech (and
Slovak) texts in Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %buildroot
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%dir %{perl_vendorlib}/Cz
%{perl_vendorlib}/Cz/*
%{_mandir}/*/*
