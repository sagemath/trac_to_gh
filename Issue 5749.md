# Issue 5749: [with patch, needs review] Bring coverage of sage/rings/power_series_poly.pyx to 100%.

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-04-11 08:25:28

Assignee: mabshoff

The attached patch brings up coverage for the `power_series_poly.pyx` file.


---

Attachment

Note that the patch is against `sage-3.4.1-rc1`, so hopefully has no merge issues with `rc2`.


---

Comment by was created at 2009-04-12 05:20:29

I noticed a serious issue/bug with power series when reading the doctests.  See #5769.


---

Comment by mabshoff created at 2009-04-12 21:04:39

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-12 21:04:39

Resolution: fixed
