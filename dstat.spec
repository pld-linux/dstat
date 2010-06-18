Summary:	Versatile resource statistics tool
Summary(pl.UTF-8):	Uniwersalne narzędzie do monitorowania użycia zasobów
Name:		dstat
Version:	0.7.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dag.wieers.com/home-made/dstat/%{name}-%{version}.tar.bz2
# Source0-md5:	bfea4dc8037a0b18fc40a4dfc104dcc8
URL:		http://dag.wieers.com/home-made/dstat/
BuildRequires:	rpm-pythonprov
Requires:	python
Requires:	python-modules
BuildArch:	noarch
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

%description -l pl.UTF-8
Dstat jest uniwersalnym zamiennikiem za vmstat, iostat, netstat,
nfsstat oraz ifstat. Dstat omija niektóre z ich ograniczeń i dodaje
nowe funkcjonalności, więcej liczników i elastyczność. Dstat jest
wygodny w monitorowaniu systemów podczas testów, benchmarków lub
rozwiązywania problemów wydajnościowych.

Dstat pozwala oglądać wszystkie zasoby jednocześnie, np. zestawić
użycie dysku ze statystykami przerwań kontrolera IDE, lub porównać
wykorzystanie łącza bezpośrednio z wykorzystaniem dysków (w takim
samym interwale czasowym).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# broken symlink
rm -f examples/dstat.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO docs/*.html docs/*.txt examples/
%attr(755,root,root) %{_bindir}/dstat
%{_mandir}/man1/dstat.1*
%{_datadir}/dstat
