%define	name	perl-Cstools
%define	real_name Cstools
%define	version	3.42
%define	release	%mkrel 11

%define	summary	Tools for dealing with Czech and Slovak texts in Perl

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Development/Perl
URL:            http://www.fi.muni.cz/~adelton/perl/
Source0:        %real_name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:	perl-devel
Requires:       perl
BuildArch:	noarch

%description
This package includes modules that are useful when dealing with Czech (and
Slovak) texts in Perl.

%prep
%setup -q -n %{real_name}-%{version}

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

