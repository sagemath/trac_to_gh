# Issue 2279: numerical noise? doctest failure in sage.rings.number_field.totallyreal.__selberg_zograf_bound with 2.10.2

Issue created by migration from https://trac.sagemath.org/ticket/2279

Original creator: cremona

Original creation time: 2008-02-23 20:25:21

Assignee: was

A fresh 64-bit install of 2.10.2 gives this (and only this) error with
"make check":


```
sage -t  devel/sage-main/sage/rings/number_field/totallyreal.py**********************************************************************
File "totallyreal.py", line 410:
   sage: sage.rings.number_field.totallyreal.__selberg_zograf_bound(8,7)
Expected:
   15.851871776151311
Got:
   15.851871776151313
**********************************************************************
1 items had failures:
  1 of   1 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_totallyreal.py
        [1.7 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


       sage -t  devel/sage-main/sage/rings/number_field/totallyreal.py
```


OS info:

```
jec@host-57-71%uname -a
Linux host-57-71 2.6.18.8-0.3-default #1 SMP Tue Apr 17 08:42:35 UTC 2007 x86_64 x86_64 x86_64 GNU/Linux
```


```
gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)
```




---

Comment by jvoight created at 2008-02-28 02:45:26

Deleted the function __selberg_zograf_bound.  Patch attached.  JV


---

Attachment


---

Attachment

Same patch as the above, but it's a patch against 2.10.2, as opposed to the current working version of the code John and I are using (which is what the other patch above is against. ;) )


---

Comment by mabshoff created at 2008-02-28 06:54:45

Merged trac-2279.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 06:54:45

Resolution: fixed


---

Comment by craigcitro created at 2008-02-28 22:47:45

Changing status from closed to reopened.


---

Comment by craigcitro created at 2008-02-28 22:47:45

Resolution changed from fixed to 


---

Comment by craigcitro created at 2008-02-28 22:50:47

In the fix posted above, I did two things:

 * removed `selberg_zograf_bound`, because it was causing numerical issues here 
 and there, and wasn't actually used anywhere.

 * changed the default choice of totally real field of discriminant 5 (which gets
 added to the list by hand), because John had done that in his patch. Unfortunately,
 I switched a `-` for a `+` when doing it, and added a non-totally-real field.

The new patch I've attached fixes the second of these.


---

Comment by cremona created at 2008-02-28 22:58:38

I don't see the new patch.  In fact the patches listed seem to be the same!


---

Comment by craigcitro created at 2008-02-28 23:00:25

Yep, I'm still waiting for my copy of rc0 to finish its `sage -clone` on sage.math. I was guessing it would finish before anyone looked at this ticket. ;)


---

Attachment


---

Comment by cremona created at 2008-02-29 09:01:43

Combined patches are fine.  Note that 8682.patch is the same as trac-2279.patch, so may be ignored, but that trac-2279.pt2.patch needs to be applied after trac-2279.patch.


---

Comment by mabshoff created at 2008-02-29 18:53:02

Resolution: fixed


---

Comment by mabshoff created at 2008-02-29 18:53:02

Merged trac-2279.pt2.patch in Sage 2.10.3.rc1
