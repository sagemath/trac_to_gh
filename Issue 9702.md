# Issue 9702: Matching polynomials for graphs

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-08-07 03:20:23

Assignee: jason, ncohen, rlm

CC:  boothby ncohen




---

Comment by rlm created at 2010-08-07 03:24:37

Changing status from new to needs_work.


---

Comment by rlm created at 2010-08-07 03:24:37

But it's very close!


---

Comment by rlm created at 2010-10-30 11:44:56

Replaces trac_9702-{1, 2, 3 and 4}.patch


---

Attachment


---

Comment by rlm created at 2010-10-30 11:49:43

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-11-04 15:38:10

Here is where I am at the moment `:-)`

Nathann


---

Comment by ncohen created at 2010-11-16 16:32:06

Helloooooooo !!!

Well, it seemed fuxxy it my mind last time I had a look at it, and it may have been because I was trying to understand how your data structure worked.... Knowing this, I opened it again today and it seemed crystal clear `:-)`

I changed nothing since the last version of my patch, short of a new doctest in the method computing the polynomials of the complete graph, using the formula given at

http://mathworld.wolfram.com/MatchingPolynomial.html

If anybody can review my patch, this ticket is good to go !

Nathann


---

Attachment


---

Comment by rlm created at 2010-11-26 16:42:58

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-11-26 16:42:58

Nathann,

Thanks for the help! I've changed the indentation in your patch for three lines, otherwise it's the same.


---

Comment by ncohen created at 2010-11-26 16:55:57

> Thanks for the help! I've changed the indentation in your patch for three lines, otherwise it's the same.

Yeah, let's skip reviewing those changes `:-D`

Nathann


---

Comment by jdemeyer created at 2010-12-06 13:41:20

Please fix the Sphinx WARNING:

```
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha0/devel/sage/doc/en/reference/sage/graphs/matchpoly.rst:215: WARNING: duplicate citation Godsil93, other instance in /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha0/devel/sage/doc/en/reference/sage/graphs/graph.rst
```



---

Comment by jdemeyer created at 2010-12-06 13:41:20

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-12-06 16:59:03

Replying to [comment:9 jdemeyer]:
> Please fix the Sphinx WARNING:
> {{{
> /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha0/devel/sage/doc/en/reference/sage/graphs/matchpoly.rst:215: WARNING: duplicate citation Godsil93, other instance in /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.2.alpha0/devel/sage/doc/en/reference/sage/graphs/graph.rst
> }}}

Nathann,

Can you fix this?


---

Comment by ncohen created at 2010-12-06 17:04:04

I will do that asap -- I was compiling Sage when I began to run the -testall on your patch for bitsets, I am now running a testall for my own patch on directed cycles, and thos one's next on the list `:-)`

Nathann


---

Attachment

Patch updated !

Nathann


---

Comment by ncohen created at 2010-12-06 17:17:00

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-12-06 17:26:24

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-12 06:32:57

Resolution: fixed


---

Comment by jdemeyer created at 2011-11-14 08:58:28

See #12028 for a follow-up (sometimes `matching_polynomial` just hangs).
