%define upstream_name    Term-StatusBar
%define upstream_version 1.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dynamic progress bar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Term::Size)

BuildArch:	noarch

%description
Term::StatusBar provides an easy way to create a terminal status bar, much
like those found in a graphical environment. Term::Size is used to ensure
the bar does not extend beyond the terminal's width. All outout is sent to
STDOUT by default.

%prep
%setup -q -n %{upstream_name}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.180.0-2mdv2011.0
+ Revision: 655222
- rebuild for updated spec-helper

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2011.0
+ Revision: 485964
- import perl-Term-StatusBar


* Sun Jan 03 2010 cpan2dist 1.18-1mdv
- initial mdv release, generated with cpan2dist
