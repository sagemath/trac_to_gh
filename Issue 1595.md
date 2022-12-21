# Issue 1595: do something about the pari overflow test

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-24 18:43:56

Assignee: failure

This disturbs people:

```
sage -t  devel/sage-main/sage/libs/pari/gen.pyx             python(85565) malloc: *** mmap(size=4096000000) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
```


This would disturb people less:

```
[This is the Trac macro *The following doctest contains an intentional memory error.* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#The following doctest contains an intentional memory error.-macro)
sage -t  devel/sage-main/sage/libs/pari/gen.pyx             python(85565) malloc: *** mmap(size=4096000000) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
```



---

Comment by mabshoff created at 2007-12-25 09:33:55

The issue has been added to the FAQ. It might be easiest to direct stderr to some file. That way people should never see the offending message.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 18:24:59

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-02-08 03:18:55

On OSX 10.5 64 bit, FreeBSD 7 as well as Solaris Sparc this overflow test leads to a segfault/failed test. I am not sure what to do with this test since the fact that it worked purely depends on the OS behavior for large allocs. 

Maybe making it "optional -- large" or "optional -- $SOME_OS_LIST" would be a way out of this. Anyway, there seems to be no reliable way to test the allocation of huge amounts of memory and expect the Sage session to survive.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-04-08 01:04:56

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-08 04:29:55

Oops, change the summary, too.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-08 10:46:31

Ooops, this patch needs to be rebased for 3.4.1.rc1 - new patch coming up in the morning.

Cheers,

Michael


---

Attachment

Merged trac_1595-rebase.patch in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 02:22:50

Resolution: fixed
