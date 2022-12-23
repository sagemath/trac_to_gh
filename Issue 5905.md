# Issue 5905: [with patch, needs review (trivial)] minor fix to ReST markup in ell_rational_field.py

Issue created by migration from https://trac.sagemath.org/ticket/5905

Original creator: cremona

Original creation time: 2009-04-26 20:05:06

Assignee: tba

Keywords: elliptic curve docbuild

There are two glitches in the docstring for function has_good_reduction_outside_S() in sage/schemes/elliptic_curves/ell_rational_field.py .

The ptach fixes them.



---

Attachment


---

Comment by jhpalmieri created at 2009-04-27 04:32:07

The patch successfully fixes two problems in the reference manual. This eliminates one of the warnings which occurs when building the reference manual.  (The only one I still see is

```
checking consistency... WARNING: /Applications/sage_builds/sage-3.4.2.alpha0-upgrade/devel/sage-new/doc/en/reference/sage/combinat/family.rst:: document isn't included in any toctree
```

in case anyone knows what to do about that.  If so, open a new ticket.)


---

Comment by cremona created at 2009-04-27 08:28:47

I worked out what causes this sort of thing.  Suppose you add a file to the ref man by adding to the table of contents, in a branch, and rebuild the docs to test.  Then (after making a patch, say) you roll back that branch to a version where that file is no longer mentioned in the toc.  But the file *.rst (which was automatically created earlier) remains in the doc tree even after both "sage -b" and "sage -docbuild ...", and causes this warning.

I don't know the right way to fix this.  Perhaps Sphinx could just delete such files (it seems too much for "sage -b" to do).


---

Comment by mabshoff created at 2009-04-30 01:09:51

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 01:09:51

Resolution: fixed
