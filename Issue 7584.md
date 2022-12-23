# Issue 7584: Pari spkg: remove junk file pari-2.3.3.p5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/7584

Original creator: schilly

Original creation time: 2009-12-02 16:57:41

Assignee: tbd

From IRC:

```
08:32 < schilly> mvngu: i found a spkg inside the pari spkg. was that me while 
                 scripting or is is this everywhere?
08:32 < mvngu> schilly: Let me check with Sage 4.3.alpha0
08:33 < schilly> ok
08:36 < mvngu> With Sage 4.2.1, it's the file pari-2.3.3.p5/pari-2.3.3.p5.spkg, 
               which a small file. The same goes for Sage 4.3.alpha0.
08:37 < mvngu> That file should be removed; it's not used anywhere as far as I 
               can tell.
08:37 < mvngu> I think it was introduced during the update to .p5
08:37 < mvngu> Unintentionally, of course.
```



---

Comment by mhansen created at 2009-12-02 19:03:28

I went ahead and removed this from the spkg.  I also checked in the changes that had been made into the repo.


---

Comment by mhansen created at 2009-12-02 19:03:28

Resolution: fixed
