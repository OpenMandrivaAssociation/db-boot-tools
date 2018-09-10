Summary:	Tools for creating images bootable on DragonBoards
Name:		db-boot-tools
Version:	20180910
Release:	1
# https://git.linaro.org/landing-teams/working/qualcomm/db-boot-tools.git
# master branch
Source0:	db-boot-tools-%{version}.tar.xz
License:	BSD
Group:		System/Kernel and hardware
Url:		https://www.96boards.org/documentation/consumer/dragonboard/dragonboard410c/guides/customize-emmc-partition.md.html
Requires:	gptfdisk

%description
Tool for creating partition tables and system images for the
DragonBoard series of devices

%files
%{_bindir}/mkgpt
%{_bindir}/mksdcard
%{_bindir}/rawprogram-sanitizer.py
%{_datadir}/%{name}

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
cp -a mkgpt mksdcard rawprogram-sanitizer.py %{buildroot}%{_bindir}/
cp -a dragonboard* sd600eval %{buildroot}%{_datadir}/%{name}/
