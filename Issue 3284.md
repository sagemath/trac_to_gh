# Issue 3284: [with patch, needs work, SEGFAULTs!] use weakref for PolyBoRi

Issue created by migration from https://trac.sagemath.org/ticket/3284

Original creator: malb

Original creation time: 2008-05-23 17:15:34

Assignee: malb

CC:  burcin polybori

Keywords: PolyBoRi, segfault

*First: Do not apply this patch unless you want to fix it, it SEGFAULTs*

This patch makes sure only one `BooleanPolynomialRing` per parameter set is created by returning a reference to a prior created object if there is such a reference. However, as a consequence the following happens:


```
$ sage -t -verbose sage/rings/polynomial/pbori.pyx   
...
Trying:
    m = M._coerce_(N(y*z)); m###line 1261:_sage_    >>> m = M._coerce_(N(y*z)); m
Expecting:
    y*z
Operands come from different manager.
```


I don't know where to look for a solution here. So I'm putting the patch up here in the hope that Burcin, Michael, Alexander or someone else doesn't have such a hard time finding the cause of this bug.


---

Comment by PolyBoRi created at 2008-05-23 21:51:32

Hello again,
"Operands come from different manager." is an error message from the deep of the BDD-package behind the PolyBoRi data structures. It means, that one tries to do a binary operation with elements from two different rings. But operation does not necessary mean the y*z operation, it maybe triggered by something else in N() oder _coerce_

Best regards,
  Alexander


---

Comment by malb created at 2008-05-25 12:57:46

My guess is that we somewhere forget to set the global ring maybe?


---

Attachment

this patch is supposed to work


---

Comment by malb created at 2008-05-25 16:09:57

Changing keywords from "PolyBoRi, segfault" to "PolyBoRi".


---

Comment by malb created at 2008-05-25 16:10:26

Please review the updated patch which fixes the doctest failure.


---

Comment by burcin created at 2008-06-04 22:33:55

I don't see why the changes to pbori.pyx other than the addition of the R._pbring.activate() at line 4131 are necessary. 

In `BooleanPolynomialRing_constructor`, the if statement (including the elif) at line 430 seems to be redundant, since normalize_names already returns a tuple. It could be that I'm reading the source of normalize_names wrong though.


---

Comment by malb created at 2008-06-04 22:36:41

True, it is unrelated to this particular weakref patch. I mixed up two things. The renaming only cleans up since vars is a built-in identifier and it is considered bad practice to use it like we used to use it.


---

Comment by craigcitro created at 2008-06-15 21:48:13

Changing keywords from "PolyBoRi" to "PolyBoRi, editor_malb".


---

Comment by burcin created at 2008-06-20 03:46:36

BooleanPolynomialRing user friendly names


---

Attachment

`BooleanPolynomialRing_constructor` in malb's original patch fails when only names are provided, attachment:trac3284_BooleanPolynomialRing_normalize_names.patch fixes this case.

I give malb's patch (followed by mine) a positive review. Someone should review my patch, especially the change to `normalize_names`.


---

Comment by malb created at 2008-06-24 06:44:37

Burcin's patch looks good and passes doctests.


---

Comment by mabshoff created at 2008-06-25 02:13:44

All doctests pass with the patch applied and valgrind gives pbori.pyx a clean bill of health.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-25 02:13:59

Resolution: fixed


---

Comment by mabshoff created at 2008-06-25 02:13:59

Merged in Sage 3.0.4.alpha1
