# Issue 1277: two further flint spkg problems

Issue created by migration from https://trac.sagemath.org/ticket/1277

Original creator: was

Original creation time: 2007-11-26 06:06:45

Assignee: was


```
On Nov 25, 2007 9:52 PM, Bill Hart <goodwillhart@googlemail.com> wrote:
> 
> This is a compiler bug which we've seen before. On Itanium the build
> should not be using the -funroll-loops flag.
> 
> I guess we need to check for ia64 when setting the compiler flags?

The culprit is this line, which is now in patches/makefile:

CFLAGS = $(INCS) -funroll-loops -fexpensive-optimizations $(FLINT_TUNE) -O3^M

On ia64 FLINT_TUNE is properly set to not include funroll-loops, but for some dumb
reason -funroll-loops is put in the CFLAGS explicitly in the patches/makefile included
in Sage.  

Changing the above line to 

CFLAGS = $(INCS)  -fexpensive-optimizations $(FLINT_TUNE) -O3^M

completely fixes the problem. 

As an aside, I don't think the .svn subdirectories should be included with
with flint-*.spkg.  

A new flint spkg is at 
```


  http://sage.math.washington.edu/home/was/tmp/flint-0.9-r1075.p2.spkg



---

Comment by mabshoff created at 2007-12-06 20:52:28

The new FLINT.spkg at

http://sage.math.washington.edu/home/mabshoff/flint-1.0.spkg

should solve the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-09 17:23:29

Resolution: fixed


---

Comment by mabshoff created at 2008-01-09 17:23:29

This was fixed in the Sage 2.9.x time frame, as confirmed by Kate in https://groups.google.com/group/sage-devel/t/40538e2d4e6742dd

Cheers,

Michael
