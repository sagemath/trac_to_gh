# Issue 5767: Bring coverage of plot3d/base.pyx up to 100%

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-04-12 00:00:11

Assignee: mabshoff

CC:  jason wcauchois




---

Comment by mabshoff created at 2009-04-13 03:41:24

Bouncing to 3.4.2.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-14 11:11:45

Before 


```
SCORE sage/plot/plot3d/base.pyx: 5% (4 of 78)
```


After


```
SCORE sage/plot/plot3d/base.pyx: 87% (69 of 79)
```


I don't know when I'll have time to work on this again, so I think we should at least get these ones in.


---

Attachment


---

Attachment


---

Comment by wcauchois created at 2009-05-04 05:52:23

REFEREE REPORT

Excellent work Robert! This patch applies to Sage 3.4.1 and the doctests are all valid. There were a number of misspellings which I corrected in 5767-referee.patch (I'm sorry I accidentally attached it twice; use either one). Besides that, I have a few concerns:

 * It looks like there are some typos due to copy-and-pasing:
   * On line 446 the documentation for tachyon() says it returns "an x3d input file".
   * On line 1202 the documentation for obj_repr() says it returns "the x3d representation of a group".
   * On line 1230 the documentation for jmol_repr() says it returns "the x3d representation of a group".
 * The documentation for jmol_repr on line 657 is somewhat confusing for me, especially when you say that jmol uses the strings to "construct self". Could you replace that with something like "construct a 3D mesh representing this object"? The same concern applies to the documentation for tachyon_repr and obj_repr.
 * Do you think it would improve the readability of the documentation to replace "self" with "!`self!`" -- that is, to apply preformatting to it?
 * What's up with the trailing spaces on every line?
 * On line 730 you use the word "preable". Is this a typo?


---

Comment by mabshoff created at 2009-05-04 06:17:39

Replying to [comment:4 wcauchois]:
> REFEREE REPORT
> 
> Excellent work Robert! This patch applies to Sage 3.4.1 <SNIP>

Hi Bill, you should *really* always apply against the latest development release. 3.4.1->3.4.2.rc0 was not a large release, but in many other cases there is a rather large, i.e. non-zero chance the patch would either not apply any more or be broken by other changes. There is always a sage.math binary of the latest release development snapshot, so you can use that. Another alternative is to have a review version of Sage that you upgrade from development snapshot to development snapshot.

Cheers,

Michael


---

Comment by wcauchois created at 2009-05-04 07:00:00

OK, I will do that. I'm sorry for the inconvenience I've caused you! The thing is, I'm building 3.4.2.rc0 right now and its taking a while -- so I figured I'd do this review and then once we addressed the issues we could handle rebasing. But I understand the importance of ensuring compatibility with the latest release.


---

Comment by mabshoff created at 2009-05-04 07:04:03

Replying to [comment:7 wcauchois]:
> OK, I will do that. I'm sorry for the inconvenience I've caused you! 

I have no clue if this is actually a problem, I just wanted to point out how to avoid problems since this has been an issue with your reviews in the past ;)

> The thing is, I'm building 3.4.2.rc0 right now and its taking a while -- so I figured I'd do this review and then once we addressed the issues we could handle rebasing. But I understand the importance of ensuring compatibility with the latest release.

Cool.

Cheers,

Michael


---

Comment by robertwb created at 2009-05-04 17:00:05

Wow, looks like I wasn't able to spell that day... thanks for looking at this, I'll address the issues you mentioned and post a patch shortly.


---

Comment by robertwb created at 2009-05-05 20:52:46

apply after other two


---

Attachment


---

Comment by robertwb created at 2009-05-05 20:59:29

Thanks for looking into this. 

Replying to [comment:4 wcauchois]:
> REFEREE REPORT
> 
> Excellent work Robert! This patch applies to Sage 3.4.1 and the doctests are all valid. There were a number of misspellings which I corrected in 5767-referee.patch (I'm sorry I accidentally attached it twice; use either one). Besides that, I have a few concerns:
> 
>  * It looks like there are some typos due to copy-and-pasing:
>    * On line 446 the documentation for tachyon() says it returns "an x3d input file".
>    * On line 1202 the documentation for obj_repr() says it returns "the x3d representation of a group".
>    * On line 1230 the documentation for jmol_repr() says it returns "the x3d representation of a group".

Fixed. 

>  * The documentation for jmol_repr on line 657 is somewhat confusing for me, especially when you say that jmol uses the strings to "construct self". Could you replace that with something like "construct a 3D mesh representing this object"? The same concern applies to the documentation for tachyon_repr and obj_repr.

I clarified it.

>  * Do you think it would improve the readability of the documentation to replace "self" with "!`self!`" -- that is, to apply preformatting to it?

I'm not sure it's worth it. 

>  * What's up with the trailing spaces on every line?

Sorry, I attached another patch that removes this (but I'm not sure if it'll apply cleanly, if not it's probably not worth it). 

>  * On line 730 you use the word "preable". Is this a typo?

Yep, I meant preamble. Fixed.


---

Attachment


---

Comment by wcauchois created at 2009-05-06 06:44:30

REFEREE REPORT:

Looking over the code again, I noticed a few other instances where "concatenate" was spelled incorrectly. I fixed these in 5767-refree2.patch. With this and Robert's changes, positive review.

(By the way Robert: Mercurial queues is awesome! I made 5767-all.patch with qfold :).)


---

Comment by robertwb created at 2009-05-06 06:46:38

Note that your 5767-all.patch lost all authorship information...


---

Attachment

this patch incorporates ALL of the changes; apply to sage 3.4.2


---

Comment by wcauchois created at 2009-05-06 07:01:17

Replying to [comment:12 robertwb]:
> Note that your 5767-all.patch lost all authorship information...

Oh shoot! OK, I fixed it manually and it works. I think that MQ unfortunately does not preserve the metadata usually associated with a changeset.


---

Comment by robertwb created at 2009-05-06 07:04:29

I'm pretty sure queues can be used to preserve metadata using qfold, but that's fine. Thanks for looking at this. 

- Robert


---

Comment by mabshoff created at 2009-05-07 07:36:07

Merged 5767-all.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-07 07:36:07

Resolution: fixed
