# Issue 5918: bring doctest coverage for posets to 100%

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2009-04-28 14:29:56

Assignee: saliola

CC:  sage-combinat

I'll post a patch in a few minutes that brings the doctest coverage for posets to 100% (well, except for 2 or 3 nested functions). It also fixes a few bugs that I noticed while adding the doctests.


---

Attachment


---

Comment by jhpalmieri created at 2009-04-28 16:52:06

The patch fails to apply to Sage 3.4.2.alpha0:

```
applying /Users/palmieri/Downloads/trac_5918.patch
patching file sage/combinat/posets/poset_examples.py
Hunk #2 FAILED at 164
1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/posets/poset_examples.py.rej
patching file sage/combinat/posets/posets.py
Hunk #12 FAILED at 547
1 out of 48 hunks FAILED -- saving rejects to file sage/combinat/posets/posets.py.rej
abort: patch failed to apply
```

(I was hoping that this patch would fix #5280 and/or #5283, but after applying the rejects by hand, I saw that it didn't.  I'll let someone else do a proper review once there is a rebased patch.)


---

Comment by saliola created at 2009-04-28 17:04:01

Hello John,

Thanks for taking a look at this. I'm aware of the other issues, and this patch does not deal with them. (It does deal with the issues in the email you posted to the sage-combinat list some time ago.) I decided to wait to fix those issues using a different patch, so not to put too much into this patch. (I'm planning to have the others fixed soon.)

I'll rebase and post an updated patch in a few hours (I have to upgrade...).


---

Comment by saliola created at 2009-04-28 20:12:44

rebased to 3.4.2.alpha0 (apply only this patch)


---

Attachment


---

Comment by ddrake created at 2009-04-29 09:13:04

I'm going to upload a patch which corrects a bunch of typos and formatting bits. I do have a couple comments:

  * before, the definitions for order ideal and filter were both obviously wrong. I corrected the definition and took the liberty of rewriting it; please check those.
  * you need a blank line between `EXAMPLES::}} (or {{{TEST::`) and the first line of the doctest; otherwise, the documentation doesn't get typeset correctly.
  * doing ``M\"obius`` doesn't work; it automatically uses LaTeX in math mode, and gets messed up. For now I just removed the backticks. (If we add a utf-8 encoding declaration, you can use the umlaut and everything works, but for now, the official rule is that Sage library code is 7-bit clean.)

Also. there seems to be a lot of duplication between posets.py and hasse_diagram.py. This makes fixing documentation hard, since you have to fix things in two places. Is it possible to somehow combine this stuff so code and documentation doesn't need to be copied? (I'm asking this of everyone, not necessarily Franco.)

I don't have time for this now, but it would be nice to add cross-references: you can do stuff like "`...see :func:`coolfunction()` for...`" and get automatically linked cross-references.

Finally, this does raise coverage to (basically) 100% and passes all doctests. I'm glad to see this!


---

Attachment

apply on top of trac_5918-rebased.patch


---

Comment by saliola created at 2009-04-29 09:46:09

Replying to [comment:5 ddrake]:
> I'm going to upload a patch which corrects a bunch of typos and formatting bits. I do have a couple comments:
> 
>   * before, the definitions for order ideal and filter were both obviously wrong. I corrected the definition and took the liberty of rewriting it; please check those.

Thanks for catching these. I checked your corrected definitions, and they are correct. (It seems that a bunch of > and < symbols disappeared at some point; most likely during the automatic conversion to ReST).

>   * you need a blank line between `EXAMPLES::}} (or {{{TEST::`) and the first line of the doctest; otherwise, the documentation doesn't get typeset correctly.

Thanks for pointing this out. Obviously, I didn't know this.

>   * doing ``M\"obius`` doesn't work; it automatically uses LaTeX in math mode, and gets messed up. For now I just removed the backticks. (If we add a utf-8 encoding declaration, you can use the umlaut and everything works, but for now, the official rule is that Sage library code is 7-bit clean.)

It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.

> Also. there seems to be a lot of duplication between posets.py and hasse_diagram.py. This makes fixing documentation hard, since you have to fix things in two places. Is it possible to somehow combine this stuff so code and documentation doesn't need to be copied? (I'm asking this of everyone, not necessarily Franco.)

Yeah, it is a bit of a pain. The original code was my first Sage/Python coding project, and some of my design decisions were not great. At some point the code needs to be updated to deal with more general posets (like very large/infinite posets), and I imagine at that point the two classes will merge into something like `FinitePosetWithHasseDiagram`.

Even though there are planned changes, I thought it was very much worth the effort to add the doctests and fix the bugs in the current code.

Thanks for taking a look at the patch. I agree with all your changes.


---

Comment by ddrake created at 2009-04-29 12:12:33

Replying to [comment:6 saliola]:
> It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.

Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version. The reference manual pulls in all the docstrings from the Sage library. The output will be in `$SAGE_ROOT/devel/sage/doc/output/` and look in the html or pdf directories. You can also create the developer's guide, installation guide, and a bunch of other stuff by replacing "reference" with "developer", "installation", "constructions", and others.

> Even though there are planned changes, I thought it was very much worth the effort to add the doctests and fix the bugs in the current code.

Yes! Definitely.


---

Comment by saliola created at 2009-04-29 15:17:21

Replying to [comment:7 ddrake]:
> Replying to [comment:6 saliola]:
> > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.
> 
> Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.

Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.


---

Comment by jhpalmieri created at 2009-04-29 16:38:08

Replying to [comment:8 saliola]:
> Replying to [comment:7 ddrake]:
> > Replying to [comment:6 saliola]:
> > > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.
> > 
> > Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.
> 
> Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.

Yes and no.  For the PDF version, there is no way to do this right now, as far as I know.  For the html version, once you've built it once for a particular branch, the next time it will only rebuild the files which have changed.  If you install the patch at #5653, you can also view the html output for individual functions from the notebook by typing `function?`.


---

Comment by ddrake created at 2009-04-30 01:21:34

Okay, after finding typos, I thought I should go through and actually look at everything: this gets a positive review, although I would like someone to comment on doctesting the nested functions. In this instance, it seems okay but someone who knows better may wish to comment/revert the positive review.


---

Comment by mabshoff created at 2009-04-30 01:39:45

I looked over Dan's patch and it looks good to me. Doctests do pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 01:40:16

Merged  trac_5918-rebased.patch and trac_5918-typos-docfixes.patch in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 01:40:16

Resolution: fixed


---

Comment by saliola created at 2009-04-30 07:36:39

Replying to [comment:9 jhpalmieri]:
> Replying to [comment:8 saliola]:
> > Replying to [comment:7 ddrake]:
> > > Replying to [comment:6 saliola]:
> > > > It seems that you are somehow typesetting the documentation. How do you do this? That would obviously make it easier for me to catch these mistakes.
> > > 
> > > Do `sage -docbuild reference html` to build the html reference manual, and `sage -docbuild reference pdf` to make the LaTeX PDF version.
> > 
> > Thanks for this answer. This seems to take a while. Is there a way to build just part of the manual? I'm thinking of something along the lines `sage -docbuild posets.py`.
> 
> Yes and no.  For the PDF version, there is no way to do this right now, as far as I know.  For the html version, once you've built it once for a particular branch, the next time it will only rebuild the files which have changed.  If you install the patch at #5653, you can also view the html output for individual functions from the notebook by typing `function?`.

Thank you, John and Dan, for you answers. These will be very useful.
