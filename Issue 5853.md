# Issue 5853: Restify and include more documentation on elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/5853

Original creator: wuthrich

Original creation time: 2009-04-22 13:26:26

Assignee: was

CC:  cremona

Keywords: documentation, elliptic curves

This is a follow-up on ticket #4933 and #5851. I plan to work on following files

   * padic_height.py
   * ell_modular_symbols.py
   * ell_tate_curve.py
   * padic_lseries.py
   * sha_tate.py


---

Comment by cremona created at 2009-04-22 13:34:47

Very good!   Nice to know I have been setting a good example.

Chris, in case you have not yet picked this up, debugging the restification involves the following.

    1. Make a new clone.
    1. In the new clone run "sage -docbuild reference html".  The first time takes a while.
    1. Point your browser at the place it says (prepend "file://" and append "index.html")
    1. If you are adding a new file to the ref manual, add a suitable line to (for example) $SAGE_ROOT/devel/sage/doc/en/reference/plane_curves.rst
    1. After making some edits, after doing "sage -b" then as well as doing "sage -t" on the file, also do (again) "sage -docbuild reference html" which will pick up that the file has changed and rebuild the html page.  Of course the page needs to be reloaded in the browser.

Not all of that was obvious to me, so I hope it helps!


---

Attachment

to be applied after tickets in #5846 and #5851


---

Comment by wuthrich created at 2009-04-24 15:24:40

No no, this patch is not right, do not even look at it. Sorry!!!!


---

Attachment

Replaces the previous ticket as before this applies to 3.4.1 + #5846 and #5851


---

Comment by wuthrich created at 2009-04-24 21:02:09

replaces all before.


---

Attachment

replaces all before


---

Comment by wuthrich created at 2009-04-24 21:10:34

What do we learn : never try to submit a patch just before catching the train.
Sorry about this patching mess. 

Only the very last patch counts. I applied it successfully against 3.4.1 + #4933 and #5851. It produces three doctest-errors in ell_rational_field with --long, but they are there even without my patch it seems to me.

One might decide against including ell_modular_symbols. The main documentation is in ell_rational_field. Of course I did not include padic_height, since it is deprecated anyway.

I do not know how to solve the issue of the alias power_series producing double documentation. I do not know how the references to article should be done correctly.


---

Comment by cremona created at 2009-04-26 19:56:12

Great work!  The patch trac_5853_2.patch applies fine to 3.4.2.alpha0.  There a docbuild glitch in ell_rational_field.py which has nothing to do with this patch.  The new sections in the manual look great. All doctests in elliptic_curves pass (as of course they should since this patch only touches docstring, apart from a few very small things).


---

Comment by mabshoff created at 2009-04-30 00:32:31

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 00:32:31

Merged trac_5853_2.patch in Sage 3.4.2.rc0.

Cheers,

Michael
