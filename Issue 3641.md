# Issue 3641: [with spkg, needs review] new Singular upstream release

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-07-11 15:30:33

Assignee: mabshoff

Keywords: singular


```
Tue Nov 27 12:16:36 CET 2007 Singular-3-0-4-1
Changes with respect to 3-0-4
- dmod.lib: fixes wrt. nc_algebra and documentation
- allow assignments like: def l=1,2,3;
```


The new version also has a memleak we reported eliminated.


---

Comment by malb created at 2008-07-11 15:31:13

The new spkg is here:

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-4-20080711.spkg


---

Comment by malb created at 2008-07-11 15:42:13

Installs fine on my Debian/Linux 64-bit, Core2Duo


```
sage -tp 2 devel/sage/sage/rings
...
All tests passed!
```


Sorry, don't have time right now to run the whole test suite.


---

Comment by mabshoff created at 2008-08-02 03:11:50

Changing keywords from "singular" to "singular, editor_mabshoff".


---

Comment by mabshoff created at 2008-08-19 22:50:42

Spkg looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-19 23:08:24

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 23:08:24

Merged in Sage 3.1.2.alpha0
