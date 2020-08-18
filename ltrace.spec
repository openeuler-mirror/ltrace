name:           ltrace
Version:        0.7.91
Release:        30
Summary:        Trace the Library and System Calls a Program Makes

License:        GPLv2+
URL:            https://gitlab.com/cespedes/ltrace
Source0:        http://repository.timesys.com/buildsources/l/ltrace/ltrace-0.7.91/ltrace-0.7.91.tar.gz

Patch0001:      ltrace-0.7.91-account_execl.patch
Patch0002:      ltrace-0.7.91-x86_64-irelative.patch
Patch0003:      ltrace-0.7.91-man.patch
Patch0004:      ltrace-0.7.91-cant_open.patch
Patch0005:      ltrace-0.7.91-aarch64.patch
Patch0006:      ltrace-0.7.2-e_machine.patch
Patch0007:      ltrace-0.7.91-parser-ws_after_id.patch
Patch0008:      ltrace-0.7.91-x86-plt_map.patch
Patch0009:      ltrace-0.7.91-x86-unused_label.patch
Patch0010:      ltrace-0.7.91-unwind-elfutils.patch
Patch0011:      ltrace-0.7.91-multithread-no-f-1.patch
Patch0012:      ltrace-0.7.91-multithread-no-f-2.patch
Patch0013:      ltrace-0.7.91-testsuite-includes.patch
Patch0014:      ltrace-0.7.91-testsuite-includes-2.patch
Patch0015:      ltrace-0.7.91-tautology.patch
Patch0016:      ltrace-0.7.91-aarch64-params.patch

# patch for openEuler
Patch9000:      bugfix-0001-ltrace-0.7.91-aarch64_be-compile-support.patch
Patch9001:      bugfix-0001-ltrace-byteswap-instruction-in-arm-be8-mode.patch
Patch9002:      bugfix-for-use-after-free-about-soname.patch

BuildRequires:  elfutils-devel dejagnu libselinux-devel autoconf automake libtool

%description
Ltrace is a program that runs the specified command until it exits. It
intercepts and records the dynamic library calls that are called by the
executed process and the signals that are received by that process. It
can also intercept and print the system calls executed by the program.

The program to trace need not be recompiled for this, so you can use
ltrace on binaries for which you do not have access to the source.

This is still a work in progress, so, for example, the tracking to
child processes may fail or some things may not work as expected.

%package help
Summary:        Help document for the ltrace package

%description help
Help document for the ltrace package.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -i
%configure --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%make_build

%install
%make_install bindir=%{_bindir}

%check
#timeout 180 make check ||:

%files
%doc NEWS CREDITS INSTALL README TODO COPYING
%{_bindir}/ltrace
%{_datadir}/ltrace

%files help
%{_mandir}/man1/ltrace.1*
%{_mandir}/man5/ltrace.conf.5*

%changelog
* Tue Aug 18 2020 senlin<xiasenlin1@huawei.com> - 0.7.91-30
- add release for update

* Wed Nov 27 2019 daiqianwen <daiqianwen@huawei.com> - 0.7.91-29
- Package init.
