
%define name	bwm-ng
%define version	0.6
%define rel	1

Summary:	Console-based live network and disk io bandwidth monitor
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
URL:		http://gropp.org/?id=projects&sub=bwm-ng
Source:		http://gropp.org/bwm-ng/bwm-ng-%{version}.tar.gz
License:	GPLv2+
Group:		Monitoring
BuildRequires:	ncurses-devel

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

%build
# (anssi 12/2007) also supports --with-libstatgrab, but statgrab not packaged
%configure2_5x --with-ncurses --with-partitions --with-procnetdev
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
