# Issue 5388: Remove hg_doc* in Sage 3.4 since it no longer works once the doc repo is gone

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-26 22:53:03

Assignee: tba

CC:  mhansen jhpalmieri

This come up via other tickets. Removing the functionality completely might be not the best solution, but having it print a warning and apply the patch to devel might be an alternative. Just printing the warning might be more prudent since any patch against the doc repo will likely be broken anyway.

I am sure the manual needs to be updated about hg_doc.* going away, but that can be another ticket in case it isn't implemented yet.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-26 22:56:39

I'm pretty sure I already removed this in the patches in alpha0.


---

Comment by mabshoff created at 2009-02-26 23:26:55

Resolution: invalid


---

Comment by mabshoff created at 2009-02-26 23:26:55

Replying to [comment:1 mhansen]:
> I'm pretty sure I already removed this in the patches in alpha0.

Yes, I should have checked first that it is gone instead of opening a ticket :(

```
sage: hg_ [TAB]
hg_extcode  hg_sage     hg_scripts  
sage:
```


I just someone (I believe it was John) mention an issue with hg_doc not working, but that might have been for a pre-3.4 sage build or one that did not have all patches applied. 

So: invalid.

Cheers,

Michael
