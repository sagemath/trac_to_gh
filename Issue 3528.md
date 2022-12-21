# Issue 3528: test_gcc_version.pl claims that gcc 4.3 is not a valid compiler to build FLINT

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-28 09:36:05

Assignee: mabshoff


```
hexagon1001: [gcc -v result.]
[02:14am] hexagon1001: Using built-in specs.
[02:14am] hexagon1001: Target: i586-suse-linux
[02:14am] hexagon1001: Configured with: ../configure --prefix=/usr 
--with-local-prefix=/usr/local --infodir=/usr/share/info 
--mandir=/usr/share/man --libdir=/usr/lib --libexecdir=/usr/lib 
--enable-languages=c,c++,objc,fortran,obj-c++,java,ada 
--enable-checking=release --with-gxx-include-dir=/usr/include/c++/4.3 
\--enable-ssp --disable-libssp --with-bugurl=http://bugs.opensuse.org/ 
--with-pkgversion='SUSE Linux' --disable-libgcj --with-slibdir=/lib 
--with-system-zlib --ena
[02:14am] hexagon1001: Thread model: posix
[02:14am] hexagon1001: gcc version 4.3.1 20080507 (prerelease) [gcc-4_3-branch revision 135036] (SUSE Linux)
[02:15am] mabshoff: ok, but gcc -dumpversion  says "4.3" ?
```


This is OpenSuSE 11, so those SuSE people need to get a life since they have been shipping odd compilers for way too many years. The fix in test_gcc_version.pl is to check also for only major and minor version.

The check should also happen before we start building Sage and should black list a bunch of known broken compilers.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-28 09:36:11

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-07 05:43:21

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/flint-1.010.p0.spkg

only tests major and minor version of gcc and not tiny. It is also somewhat more verbose than the old script. 

Cheers,

Michael


---

Comment by was created at 2008-07-07 05:55:46

Look relatively harmless.


---

Comment by mabshoff created at 2008-07-07 05:56:28

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 05:56:28

Merged in Sage 3.0.4.alpha2
