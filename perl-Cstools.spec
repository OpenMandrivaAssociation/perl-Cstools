%define	upstream_name    Cstools
%define	upstream_version 3.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Tools for dealing with Czech and Slovak texts in Perl
License:	GPL
Group:		Development/Perl
Url:		http://www.fi.muni.cz/~adelton/perl/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This package includes modules that are useful when dealing with Czech (and
Slovak) texts in Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 3.420.0-2mdv2011.0
+ Revision: 680873
- mass rebuild

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.420.0-1mdv2011.0
+ Revision: 409039
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.42-11mdv2009.0
+ Revision: 256397
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.42-9mdv2008.1
+ Revision: 131445
- kill re-definition of %%buildroot on Pixel's request


* Sat Dec 03 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 3.42-9mdk
- mkrel

* Fri Nov 19 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 3.42-8mdk
- rebuild for new perl

* Mon Sep 06 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 3.42-7mdk
- rebuild

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.42-6mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Wed May 14 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 3.42-5mdk
- rebuild for new perl provides/requires

* Sun Apr 27 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 3.42-4mdk
- add missing dir into files section (mr. distlint)

* Sun Apr 13 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 3.42-3mdk
- added checking about buildroot
- changed BuildaArch to noarch

* Sat Apr 12 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 3.42-2mdk
- ops, fixed spec name..

* Sat Apr 12 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 3.42-1mdk
- initial import into Mandrake, thanks for inspiration by Lubomir Sedlacik

