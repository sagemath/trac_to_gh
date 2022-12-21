# Issue 9114: Improve documentation of infinite polynomial rings

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-06-02 11:01:58

Assignee: Simon King

Keywords: documentation, infinite polyonomial ring, symmetric reduction

At #9108, it was reported that the doc tests for symmetric ideals time out on some machines. As a quick solution, it was suggested to simply mark them as 'long'.

Here, I replace the offensive test (it is only one) by something more easy, that is still instructive.

At this occasion, I tried to improve other aspects of the doc strings as well, e.g., I tried to shorten the lines and to adhere to the standards in describing optional arguments.

The attached patch is relative to #9108, which already has a positive review. The new patch replaces the doc test that was marked 'long' in #9108.


---

Comment by SimonKing created at 2010-06-02 11:03:48

Shorter doc test (avoiding a time out on some systems), better doc formatting.


---

Comment by SimonKing created at 2010-06-02 11:04:27

Changing status from new to needs_review.


---

Attachment


---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2010-06-14 12:15:12

Looks fine to me; it builds and passes tests under 4.4.4.alpha0, the tests pass in a reasonable length of time (25 seconds on my machine, as opposed to 17 seconds without "-long" and a ridiculously long time with "-long"). Documentation builds OK and looks good.

There is one minor problem: quite a few doctests are marked with "# indirect doc test" (with space), while the coverage script looks for "# indirect doctest". I have fixed these and added a few more doctests. (I also streamlined the `__contains__` methods slightly, since all they did was try to convert x into self and then test equality, which the coercion framework does automatically anyway.) All four files relating to infinite polynomial rings now pass `sage -coverage` with no complaints.

Simon: if you are happy with the changes in my reviewer patch, then feel free to put the status to "positive review".


---

Comment by SimonKing created at 2010-06-14 13:03:59

Replying to [comment:2 davidloeffler]:
> ...
> 
> Simon: if you are happy with the changes in my reviewer patch, then feel free to put the status to "positive review".

I am happy with it! So, I changed that status to "positive review", and inserted your name as reviewer.

Best regards,
Simon


---

Comment by SimonKing created at 2010-06-14 13:03:59

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 01:45:27

Resolution: fixed
