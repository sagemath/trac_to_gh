# Issue 8607: add deprecation option to the plot option rename decorator

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-03-25 19:05:27

Assignee: was

CC:  mhansen

This lets people change option names and automatically deprecate the old option name.


---

Attachment


---

Comment by jason created at 2010-03-30 16:09:23

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-04-18 20:21:47

All test passed in `sage/plot/misc.py`. I tested it on a keyword I changed recently and everything works as expected. I tested the sphinx docbuild and no new warning are created... but that is because the doc of the affected file is not generated. To me this is a positive review.

I added a patch where I make use of the `rename_keyword` with deprecation warning and where I fixed some small sphinx syntax. If Jason aggrees with my patch, I allow him to change the status of this ticket to positive review.


---

Comment by jason created at 2010-04-20 04:50:00

Positive review on the documentation changes.  I'm not qualified to comment on the deprecation you did in the word code, though, so I'll let someone else review that deprecation.


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-04-21 09:21:22

I removed the deprecation in the word code from the review patch. I realize more and more that mixing independent things in the same ticket is not a good idea : the review process gets unnecessarily longer. Hence, I kept in the review patch only the documentation changes to the file `sage/plot/misc.py` which was given a positive review by Jason. Therefore, this ticket now deserves a positive review.

Sorry again for the first version of the review patch. I hope it will make it into sage-4.4. Thanks again for the idea about this ticket : I like it and will definitively use it ...in later patches!

One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.

Sébastien


---

Comment by slabbe created at 2010-04-21 09:21:22

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-04-21 15:32:12

Replying to [comment:4 slabbe]:

> 
> One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.
> 

+1.  In fact, the other decorators in that file probably ought to be moved up to sage/misc as well.


---

Comment by jhpalmieri created at 2010-04-23 17:10:12

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:10:12

Merged into 4.4.alpha2:
 - trac-8607-rename-deprecation.patch
 - trac_8607_review-sl.patch


---

Comment by jsrn created at 2010-09-14 18:49:05

Replying to [comment:5 jason]:
> Replying to [comment:4 slabbe]:
> 
> > 
> > One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.
> > 
> 
> +1.  In fact, the other decorators in that file probably ought to be moved up to sage/misc as well.

I submitted a patch for this: Trac #9907.
Cheers,
Johan
