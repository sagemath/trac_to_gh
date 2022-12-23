# Issue 7815: Flint fails to build 64-bit on Open Solaris

Issue created by migration from https://trac.sagemath.org/ticket/7815

Original creator: drkirkby

Original creation time: 2010-01-02 06:21:14

Assignee: drkirkby

CC:  jst rlm

There are several problems in the Flint spkg-install and makefile which prevent it building 64-bit on any platform other than OS X. Apart from the usual changes of adding -m64 to CFLAGS, the makefile has previously been changed to make it work on OS X. However, it does not work on Open Solaris in 64-bit mode, as the -m64 flag is not being added where it should be. 




---

Comment by drkirkby created at 2010-01-02 06:46:57

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-02 06:46:57

Here's an updated spkg which corrects the faults. It essentially does that by adding the environment variable CXXFLAG64 to the Makefile. This will add -m64 whenever SAGE64 is set to yes. If you look at the makefile you will see -m64 has been hard-coded when building the library on OS X, but not for other platforms. 

The changes have been checked in with 'hg'

Revised .spkg and diff can be found at

http://boxen.math.washington.edu/home/kirkby/portability/flint-1.5.0.p3/

Dave


---

Comment by drkirkby created at 2010-01-06 01:53:28

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-06 02:03:39

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-06 02:03:39

Make sure CFLAG64 and CXXFLAG64 are both exported to -m64 when testing this. It relies on that, which will happen automatically very soon I hope, when my updates to sage-env get incorporated.


---

Comment by drkirkby created at 2010-01-13 07:55:25

This depends on  #7818 so should not be applied until that is applied.


---

Comment by rlm created at 2010-01-14 08:12:31

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-14 08:12:31

Everything works on boxen, and I trust dkirkby on the Open Solaris end.


---

Comment by rlm created at 2010-01-14 08:12:48

Resolution: fixed


---

Comment by drkirkby created at 2010-01-14 09:02:10

Not only does it work on Open Solaris on x86 hardware, but I just tried for the first time to build a 64-bit version of Sage on a Sun Blade 2000 with a pair of UltraSPARC III+ CPUs running Solaris 10. This was based on the 4.3.1.alpha2 source code, but with this patch added. There are warnings issued during the 64-bit SPARC build that there are no 64-bit assembly routines, so C is used. But apart from that, Flint is now at least building on:

 * 32-bit Solaris 10 SPARC 
 * 64-bit Solaris 10 SPARC
 * 64-bit Open Solaris x86
