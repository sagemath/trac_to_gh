# Issue 4199: Followup to #4111: pari related real_mpfr.pyx doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/4199

Original creator: mabshoff

Original creation time: 2008-09-26 02:45:11

Assignee: robertwb

CC:  alexghitza

After merging the patches from #4111 the following happens in Sage 3.1.3.alpha2:

```
sage -t -long devel/sage/sage/rings/real_mpfr.pyx           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/real_mpfr.py", line 1900:
    sage: RR(-1.234567)._pari_()
Expected:
    -1.2345670000000000000
Got:
    -1.2345670000000000001
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_58
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_real_mpfr.py
         [11.2 s]
exit code: 1024
```

RobertWB says:
Actually, after those patches I get

```
sage: 1.2.parent() is RR
True
```

Sit looks like a pari issue for sure. For example, I get

```
sage: (-1.23456)._pari_()
-1.2345600000000000001
```

which isn't using RR.__call__ at all.

Alex Ghitza claims that #4096 (which is also wanted for 3.1.3) will fix the issue. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 04:08:11

Fixed by merging #4096.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 04:08:11

Resolution: fixed
