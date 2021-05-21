#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-curry
Version  : 1.001000
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/curry-1.001000.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/curry-1.001000.tar.gz
Summary  : 'Create automatic curried method call closures for any class or object'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-curry-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
curry - Create automatic curried method call closures for any class or
object

%package dev
Summary: dev components for the perl-curry package.
Group: Development
Provides: perl-curry-devel = %{version}-%{release}
Requires: perl-curry = %{version}-%{release}

%description dev
dev components for the perl-curry package.


%package perl
Summary: perl components for the perl-curry package.
Group: Default
Requires: perl-curry = %{version}-%{release}

%description perl
perl components for the perl-curry package.


%prep
%setup -q -n curry-1.001000
cd %{_builddir}/curry-1.001000

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/curry.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/curry.pm
/usr/lib/perl5/vendor_perl/5.34.0/curry/weak.pm
