# Component versions
%define setxkbmap 1.3.0
%define xkbcomp 1.3.0
%define xkbevd 1.1.3
%define xkbprint 1.0.3
%define xkbutils 1.0.4

Summary:    X.Org X11 xkb utilities
Name:       xorg-x11-xkb-utils
Version:    7.7
Release:    12%{?dist}
License:    MIT
Group:      User Interface/X
URL:        http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    http://www.x.org/pub/individual/app/setxkbmap-%{setxkbmap}.tar.bz2
Source1:    http://www.x.org/pub/individual/app/xkbcomp-%{xkbcomp}.tar.bz2
Source2:    http://www.x.org/pub/individual/app/xkbevd-%{xkbevd}.tar.bz2
Source3:    http://www.x.org/pub/individual/app/xkbprint-%{xkbprint}.tar.bz2
Source4:    http://www.x.org/pub/individual/app/xkbutils-%{xkbutils}.tar.bz2

BuildRequires:  byacc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
# xkbutils/xkbvleds requires libXext and libXpm, but autotools don't check/require them:
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)


Provides:   setxkbmap = %{setxkbmap}
Provides:   xkbcomp = %{xkbcomp}

%description
X.Org X11 xkb core utilities.

%package devel
Summary:    X.Org X11 xkb utilities development package
Group:      Development/Libraries
Requires:   pkgconfig

%description devel
X.Org X11 xkb utilities development files.

%package -n xorg-x11-xkb-extras
Summary:    X.Org X11 xkb gadgets
Provides:   xkbevd = %{xkbevd}
Provides:   xkbprint = %{xkbprint}
Provides:   xkbutils = %{xkbutils}

%description -n xorg-x11-xkb-extras
X.Org X11 xkb gadgets.

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4

%build
# Build all apps
{
    for app in * ; do
        pushd $app
            case $app in
                xkbcomp-*)
                    rm xkbparse.c # force regen
                    ;;
                *)
                    ;;
            esac
            %configure
            make %{?_smp_mflags}
        popd
    done
}

%install
# Install all apps
{
    for app in * ; do
        pushd $app
            %make_install
        popd
    done
}

%files
%defattr(-,root,root,-)
%{_bindir}/setxkbmap
%{_bindir}/xkbcomp
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/xkbcomp.1*

%files -n xorg-x11-xkb-extras
%defattr(-,root,root,-)
%doc xkbutils-%{xkbutils}/COPYING
%doc xkbutils-%{xkbutils}/README
%{_bindir}/xkbbell
%{_bindir}/xkbevd
%{_bindir}/xkbprint
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch
%{_mandir}/man1/xkbbell.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xkbvleds.*
%{_mandir}/man1/xkbwatch.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
* Mon Apr 20 2015 Peter Hutterer <peter.hutterer@redhat.com> 7.7-12
- Merge with F22 (#1194895)

* Wed Feb 12 2014 Adam Jackson <ajax@redhat.com> 7.7-9.1
- Mass rebuild

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 7.7-9
- Mass rebuild 2013-12-27

* Thu Aug 29 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-8
- Fix warning about redefinition of compat map (#968996)
- Null-terminate long key names (#1002343)

* Tue May 21 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-7
- Apply the patch this time...

* Tue May 21 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-6
- Add missing options to xkbcomp man page (#948842)

* Mon Feb 11 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-5
- xkbutils 1.0.4

* Tue Nov 13 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.7-4
- xkbcomp: Fix generation of XKB directory listing, missing reset on file
  handler caused parse errors and incomplete directory listings

* Tue Aug 28 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.7-2
- Remove duplicate sources

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.7-1
- X11R7.7 updates:
- xkbcomp 1.2.4
- setxkbmap 1.3.0
- xkbevd 1.1.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-5
- xkbcomp 1.2.3

* Fri Feb 11 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-4
- xkbcomp 1.2.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.5-2
- xkbprint-1.0.3

* Mon Nov 01 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.5-1
- setxkbmap 1.2.0
- xkbcomp 1.2.0
- xkbutils 1.0.3
- xkbevd 1.1.1

* Mon Oct 11 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.4-9
- xkbcomp-hex-parsing.patch: fix up parsing of hex-code symbols (#638244)

* Thu Jul 08 2010 Adam Jackson <ajax@redhat.com> 7.4-8
- xkbcomp-speed.patch: Backport performance changes from git master.
