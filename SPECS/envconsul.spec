Name:           envconsul
Version:        0.5.0
Release:        1%{?dist}
Summary:        envconsul provides a convenient way to populate values from Consul into an child process environment using the envconsul daemon.
Group:          Applications/System
License:        MPLv2.0
URL:            https://github.com/hashicorp/%{name}
Source0:        https://github.com/hashicorp/%{name}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%endif

%description
envconsul provides a convenient way to populate values from Consul into an child process environment using the envconsul daemon.

The daemon envconsul allows applications to be configured with environmental variables, without having knowledge about the existence of Consul. This makes it especially easy to configure applications throughout all your environments: development, testing, production, etc.

envconsul is inspired by envdir in its simplicity, name, and function.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name}_%{version}_linux_amd64/%{name} %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}

%doc

%changelog
* Thu Feb 19 2015 dan phrawzty <phrawzty@mozilla.com>
- init v0.5.0
