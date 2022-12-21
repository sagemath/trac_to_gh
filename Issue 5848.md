# Issue 5848: [with patch, needs review] untabify Sage

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-04-21 23:51:34

Assignee: jhpalmieri

CC:  roed

The attached patch removes all of the TABs I could find in .py and .pyx files in the Sage library.



---

Attachment

Patch choked twice on `modular/dirichlet.py`, which seems odd, given how fresh it is, and I can't really tell why.  I was applying it to an upgraded 3.4.1.rc4   Maybe it will patch better under mabshoff's firm guidance.

Builds just fine.  Passes `sage -testall`, except some unpickling errors in `structure/sage_object.pyx` and `algebras/quaternion_algebra_element.py` concerning `QuaternionAlgebraElements`, but the changes to these files don't appear implicated in these errors,

Documentation builds fine as well (PDF of reference manual) with no TeX errors.

Positive review, subject to the business above about patching `modular/dirichlet.py`.


---

Comment by mabshoff created at 2009-04-22 20:37:08

I am not sure which rejects Rob saw, but it is applying fine for me.

Cheers,

Michael


---

Comment by rbeezer created at 2009-04-22 20:41:58

Replying to [comment:2 mabshoff]:
> I am not sure which rejects Rob saw, but it is applying fine for me.

Superior Merge-Fu.  ;-)


---

Comment by mabshoff created at 2009-04-24 09:25:43

Ok, the patch still applies modulo three the diff for three files 

 * sage/algebras/algebra_order.py
 * sage/algebras/algebra_order.py
 * sage/algebras/algebra_order_ideal.py

that no longer exist. This patch besides the latex one I just merged at #5610 has high risks for rejects, but since I merged the other one I might as well merge this one.

David: Some of the padics files are touched, so if you rebase your patch bomb in the morning please also apply the patch I will post in a minute.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 09:27:29

John's patch with the changes for three no longer existing files removed.


---

Attachment

Merged trac_5848_untabify.patch in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 09:27:49

Resolution: fixed
