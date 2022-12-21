# Issue 7044: eclib 20080310.p7 has code Sun's C++ compiler does not understand.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-28 00:48:03

Assignee: burcin

CC:  cremona dimpase

I'm using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha4
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021


```
eclib-20080310.p7/.hg/branch
eclib-20080310.p7/.hg/undo.branch
eclib-20080310.p7/spkg-install
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
Disabling parallel make for now
Deleting old versions of cremona libraries, which
would interfere with new builds.
libcurvesntl.*: No such file or directory
libg0nntl.*: No such file or directory
libjcntl.*: No such file or directory
librankntl.*: No such file or directory
libmwrank.*: No such file or directory
Deleting old include directory
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/eclib-20080310.p7/src'
mkdir -p include
mkdir -p lib
cd procs && make lib install
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/eclib-20080310.p7/src/procs'
Makefile:93: warning: overriding commands for target `clean'
../Makefile:76: warning: ignoring old commands for target `clean'
Makefile:96: warning: overriding commands for target `veryclean'
../Makefile:84: warning: ignoring old commands for target `veryclean'
Makefile:109: warning: overriding commands for target `check'
../Makefile:95: warning: ignoring old commands for target `check'
/opt/xxxsunstudio12.1/bin/CC -c -fPIC -g -O2 -DNEW_OP_ORDER -DUSE_PARI_FACTORING -DNTL_ALL -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include interface.cc -o interface_n.o
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
"interface.h", line 54: Error: Could not open include file<ext/numeric>.
"interface.h", line 122: Error: Could not open include file<NTL/ZZ.h>.
"interface.h", line 123: Error: Could not open include file<NTL/ZZXFactoring.h>.
"interface.h", line 124: Error: NTL is not defined.
"interface.h", line 130: Error: ZZ is not defined.
"interface.h", line 130: Error: The function "to_ZZ" must have a prototype.
"interface.h", line 137: Error: ")" expected instead of "&".
"interface.h", line 137: Error: x is not defined.
"interface.h", line 138: Error: ")" expected instead of "&".
"interface.h", line 138: Error: x is not defined.
"interface.h", line 139: Error: ")" expected instead of "&".
"interface.h", line 139: Error: x is not defined.
"interface.h", line 140: Error: ")" expected instead of "&".
"interface.h", line 140: Error: x is not defined.
"interface.h", line 141: Error: ")" expected instead of "&".
"interface.h", line 141: Error: a is not defined.
"interface.h", line 142: Error: ")" expected instead of "&".
"interface.h", line 142: Error: a is not defined.
"interface.h", line 143: Error: ")" expected instead of "&".
"interface.h", line 143: Error: c is not defined.
"interface.h", line 143: Error: a is not defined.
"interface.h", line 143: Error: i is not defined.
"interface.h", line 144: Error: ")" expected instead of "&".
"interface.h", line 144: Error: c is not defined.
"interface.h", line 144: Error: a is not defined.
Compilation aborted, too many Error messages.
make[3]: *** [interface_n.o] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/eclib-20080310.p7/src/procs'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/eclib-20080310.p7/src'
Error building cremona

real    0m1.043s
user    0m0.779s
sys     0m0.156s
sage: An error occurred while installing eclib-20080310.p7
Please email sage-devel http://groups.google.com/group/sage-devel

```



---

Comment by burcin created at 2009-11-30 15:07:31

The `eclib` package is used for elliptic curve computations, it has nothing to do with `calculus`.

I added John Cremona, the developer of eclib, to the CC list.


---

Comment by burcin created at 2009-11-30 15:07:31

Changing component from calculus to solaris.


---

Comment by burcin created at 2009-11-30 15:07:31

Changing assignee from burcin to drkirkby.


---

Comment by cremona created at 2009-11-30 15:13:34

burcin is right, this is my code.  It seems that the compiler is not finding the NTL library (I mean the NTL include files) which is bound to cause the compilation to fail.

Is NTL building and installing itself properly before this point in the build?

John


---

Comment by leif created at 2010-09-03 22:27:16

Is this ticket still valid?


---

Comment by cremona created at 2011-05-24 21:19:56

Please see #10993 to see if there is still a problem (not that I have fixed anything relevant on purpose).  I do not propose to make changes to this old version of eclib, but could change the newer version if that would help.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mjo created at 2020-07-12 20:01:50

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2020-07-12 20:01:50

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
