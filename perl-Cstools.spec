%define	upstream_name    Cstools
%define upstream_version 3.44
Name:		perl-%{upstream_name}
Version:	3.44
Release:	1

Summary:	Tools for dealing with Czech and Slovak texts in Perl
License:	GPL
Group:		Development/Perl
Url:		https://www.fi.muni.cz/~adelton/perl/
Source0:	https://cpan.metacpan.org/authors/id/J/JA/JANPAZ/Cstools-3.44.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This package includes modules that are useful when dealing with Czech (and
Slovak) texts in Perl.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc README
%{_bindir}/*
%dir %{perl_vendorlib}/Cz
%{perl_vendorlib}/Cz/*
%{_mandir}/*/*


