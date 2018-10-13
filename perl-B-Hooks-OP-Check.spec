#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Hooks-OP-Check
Version  : 0.22
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-OP-Check-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-OP-Check-0.22.tar.gz
Summary  : 'Wrap OP check callbacks'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-B-Hooks-OP-Check-data = %{version}-%{release}
Requires: perl-B-Hooks-OP-Check-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Depends)

%description
This archive contains the distribution B-Hooks-OP-Check,
version 0.22:
Wrap OP check callbacks

%package data
Summary: data components for the perl-B-Hooks-OP-Check package.
Group: Data

%description data
data components for the perl-B-Hooks-OP-Check package.


%package dev
Summary: dev components for the perl-B-Hooks-OP-Check package.
Group: Development
Requires: perl-B-Hooks-OP-Check-lib = %{version}-%{release}
Requires: perl-B-Hooks-OP-Check-data = %{version}-%{release}
Provides: perl-B-Hooks-OP-Check-devel = %{version}-%{release}

%description dev
dev components for the perl-B-Hooks-OP-Check package.


%package lib
Summary: lib components for the perl-B-Hooks-OP-Check package.
Group: Libraries
Requires: perl-B-Hooks-OP-Check-data = %{version}-%{release}

%description lib
lib components for the perl-B-Hooks-OP-Check package.


%prep
%setup -q -n B-Hooks-OP-Check-0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-Hooks-OP-Check
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-B-Hooks-OP-Check/LICENCE
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
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/B/Hooks/OP/Check.pm
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/B/Hooks/OP/Check/Install/Files.pm
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/B/Hooks/OP/Check/Install/hook_op_check.h

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-B-Hooks-OP-Check/LICENCE

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::Hooks::OP::Check.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/B/Hooks/OP/Check/Check.so
