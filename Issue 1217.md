# Issue 1217: libfplll error codes - leftover from #1188

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 15:54:11

Assignee: malb

On IRC:

```
[11:46] <wjp> malb: I slightly updated your fplll patch replacing ret < 0 by ret != 0 since fpLLL returns positive values on error
[11:46] <malb> I disagree
[11:46] <malb> are you sure it has to be an error if !=0 ?
[11:47] <malb> it just returns kappa, doesn't it?
[11:47] <wjp> only in error case, as far as I can tell
[11:47] <malb> the example will not work if you test for ret != 0
[11:47] <malb> i.e. the doctest I just added
[11:48] <wjp> that's strange; I'll look through the fplll sources again then
[11:48] <malb> also heuristic may return kappa != 0 because it is not guaranteed to be LLL reduced anyway
[11:48] <malb> I only superficially scanned the source though
[11:48] <wjp> hm, so it might not be usable as an error code
[11:49] <malb> yes, but I am not sure, we could ask Damien?
```

For a patch see fplll2.patch from #1188.

Cheers,

Michael


---

Comment by malb created at 2008-01-16 17:21:08

Changing keywords from "" to "wjp".


---

Comment by malb created at 2008-01-16 17:21:08

Checking for "< 0" seems to be fine as far as I can see (we do that). So I vote for `invalid`.


---

Comment by malb created at 2008-01-16 17:21:16

Changing keywords from "wjp" to "".


---

Comment by wjp created at 2008-01-16 19:04:24

I think that we should check for != 0 in all fpLLL calls that are guaranteed to return an LLL-reduced basis, including 'wrapper'.

Rationale: Damien Stehlé writes:

```
Internally, LLL calls may fail (which is why we need the wrapper). If
a LLL call returns 0, then it went fine. Otherwise, it can return -1
or a positive value. -1 means that there were too many loop iterations
(very unfrequent), and >0 means that the size-reduction failed (much
more frequent if the precision is not high enough).
```

This means that a positive value indicates a non-reduced basis, which is an error condition for the proved fpLLL functions. (The actual returned value kappa seems to indicate the row in which the size-reduction failed.)

malb: on IRC, you mentioned a testcase that triggered a positive return value in the main wrapper. Which one? The doctest in `fplll.pyx`'s `wrapper()` seems to work for me. (I tried ~20 times since it has random input.)


---

Comment by malb created at 2008-01-18 16:25:18

I suggest to check for
 * wrapper: !=0
 * proved: !=0
 * heuristic: nothing
 * fast: nothing

as this seems to be correct and to worry about resulting errors afterwards.


---

Comment by wjp created at 2008-01-18 16:57:25

That makes sense. The attached patch implements it.


---

Attachment


---

Comment by malb created at 2008-01-18 17:21:18

The patch looks good and applies cleanly, but:


```
File "fplll.pyx", line 162:
    sage: F.wrapper()
Exception raised:
    Traceback (most recent call last):
      File "/home/malb/SAGE/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[4]>", line 1, in <module>
        F.wrapper()###line 162:
    sage: F.wrapper()
      File "fplll.pyx", line 187, in sage.libs.fplll.fplll.FP_LLL.wrapper
        raise RuntimeError, "fpLLL returned %d != 0"%ret
    RuntimeError: fpLLL returned 3 != 0
```


This is on a 64-bit Linux. I assume this can be reproduced on `sage.math`.

PS: Trying something bold and reassigning this ticket to wjp, feel free to bounce it.


---

Comment by malb created at 2008-01-18 17:21:18

Changing assignee from malb to wjp.


---

Comment by malb created at 2008-01-18 17:52:54


```
sage: from sage.libs.fplll.fplll import FP_LLL
sage: W = random_matrix(ZZ,7,7)
sage: W # result random

[ -1  -1  -5  -1  -1  -8   3]
[  2   1   1   3  -3  -6   1]
[  1   1   1  -1  -3   1   2]
[ -2   2   1   1 -58  -1  -2]
[  1   1   1  -1   1  -3  -1]
[ -1   1   1   1   3   2 -31]
[  1  -1  -3   1   1  -2   1]

sage: print W.list()

[-1, -1, -5, -1, -1, -8, 3, 2, 1, 1, 3, -3, -6, 1, 1, 1, 1, -1, -3, 1, 2, -2, 2, 1, 1, -58, -1, -2, 1, 1, 1, -1, 1, -3, -1, -1, 1, 1, 1, 3, 2, -31, 1, -1, -3, 1, 1, -2, 1]

sage: F = FP_LLL(W)
sage: F.wrapper()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)
/home/malb/<ipython console> in <module>()
/home/malb/fplll.pyx in sage.libs.fplll.fplll.FP_LLL.wrapper()
<type 'exceptions.RuntimeError'>: fpLLL returned 3 != 0
sage: F._sage_()
[                    1                     1                     1                    -1                     1                    -3                    -1]
[                    1                     1                     1                    -1                    -3                     1                     2]
[                    1                    -1                    -3                     1                     1                    -2                     1]
[  1889035965444230183   -782769071737015336  -3454574108918260854    782769071737015340 -16557708108281492442  14115538695983654830  14617827127031307303]
[                   -5                    -1                    -1                    -1                    -1                    -2                     0]
[                   -4                     4                     3                     3                     4                    -1                     6]
[                   -4                     9                    -3                     1                  
```



---

Comment by malb created at 2008-01-20 17:44:44

The patch is fine, it just exposes a bug on my machine. I say apply.


---

Comment by mabshoff created at 2008-01-21 05:34:56

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:34:56

Resolution: fixed
