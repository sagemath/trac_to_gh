# Issue 1189: update sympy to 0.5.7, patch to make SymPy and SAGE work nicely

Issue created by migration from https://trac.sagemath.org/ticket/1189

Original creator: certik

Original creation time: 2007-11-17 00:15:13

Assignee: was

Please update to sympy 0.5.7 using the attached spkg.

Then apply the attached patch that will allow SAGE to freely mix SymPy and SAGE expressions.


---

Comment by certik created at 2007-11-17 00:18:56

Changing type from defect to enhancement.


---

Attachment

Here is the link to the new sympy spkg:

http://dakol.fsik.cvut.cz/~ondra/sympy-0.5.7.spkg

Please update this first, only then use the patch above.


---

Comment by certik created at 2007-11-17 00:18:56

Changing component from algebraic geometry to calculus.


---

Comment by certik created at 2007-11-17 00:26:12

After upgrading the spkg and applying the patch, please check, that everything works as it should by:

$ ./sage -t devel/sage/sage/calculus/test_sympy.py 
sage -t  devel/sage-main/sage/calculus/test_sympy.py        
         [2.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.9 seconds


---

Comment by certik created at 2007-11-17 23:20:51

Changelog of the spkg:

* Script "get-hg" for getting hg sources added
* get-orig-sources updated to download SymPy 0.5.7

Changelog of the patch:

* basic SymPy and SAGE objects can now be freely mixed


---

Comment by certik created at 2007-11-17 23:23:49

Once again, this time with correct formatting.

Changelog of the spkg:

* Script "get-hg" for getting hg sources added


* "get-orig-sources" updated to download SymPy 0.5.7

Changelog of the patch:

* basic SymPy and SAGE objects can now be freely mixed


---

Comment by mabshoff created at 2007-11-18 06:15:32

Merged in 2.8.13.alpha0.


---

Comment by mabshoff created at 2007-11-18 06:15:32

Resolution: fixed


---

Comment by mabshoff created at 2007-11-18 13:31:34

Arrg, the bit of the patch in coerce.pyx causes segfaults. So the patch is backed out, but the spkg is still in.

Ondrej: Either open a new ticket and resubmit the patch or reopen this ticket.

Cheers,

Michael


---

Comment by certik created at 2007-11-18 13:59:08

Oops. I only executed the tests in calculus/test_sympy.py.

I am openning the ticket, but leaving it to a later milestone, because I don't have time at the moment to fix that. Is there someone more experienced to maybe see immediatelly what is wrong?

I run "./sage -t *" and indeed I am getting these errors:

sage -t  devel/sage-main/sage/schemes/generic/spec.py       sh: line 1:  9143 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_spec.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


sage -t  devel/sage-main/sage/rings/number_field/order.py   sh: line 1:  9354 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_order.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage -t  devel/sage-main/sage/rings/integer_ring.pyx        sh: line 1:  9855 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_integer_ring.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


sage -t  devel/sage-main/sage/rings/complex_field.py        sh: line 1:  9919 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_complex_field.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage -t  devel/sage-main/sage/rings/quotient_ring.py        sh: line 1:  9934 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_quotient_ring.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.pysh: line 1: 10028 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_multi_polynomial_ideal.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage -t  devel/sage-main/sage/rings/real_rqdf.pyx           sh: line 1: 10557 Segmentation fault      /home/ondra/ext/sage-2.8.12-debian32-i686-Linux/local/bin/python .doctest_real_rqdf.py >.doctest/out 2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

...


---

Comment by certik created at 2007-11-18 13:59:08

Resolution changed from fixed to 


---

Comment by certik created at 2007-11-18 13:59:08

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-11-18 14:03:02

Hehe, I assumed you ran testall, especially after touching coerce.pyx. I tagged this against 2.9 for now. It will automatically get moved forward every time we complete a milestone.

I also changed the summary to reflect the remaining issue.

Cheers,

Michael


---

Comment by certik created at 2007-11-19 08:40:20

> Hehe, I assumed you ran testall, especially after touching coerce.pyx.

Yeah, I am still learning how to properly contribute to SAGE. :)


---

Attachment

The patch was fixed, now it passes all tests:

http://sagetrac.org/sage_trac/attachment/ticket/1189/sympy2.patch

But probably needs some review before committing.


---

Comment by robertwb created at 2007-11-27 03:43:37

I was not able to apply sympy2.patch cleanly against Sage 2.8.14. 

That said, I think _verify_canonical_coercion_c is the wrong thing to call here--please see the attached change which should fix the segfault issue in a much cleaner way and allow stuff like
 

```
sage: Integer(1) + sympy.Symbol("x")
x + 1
```



---

Attachment


---

Comment by certik created at 2007-11-27 17:10:35

Unfortunately, I don't have time to do it (leaving to Spain tomorrow). But please use the original sympy.patch + sympy-coerce.patch from Robert, that should do the job.

Thanks a lot.


---

Comment by mabshoff created at 2007-12-02 23:23:01

Merged in 2.8.15.rc0 - finally ;)


---

Comment by mabshoff created at 2007-12-02 23:23:01

Resolution: fixed


---

Comment by mabshoff created at 2007-12-03 00:30:05

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-03 00:30:05

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-03 00:30:05

On sage.math the above two patches cause doctest failures in rings/polynomial/multi_polynomial_ideal.py - so reopen.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 02:40:23

This is probably not the patches direct fault, but we need to fix the other segfault first before merging this. Sage not working on sage.math isn't really an option.

Sorry, Ondrej.

Cheers,

Michael


---

Comment by robertwb created at 2007-12-06 21:41:39

I wasn't able to reproduce the errors in rings/polynomial/multi_polynomial_ideal.py, or anywhere for that matter. Could you clarify? 

Still running testall...


---

Comment by robertwb created at 2007-12-06 22:37:51

Testall succeeded for me with these patches.


---

Comment by mabshoff created at 2007-12-09 12:50:51

Well, the segfault happened to me on sage.math. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-10 22:30:24

Resolution: fixed


---

Comment by mabshoff created at 2007-12-10 22:30:24

Finally merged in 2.9.alpha5 :)
