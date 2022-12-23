# Issue 4305: [with patch, needs review] move finite fields into their own directory

Issue created by migration from https://trac.sagemath.org/ticket/4305

Original creator: robertwb

Original creation time: 2008-10-15 20:50:56

Assignee: tbd

This is in anticipation of much re-factoring and refinement. 


---

Attachment


---

Comment by robertwb created at 2008-10-15 21:00:08

apply to docs repo


---

Attachment

Looks good to me - damn the torpedoes :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-16 09:30:52

Due to trouble when building the tree with the patch applied on sage.math, i.e. finite_field_givaro not being found, this patch unfortunately needs work :(

I will attach a reviewer patch shortly once I have proper net again.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-12-05 09:58:41

Robert,

is anything going on here? I am not sure how much happened to the finite fields since SD 10, but that patch here certainly has gone stale. Should you plan to work on this in the short term please ping me so we can coordinate the big move. Otherwise we should delete the patches and wait until someone tackles this again.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-07 09:41:47

I'm hoping to have a little time to look into this over the break. Don't delete the patches just yet.


---

Comment by mabshoff created at 2008-12-07 09:51:08

Replying to [comment:4 robertwb]:
> I'm hoping to have a little time to look into this over the break. Don't delete the patches just yet. 

Ok, I just think that a lot of this patch needs to be rebased, so it might be a good idea to start over, but we will see. One aspect that puzzles me to this day is that we never got it to work on any other system but your own.

One issue that likely will need addressing is pickling issues.

Cheers,

Michael


---

Comment by ylchapuy created at 2010-02-09 14:31:53

Should be closed because of #8218 I guess.


---

Comment by davidloeffler created at 2010-06-29 08:29:07

I concur. I'm setting this to "positive review" to bring it to the attention of the release manager who has the authority to close it.

*** Please close this ticket without applying any of the patches! ***


---

Comment by davidloeffler created at 2010-06-29 08:29:07

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-29 08:29:17

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:23:26

I'm resolving this ticket as a "duplicate."


---

Comment by mpatel created at 2010-07-20 09:23:26

Resolution: duplicate
