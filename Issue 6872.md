# Issue 6872: #6596 follow-up: typo in docstring

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-03 05:28:35

Assignee: tba

CC:  malb

This is a follow-up to #6596 to fix a typo introduced in a docstring.


---

Comment by mvngu created at 2009-09-03 05:31:19

depends on #6596


---

Attachment


---

Comment by malb created at 2009-09-03 08:50:36

I don't understand the reason for the change (because I didn't look at the produced HTML) but it is definitely fine.


---

Attachment

without the patch


---

Comment by mvngu created at 2009-09-03 09:14:37

The module `sage/libs/singular/groebner_strategy.pyx` is currently not in the reference manual. After adding it to the reference manual and (re)building it, you get something like that shown in the screenshot `trac_6872-without-patch.png`. Notice the redundant colon ":" after "ALGORITHM". Now supposing you leave "ALGORITHM::" alone and move "Uses Singular via libSINGULAR" to a new line. Building the reference manual would result in a warning:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/libs/singular/groebner_strategy.so:docstring of sage.libs.singular.groebner_strategy.GroebnerStrategy:8: (WARNING/2) Literal block expected; none found.
```

But removing the redundant colon and the documentation builder is now happy. Hence the patch `trac_6872-fix-typo.patch`.


---

Comment by mvngu created at 2009-09-03 09:14:37

Resolution: fixed


---

Comment by malb created at 2009-09-03 11:16:16

Thanks, very well explained!
