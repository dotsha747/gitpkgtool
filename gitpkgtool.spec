%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name: gitpkgtool
Summary: A tool to assist project versioning and packaging with git
Version:
Vendor: http://home.abubakar.net
Release: 1
License: GPL
Group: Development/Tools
Source:
URL: http://home.abubakar.net/pubdoc

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*

%changelog
