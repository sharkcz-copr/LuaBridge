Name:           LuaBridge
Version:        2.6
Release:        1%{?dist}
Summary:        Bridge between C++ and Lua

License:        MIT
URL:            https://github.com/vinniefalco/LuaBridge
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       lua-devel

# this is a header-only library
BuildArch:      noarch


%description
LuaBridge is a lightweight and dependency-free library for mapping data,
functions, and classes back and forth between C++ and Lua (a powerful,
fast, lightweight, embeddable scripting language) 


%package devel
Summary:        Bridge between C++ and Lua

%description devel
LuaBridge is a lightweight and dependency-free library for mapping data,
functions, and classes back and forth between C++ and Lua (a powerful,
fast, lightweight, embeddable scripting language) 


%prep
%autosetup


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{_includedir}
cp -a Source/%{name} %{buildroot}/%{_includedir}


%files devel
%doc *.md *.html
%{_includedir}/%{name}/


%changelog
* Fri Jul 08 2022 Dan Horák <dan@danny.cz> - 2.6-1
- initial Fedora version
