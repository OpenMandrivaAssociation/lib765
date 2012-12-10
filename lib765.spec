%define sname 765

%define lib_major 3
%define lib_name %mklibname %{sname}_ %{lib_major}
%define devel_name %mklibname %{sname} -d

Name:		lib%{sname}
Version:	0.4.2
Release:	2
Summary:	Emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
License:	GPLv2
Group:		System/Libraries
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
Source:		%{name}-%{version}.tar.gz
BuildRequires:	libdsk-devel

%description
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.

%package -n %{lib_name}
Summary:	Libraries for emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{lib_name}
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.

This package provides the libraries for using 765 emulation.

%package -n %{devel_name}
Summary:	Libraries and include files for developing with lib765
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devel_name}
This package provides the necessary development libraries and include
files to allow you to develop with lib765.

%prep
%setup -q

%build
#fix x86_64 OS detection first
autoreconf -if
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{lib_name}
%defattr(0644,root,root,0755)
%{_libdir}/*.so.*
%doc ChangeLog doc/COPYING.LIB

%files -n %{devel_name}
%defattr(0644,root,root,0755)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*.h
%doc doc/765.txt

%changelog
* Sun Sep 11 2011 Andrey Bondrov <abondrov@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 699407
- Fix x86_64 build
- imported package lib765


* Sun Sep 11 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.4.2-1mdv2010.2
- 0.4.2
- Remove PLF reference

* Mon Jan 28 2008 Guillaume Bedot <littletux@zarb.org> 0.4.1-1plf2008.1
- 0.4.1

* Wed May  2 2007 Guillaume Bedot <littletux@zarb.org> 0.4.0-1plf2008.0
- 0.4.0

* Tue Jun 28 2005 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.3.3-2plf
- added lib765_2-static-devel to obsoletes in lib765_3-devel

* Wed Feb 16 2005 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.3.3-1plf
- new version

* Fri May 7 2004 Miguel Barrio Orsikowsky <megamik@zarb.org> 0.3.1.1-5plf
- introduce in PLF
- changed spec file to meet Mandrake's skel spec
- repackaged sources to bz2 format
- removed static-devel package

* Wed Apr 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.1.1-4mdk
- rebuild for new libsdk

* Mon Dec 15 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.3.1.1-3mdk
- introduce in contrib

* Sat Nov 1 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.3.1.1-2mdk
- made lots of fixes and cosmetic changes to the spec file

* Thu Sep 2 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.3.1.1-1mdk
- new version

* Thu May 22 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.3.0-3mdk
- added BuildRequires

* Tue May 13 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.3.0-2mdk
- unified %%changelog

* Thu Apr 24 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.3.0-1mdk
- first version of the package
- spec file written using Mandrake RPM HOWTO 1.1.1
