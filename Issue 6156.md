# Issue 6156: gap packages don't load anymore on itanium, even with gap-4.4.10.p11 (!)

Issue created by migration from https://trac.sagemath.org/ticket/6156

Original creator: was

Original creation time: 2009-05-30 04:06:32

Assignee: tbd




---

Comment by was created at 2009-05-30 23:48:42

mabshoff: "gcc-4.4.0 is the reason GAP doesn't work on itanium skynet."

mabshoff: "the correct thing to do is to not compile gcc with arch or march settings. I have fixed 95% of #2999-3001 in all spkgs which would all to inject flags like march into each spkg."


---

Comment by was created at 2009-06-03 06:19:56

A fix for this problem is to build GAP with -O0. That's what we'll do.  

I do wonder if gap-4.4.12 would work fine with -O0?

An spkg is up here, ready for review:   

       http://sage.math.washington.edu/home/wstein/patches/gap-4.4.10.p12.spkg


---

Comment by mhansen created at 2009-06-04 05:55:48

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 05:55:48

Looks good to me.

Merged in 4.0.1.rc0.
