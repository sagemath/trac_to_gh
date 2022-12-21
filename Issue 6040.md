# Issue 6040: Added Doctests for QuadraticForms methods

Issue created by migration from Trac.

Original creator: jonhanke

Original creation time: 2009-05-15 03:40:59

Assignee: justin

CC:  mabshoff wstein tornaria

Keywords: quadraticform

Adding Doctests to bring coverage up to 100% (coming soon).


---

Attachment

Note:  There are currently two broken doctests in this patch (using the older routine IsPadic Square()), which should resolve themselves once Cremona's patch (Ticket #5834) is applied.


---

Comment by jonhanke created at 2009-05-15 11:15:41

Additional patch to bring QuadraticForm doctests to 100%.

Known Issues:
    Several doctests fail because of the need for hilbert_symbol() to accept rational numbers, and similarly for IsPadicSquare().  These should be addressed by the changes made in Ticket #5834.


---

Attachment


---

Comment by mabshoff created at 2009-05-15 11:22:49

Together with #5954 this brings coverage in the QF code to 100%.

Cheers,

Michael


---

Comment by jonhanke created at 2009-05-15 18:19:16

Also the patch in Ticket #6037 (rewrite and careful documentation of local density routines) is related to getting the doctest coverage to 100%.


---

Comment by tornaria created at 2009-05-17 21:48:55

So, it turns out there are 4 patches in this series, and they must be applied in order. In particular, patch-3 depends on patch-2, which is at #6037, but I misunderstood that.
The correct sequence is to apply patch-1 in #5954, then patch-2 in #6037, then patch-3 and patch-4 in this ticket.

If that order is followed, the patch sequence applies cleanly to 3.4.1 as well as 4.0.alpha0.


---

Attachment

fix doctests for 4.0.alpha0


---

Comment by tornaria created at 2009-05-18 05:54:33

Some doctests were broken on 4.0.alpha0 + patch-1 (#5954) + patch-2 (#6037) + patch-3 + patch-4.

All doctests pass for me when adding on top of that
 - attachment:patch-5__QF_reviewer__4.0.alpha0.patch
 - patch in #6059
 - patch in #6062
 - patch in #6064

Note that the `patch-3__QF_misc_doctests__4.0.alpha0.patch` I uploaded earlier is a mistake, just ignore it.


---

Comment by tornaria created at 2009-05-18 05:59:01

Note: the patch-5 also adds a few "#long time" comments to file `quadratic_form__local_representation_conditions.py`. Skipping these reduces the time for doctesting the whole file from 48 s to 20 s.


---

Comment by mabshoff created at 2009-05-18 23:57:04

Add positive review due to Gonzalo.

Cheers,

Michael


---

Comment by tornaria created at 2009-05-19 00:37:49

I'm ok with the positive review. I'll list the renamed/removed functions as for the other tickets, and I'll post a ticket to add compatibility functions with deprecation warnings.
 - `hanke_mass__maximal` was removed.
 - `GHY_mass_maximal` was renamed `GHY_mass__maximal`.
 - `conway_generic_mass` was removed.
 - `conway_p_mass_adjustment` was removed.
 - `local_diagonal` was removed.
 - `find_primitive_p_divisible_vector__all` was removed.


---

Comment by mabshoff created at 2009-05-19 00:41:25

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 00:41:25

Resolution: fixed
