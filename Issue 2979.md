# Issue 2979: clisp -- try to build using -O2; if that fails try again but using -O0.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 02:37:55

Assignee: mabshoff

This is needed on some gcc-4.3 installs, some architectures, etc. 


---

Comment by was created at 2008-04-21 15:42:57

Please see http://sage.math.washington.edu/home/was/build/sage-3.0.rc1/spkg/standard/clisp-2.41.p14.spkg
which at least sets up a simple way to do this.  It might not work though because of CFLAGS possibly being ignored by clisp's build system.


---

Comment by was created at 2008-04-21 16:51:19

Do not use the spkg I suggested above.  It will just lead to the following error.  Throwing
in a make distclean to spkg-do-install would probably fix the problem though.  That said,
this will not fix the user's problem on the mailing list.  It fixes *some* users's problems
though (e.g., Martin Albrecht).

```
configure: loading cache config.cache
configure: error: `CFLAGS' was not set in the previous run
configure: error: changes in the environment can compromise the build
configure: error: run `make distclean' and/or `rm config.cache' and
start over
Error configuring clisp

real    1m19.616s
user    0m33.158s
sys     0m22.378s
sage: An error occurred while installing clisp-2.41.p14
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/zarathustra/Download/sage-3.0.rc1/install.log.  Describe your
computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/zarathustra/Download/sage-3.0.rc1/spkg/build/clisp-2.41.p14 and
type 'make'.
Instead type "/home/zarathustra/Download/sage-3.0.rc1/sage -sh"
in order to set all environment variables correctly, then cd to
/home/zarathustra/Download/sage-3.0.rc1/spkg/build/clisp-2.41.p14
(When you are done debugging, you can type "exit" to leave the
subshell.)
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or
SAGE_ROOT/local/bin/ directory.
clisp-2.41.p14
Machine:
Linux localhost.localdomain 2.6.25-1.fc9.i686 #1 SMP Thu Apr 17
01:47:10 EDT 2008 i686 i686 i386 GNU/Linux

And I get the same error as above after setting the CFLAGS
```



---

Comment by was created at 2008-04-21 20:03:00


```
12:57 < gginiu> wstein: I made that clisp build... I noticed that CFLAGS takes no effect, they are set in 
                Makefile, and I only had to enable fix that is there for 4.2.x, patches/makefile.in line 
                1127, changed 4.2* into 4.[2-3]*
```



---

Comment by mhansen created at 2008-04-21 20:39:44

There is a new spkg here: http://giniu.ravenlord.ws/clisp-2.41.p15.spkg

It worked fine on my Ubuntu 7.10 64-bit Core 2 Duo.


---

Comment by mabshoff created at 2008-04-22 04:57:41

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/final/clisp-2.41.p14.spkg

contains the fix to force "-O0" with gcc 4.3.

Credit goes to Andrzej Giniewicz


---

Comment by mabshoff created at 2008-04-22 05:00:20

Spkg looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-22 05:11:54

Merged in Sage 3.0.final


---

Comment by mabshoff created at 2008-04-22 05:11:54

Resolution: fixed
