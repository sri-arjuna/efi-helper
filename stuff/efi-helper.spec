Name:           efi-helper
Version:        0.3.9
Release:        3%{?dist}
Summary:        Help to work around EFI issues

License:        GPLv3
URL:            https://github.com/sri-arjuna/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

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
* Wed Nov 26 2014 Simon A. Erat <erat.simon@gmail.com> 0.3.9
- TUI had changed name for tui-value-* to tui-conf-*
- Windows is now ver 8.1
- Fixed 'efi' file for fedora

* Fri Oct 24 2014 Simon A. Erat <erat.simon@gmail.com> 0.0.5
- Initial package
