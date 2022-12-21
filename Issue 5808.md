# Issue 5808: [with patch, needs review] fix most warnings when building the reference manual

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-04-17 06:04:42

Assignee: jhpalmieri

Along with #5541, this patch fixes most of the warnings when building the reference manual in 3.4.1.rc3.  I still get these:

```
checking consistency... WARNING: /Applications/sage_builds/sage-3.4.1.rc3/devel/sage-test/doc/en/reference/sage/combinat/family.rst:: document isn't included in any toctree
done
preparing documents... WARNING: html_favicon is not an .ico file
```

but that's it.




---

Comment by cremona created at 2009-04-17 14:12:37

John,

I just uploaded a patch at #4933 which fixes some of the same things for ell_rational_field and ell_generic.  We might have difficulties merging these.  I am about to test yours and hope to give a positive review shortly...

PS I would like to add \AA and \PP to the "blackboard bold" list (for affine and projective space).  I read your clear instructions on how to do that, but have not done so as I thought you were probably touching that file.


---

Comment by cremona created at 2009-04-17 14:47:14

Apply after the first patch


---

Attachment

Applies fine to 3.4.1.rc3.  When I did "sage -docbuild all html" I got lots of warnings in the tutrial (ok, not dealt with here) and a couple in algebras/quatalg/quaternion_algebra.py.

So I added some edits to that file, as in the second patch attached.

My positive review applies to the first patch.  If John likes the second one, that's good.


---

Comment by jhpalmieri created at 2009-04-17 15:15:20

Hi John,

I think your patch to quaternion_algebra.py is going to clash with the one at #5541, mentioned in the summary above.


---

Comment by cremona created at 2009-04-17 15:32:41

Replying to [comment:3 jhpalmieri]:
> Hi John,
> 
> I think your patch to quaternion_algebra.py is going to clash with the one at #5541, mentioned in the summary above.

OK, kill that patch, I should not have wasted my time!

I'm about to add a patch doing what you suggested for mwrank.  Which will make 4933 even harder to merge...so on second thoughts I will not post it here but will rebase my #4933 patch on this one and include the mwrank changes there.

UPSHOT:   Positive review for ref-warnings.patch;  ignore the seond one.


---

Comment by jhpalmieri created at 2009-04-17 15:40:16

Okay, thanks, and sorry for the extra work you'll have to do rebasing.


---

Comment by cremona created at 2009-04-17 15:57:08

Replying to [comment:5 jhpalmieri]:
> Okay, thanks, and sorry for the extra work you'll have to do rebasing.
No problem -- done!


---

Attachment

apply only this patch


---

Comment by jhpalmieri created at 2009-04-17 22:53:37

This version removes the "..link::" directives from sudoku.py; otherwise, it's identical to the previous patch.


---

Comment by jhpalmieri created at 2009-04-17 22:55:15

mabshoff: the only issue with the latest patch is whether it passes doctests. I think it does; if you agree, I think you can re-issue the positive review.


---

Comment by mabshoff created at 2009-04-18 01:29:15

With only ref-warnings.patch applied doctests do pass. So I am reinstating the positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 01:29:52

Merged in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 01:29:52

Resolution: fixed
