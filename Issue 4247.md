# Issue 4247: plotting -- bug in text and pdf export

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-06 21:25:32

Assignee: was

This works:

```
sage: text("sage", (0,0), rgbcolor=(0r,0r,0r)).save(SAGE_TMP + 'a.pdf')
```

but this doesn't (big confusing traceback):

```
sage: text("sage", (0,0), rgbcolor=(0,0,0)).save(SAGE_TMP + 'a.pdf')
```


The fix will be to make sure text (or whatever) normalizes the rgb input
params to all be of type float. 


---

Attachment


---

Attachment

Apply only trac_4247.patch -- it is rebased against the latest plot.py.  Otherwise, it looks good to me.


---

Comment by mabshoff created at 2008-10-07 23:21:27

Resolution: fixed


---

Comment by mabshoff created at 2008-10-07 23:21:27

Merged in Sage 3.1.3.alpha3
