#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Hooks-OP-Check
Version  : 0.22
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-OP-Check-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-OP-Check-0.22.tar.gz
Summary  : 'Wrap OP check callbacks'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-B-Hooks-OP-Check-license = %{version}-%{release}
Requires: perl-B-Hooks-OP-Check-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Depends)

%description
This archive contains the distribution B-Hooks-OP-Check,
version 0.22:
Wrap OP check callbacks

%package dev
Summary: dev components for the perl-B-Hooks-OP-Check package.
Group: Development
Provides: perl-B-Hooks-OP-Check-devel = %{version}-%{release}
Requires: perl-B-Hooks-OP-Check = %{version}-%{release}

%description dev
dev components for the perl-B-Hooks-OP-Check package.


%package license
Summary: license components for the perl-B-Hooks-OP-Check package.
Group: Default

%description license
license components for the perl-B-Hooks-OP-Check package.


%package perl
Summary: perl components for the perl-B-Hooks-OP-Check package.
Group: Default
Requires: perl-B-Hooks-OP-Check = %{version}-%{release}

%description perl
perl components for the perl-B-Hooks-OP-Check package.


%prep
%setup -q -n B-Hooks-OP-Check-0.22
cd %{_builddir}/B-Hooks-OP-Check-0.22

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-Hooks-OP-Check
cp %{_builddir}/B-Hooks-OP-Check-0.22/LICENCE %{buildroot}/usr/share/package-licenses/perl-B-Hooks-OP-Check/16031c2d4c62ec1d2d159358d2bf163af42055ef
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
/usr/share/man/man3/B::Hooks::OP::Check.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-B-Hooks-OP-Check/16031c2d4c62ec1d2d159358d2bf163af42055ef

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/B/Hooks/OP/Check.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/B/Hooks/OP/Check/Install/Files.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/B/Hooks/OP/Check/Install/hook_op_check.h
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/B/Hooks/OP/Check/Check.so
