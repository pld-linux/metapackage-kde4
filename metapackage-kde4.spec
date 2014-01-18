%define		kdebase_workspace	4.11.5

Summary:	K Desktop Environment 4 with additional packages
Summary(pl.UTF-8):	Środowisko graficzne KDE4 z dodatkowymi pakietami
Name:		metapackage-kde4
Version:	4.12.0
Release:	2
License:	GPL/LGPL
Group:		X11/Applications
Requires:	kde4-decoration-oxygen >= %{kdebase_workspace}
Requires:	kde4-desktopthemes >= %{version}
Requires:	kde4-dolphin >= %{version}
Requires:	kde4-icons-oxygen >= %{version}
Requires:	kde4-kdeartwork-screensavers >= %{version}
Requires:	kde4-kdeartwork-wallpapers >= %{version}
Requires:	kde4-kdebase >= %{version}
Requires:	kde4-kdebase-artwork >= %{version}
Requires:	kde4-kdebase-kdialog >= %{version}
Requires:	kde4-kdebase-kfind >= %{version}
Requires:	kde4-konsole >= %{version}
Requires:	kde4-kate >= %{version}
Requires:	kde4-kdebase-runtime >= %{version}
Requires:	kde4-kdebase-useraccount >= %{version}
Requires:	kde4-kdebase-workspace >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-infocenter >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-kfontinst >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-klipper >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-kwin >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-kwrited >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-plasma >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-screensavers >= %{kdebase_workspace}
Requires:	kde4-kdebase-workspace-solid >= %{kdebase_workspace}
Requires:	kde4-wallpapers >= %{version}
Requires:	kde4-gwenview >= %{version}
Requires:	kde4-kamera >= %{version}
Requires:	kde4-kcolorchooser >= %{version}
Requires:	kde4-kdegraphics-thumbnailers >= %{version}
Requires:	kde4-kdegraphics-strigi-analyzer >= %{version}
Requires:	kde4-kgamma >= %{version}
Requires:	kde4-knetworkmanager
Requires:	kde4-kolourpaint >= %{version}
Requires:	kde4-kruler >= %{version}
Requires:	kde4-ksaneplugin >= %{version}
Requires:	kde4-ksnapshot >= %{version}
Requires:	kde4-okular >= %{version}
Requires:	kde4-svgpart >= %{version}
Requires:	kde4-kdelibs >= %{version}
Requires:	kde4-audiocd-kio >= %{version}
Requires:	kde4-dragon >= %{version}
Requires:	kde4-juk >= %{version}
Requires:	kde4-kmix >= %{version}
Requires:	kde4-kscd >= %{version}
Requires:	kde4-libkcddb >= %{version}
Requires:	kde4-libkcompactdisc >= %{version}
Requires:	kde4-kdenetwork-filesharing >= %{version}
Requires:	kde4-kget >= %{version}
Requires:	kde4-kopete >= %{version}
Requires:	kde4-krfb >= %{version}
Requires:	kde4-kdepim >= %{version}
Requires:	kde4-kdepim-akregator >= %{version}
Requires:	kde4-kdepim-blogilo >= %{version}
Requires:	kde4-kdepim-kaddressbook >= %{version}
Requires:	kde4-kdepim-kalarm >= %{version}
Requires:	kde4-kdepim-kjots >= %{version}
Requires:	kde4-kdepim-kleopatra >= %{version}
Requires:	kde4-kdepim-kmail >= %{version}
Requires:	kde4-kdepim-knode >= %{version}
Requires:	kde4-kdepim-konsolekalendar >= %{version}
Requires:	kde4-kdepim-kontact >= %{version}
Requires:	kde4-kdepim-kontact-plugin-akregator >= %{version}
Requires:	kde4-kdepim-kontact-plugin-kaddressbook >= %{version}
Requires:	kde4-kdepim-kontact-plugin-kmail >= %{version}
Requires:	kde4-kdepim-kontact-plugin-knode >= %{version}
Requires:	kde4-kdepim-kontact-plugin-knotes >= %{version}
Requires:	kde4-kdepim-kontact-plugin-korganizer >= %{version}
Requires:	kde4-kdepim-kontact-plugin-specialdates >= %{version}
Requires:	kde4-kdepim-kontact-plugin-summary >= %{version}
Requires:	kde4-kdepim-korganizer >= %{version}
Requires:	kde4-kdepim-ktimetracker >= %{version}
Requires:	kde4-kdepim-libs >= %{version}
Requires:	kde4-kdepim-runtime >= %{version}
Requires:	kde4-kdepimlibs >= %{version}
Requires:	kde4-kdeplasma-addons >= %{version}
Requires:	kde4-ark >= %{version}
Requires:	kde4-kwallet >= %{version}
Requires:	kde4-kdm >= %{kdebase_workspace}
Requires:	kde4-kgreet-classic >= %{kdebase_workspace}
Requires:	kde4-kgreet-generic >= %{kdebase_workspace}
Requires:	kde4-konqueror >= %{version}
Requires:	kde4-konqueror-libs >= %{version}
Requires:	kde4-libkipi >= %{version}
Requires:	kde4-phonon >= %{version}
Requires:	kde4-style-oxygen >= %{kdebase_workspace}
Requires:	qt4-phonon-backend
Requires:	xine-decode-ogg
Requires:	xinitrc-ng
Requires:	xterm
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
