# Issue 450: clisp build fixes for Solaris

Issue created by migration from https://trac.sagemath.org/ticket/450

Original creator: mabshoff

Original creation time: 2007-08-19 07:54:42

Assignee: mabshoff

There is a bug in clisp's spkg-install that causes compilation
failures on Solaris:

The initial configure run has "--without-dynamic-ffi", the makemake
job doesn't, this leads to the following definitions in clisp.h:

  #define uint64_to_I(val)  uint64_to_I(val)
  #define sint64_to_I(val)  sint64_to_I(val)

As you can imagine that doesn't go over too well at link-time. This
should also fix the compilation failure of clisp on Nexenta OS that
Didier reported. With the added flag to makemake clisp builds, but
crashes in "make check". Even with the fix clisp doesn't compile with
gcc 4.2.1 on Solaris, at the moment we use gcc 3.4.6.

We also have to make sure that we don't have "-g" in the build flags. 
This is due to  due to an interaction between gcc's gas and the Sun
 ld when using dwarf2 debugging symbols are used.

A detailed explainaition can be found at
http://www.mail-archive.com/bug-binut...`@`gnu.org/msg00615.html


---

Comment by mabshoff created at 2007-08-19 18:37:18

Okay,

there is an updated spkg-install at 

http://sage.math.washington.edu/home/mabshoff/spkg-install-clisp_--without-dynamic-ffi-fix

Caution: The CFLAGS are still "-O0", which makes it compile on Itanium, because if I remember correctly "-O2" caused crashes there. So the best solution might be to set the CFLAGS conditionally.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-22 19:38:06

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-17 07:39:39

Sam Steingold, the current clisp maintainer, has gotten an account to neron, i.e. our Sun Sparc test platform. Hopefully this will fix all issues we are seeing with clisp :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 21:07:24

Resolution: fixed


---

Comment by mabshoff created at 2008-03-22 21:07:24

Clisp 2.44.1 now builds fine with clisp 2.44.1 on Solaris with gcc 3.4.6. Since the fix is upstream we can close this.

Cheers,

Michael
