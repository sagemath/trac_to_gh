# Issue 7072: scipy 0.7.p2 has a GNUism, sending GNU flags to the Sun compiler.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-29 13:40:09

Assignee: tbd

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used #7021 


```
scipy-0.7.p2/patches/setup.py.integrate
scipy-0.7.p2/patches/optimize.py
scipy-0.7.p2/spkg-check
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details

```




---

Comment by drkirkby created at 2009-11-09 14:03:27

Changing component from algebra to solaris.


---

Comment by mkoeppe created at 2019-11-23 16:30:05

This is outdated and should be closed.


---

Comment by chapoton created at 2019-11-23 19:37:11

Resolution: invalid
