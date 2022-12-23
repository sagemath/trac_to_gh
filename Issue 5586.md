# Issue 5586: [with patch, needs review]

Issue created by migration from https://trac.sagemath.org/ticket/5586

Original creator: malb

Original creation time: 2009-03-22 17:54:03

Assignee: malb

CC:  burcin rpw

Keywords: crypto, aes

*Before*:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 23.46 s, sys: 0.07 s, total: 23.52 s
Wall time: 23.61 s
```


*After*:

```
sage: sr = mq.SR(4,4,4,8,gf2=True,polybori=True,allow_zero_inversions=True)
sage: %time F,s = sr.polynomial_system()
CPU times: user 3.58 s, sys: 0.04 s, total: 3.62 s
Wall time: 3.63 s
sage: %time F,s = sr.polynomial_system()
CPU times: user 2.05 s, sys: 0.00 s, total: 2.05 s
Wall time: 2.05 s
```



---

Attachment


---

Comment by malb created at 2009-03-25 14:18:46

allows symbols for plaintext/ciphertext bits


---

Attachment


---

Comment by burcin created at 2009-03-25 18:28:37

Does attachment:sr_symbolic.patch depend on anything?

I get this while trying to apply to a clean 3.4 tree, or after applying attachment:faster_sr.patch:


```
applying sr_symbolic.patch
patching file sage/crypto/mq/sr.py
Hunk #3 succeeded at 1618 with fuzz 1 (offset 29 lines).
Hunk #4 FAILED at 1925
1 out of 7 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh sr_symbolic.patch
```



---

Comment by malb created at 2009-03-25 18:42:50

Uh, it seems this ticket depends on #5493 and #5527.


---

Comment by mvngu created at 2009-03-27 06:02:20

OK, I applied the patches against Sage 3.4 in this order:
 1. the patch at #5493
 1. that patch at #5527
 1. finally the patches on this ticket
But I got doctest failure:

```
[mvngu@sage sage-3.4]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py 
sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"        
**********************************************************************
File "/home/mvngu/sage-3.4/devel/sage-5586/sage/crypto/mq/sr.py", line 2002:
    sage: F.round(0)
Expected:
    (P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003)
Got:
    [P000 + w100 + k000, P001 + w101 + k001, P002 + w102 + k002, P003 + w103 + k003]
**********************************************************************
File "/home/mvngu/sage-3.4/devel/sage-5586/sage/crypto/mq/sr.py", line 2004:
    sage: F.round(-2)
Expected:
    (k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, ...)
Got:
    [k100 + x100 + x102 + x103 + C000, k101 + x100 + x101 + x103 + C001 + 1, k102 + x100 + x101 + x102 + C002 + 1, k103 + x101 + x102 + x103 + C003, x100*w100 + x100*w103 + x101*w102 + x102*w101 + x103*w100, x100*w100 + x100*w101 + x101*w100 + x101*w103 + x102*w102 + x103*w101, x100*w101 + x100*w102 + x101*w100 + x101*w101 + x102*w100 + x102*w103 + x103*w102, x100*w100 + x100*w102 + x100*w103 + x100 + x101*w100 + x101*w101 + x102*w102 + x103*w100, x100*w101 + x100*w103 + x101*w101 + x101*w102 + x101 + x102*w100 + x102*w103 + x103*w101, x100*w100 + x100*w102 + x101*w100 + x101*w102 + x101*w103 + x102*w100 + x102*w101 + x102 + x103*w102, x100*w101 + x100*w102 + x101*w100 + x101*w103 + x102*w101 + x103*w103 + x103, x100*w100 + x100*w101 + x100*w103 + x101*w101 + x102*w100 + x102*w102 + x103*w100 + w100, x100*w102 + x101*w100 + x101*w101 + x101*w103 + x102*w101 + x103*w100 + x103*w102 + w101, x100*w100 + x100*w101 + x100*w102 + x101*w102 + x102*w100 + x102*w101 + x102*w103 + x103*w101 + w102, x100*w101 + x101*w100 + x101*w102 + x102*w100 + x103*w101 + x103*w103 + w103, x100*w102 + x101*w101 + x102*w100 + x103*w103 + 1]
**********************************************************************
1 items had failures:
   2 of  25 in __main__.example_35
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/sage-3.4/tmp/.doctest_sr.py
         [73.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"
Total time for all tests: 73.1 seconds
```



---

Comment by malb created at 2009-03-27 10:47:44

Sorry 'bout this: you'll also need to apply the patch from #5576 (`mpolynomialsystem_rest.patch`). I kept working on too many things in parallel and thus the mess:

Here's what I've applied locally:
 * sr_sphinx.patch #5493
 * weil_restriction.patch #5569
 * mpolynomialsystem_rest.patch #5576
 * trac_5527_sr-sphinx.patch #5527
 * faster_sr.patch #5586
 * sr_symbolic.patch #5586


---

Comment by mvngu created at 2009-03-31 04:37:27

Again, I see timed out errors. With Sage 3.4, I applied patches in this order:
 1. sr_sphinx.patch at #5493
 1. weil_restriction.patch at #5569
 1. mpolynomialsystem_rest.patch at #5576
 1. trac_5527_sr-sphinx.patch at #5527
 1. faster_sr.patch at #5586 (this ticket)
 1. sr_symbolic.patch at #5586  (this ticket)
Doctesting gave me this:

```
[mvngu@sage sage-3.4-sage.math-only-x86_64-Linux]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py 
sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"        
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"
Total time for all tests: 1800.2 seconds
```




As for Sage 3.4.1.alph0, I applied patches in this order:
 1. mpolynomialsystem_rest.patch at #5576
 1. faster_sr.patch at #5586 (this ticket)
 1. sr_symbolic.patch at #5586  (this ticket)
Doctesting gave me timed out errors as well:

```
[mvngu@sage sage-3.4.1.alpha0-sage.math-only-x86_64-Linux]$ ./sage -t -long devel/sage-5586/sage/crypto/mq/sr.py
sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"        
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [1800.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-5586/sage/crypto/mq/sr.py"
Total time for all tests: 1800.1 seconds
```



---

Comment by malb created at 2009-03-31 08:38:01

I hope you don't mind me asking, but are you sure you applied the correct mpolynomialsystem_rest.patch? Can you check that the `test_consistency()` function sr.py has the line 

```
F = F.subs(s)
```

instead of

```
F.subs(s)
```


Cheers,
Martin


---

Comment by mvngu created at 2009-04-02 08:11:36

Replying to [comment:8 malb]:
> I hope you don't mind me asking, but are you sure you applied the correct mpolynomialsystem_rest.patch? Can you check that the `test_consistency()` function sr.py has the line 
> {{{
> F = F.subs(s)
> }}}
> instead of
> {{{
> F.subs(s)
> }}}


Yep, you're right. I downloaded `mpolynomialsystem_rest.patch` again and then proceeded with applying patches against Sage 3.4.1.alpha0 in this order:
 1. mpolynomialsystem_rest.patch at #5576
 1. faster_sr.patch at #5586 (this ticket)
 1. sr_symbolic.patch at #5586 (this ticket) 
This time doctests didn't reveal any timed out errors. I don't feel qualified to review the math content of the patches; I was only trying to apply patches and run doctests to see if they succeed or fail.


---

Comment by burcin created at 2009-05-12 14:58:10

Looks good to me.


---

Attachment

apply last


---

Comment by mabshoff created at 2009-05-12 17:14:06

fix_long_doctest.patch fixes the timeout problem.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 17:15:48

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 17:15:48

Resolution: fixed
