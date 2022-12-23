# Issue 8938: Multivariate polynomials can be incorrectly formatted in LaTeX

Issue created by migration from https://trac.sagemath.org/ticket/8938

Original creator: fwclarke

Original creation time: 2010-05-09 20:46:29

Assignee: AlexGhitza

Keywords: Multivariate polynomials latex


```
sage: C5.<z> = CyclotomicField(5)
sage: P.<s, t> = C5[]
sage: f = (z^2 + z)*s
sage: f
(z^2 + z)*s
sage: latex(f)
z^{2} + z s
```



---

Attachment

The patch solves this problem, providing latex code which is modelled on that used for single-variable polynomials.  A few doctests have had to be adjusted and LaTeX output provided for elements of QQbar.


---

Comment by fwclarke created at 2010-05-09 20:58:36

Changing status from new to needs_review.


---

Comment by malb created at 2010-06-24 08:54:48

Applies cleanly, doctests pass, reads good.


---

Comment by malb created at 2010-06-24 08:54:48

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-01 07:36:39

I'm getting doctest failures with this under 4.5.alpha1:

```
sage -t  "devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py"
**********************************************************************           
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py", line 379:                                                                                                    
    sage: latex(-I*y+I*x^2)                                                                                   
Expected:                                                                                                     
    \sqrt{-1} x^{2} - \sqrt{-1} y                                                                             
Got:                                                                                                          
    \left(\sqrt{-1}\right) x^{2} + \left(-\sqrt{-1}\right) y                                                  
**********************************************************************                                        
1 items had failures:                                                                                         
   1 of   7 in __main__.example_15                                                                            
***Test Failed*** 1 failures.                                                                                 
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_multi_polynomial_element.py              
         [3.7 s]                                                                                              
sage -t  "devel/sage-reviewing/sage/rings/qqbar.py"                                                           
**********************************************************************                           File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/rings/qqbar.py", line 2223:
    sage: latex(-QQbar.zeta(4) + 5)
Expected:
    -i + 5
Got:
    -\sqrt{-1} + 5
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_42
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_qqbar.py
         [19.5 s]
sage -t  "devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py", line 595:
    sage: S._latex_()
Expected:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} - y z'
Got:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} + 10 y z'
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py", line 602:
    sage: S._latex_()
Expected:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} - y z, x^{5}'
Got:
    '\\text{Closed subscheme of } {\\mathbf P}_{\\Bold{F}_{11}}^2 \\text{ defined by } x^{2} + 10 y z, x^{5}'
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_23
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_algebraic_scheme.py
         [5.4 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-reviewing/sage/rings/polynomial/multi_polynomial_element.py"
        sage -t  "devel/sage-reviewing/sage/rings/qqbar.py"
        sage -t  "devel/sage-reviewing/sage/schemes/generic/algebraic_scheme.py"
Total time for all tests: 28.6 seconds
```



---

Comment by davidloeffler created at 2010-07-01 07:36:39

Changing status from positive_review to needs_work.


---

Comment by fwclarke created at 2010-07-02 07:34:45

It looks like the new failures are caused by #9017 and #9108, both of which overtook this patch.  I'll try to make a new patch compatible with the changes introduced by the other two.


---

Comment by fwclarke created at 2010-07-02 20:00:07

See also #9394.


---

Comment by novoselt created at 2010-11-08 15:56:42

See also #9478.


---

Comment by novoselt created at 2011-07-22 16:39:12

In Sage 4.7.1.rc0 I get for the last line

```
\left(z^{2} + z\right) s
```

so this bug has been fixed along the way.


---

Attachment


---

Comment by novoselt created at 2011-07-22 16:41:33

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-07-22 20:42:44

Changing priority from major to minor.


---

Comment by jhpalmieri created at 2011-07-22 20:42:44

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2011-07-22 20:42:44

Looks good to me.  (There are probably other doctests verifying this from whatever ticket originally fixed it, but having another one can't hurt.)


---

Comment by jdemeyer created at 2011-08-03 14:36:28

Resolution: fixed
