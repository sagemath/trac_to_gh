# Issue 1810: [with patch] refactoring to improve finite field reference manual

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-17 21:29:21

Assignee: tba

The patch removes `FiniteField_prime_modn` from `finite_field.py` because it was odd that this implementation was the only showing up in the reference manual. Also, `GF` is now defined in `rings.all` rather than in `rings.finite_field` to avoid that the documentation for it shows up twice. Finally, a more verbose description of the finite field module is given at the top of the `finite_field.py` file and some doctests were added to `FiniteField_prime_modn`.


---

Attachment


---

Comment by mhansen created at 2008-02-27 18:21:34

I get the following on a clean 2.10.2 install:


```
applying /home/mike/Desktop/finite_field_refactor_doc.patch
patching file sage/rings/finite_field.py
Hunk #1 succeeded at 1 with fuzz 2 (offset -2 lines).
Hunk #5 FAILED at 147
1 out of 13 hunks FAILED -- saving rejects to file sage/rings/finite_field.py.rej
abort: unable to find sage/rings/padics/eisenstein_extension_generic_element.py or sage/rings/padics/eisenstein_extension_generic_element.py for patching

```



---

Comment by malb created at 2008-02-27 18:38:37

I am rebasing right now. `make test` is running and looking good. Then, I'm afraid I'll have to check if I can apply the patch against 2.10.3.alpha0.


---

Comment by malb created at 2008-02-27 18:46:22

rebased against 2.10.2


---

Attachment

rebased against 2.10.3.alpha3


---

Attachment

add this on top of the 2.10.3.alpha0 patch, I forgot to hg add a file


---

Attachment

Add `gfp.patch` on top of `finite_field_refactor_doc.3.patch`, I forgot to `hg add finite_field_prime_modn.py`


---

Attachment

guava_fix.patch needs also to be applied after the other patches


---

Comment by mhansen created at 2008-02-28 08:37:00

Applies cleanly to 2.10.3.alpha0 and passes tests for me.  

To apply the patch, do the following,

1) Apply finite_field_refactor_doc.3.patch

2) Apply gfp.patch

3) hg add finite_field_prime_modn.py

4) Apply guava_fix.patch


---

Comment by mabshoff created at 2008-03-02 22:51:10

Merged finite_field_refactor_doc.3.patch, gfp.patch and guava_fix.patch in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-02 22:51:10

Resolution: fixed
