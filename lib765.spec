%define sname 765
%define name lib%{sname}

%define version 0.4.2
%define release %mkrel 1
%define summary Emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
%define lib_major 3
%define lib_name %mklibname %{sname}_ %{lib_major}
%define devel_name %mklibname %{sname} -d

%define old_lib_name %mklibname %{sname}_ 2
%define old_devel_name %mklibname %{sname}_ 3 -d
%define very_old_devel_name %mklibname %{sname}_ 2 -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	GPLv2
Group:		System/Libraries
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libdsk-devel

%description
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.

%package -n %{lib_name}
Summary: Libraries for emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
Group: System/Libraries
Provides:  %{name} = %{version}-%{release}
Obsoletes: %{old_lib_name}

%description -n %{lib_name}
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.

This package provides the libraries for using 765 emulation.

%package -n %{devel_name}
Summary: Libraries and include files for developing with lib765
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{old_devel_name}
Obsoletes: %{very_old_devel_name}

%description -n %{devel_name}
This package provides the necessary development libraries and include
files to allow you to develop with lib765.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(0644,root,root,0755)
%{_libdir}/*.so.*
%doc ChangeLog doc/COPYING.LIB

%files -n %{devel_name}
%defattr(0644,root,root,0755)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h
%doc doc/765.txt

