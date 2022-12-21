# Issue 4616: cosine_series_coefficient hangs

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-11-25 12:47:24

Assignee: wdj

This is a method of the Piecewise class (which I use almost on a daily basis in teaching):


```
sage: f1 = lambda x: x*(pi-x)
sage: f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (0,pi),f1)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: f.cosine_series_coefficient(0,pi)
                                               
```

Requires a ctl-c.


---

Comment by mabshoff created at 2008-11-25 12:57:49

I can confirm this problem on a box that has no problem with the Sage <-> Maxima communication (I was dubious initially since David has reported problems with Maxima for his recent Sage installs).

Cheers,

Michael


---

Comment by wdj created at 2008-12-04 16:53:28

Does #4693 fix this bug?


---

Comment by mabshoff created at 2008-12-04 17:06:38

Yes, #4693 fixes the bug:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f1 = lambda x: x*(pi-x)
sage: f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (0,pi),f1)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: f.cosine_series_coefficient(0,pi)
pi^2/3
sage: 
Exiting SAGE (CPU time 0m0.17s, Wall time 2m3.53s).
Exiting spawned Maxima process.
```

Do you want to add a doctest so we can close this?
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by wdj created at 2008-12-04 18:19:43

I would but I still can't apply the patch for #4693:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: piecewise2
sage: hg_sage.apply("/Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch")
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage" && hg status
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage" && hg status
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage" && hg import   "/Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch"
applying /Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch
patching file sage/functions/piecewise.py
Hunk #25 FAILED at 717
1 out of 44 hunks FAILED -- saving rejects to file sage/functions/piecewise.py.rej
abort: patch failed to apply
sage: 
```



---

Attachment

Verified that this is now fixed, attached a patch with a doctest.


---

Comment by wdj created at 2009-01-22 17:40:23

I can read the docstring and check in Sage that it is correct. (I did not try to apply it though.)


```

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f1 = lambda x: x*(pi-x)
sage: f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (0,pi),f1)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: f.cosine_series_coefficient(0,pi)
pi^2/3
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
```


Hope this is sufficient for a positive review.


---

Comment by mabshoff created at 2009-01-23 10:26:38

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 10:26:38

Merged in Sage 3.3.alpha1

Cheers,

Michael
