Name:           efi-helper
Version:        0.3.1
Release:        0%{?dist}
Summary:        Help to work around EFI issues

License:        GPLv3
URL:            https://github.com/sri-arjuna/%{name}
Source0:        %{name}-%{version}.tar.gz

Requires:       tui


%description
A little wrapper for some tasks related
to workarounds with EFI issues

%prep
%setup -q -c %{name}-%{version}

%build
# Nothing to do

%install
rm -rf $RPM_BUILD_ROOT
##%make_install

mkdir -p %{buildroot}%{_bindir}/ \
         %{buildroot}%{_datarootdir}/%{name}
rm -fr %{name}/.git
rm -fr build-rpm-efi-helper.sh
mv %{name}/efi-helper.sh %{buildroot}%{_bindir}/efi-helper
mv %{name}/[RL]*  %{buildroot}%{_datarootdir}/%{name}

%files
%doc %{_datarootdir}/%{name}/README.md 
%doc %{_datarootdir}/%{name}/LICENSE
%{_bindir}/efi-helper

%changelog
* Fri Oct 24 2014 Simon A. Erat <erat.simon@gmail.com> 0.0.5
- Initial package
