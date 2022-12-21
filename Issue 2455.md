# Issue 2455: [with patch, needs review] improve documentation for multivariate polynomial ideals

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-10 12:07:54

Assignee: tba

CC:  ncalexan

After the patch was applied:


```
SCORE devel/sage-docday2/sage/rings/polynomial/multi_polynomial_ideal.py: 88% (40 of 45)

Missing doctests:
         * redSB(func)
         * wrapper(*args, **kwds)
         * _variety(T, V, v=None)
         * _macaulay2_(self, macaulay2=None)
         * groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)
```


I cannot write Macaulay2 doctests right now because the optional SPKG fails to install. Groebner fan also has issues.

Old:

```
----------------------------------------------------------------------
devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py
SCORE devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py: 68% (32 of 47)

Missing documentation:
         * is_MPolynomialIdeal(x)
         * __enter__(self)
         * __exit__(self, type, value, tb)
         * wrapper(*args, **kwds)
         * f(x,y)
         * _singular_groebner_basis(self)
         * _variety(T, V, v=None)


Missing doctests:
         * __init__(self, singular=singular_default)
         * redSB(func)
         * dimension(self)
         * genus(self)
         * syzygy_module(self)
         * reduced_basis(self)
         * _macaulay2_(self, macaulay2=None)
         * groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)


Possibly wrong (function name doesn't occur in doctests):
         * _magma_groebner_basis(self)
         * _contains_(self, f)
         * _macaulay2_groebner_basis(self)

----------------------------------------------------------------------
```


This patch does not increase the number of doctests very much but focuses on the quality of the doctests and documentation.



---

Attachment

apply against code repository


---

Comment by malb created at 2008-03-12 16:52:50

this patch adds a doctest for the groebner_fan method


---

Comment by malb created at 2008-03-12 16:53:03

Changing assignee from tba to malb.


---

Comment by malb created at 2008-03-12 16:53:03

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2008-03-12 17:57:15

This looks good to me, with one major exception: all the Groebner's were changed to "GrÃ¶bner" and it doesn't display correctly for me.  I think we should stick to standard transliteration or latex.

I say apply after fixing that Groebner business.


---

Comment by malb created at 2008-03-12 18:10:51

Replying to [comment:3 ncalexan]:
> This looks good to me, with one major exception: all the Groebner's were changed to "GrÃ¶bner" and it doesn't display correctly for me.  I think we should stick to standard transliteration or latex.

This is a Trac issue. It prints correctly (as "Gröbner") in my shell, in the reference manual PDF and in the Sage notebook.


---

Comment by ncalexan created at 2008-03-12 18:27:46

I downloaded the patch and it displays wrong in my emacs and in my shell.


---

Comment by malb created at 2008-03-12 18:40:34

this is the UTF-8 free version of the earlier patch


---

Attachment

I've uploaded an UTF-8 free version of the patch. Unfortunately, the time doesn't seem right for Umlauts in Python yet. "Umlauts über alles" postponed, I reckon.


---

Comment by AlexGhitza created at 2008-03-15 18:30:02

Good stuff.  I applied mpoly-ideal-docday-wo-utf8.patch against sage-2.10.3, everything seems fine.  Then I applied 
mpoly-ideal-gfan.patch, and it's also good.  All doctests in sage/rings pass.


---

Comment by mabshoff created at 2008-03-15 19:23:02

Merged mpoly-ideal-docday-wo-utf8.patch and mpoly-ideal-gfan.patch in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-15 19:23:02

Resolution: fixed
