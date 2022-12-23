# Issue 9227: units.length.millimeter missing

Issue created by migration from https://trac.sagemath.org/ticket/9227

Original creator: schilly

Original creation time: 2010-06-12 12:55:42

Assignee: AlexGhitza

CC:  asjarman@xtra.co.nz

a millimeter [mm] is 1/1000 of a meter and very often used by engineers.


---

Attachment

patch to add mm and km


---

Comment by allmar created at 2010-08-29 06:07:32

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-09-02 11:09:50

Changing component from algebra to misc.


---

Comment by aapitzsch created at 2011-01-07 09:02:12

You mentioned

```
Equal to 1000 meters.
```

twice. You should replace one by a comparison to yards, feet or something else.


---

Attachment


---

Comment by spice created at 2011-01-07 23:04:37

Doctests fail due to there being TAB characters in this patch.

I've added an updated patch, which replaces the TAB characters in the patch with spaces, as well as changing line 650:
`'kilometer':'Equal to 1000 meters.\nEqual to 1000 meters.',`
to
`'kilometer':'Equal to 1000 meters.\nEqual to 3280.8399 feet.',`


---

Comment by aly.deines created at 2011-01-10 01:12:34

Looks good to me.


---

Comment by aly.deines created at 2011-01-10 01:12:34

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-25 08:14:40

Resolution: fixed
