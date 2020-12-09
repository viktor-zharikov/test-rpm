Name:       helloprog
Version:    1.0
Release:    1
Summary:    helloprog
License:    -
Source0:    helloprog
BuildRoot:  %{_tmppath}/%{name}


%description
print Hello RAIDIX! in stdout, wtite on bash.
This programm install at /usr/local/bin/.


%install
install -D -pm 755 %{SOURCE0} %{buildroot}/usr/local/bin/helloprog

%files
%defattr(755,root,root)
/usr/local/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Dec 9 2020 <user>
- Add bin file
