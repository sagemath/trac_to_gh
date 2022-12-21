# Issue 3811: number fields in different polynomials compare differently

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-08-12 05:06:52

Assignee: was

Keywords: number field comparison cmp

The doctests describe it best, but it was the case that


```
sage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(ZZ['y'].0^4 + 23, 'a')
True
sage: NumberField(ZZ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')
False
sage: NumberField(QQ['x'].0^4 + 23, 'a') == NumberField(QQ['y'].0^4 + 23, 'a')
False
```


Not good.  The variable of the defining polynomial should not matter.


---

Attachment


---

Comment by was created at 2008-08-13 02:46:17

EXCELLENT PATCH!


Request: Please stop exporting plain text patches.  Export hg patches instead, or there will be no commit messages in the hg log, and the default is to check the patch in as the person applying it.


---

Comment by mabshoff created at 2008-08-13 02:47:22

Nick,

there is a qexport command that you should use. It will produce proper patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 08:35:27

Merged in Nick's name in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-13 08:35:27

Resolution: fixed
