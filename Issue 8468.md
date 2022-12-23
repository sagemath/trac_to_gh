# Issue 8468: add "Group Theory and Sage: A Primer" to the classification "Sage HOWTOs"

Issue created by migration from https://trac.sagemath.org/ticket/8468

Original creator: mvngu

Original creation time: 2010-03-07 02:22:36

Assignee: mvngu

CC:  rbeezer

Keywords: group theory

Add the document [Group Theory and Sage: A Primer](http://buzzard.ups.edu/sage/sage-group-theory-primer.pdf) to the documentation category "Sage HOWTOs". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).


---

Attachment


---

Comment by rbeezer created at 2010-03-11 01:25:21

Changing status from new to needs_review.


---

Attachment

TeX and PDF are posted here.  License should be compatible with the rest of Sage documentation now.  Any updates in the future should appear at http://abstract.ups.edu


---

Comment by wdj created at 2010-03-11 03:14:44

Looks good to me.

Thanks Rob!


---

Comment by wdj created at 2010-03-11 03:14:44

Changing status from needs_review to positive_review.


---

Attachment

based on Sage 4.3.4.alpha1; depends on #8469


---

Comment by mvngu created at 2010-03-12 06:51:58

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-03-12 06:51:58

The attachment [trac_8468-groups.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8468/trac_8468-groups.patch) is a ReSTified version of Rob's group theory primer. This patch depends on ticket #8469. So only the patch needs review by anyone but me.


---

Comment by mvngu created at 2010-03-12 06:52:06

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-03-12 14:25:27

Do the new review require more than just looking at 
http://sage.math.washington.edu/home/mvngu/8470-newdoc/thematic_tutorials/group_theory.html
and checking if it looks okay?

It looks okay to me by maybe Rob Beezer is a better judge since he wrote the original version.


---

Comment by bump created at 2010-03-12 18:05:09

One point is that it would be nice if the primer showed how to construct character tables. (I don't think that should be a prerequisite for positive review.)


---

Comment by rbeezer created at 2010-03-13 06:31:26

Minh - the HTML version looks very nice.  Thanks for your work on this.  As David suggests, I'll do a more careful once-over in the next couple days (ie this is not a review - just a promise to do so).

Dan - This was written to accompany an undergraduate course, where we don't come close to character tables.  But it would be a good thing to add I think, maybe under something like an "advanced topic" section so it doesn't scare off the beginners.  I've not used this function much (OK, first time was 2 minutes ago).   Any "gotchas" I should document besides the occurrence of primitive roots of unity?

Anything else anybody would want to see in an "advanced" section?

Rob


---

Comment by wdj created at 2010-03-13 14:00:03

Replying to [comment:9 rbeezer]:

...

> 
> Anything else anybody would want to see in an "advanced" section?


Since you ask:-)
Other topics could be 

 * automorphism groups of various structures (graphs, designs, codes, ...) 

 * Cayley graphs of groups
 
 * actions of groups on sets, 

 * action of groups on polynomials and invariant theory.

 * applications to the Rubik's cube.

I'm not saying you *should* do this or that it really needs to be done but you asked:-)

> 
> Rob


---

Comment by bump created at 2010-03-15 23:24:58

> The attachment  trac_8468-groups.patch is a ReSTified version of Rob's group theory primer. This patch depends on ticket #8469. So only the patch needs review by anyone but me.

To summarize the thread, the tutorial could be expanded later but that is not the purpose of this patch. I have built the html and pdf documentation. The only defect I see is long lines in the pdf file.
I would suggest breaking these even though Sage output does not. However I don't think this is a prerequisite to
merging the patch and I am changing status to positive review.


---

Comment by bump created at 2010-03-15 23:24:58

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-02 07:35:30

Resolution: fixed


---

Comment by mvngu created at 2010-05-02 07:35:30

Close since this is merged due to the merging of #8823.
