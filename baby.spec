%global goipath         github.com/manuwarfare/baby
Version:        1.0.55
%global debug_package %{nil}
%global with_devel 0
%global with_bundled 1
%global with_check 0
%global with_unit_test 0
Name:           baby
Release:        1%{?dist}
Summary:        Abbreviate long commands in terminal
License:        GPLv3+
URL:            https://%{goipath}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  golang,
Requires:       glibc >= 2.28

%description
Server oriented command assistant for the GNU/Linux terminal.
You can easily short and manage your commands by setting, deleting,
listing, updating, importing and exporting your rules with a clear
list of parameters. It should be functional in any Unix like system.

%prep
%autosetup

%build
# Configurar GOFLAGS para usar buildmode=pie
export GOFLAGS="-buildmode=pie -linkshared"

# Limitar las bibliotecas enlazadas
export CGO_CFLAGS="-O2 -g -fno-omit-frame-pointer"
export CGO_CXXFLAGS="$CGO_CFLAGS"

# Compilar el programa
go build -ldflags "-s -w -linkmode=external -extldflags '%{build_ldflags} -Wl,--as-needed -Wl,--gc-sections -static-libgcc'" -o %{name} .

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 baby.1.gz %{buildroot}%{_mandir}/man1/baby.1.gz
install -Dpm 0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_bindir}/%{name}
%{_mandir}/man1/baby.1*

%changelog
* Thu Jun 27 2024 Manuel Guerra <ar.manuelguerra@gmail.com> - 1.0.55-1
- Initial RPM release
