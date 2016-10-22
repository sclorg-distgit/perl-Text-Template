%{?scl:%scl_package perl-Text-Template}

Name:           %{?scl_prefix}perl-Text-Template
Version:        1.46
Release:        6%{?dist}
Summary:        Expand template text with embedded Perl

Group:          Development/Libraries
# See CPAN RT#102523
# lib/Text/Template.pm: (GPL+ or Artistic) and (GPLv2+ or Artistic)
# other files:          (GPLv2+ or Artistic)
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic)
URL:            http://search.cpan.org/dist/Text-Template/
Source0:        http://www.cpan.org/authors/id/M/MJ/MJD/Text-Template-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests:
BuildRequires:  %{?scl_prefix}perl(lib)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A 'template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
'fill in' a template, you evaluate the little programs and replace
them with their values.


%prep
%setup -q -n Text-Template-%{version}


%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}


%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} '}make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Artistic COPYING README
%{perl_vendorlib}/Text/
%{_mandir}/man3/*.3pm*


%changelog
* Wed Jul 20 2016 Petr Pisar <ppisar@redhat.com> - 1.46-6
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-2
- Perl 5.22 rebuild

* Fri Mar 27 2015 Tom Callawau <spot@fedoraproject.org> - 1.46-1
- update to 1.46

* Fri Mar 06 2015 Petr Pisar <ppisar@redhat.com> - 1.45-18
- Correct license declaration to ((GPL+ or Artistic) and (GPLv2+ or Artistic))
  (bug #1198991)

* Thu Jan 15 2015 Petr Pisar <ppisar@redhat.com> - 1.45-17
- Specify all dependencies

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.45-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.45-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.45-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.45-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.45-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.45-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 23 2008 Ralf Corsépius <rc040203@freenet.de> - 1.45-1
- Upstream update.
- Abandon perl-Text-Template-perl510-fixtest09.patch.

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.44-6
- fix test 09 for perl5.10

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.44-5
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.44-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.44-4
- Rebuild for FC6.

* Thu Feb 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.44-3
- Rebuild for FC5 (perl 5.8.8).

* Thu Aug 25 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.44-2
- Removed the explicit perl build requirement.

* Wed Aug 10 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.44-1
- Update to Fedora Extras template.

* Sat Dec 18 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.44-0.fdr.1
- First build.
