
%define name	bwm-ng
%define version	0.6
%define rel	3

Summary:	Console-based live network and disk io bandwidth monitor
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
URL:		http://gropp.org/?id=projects&sub=bwm-ng
Source:		http://gropp.org/bwm-ng/bwm-ng-%{version}.tar.gz
# fixes build, from upstream
Patch0:		bwm-ng-fmt+retvalues.patch
License:	GPLv2+
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	ncurses-devel
BuildRequires:	libstatgrab-devel

%description
Bandwidth Monitor NG is a small and simple console-based live
network and disk io bandwidth monitor for Linux, BSD, Solaris, Mac
OS X and others.

Short list of features:
- supports /proc/net/dev, netstat, getifaddr, sysctl, kstat,
  /proc/diskstats, /proc/partitions, IOKit, devstat and libstatgrab
- unlimited number of interfaces/devices supported
- interfaces/devices are added or removed dynamically from list
- white-/blacklist of interfaces/devices
- output of KB/s, Kb/s, packets, errors, average, max and total sum
- output in curses, plain console, CSV or HTML
- configfile

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x --with-ncurses --with-partitions --with-procnetdev --with-libstatgrab
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS THANKS bwm-ng.conf-example bwm-ng.css
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdv2011.0
+ Revision: 610088
- rebuild

* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 0.6-2mdv2010.1
+ Revision: 501440
- fix build (fmt+retvalues.patch from upstream)
- build with libstatgrab support

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6-1mdv2009.0
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 03 2007 Anssi Hannula <anssi@mandriva.org> 0.6-1mdv2008.1
+ Revision: 114538
- initial Mandriva release

