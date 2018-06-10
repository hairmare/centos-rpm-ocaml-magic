%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:     ocaml-magic

%define git_ish 3b883ad9cf7c32dc1309d4200bd0af87e5841119

Version:  0.7.3
Release:  1
Summary:  OCaml bindings for libmagic
License:  GPLv2+
URL:      https://github.com/Chris00/ocaml-magic
Source0:  https://github.com/Chris00/ocaml-magic/archive/%{git_ish}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: file-devel
BuildRequires: which

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh
Requires:      file


%description
OCAML bindings for libmagic

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ocaml-magic-%{git_ish}


%build
./configure \
   --prefix=%{_prefix} \
   --disable-ldconf
make byte
%if %opt
make opt
%endif


%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install


%files
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/ocaml/magic
%if %opt
%exclude %{_libdir}/ocaml/magic/*.a
%exclude %{_libdir}/ocaml/magic/*.cmxa
%exclude %{_libdir}/ocaml/magic/*.cmx
%endif
%exclude %{_libdir}/ocaml/magic/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%defattr(-,root,root,-)
%doc README.md
%if %opt
%{_libdir}/ocaml/magic/*.a
%{_libdir}/ocaml/magic/*.cmxa
%{_libdir}/ocaml/magic/*.cmx
%endif
%{_libdir}/ocaml/magic/*.mli
