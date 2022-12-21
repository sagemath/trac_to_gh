# Issue 5374: [with patch, needs review] minor problem with ReST in misc/hg.py

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-02-26 00:17:28

Assignee: jhpalmieri

This fixes the one problem remaining from ticket #4919.



---

Attachment


---

Comment by jhpalmieri created at 2009-02-26 00:37:23

Changing component from misc to documentation.


---

Comment by mvngu created at 2009-02-27 09:11:15

REFEREE REPORT



The patch *hg-rst.patch* applied fine against 3.4.alpha0 and all doctests passed with the options

```
-t -long -optional
```

Well, one doesn't need to run doctests on `sage/misc/` since this is just a minor formatting fix, but I did so anyway just to make sure... The reference manual built OK with this command

```
sage -docbuild reference html
```

Checking the relevant file

```
/path/to/html/en/reference/sage/misc/hg.html
```

I see that the formatting of both `import_patch()` and `patch()` is consistent with each other. So positive review.


---

Comment by mabshoff created at 2009-02-28 16:23:42

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 16:23:42

Resolution: fixed
