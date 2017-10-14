#
# RPM Spec file for the PMDA++ project.
#

# Note, the following _pmdasdir definition should (does) match the one defined
# in the PCP project's build/rpm/fedora.spec file.
%global _pmdasdir %{_localstatedir}/lib/pcp/pmdas

Summary: PMDA++ Library
Name: pcp-pmda-cpp
Version: 0.4.5
Release: 1%{?dist}
License: Boost
Group: System Environment/Libraries
Source: https://github.com/pcolby/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/pcolby/%{name}

BuildRequires: boost-devel >= 1.32
BuildRequires: cmake >= 2.6
BuildRequires: gtest-devel
BuildRequires: pcp pcp-libs-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PMDA++ is a header-only library that allows developers to write Performance
Metrics Domain Agents (PMDAs) for Performance Co-Pilot (PCP) in C++.

%prep
%setup -c -q

%build
%{cmake} %{name}-%{version}
%{__make} %{?_smp_mflags}

%install
%if 0%{?rhel} < 6
%{__rm} -rf %{buildroot}
%endif
%{__make} install DESTDIR=%{buildroot}

%check
%{__make} check

%if 0%{?rhel} < 6
%clean
%{__rm} -rf %{buildroot}
%endif

%package devel
Summary: Development headers for the PMDA++ library
Group: Development/Libraries
Provides: %{name}-static = %{version}-%{release}
Requires: pcp-libs-devel%{?_isa}

%description devel
PMDA++ is a header-only library that allows developers to write Performance
Metrics Domain Agents (PMDAs) for Performance Co-Pilot (PCP) in C++.

%package examples
Summary: Examples for the PMDA++ library
Group: Development/Libraries
Requires: pcp

%description examples
Examples from the PMDA++ project.

%files devel
%doc %{name}-%{version}/CHANGELOG.md
%doc %{name}-%{version}/README.md
%{_includedir}/pcp-cpp
%{license} %{name}-%{version}/LICENSE.md

%files examples
%{_pmdasdir}/%{name}-examples

%changelog
* Sun Oct 15 2017 Paul Colby <git@colby.id.au> - 0.4.5-1
- updated to pcp-pmda-cpp 0.4.5.

* Sat Oct 14 2017 Paul Colby <git@colby.id.au> - 0.4.4-1
- updated to pcp-pmda-cpp 0.4.4.

* Tue Jul 12 2016 Paul Colby <git@colby.id.au> - 0.4.3-1
- updated to pcp-pmda-cpp 0.4.3.

* Sat Mar 14 2015 Paul Colby <git@colby.id.au> - 0.4.2-1
- updated to pcp-pmda-cpp 0.4.2.

* Sat Sep 06 2014 Paul Colby <git@colby.id.au> - 0.4.1-1
- updated to pcp-pmda-cpp 0.4.1.

* Thu May 15 2014 Paul Colby <git@colby.id.au> - 0.4.0-1
- updated to pcp-pmda-cpp 0.4.0.

* Sat May 10 2014 Paul Colby <git@colby.id.au> - 0.3.4-1
- updated to pcp-pmda-cpp 0.3.4.

* Tue Feb 18 2014 Paul Colby <git@colby.id.au> - 0.3.3-1
- updated to pcp-pmda-cpp 0.3.3.

* Sun Feb 16 2014 Paul Colby <git@colby.id.au> - 0.3.2-1
- updated to pcp-pmda-cpp 0.3.2.

* Fri Feb 14 2014 Paul Colby <git@colby.id.au> - 0.3.1-1
- initial pcp-pmda-cpp spec file.
