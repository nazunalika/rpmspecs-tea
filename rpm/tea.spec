# TODO: Add the autocomplete scripts
%global major_version 0
%global minor_version 9
%global micro_version 2
%define debug_package %{nil}

Name:		tea
Version:	%{major_version}.%{minor_version}.%{micro_version}
Release:	1%{?dist}
Summary:	The official CLI for Gitea
License:	MIT
URL:		https://gitea.com/gitea/tea
Source0:	https://gitea.com/gitea/tea/archive/v%{version}.tar.gz

BuildRequires:	go >= 1.16.0
BuildRequires:	git
BuildRequires:	make
BuildRequires:	go-srpm-macros
Requires: git

%description
Tea is the official CLI tool for Gitea. It can be used to manage most entities
on one or more Gitea instances and provides local helpers like
'tea pull checkout'

%prep
%setup -q -n %{name}

%build
go mod vendor
make

%install
install -D -m 755 tea $RPM_BUILD_ROOT%{_bindir}/tea

%files
%{_bindir}/tea

%changelog
* Tue Feb 28 2023 Louis Abel <tucklesepk@gmail.com> - 0.9.2-1
- Rebase to 0.9.2

* Wed Jan 11 2023 Louis Abel <tucklesepk@gmail.com> - 0.9.0-1
- Rebase to 0.9.0

* Fri Feb 11 2022 Louis Abel <tucklesepk@gmail.com> - 0.8.0-1
- Initial release of 0.8.0 for Fedora and Enterprise Linux
