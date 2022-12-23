# Issue 9027: Explain Sage and tex interactions in the tutorial

Issue created by migration from https://trac.sagemath.org/ticket/9027

Original creator: rbeezer

Original creation time: 2010-05-24 05:45:32

Assignee: mvngu

CC:  jhpalmieri mvngu

Keywords: latex

There are a variety of ways to use latex in Sage, which often leads to some confusion.  This new section of the tutorial will present an overview and the basics of usage from a users perspective.  However, doctests might also help developers understand how to make changes related to various aspects of tex support.


---

Attachment


---

Comment by rbeezer created at 2010-05-24 05:51:02

Changing status from new to needs_work.


---

Comment by rbeezer created at 2010-05-24 05:51:02

Version 1 patch is incomplete, but should build with just a handful of errors, and contains initial sections followed by a rough outline for contents of subsequent section.


---

Attachment

Version 2 patch has about 80% of the content I'd like to add.  So general comments about direction or scope are welcome.  I'll then be adding the missing sections, filling in doctests, links to methods, etc.


---

Comment by jhpalmieri created at 2010-06-08 04:09:34

Hi Rob,

Here are some comments.  

 - Overall, it looks good.  It seems to cover all of the points I would want it to.  I also think it makes sense to include this material in the tutorial.

 - In general, make it more clear just how much of this is automatic?  (for example the png conversion discussed at line 237 and nearby)

 - how much do we care about consistency between ``\TeX`` and `tex`, ``\LaTeX`` and `latex`?

typos:
 
 - line 7: intensley synergetic --> intensely synergistic

 - line 24: constructiing

 - line 100: Effecting --> Affecting

 - line 173: mathbb?  This might be mathbf unless you use a .. link:: directive to link it to the previous examples.  same issue on lines 183, 188, etc.

 - line 235: Typset

 - line 240: this class --> This class

 - line 240: wwwhat

 - line 240: To actual see --> To actually see

 - line 262 and following, the sentence starting "So all of these components need".  Change to "So you should make sure that up-to-date versions of these are available"

 - line 311: "::math" --> ".. math::"

 - line 318: there is a section in the tutorial on sagetex, so you should refer to that.


---

Comment by rbeezer created at 2010-06-08 12:21:27

Replying to [comment:3 jhpalmieri]:

Hi John,

Thanks for all the comments, suggestions and fixes.  I'm away doing this Sage workshop this week, but expect to get back to this next week sometime.

Rob


---

Attachment


---

Comment by rbeezer created at 2010-06-17 04:58:41

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-06-17 04:58:41

Version 3 patch is now ready for review.  This takes into account all of John's comments above, but likely introduces a few new typos (though I'd like to think not).  Two comments:

1.  graphviz otional spkg is broken (#7438) so I can't learn that right now, a section on that could be added later.

2.  I had a tentative section about using TeX in documentation.  I think I might write more for the developer's guide (linking back to this) and I can include the documentation stuff there.  So I dropped that.


---

Comment by jhpalmieri created at 2010-06-21 21:47:19

The most recent patch doesn't apply cleanly, because macros.tex is no longer part of the Sage distribution.

Also, if you do `sage -docbuild tutorial html -j` to build using jsMath, then jsMath doesn't know about the command `\LaTeX`, and this causes problems.  I also couldn't get ``\mbox{\TeX}`{}shop` to work right, either.  So I'm attaching a reviewer's patch which changes `\mbox{\LaTeX}` to the plain-text `LaTeX`, and similarly for `TeX`.  I've also added a few links.


---

Attachment

apply on top of v3 patch


---

Comment by jhpalmieri created at 2010-06-21 21:50:15

Oh, there were also a few doctest failures: I think the examples don't get run in order, so the latex preamble was not empty when it was supposed to be, for example.  My patch fixes those (I think).


---

Comment by jhpalmieri created at 2010-06-21 22:13:50

See also #9300.  How's your French?


---

Comment by rbeezer created at 2010-06-21 23:46:03

Replying to [comment:8 jhpalmieri]:
> See also #9300.  How's your French?

Possibly passable enough to review, but not good enough to create.  ;-)

Thanks for the fixes and changes.  I'll look them over soon - busy with out-of-town guests right at the moment.

<joke>

You know the seasons in the Pacific Northwest, don't you?

10 months of rain and two months of visitors.  ;-)

</joke>


---

Comment by rbeezer created at 2010-07-17 04:35:44

Stand-alone, apply before reviewer patch


---

Attachment

Apply after reviewer patch


---

Attachment

Replying to [comment:7 jhpalmieri]:

v4 patch removes the changes to macros.tex so will now apply cleanly.

reviewer patch looks good to me, so that's a positive review on that.

doctesting patch makes a few more changes to make random-order doctesting work properly.  The general strategy is to clean-up on finishing a block (rather than always initializing on starting a block).  There are a few report of macros, preamble etc on starting a block, but that is to illustrate, rather than check.

Apply three patches in this order:  v4, reviewer, doctesting.  This all applies, builds (documentation) and passes tests (in random order!).  I'll make a mega-patch once final.

> Oh, there were also a few doctest failures: I think the examples don't get run in order, so the latex preamble was not empty when it was supposed to be, for example.  My patch fixes those (I think).


---

Comment by jhpalmieri created at 2010-07-22 22:53:08

Hi Rob,

It looks like trac_9074-tkz-graph-latex-v4.patch belongs on #9074 instead of here. Can you move it there?  Is there a new version of the patch for this ticket?


---

Comment by rbeezer created at 2010-07-22 23:30:35

Stand-alone v4 patch, apply before reviewer patch


---

Attachment

Replying to [comment:11 jhpalmieri]:
> Hi Rob,
> 
> It looks like trac_9074-tkz-graph-latex-v4.patch belongs on #9074 instead of here. Can you move it there?  Is there a new version of the patch for this ticket?

Ooh, that's bad.  The #9074 patch is already there where it belongs.  These two v4 patches were next to each other in my local storage, thus......

The real 9027 v4 patch is here now, sorry for the confusion.  I've never been able to delete files.  Do I need some extra privileges, or can you trash 9074-v4 for me?  Thanks.

Rob


---

Comment by jhpalmieri created at 2010-07-23 03:41:22

Looks good to me.

To the release manager, merge

 - trac_9027_tutorial_latex_v4.patch
 - trac_9027-reviewer.patch


---

Comment by jhpalmieri created at 2010-07-23 03:41:22

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-26 02:17:30

Resolution: fixed


---

Comment by ddrake created at 2010-07-26 02:17:30

Replying to [comment:13 jhpalmieri]:
> Looks good to me.
> 
> To the release manager, merge
> 
>  - trac_9027_tutorial_latex_v4.patch
>  - trac_9027-reviewer.patch

Merged in 4.5.2.alpha1.


---

Comment by mpatel created at 2010-07-27 07:01:41

Please see #9607 for a potentially related doctest failure.
