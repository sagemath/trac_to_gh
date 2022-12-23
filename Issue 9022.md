# Issue 9022: python fails to build _socket on OpenSolaris x64, so ipython fails to build.

Issue created by migration from https://trac.sagemath.org/ticket/9022

Original creator: drkirkby

Original creation time: 2010-05-23 19:23:26

Assignee: drkirkby

CC:  jsp

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.4.2
 * gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby@hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv. 

## How the Sage build was attempted
 * 64-bit build. SAGE64 was set to "yes"
 * #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
 * #9009 update mercurial spkg to build 64-bit.
 * #7982 update sage_fortran so it can build 64-bit binaries.
 * 'touch' spkg/installed/gdmodule-0.56.p7 to fool Sage into thinking gdmodule had installed, as it is failing to (see #9021)

## The problem

One can see that _socket is not being built:

```
gcc -m64 -fPIC -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I. -I/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/./Include -I. -IInclude -I./Include -I/export/home/drkirkby/sage-4.4.2/local/include -I/usr/local/include -I/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Include -I/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src -c /export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c -o build/temp.solaris-2.11-i86pc-2.6/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.o
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c: In function ‘makesockaddr’:
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:1103: error: ‘struct ifreq’ has no member named ‘ifr_ifindex’
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:1104: error: ‘SIOCGIFNAME’ undeclared (first use in this function)
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:1104: error: (Each undeclared identifier is reported only once
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:1104: error: for each function it appears in.)
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c: In function ‘getsockaddrarg’:
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:1411: error: ‘SIOCGIFINDEX’ undeclared (first use in this function)
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:1423: error: ‘struct ifreq’ has no member named ‘ifr_ifindex’
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c: In function ‘init_socket’:
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:4589: error: ‘PACKET_LOOPBACK’ undeclared (first use in this function)
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p7/src/Modules/socketmodule.c:4590: error: ‘PACKET_FASTROUTE’ undeclared (first use in this function)
building '_ssl' extension
```

This is shown later when the list of failed modules is displayed in the Sage build log. 


```
Failed to build these modules:
_curses            _curses_panel      _socket
_ssl               _tkinter           sunaudiodev
```


This then causes ipython to fail to build. 


```
  File "/export/home/drkirkby/sage-4.4.2/spkg/build/ipython-0.9.1.p0/src/IPython/iplib.py", line 71, in <module>
    from IPython.Prompts import CachedOutput
  File "/export/home/drkirkby/sage-4.4.2/spkg/build/ipython-0.9.1.p0/src/IPython/Prompts.py", line 23, in <module>
    import socket
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/socket.py", line 46, in <module>
    import _socket
ImportError: No module named _socket
Error installing Ipython

real    0m0.186s
user    0m0.136s
sys     0m0.046s
sage: An error occurred while installing ipython-0.9.1.p0
```


## Likely hints as to the cause
The following couple of links have something written about the _socket issue:

 * http://www.opensolaris.org/jive/thread.jspa?threadID=5426&tstart=0
 * http://www.lotuseyes.de/blog/error-installing-plone-on-opensolaris-using-the-unified-installer

As of this minute, I don't have a solution for this. 

The solution proposed at 

http://www.lotuseyes.de/blog/error-installing-plone-on-opensolaris-using-the-unified-installer 

may be workable, though I would restrict the patch to just OpenSolaris, not just any Solaris release, which is what suspect his


```
#if defined(__sun)
#  define ifr_ifindex ifr_index
#  undef HAVE_NETPACKET_PACKET_H
#endif
```


will do. 

Dave


---

Comment by drkirkby created at 2010-05-24 18:24:38

For other OpenSolaris issues, see #9026


---

Comment by drkirkby created at 2010-05-29 15:35:06

I've reported this as a bug. 

http://bugs.python.org/issue8852

and have received some feedback, though it is not yet acknowledged as a bug or not. 


Dave


---

Comment by drkirkby created at 2010-05-30 05:56:02

The failure of _socket to build is also causing pygments to fail to build - see #9041. Once I've produced a patch, hopefully both ipython and pygments will build ok. 

Dave


---

Comment by drkirkby created at 2010-05-30 09:04:17

The fix for this is the same as required for #9041. So please review #9041. The changes have been tested on 
 
 * Linux
 * OS X 
 * OpenSolaris on x64 (where the problem occured)
 * Solaris 10 on SPARC

See all the supporting evidence at #9041. 

## Notes to the release manager
This ticket may be closed when #9041 is closed. 

Dave


---

Comment by rlm created at 2010-06-25 11:44:05

See #9041


---

Comment by rlm created at 2010-06-25 11:44:05

Resolution: duplicate


---

Comment by drkirkby created at 2010-06-25 13:48:00

I would also see #9295, which is an improvement on #9041, adding the facility to check Python by adding an spkg-check file. 

Dave
