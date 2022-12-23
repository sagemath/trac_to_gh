# Issue 6641: switch the poset antichains method to use GenericBacktracker and add antichains_iterator.

Issue created by migration from https://trac.sagemath.org/ticket/6641

Original creator: saliola

Original creation time: 2009-07-27 15:01:27

Assignee: saliola

CC:  chapoton

The current implementation of antichains must construct the complete set of antichains, but it can be done via an iterator (using the `GenericBacktracker` class).

I have a patch that I will post shortly.


---

Attachment


---

Comment by saliola created at 2009-07-27 15:32:56

Thanks to Dan Drake for teaching me how to use the backtracker.


---

Attachment


---

Comment by ddrake created at 2009-09-16 02:43:19

Changing type from task to enhancement.


---

Comment by ddrake created at 2009-09-16 02:43:19

I like using the backtracker code, and I'm the one who showed it to Franco and said it was all great and stuff...but I think this is "needs work". I've done a bunch of testing, and this patch is consistently 30-50% slower than the current code. For some things, it was only about 15-20% slower, but mostly it's 30-50%. Here's what I tested:

  * antichain posets 5 and 10 elements
  * symmetric group Bruhat order 3, 4
  * chains with 10-14 elements
  * random posets: 100 elements and 500 elements, with probabilities .05, .2, and .5. The .sobj files for these are in my home directory on sage.math.

A slowdown might be acceptable if there's a big win in code clarity, memory use, ease of doctesting, etc, but I'm not sure we get any of that, except maybe the memory usage. Thoughts?


---

Comment by saliola created at 2009-09-16 13:11:23

Thanks for running the timings. That is a significant difference. I agree that this should be marked as needs work.

For the record, I took the recursive algorithm that is currently used and did very minor adaptations to be able to use it with the backtracker code. So the backtracker code seems to be adding a lot of overhead in this case. The best way to proceed would be to better adapt the recursive construction.

The main advantage to using the backtracker code is that you get an iterator instead of a list.


---

Comment by hivert created at 2010-04-21 21:13:00

I had to rebase the patch which now depends on #8735. I reuploaded it from sage-combinat queue.

Florent


---

Comment by hivert created at 2010-04-21 21:13:59

Rebased version against #8735


---

Attachment


---

Comment by jmantysalo created at 2018-02-23 10:23:35

Changing status from needs_work to needs_review.


---

Comment by jmantysalo created at 2018-02-23 10:23:35

`antichains_iterator` has been done in some other ticket.


---

Comment by chapoton created at 2018-02-23 19:33:22

ok


---

Comment by chapoton created at 2018-02-23 19:33:22

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
