#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Dumper
Summary:	Catalyst::Plugin::Dumper - Data::Dumper plugin for Catalyst
Summary(pl.UTF-8):	Catalyst::Plugin::Dumper - wtyczka Data::Dumper dla Catalysta
Name:		perl-Catalyst-Plugin-Dumper
Version:	0.000002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CH/CHISEL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	adaa5284e011ebeef369327682c64597
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Dumper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-version
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin injects a dumper() method into the Catalyst::Log
namespace.

%description -l pl.UTF-8
Ta wtyczka wprowadza metodę dumper() do przestrzeni nazw
Catalyst::Log.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{_mandir}/man3/*
