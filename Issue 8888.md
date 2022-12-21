# Issue 8888: Returns the frontier of a partition

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-05 11:33:20

Assignee: hivert

CC:  sage-combinat

Keywords: Partitions border rim

The name of the actual method is being discussed on [sage-combinat](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/27e68b86cf8e0578/1869144ca150bda6?hl=en&lnk=gst&q=frontier#1869144ca150bda6)


---

Attachment

Please review.


---

Comment by hivert created at 2010-05-05 17:01:29

Changing status from new to needs_review.


---

Comment by jbandlow created at 2010-05-12 02:48:19

Hi Florent,

I've tried to apply this patch to a clean sage-4.4.1, and I'm getting strange behavior.  After applying your patch, the entire code for the `quotient` method in `partition.py` (after the docstring) looks like this:

```
        p = self
        #Normalize the length
        remainder = len(p) % length
        part = p[:] + [0]*(length-remainder)
```


The rest is just gone, and obviously this causes doctest failures.  Looking at the patch file, I don't understand why this should happen.  It looks fine!  But I can't approve with this behavior.  Can you rebase?  Or explain what might be going on?


---

Comment by jbandlow created at 2010-05-12 02:48:19

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-05-12 17:25:18

Hi Jason,

Thanks for taking care of this review

> The rest is just gone, and obviously this causes doctest failures.  Looking at the patch file, I don't understand why this should happen.  It looks fine!  But I can't approve with this behavior.  Can you rebase?  Or explain what might be going on?

Oups ! I didn't realize that this patch depend on #6655 (allready merged in 4.4.2.rc0). Sorry for the trouble.


---

Comment by hivert created at 2010-05-12 17:25:18

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jbandlow created at 2010-05-13 15:07:40

After applying #6655 everything applies fine.  Thanks.  I give a positive review to the code, but  I included a trivial reviewer patch to clean up the doc a little bit.


---

Comment by hivert created at 2010-05-13 15:27:35

Replying to [comment:5 jbandlow]:
Jason's reviewer patch looks perfectly good to me. Positive review

Jason: Can you push your review patch to combinat server ?


---

Comment by hivert created at 2010-05-13 15:28:41

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2010-05-13 20:00:18

Replying to [comment:6 hivert]:
> Replying to [comment:5 jbandlow]:
> Jason's reviewer patch looks perfectly good to me. Positive review
> 
> Jason: Can you push your review patch to combinat server ? 

Done.


---

Comment by mhansen created at 2010-06-05 22:23:55

Resolution: fixed
