# Issue 8365: Reorganize slightly the outline of the documentation of Polynomial Rings

Issue created by migration from Trac.

Original creator: mmezzarobba

Original creation time: 2010-02-25 16:25:37

Assignee: mvngu




---

Attachment


---

Comment by mmezzarobba created at 2010-02-25 16:31:45

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-26 00:20:20

apply on top of previous


---

Attachment

The patch [trac_8365_PolynomialRings_doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8365/trac_8365_PolynomialRings_doc.patch) does some much needed re-organization of the chapter on polynomial rings. It re-organizes the stuff relating to infinite polynomial rings into a new section, but doesn't provide a link to get to that new section. The patch [trac_8365-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8365/trac_8365-reviewer.patch) provides such a link. Only the latter patch needs review by anyone but me. If it gets a positive review, then the whole ticket gets a positive review.


---

Comment by mmezzarobba created at 2010-02-26 08:38:43

Changing status from needs_review to positive_review.


---

Comment by mmezzarobba created at 2010-02-26 08:38:43

Looks like I forgot one line in polynomial_rings.rst, indeed (sorry for that). The reviewer patch fixes that and works fine for me. If I understand the previous comment correctly, this means I can give it positive review.


---

Comment by mvngu created at 2010-03-02 22:27:13

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 22:27:13

Merged in this order:

 1. [trac_8365_PolynomialRings_doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8365/trac_8365_PolynomialRings_doc.patch)
 1. [trac_8365-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8365/trac_8365-reviewer.patch)

Marc: Avoid putting the following line in your patch file:

```
exporting patch:
```

It would result in Mercurial ignoring your commit message, so that your commit message won't show up in the changelog.
