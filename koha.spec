# TODO:
# - include apache configuration
Summary:	A library and collection management system
Summary(pl.UTF-8):	System zarządzania bibliotekami i kolekcjami
Name:		koha
Version:	2.2.4
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/koha/%{name}-%{version}.tar.gz
# Source0-md5:	68ec84cea8975f615722140dc25b3027
URL:		http://www.koha.org/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_kohadir	/home/services/httpd/html/koha/intranet
%define		_opacdir	/home/services/httpd/html/koha/opac

%description
Koha is a library and collection management system. It is designed to
manage physical collections of items (books, CDs, videos, reference,
etc.). It provides cataloguing, searching, member/patron management,
an acqusitions system, and circulation (issues, returns, and
reserves). Circulation is handled with a full screen curses interface
or a Web-based interface, and the rest of the system is Web-based.

%description -l pl.UTF-8
Koha to system zarządzania bibliotekami i kolekcjami. Został
zaprojektowany do zarządzania fizycznymi kolekcjami przedmiotów
(książek, płyt CD, nośników wideo, odnośników itp.). Pozwala na
katalogowanie, przeszukiwanie, zarządzanie członkami/opiekunami,
systemem akwizycji i obiegu (wyjścia, powroty i rezerwacje). Obieg
jest obsługiwany przez pełnoekranowy interfejs oparty o curses lub
WWW, a reszta systemu jest oparta o WWW.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_kohadir}/{htdocs,cgi-bin,scripts,modules},%{_opacdir}/{htdocs,cgi-bin},%{_sysconfdir},/var/log/koha}

install opac-cgi/* $RPM_BUILD_ROOT%{_opacdir}/cgi-bin
cp -R opac-html/* $RPM_BUILD_ROOT%{_opacdir}/htdocs
cp -R intranet-cgi/* $RPM_BUILD_ROOT%{_kohadir}/cgi-bin
cp -R intranet-html/* $RPM_BUILD_ROOT%{_kohadir}/htdocs
cp -R modules/* $RPM_BUILD_ROOT%{_kohadir}/modules
cp -R scripts/* $RPM_BUILD_ROOT%{_kohadir}/scripts

cat > $RPM_BUILD_ROOT%{_sysconfdir}/koha.conf << EOF
database=koha
hostname=localhost
user=koha
pass=koha
includes=%{_kohadir}/htdocs/includes
intranetdir=%{_kohadir}
opacdir=%{_opacdir}
kohalogdir=/var/log/koha
kohaversion=%{version}
httpduser=httpd
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* Hints TODO README koha.mysql
%attr(640,root,httpd) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/koha.conf
%attr(770,root,httpd) %dir /var/log/koha
%attr(770,root,httpd) %dir %{_opacdir}
%attr(770,root,httpd) %dir %{_opacdir}/cgi-bin
%attr(770,root,httpd) %dir %{_opacdir}/htdocs
%attr(770,root,httpd) %dir %{_kohadir}
%attr(770,root,httpd) %dir %{_kohadir}/cgi-bin
%attr(770,root,httpd) %dir %{_kohadir}/htdocs
%attr(770,root,httpd) %dir %{_kohadir}/modules
%attr(770,root,httpd) %dir %{_kohadir}/scripts
%attr(750,root,httpd) %{_opacdir}/cgi-bin/*
%attr(750,root,httpd) %{_opacdir}/htdocs/*
%attr(750,root,httpd) %{_kohadir}/cgi-bin/*
%attr(750,root,httpd) %{_kohadir}/htdocs/*
%attr(750,root,httpd) %{_kohadir}/modules/*
%attr(750,root,httpd) %{_kohadir}/scripts/*
