%define sname 765

%define major 3
%define libname %mklibname %{sname}_ %{major}
%define devname %mklibname %{sname} -d

Summary:	Emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
Name:		lib%{sname}
Version:	0.4.2
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.seasip.demon.co.uk/Unix/LibDsk/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libdsk-devel

%description
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.

This package provides the libraries for using 765 emulation.

%files -n %{libname}
%doc ChangeLog doc/COPYING.LIB
%{_libdir}/lib765.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and include files for developing with lib765
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides the necessary development libraries and include
files to allow you to develop with lib765.

%files -n %{devname}
%doc doc/765.txt
%{_libdir}/lib765.so
%{_libdir}/lib765.a
%{_includedir}/765.h

#----------------------------------------------------------------------------

%prep
%setup -q

%build
#fix x86_64 OS detection first
autoreconf -if
%configure2_5x
%make

%install
%makeinstall_std

