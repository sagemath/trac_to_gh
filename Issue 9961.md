# Issue 9961: vector plot should have optional "start" argument

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-09-21 20:02:44

Assignee: jason, was

CC:  ryan kcrisman

Keywords: beginner

It would be really nice if this plotted an arrow from (1,2) to (3,4):


```
sage: v=vector([1,2])
sage: u=vector([2,2])
sage: plot(u,start=v)
```


or maybe the option should be "base" or "origin"

To fix this, just change the plot method in `devel/sage/sage/modules/free_module_element.pyx`


---

Comment by jason created at 2010-09-21 20:03:21

I think "start=list/tuple/vector" is the best convention for this option.


---

Comment by ryan created at 2011-01-09 06:24:42

tentative patch


---

Attachment

the patch gives the described output, but someone should double check my code for correctness.


---

Comment by ryan created at 2011-01-09 06:26:25

Changing status from new to needs_review.


---

Comment by aly.deines created at 2011-01-09 16:33:55

Changing status from needs_review to positive_review.


---

Comment by aly.deines created at 2011-01-09 16:33:55

Replying to [comment:2 ryan]:
> the patch gives the described output, but someone should double check my code for correctness.

It looks good to me.


---

Comment by ryan created at 2011-01-10 23:44:37

updated patch


---

Attachment


---

Comment by ryan created at 2011-01-11 00:36:37

Changing status from positive_review to needs_work.


---

Comment by ryan created at 2011-01-11 00:44:00

updated patch + doctests


---

Comment by ryan created at 2011-01-11 00:46:08

Changing status from needs_work to needs_review.


---

Attachment

updated patch:

Included error handling for some cases where the two coordinates are not of the same dimension.  Also, added doctests.

Much cleaner patch.

I appreciate the suggestions for making this patch better.


---

Comment by aly.deines created at 2011-01-11 22:10:02

Changing status from needs_review to positive_review.


---

Comment by aly.deines created at 2011-01-11 22:10:02

Replying to [comment:7 kcrisman]:


---

Comment by jdemeyer created at 2011-01-17 17:13:56

Please make it clear which patches have to be applied.


---

Comment by jdemeyer created at 2011-01-17 17:13:56

Changing status from positive_review to needs_work.


---

Comment by ryan created at 2011-01-17 17:25:49

It would be the latest patch, trac_9962_vector_start.2.patch


---

Comment by ryan created at 2011-01-17 17:25:49

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-01-17 20:26:04

You may want to check whether this really does the same thing as `v.plot()` - see #10638.


---

Comment by jdemeyer created at 2011-01-19 01:50:09

Replying to [comment:11 kcrisman]:
> You may want to check whether this really does the same thing as `v.plot()` - see #10638.

I am interpreting this comment as a needs_work (if it's not, then please set positive_review).


---

Comment by jdemeyer created at 2011-01-19 01:50:09

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-01-19 02:12:01

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-01-19 02:12:01

No, it's neither positive review nor needs work.  I haven't had the time to review this, but any reviewer should be sure to check this out.  That's all I am saying.


---

Comment by kcrisman created at 2011-03-13 01:24:22

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-03-13 01:24:22

This patch causes an amusing error, which does not occur in the vanilla Sage:

```

sage: plot(vector([1]))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2, 0))

---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
<snip>
ArithmeticError: Cross product only defined for vectors of length three or seven, not (3 and 1)
```

I think I can fix this, so patch hopefully coming up.


---

Comment by kcrisman created at 2011-03-13 01:50:16

I think I have it fixed.  However, the bizarre error messages remain for one-dimensional arrows, so I have created followup ticket #10925 for that.


---

Attachment

Apply after vector_start.2 patch


---

Comment by kcrisman created at 2011-03-13 02:01:50

Okay, positive review on this nice addition from the original patch.  

The reviewer patch still needs review; it fixes the problem by extending the one-dimensional start as well, and adds/spruces up some documentation.  Reviewer should check things work, doctests, and that documentation looks ok.


---

Comment by kcrisman created at 2011-03-13 02:01:50

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-05-11 18:47:14

Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.


---

Comment by ryan created at 2011-05-13 16:24:12

Replying to [comment:17 kcrisman]:
> Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.

I'll look at it this evening.


---

Comment by ryan created at 2011-05-14 06:09:57

everything looks good here.  I'm going to go ahead an change this to positive review for the reviewer patch.


---

Comment by ryan created at 2011-05-14 06:09:57

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-31 17:07:11

Resolution: fixed
