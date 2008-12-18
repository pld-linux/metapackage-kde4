Summary:	K Desktop Environment 4 with additional packages
Summary(pl.UTF-8):	Środowisko graficzne KDE4 z dodatkowymi pakietami
Name:		metapackage-kde4
Version:	4.1.85
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Requires:	kde4-decoration-ozone >= %{version}
Requires:	kde4-dolphin >= %{version}
Requires:	kde4-icons-oxygen >= %{version}
Requires:	kde4-kdeartwork-screensavers >= %{version}
Requires:	kde4-kdeartwork-wallpapers >= %{version}
Requires:	kde4-kdebase >= %{version}
Requires:	kde4-kdebase-infocenter >= %{version}
Requires:	kde4-kdebase-kappfinder >= %{version}
Requires:	kde4-kdebase-kdialog >= %{version}
Requires:	kde4-kdebase-kfind >= %{version}
Requires:	kde4-kdebase-konsole >= %{version}
Requires:	kde4-kdebase-kwrite >= %{version}
Requires:	kde4-kdebase-runtime >= %{version}
Requires:	kde4-kdebase-useraccount >= %{version}
Requires:	kde4-kdebase-workspace >= %{version}
Requires:	kde4-kdebase-workspace-kfontinst >= %{version}
Requires:	kde4-kdebase-workspace-klipper >= %{version}
Requires:	kde4-kdebase-workspace-kwin >= %{version}
Requires:	kde4-kdebase-workspace-kwrited >= %{version}
Requires:	kde4-kdebase-workspace-networkmanager >= %{version}
Requires:	kde4-kdebase-workspace-plasma >= %{version}
Requires:	kde4-kdebase-workspace-screensavers >= %{version}
Requires:	kde4-kdebase-workspace-solid >= %{version}
Requires:	kde4-kdebase-workspace-wallpapers >= %{version}
Requires:	kde4-kdegraphics-gwenview >= %{version}
Requires:	kde4-kdegraphics-kamera >= %{version}
Requires:	kde4-kdegraphics-kcolorchooser >= %{version}
Requires:	kde4-kdegraphics-kfile >= %{version}
Requires:	kde4-kdegraphics-kgamma >= %{version}
Requires:	kde4-kdegraphics-kolourpaint >= %{version}
Requires:	kde4-kdegraphics-kruler >= %{version}
Requires:	kde4-kdegraphics-ksane >= %{version}
Requires:	kde4-kdegraphics-ksnapshot >= %{version}
Requires:	kde4-kdegraphics-okular >= %{version}
Requires:	kde4-kdegraphics-svgpart >= %{version}
Requires:	kde4-kdelibs >= %{version}
Requires:	kde4-kdelibs-libs >= %{version}
Requires:	kde4-kdemultimedia-audiocd >= %{version}
Requires:	kde4-kdemultimedia-cddb >= %{version}
Requires:	kde4-kdemultimedia-dragon >= %{version}
Requires:	kde4-kdemultimedia-juk >= %{version}
Requires:	kde4-kdemultimedia-kmix >= %{version}
Requires:	kde4-kdemultimedia-kscd >= %{version}
Requires:	kde4-kdemultimedia-libkcddb >= %{version}
Requires:	kde4-kdenetwork-filesharing >= %{version}
Requires:	kde4-kdenetwork-kget >= %{version}
Requires:	kde4-kdenetwork-kopete >= %{version}
Requires:	kde4-kdenetwork-kopete-protocol-gg >= %{version}
Requires:	kde4-kdenetwork-kopete-protocol-icq >= %{version}
Requires:	kde4-kdenetwork-kopete-protocol-jabber >= %{version}
Requires:	kde4-kdenetwork-kopete-protocol-wlm >= %{version}
Requires:	kde4-kdenetwork-kopete-tool-history >= %{version}
Requires:	kde4-kdenetwork-krfb >= %{version}
Requires:	kde4-kdepim >= %{version}
Requires:	kde4-kdepim-akonadi >= %{version}
Requires:	kde4-kdepim-akregator >= %{version}
Requires:	kde4-kdepim-kaddressbook >= %{version}
Requires:	kde4-kdepim-kmail >= %{version}
Requires:	kde4-kdepim-knode >= %{version}
Requires:	kde4-kdepim-kontact >= %{version}
Requires:	kde4-kdepim-kontact-plugin-akregator >= %{version}
Requires:	kde4-kdepim-kontact-plugin-kaddressbook >= %{version}
Requires:	kde4-kdepim-kontact-plugin-kmail >= %{version}
Requires:	kde4-kdepim-kontact-plugin-knode >= %{version}
Requires:	kde4-kdepim-kontact-plugin-korganizer >= %{version}
Requires:	kde4-kdepim-kontact-plugin-planner >= %{version}
Requires:	kde4-kdepim-kontact-plugin-summary >= %{version}
Requires:	kde4-kdepim-libs >= %{version}
Requires:	kde4-kdepimlibs >= %{version}
Requires:	kde4-kdeplasma-addons >= %{version}
Requires:	kde4-kdeutils-kwalletmanager >= %{version}
Requires:	kde4-kdm >= %{version}
Requires:	kde4-kgreet-classic >= %{version}
Requires:	kde4-kgreet-generic >= %{version}
Requires:	kde4-konqueror >= %{version}
Requires:	kde4-konqueror-libs >= %{version}
Requires:	kde4-libkipi >= %{version}
Requires:	kde4-phonon >= %{version}
Requires:	kde4-splash-Default >= %{version}
Requires:	kde4-style-oxygen >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment 4 with additional packages (metapackage).

%description -l pl.UTF-8
Środowisko graficzne KDE4 z dodatkowymi pakietami (metapakiet).

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
