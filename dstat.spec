Summary:	Versatile resource statistics tool
Summary(pl):	Uniwersalne narz�dzie do monitorowania u�ycia zasob�w
Name:		dstat
Version:	0.6.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dag.wieers.com/home-made/dstat/%{name}-%{version}.tar.bz2
# Source0-md5:	aad1d918a982d8392a24a06760175e93
URL:		http://dag.wieers.com/home-made/dstat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dstat is a versatile replacement for vmstat, iostat, netstat, nfsstat
and ifstat. Dstat overcomes some of their limitations and adds some
extra features, more counters and flexibility. Dstat is handy for
monitoring systems during performance tuning tests, benchmarks or
troubleshooting.

Dstat allows you to view all of your system resources instantly, you
can eg. compare disk usage in combination with interrupts from your
IDE controller, or compare the network bandwidth numbers directly with
the disk throughput (in the same interval).

%description -l pl
Dstat jest uniwersalnym zamiennikiem za vmstat, iostat, netstat,
nfsstat oraz ifstat. Dstat omija niekt�re z ich ogranicze� i dodaje
nowe funkcjonalno�ci, wi�cej licznik�w i elastyczno��. Dstat jest
wygodny w monitorowaniu system�w podczas test�w, benchmark�w lub
rozwi�zywania problem�w wydajno�ciowych.

Dstat pozwala ogl�da� wszystkie zasoby jednocze�nie, np. zestawi�
u�ycie dysku ze statystykami przerwa� kontrolera IDE, lub por�wna�
wykorzystanie ��cza bezpo�rednio z wykorzystaniem dysk�w (w takim
samym interwale czasowym).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/*.html docs/*.txt examples/ dstat.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/dstat/
