
 Here are some links and information about distributing Sage.

Related pages: [Sage wiki: days77/packaging](https://wiki.sagemath.org/days77/packaging), [[Infrastructure]]

[[PageOutline]]


# Source distributions

The release manager releases the source for each development release
and each stable release.

  * source (stable): http://www.sagemath.org/download-source.html
  * source (devel): http://www.sagemath.org/download-latest.html


# Containers


## Binder

  * url: https://github.com/sagemath/sage-binder-env


## Docker images


### CoCalc Docker images (recommended)

As of 2022-08, this is recommended for general use.

Official CoCalc Docker image:

  * ships CoCalc, including SageMath
  * url: https://hub.docker.com/r/sagemathinc/cocalc/
  * GitHub repo: https://github.com/sagemathinc/cocalc-docker
  * people: wstein

Other CoCalc Docker images might ship SageMath too:

  * https://hub.docker.com/search/?q=cocalc


### Computational topology Sage Docker image

  * ships: SageMath, SnapPy, Regina, PHCPack, pandas, pe, gridlink, flipper, curver, heegaard, pygraphviz
  * url: https://hub.docker.com/r/computop/sage/
  * bitbucket repo: https://bitbucket.org/t3m/sagedocker
  * dockerfile: https://bitbucket.org/t3m/sagedocker/src/tip/sage/Dockerfile
  * people: Nathan Dunfield


### Official SageMath Docker images (in search of maintainers)

As of 2022-08, outdated/broken and in search of new maintainers to fix [various outstanding issues](https://trac.sagemath.org/query?status=needs_info&status=needs_review&status=needs_work&status=new&status=positive_review&component=docker&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=time&col=changetime&col=author&col=reviewer&order=priority)

  * url: https://hub.docker.com/u/sagemath/
  * admin: vbraun, sebasguts, nthiery, embray



# Live USB


## Clef agreg

  * url: http://clefagreg.dnsalias.org/
  * what: bootable "Linux + math software" environment for French "agrégation" exams
  * admin: François Boisson


## Sage Debian Live (defunct)

  * admin: tmonteil
  * hosted at: http://sagedebianlive.metelu.net/ (defunct as of 2022-08)
  * mailing list: https://sagedebianlive.metelu.net/mailman/listinfo/devel (defunct as of 2022-08)


## AIMS Desktop (abandoned 2017)

  * url: https://launchpad.net/~aims/+archive/ubuntu/aims-desktop
  * admin: pipedream


# Package managers

This section is about SageMath packages in package managers, which can be
related to particular Linux distributions, or macOS-specific (like Homebrew),
or distribution-agnostic, or even OS-agnostic.

See https://repology.org/project/sagemath/versions for an overview of package versions.

  * general SageMath packaging mailing list:
    [[https://groups.google.com/forum/#!forum/sage-packaging|sage-packaging]]


## Arch-linux

  * hosted at: https://www.archlinux.org/packages/community/x86_64/sagemath/
  * wiki page: https://wiki.archlinux.org/index.php/SageMath
  * repo: https://git.archlinux.org/svntogit/community.git/?h=packages/sagemath
  * to install: ```sudo pacman -S sagemath```
  * maintainer: Antonio Rojas


## Conda / Anaconda / Miniconda / Conda Forge

  * [Sage wiki: Conda](https://wiki.sagemath.org/Conda)
  * people: isuruf, saraedum
  * Feedstocks: https://github.com/conda-forge/sage-feedstock/tree/master/recipe
  * Related Sage tickets: https://trac.sagemath.org/query?order=id&desc=1&summary=~conda


## Debian

  * wiki page: https://wiki.debian.org/DebianScience/Sage
  * packages: https://packages.debian.org/sagemath
  * package tracker: https://tracker.debian.org/teams/debian-sagemath/
  * build logs: https://buildd.debian.org/status/package.php?p=sagemath including ptestlong results
  * repo: https://salsa.debian.org/math-team/sagemath
    * patches: https://salsa.debian.org/math-team/sagemath/-/tree/master/debian/patches
  * mailing list: https://lists.alioth.debian.org/mailman/listinfo/debian-science-sagemath
    * see also [[https://lists.debian.org/debian-math/|debian-math mailing list]]
    * earlier discussions happened on the [[https://lists.debian.org/debian-science/|debian-science mailing list]]
    * Sage-side mailing list (dormant): [[https://groups.google.com/forum/#!forum/debian-sage|debian-sage]]
  * status pages: [master branch](http://people.debian.org/~thansen/debian-sage-status.html) [develop branch](http://people.debian.org/~thansen/debian-sage-dev-status.html)
  * bug tracker: [Debian bugs: package sagemath](https://bugs.debian.org/cgi-bin/pkgreport.cgi?pkg=sagemath)
  * people: Tobias Hansen, Julien Puydt, Jerome Benoit, Ximin Luo


## Fedora package

  * hosted at: https://apps.fedoraproject.org/packages/sagemath
  * wiki page: https://fedoraproject.org/wiki/SIGs/SciTech/SAGE
  * see also: https://admin.fedoraproject.org/pkgdb/package/rpms/sagemath/
  * mailing list: https://lists.fedoraproject.org/archives/list/scitech`@`lists.fedoraproject.org/
  * maintainer: Paulo Cesar Pereira de Andrade (pcpa)


## Gentoo: Sage-on-Gentoo

  * repository: https://github.com/cschwan/sage-on-gentoo
  * Issues: https://github.com/cschwan/sage-on-gentoo/issues
  * Maintainer: François Bissey (fbissey/kiwifb)


## Homebrew

SageMath can now be installed on macOS via Homebrew by running
```
brew cask install sage
```
This fetches the dmg for the app, and installs the app from that dmg.
See [this post on sage-devel](https://groups.google.com/d/msg/sage-devel/jdLfIKQ1M18/PVQqJUUqAgAJ).


## Nix

  * Nix package manager: https://nixos.org/nix/
  * Sage package: https://github.com/NixOS/nixpkgs/tree/master/pkgs/applications/science/math/sage
  * Distribution-agnostic, functional, declarative package managing.
  * Should always have 0 doctest failures. To achieve that, [some](https://github.com/NixOS/nixpkgs/tree/master/pkgs/applications/science/math/sage/default.nix) dependency versions are pinned. That is not an issue because Nix allows multiple versions of a package to be installed at the same time. However the goal is to minimize the amount of pinned dependencies.
  * Should work on most Linux distributions. More precisely any Linux distro where the Nix package manager is available, e.g. [ArchLinux](https://aur.archlinux.org/packages/nix), Debian, [others](https://nixos.org/nix/) -- definitely works on [NixOS](https://nixos.org/).
  * Tested on x86 Linux. Probably works on ARM but that is as of yet untested.
  * Could run on Darwin, but currently doesn't since some dependencies don't have Darwin-specific patches. If you're a Darwin user, help with that would be very much appreciated. This is [work in progress](https://github.com/NixOS/nixpkgs/pull/45364).
  * Might even work with the "Windows Subsystem for Linux", but probably needs some patches. Absolutely untested.
  * Allows user-installs, given that the nix package manager is already installed.
  * To install: `nix-env -iA nixpkgs.sage` or on NixOS just add sage to your `environment.systemPackages`
  * Betas are usually packaged in [a PR](https://github.com/NixOS/nixpkgs/pull/44527) until the release is final.
  * Currently (2018-07-26) maintained by timokau. Any help is appreciated. If you are interested (even if you don't know anything about nix yet), [[open an issue||https://github.com/NixOS/nixpkgs/issues/new]] pinging `@`timokau and I'll help you get started.


## RPM package (Fedora, Mandriva)

  * hosted at: http://rpmfind.net/linux/rpm2html/search.php?query=sagemath


## Ubuntu

  * packages: http://packages.ubuntu.com/sagemath derived from the [[#Debian|Debian]] packages
  * earlier PPA: https://launchpad.net/~aims/+archive/ubuntu/sagemath


## Other

Please edit this wiki or email slelievre if you know about other package managers
providing SageMath... See
[wikipedia's list of package managers](https://en.wikipedia.org/wiki/List_of_software_package_management_systems).


# Windows


## Windows Subsystem for Linux (recommended)

  * Under Windows 10, one can run the "Windows Subsystem for Linux" to "run Linux under Windows".
  * Documented in [Sage installation guide](https://doc.sagemath.org/html/en/installation/index.html#windows) since Sage 9.6.


## Cygwin (in search of maintainers)

As of 2022-08 (Sage 9.6/9.7) in search of maintainers.

  * pending tickets: [component: "porting: cygwin"](https://trac.sagemath.org/query?status=!closed&component=porting%3A+Cygwin)
  * wiki pages on Sage's trac: [Cygwin32](https://trac.sagemath.org/wiki/CygwinPort), [Cygwin64](https://trac.sagemath.org/wiki/Cygwin64Port)


## SageMath installer for Windows (abandoned 2021)

  * see https://wiki.sagemath.org/SageWindows
  * hosted at: https://github.com/sagemath/sage-windows/releases
  * based on the Cygwin port of Sage



## Discussion

  * mailing list (dormant): [sage-windows](https://groups.google.com/forum/#!forum/sage-windows)


# Porting to exotic architectures

  * trac-wiki: [Porting SageMath to Exotic architectures](https://trac.sagemath.org/wiki/ExoticPorts)


## BSD (2020 most recent activity as of 2022)

  * pending tickets: [component: "porting: BSD"](https://trac.sagemath.org/query?status=!closed&component=porting%3A+BSD)
  * previous effort: [Sage on FreeBSD](https://svnweb.freebsd.org/ports/head/math/sage/)


## Solaris (abandoned 2010)

  * pending tickets: [component: "porting: Solaris"](https://trac.sagemath.org/query?status=!closed&component=porting%3A+Solaris)


## AIX, HP-UX (abandoned 2011)

  * pending tickets: [component: "porting: AIX or HP-UX"](https://trac.sagemath.org/query?status=!closed&component=porting%3A+AIX+or+HP-UX)



# Discussion

  * Sage Days 77: https://wiki.sagemath.org/days77
