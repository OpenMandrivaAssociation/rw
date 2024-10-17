%define major 0
%define libname %mklibname %name %major

Name:		rw
Summary:	Program that calculates rank-width and rank-decompositions
Version:	0.7
Release:	1
License:	GPLv2+
URL:		https://pholia.tdi.informatik.uni-frankfurt.de/~philipp/software/%{name}.shtml
Source0:	http://pholia.tdi.informatik.uni-frankfurt.de/~philipp/software/%{name}-%{version}.tar.gz
BuildRequires:	igraph-devel

%description
rw is a program that calculates rank-width and rank-decompositions.
It is based on ideas from "Computing rank-width exactly" by Sang-il Oum,
"Sopra una formula numerica" by Ernesto Pascal, "Generation of a Vector
from the Lexicographical Index" by B.P. Buckles and M. Lybanon and
"Fast additions on masked integers" by Michael D. Adams and David S. Wise.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	%libname = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%libpackage %name %major

%prep
%setup -q

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make

%install
make install DESTDIR="%{buildroot}"
rm %{buildroot}%{_libdir}/*.la

# It already installs docs in proper directory
# avoid duplicate entries in $files
cp -p AUTHORS NEWS %{buildroot}%{_docdir}/%{name}/

%files
%doc COPYING
%{_bindir}/rw

%files		devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
