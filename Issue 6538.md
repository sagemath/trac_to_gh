# Issue 6538: bug in Partitions

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-15 18:55:17

Assignee: mhansen

CC:  brunellus

Keywords: partitions

Looks like there is a bug in Partitions.  Partitions(n, max_slope=-1)  should give the partitions of n with distinct parts, right?

```
sage: Partitions(2, max_slope=-1).list()
[This is the Trac macro *2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2-macro)
sage: Partitions(4, max_slope=-1).list()
[[4], [3, 1]]
```

But if you add the "length" keyword, it doesn't work anymore, at least not completely:

```
sage: Partitions(2, max_slope=-1, length=2).list()  # doesn't work
[This is the Trac macro *1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1-macro)
sage: Partitions(4, max_slope=-1, length=2).list()  # works
[This is the Trac macro *3, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3, 1-macro)
sage: Partitions(4, max_slope=-1, length=3).list()  # doesn't work
[This is the Trac macro *2, 1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 1, 1-macro)
```



---

Comment by tscrim created at 2012-05-16 04:24:13

Fixed by making changes to IntergerListLex and not increasing algorithm's complexity. Fixed some other bugs in IntegerListLex and Partitions when bad input is given.

Note: most of the work on this patch was done during Sage Days 38.


---

Comment by tscrim created at 2012-05-16 04:24:13

Changing keywords from "partitions" to "partitions, days38".


---

Comment by tscrim created at 2012-05-16 04:24:13

Changing status from new to needs_review.


---

Comment by benjaminfjones created at 2012-06-05 14:45:03

Changing status from needs_review to needs_work.


---

Comment by benjaminfjones created at 2012-06-05 14:45:03

The code you've written looks good. I think you should also add a few doctests in EXAMPLES or TESTS where appropriate to demonstrate that the issue in this ticket it resolved.


---

Comment by tscrim created at 2012-06-27 03:24:26

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2012-06-27 03:24:26

Doctests have been added.

Thanks for reviewing.


---

Comment by benjaminfjones created at 2012-06-27 19:38:01

Changing status from needs_review to positive_review.


---

Comment by benjaminfjones created at 2012-06-27 19:38:01

Changes look good and thanks for adding the doctests. You done some nice code cleanup too, which is great. Positive review pending `make ptestlong`.


---

Comment by jdemeyer created at 2012-07-02 20:42:14

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-07-02 20:42:14

It fails a doctest:

```
sage -t  -force_lib devel/sage/sage/combinat/integer_vector.py
**********************************************************************
File "/release/merger/sage-5.2.beta1/devel/sage-main/sage/combinat/integer_vector.py", line 988:
    sage: IntegerVectors(3, 0, min_part=1).list()
Expected:
    []
Got:
    [This is the Trac macro *3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3-macro)
**********************************************************************
```

It also fails a test added by #12925:

```
sage -t  -force_lib devel/sage/sage/combinat/tutorial.py
**********************************************************************
File "/release/merger/sage-5.2.beta1/devel/sage-main/sage/combinat/tutorial.py", line 1635:
    sage: Partitions(2, max_slope=-1, length=2).list()
Expected:
    [This is the Trac macro *1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1-macro)
Got:
    []
**********************************************************************
```



---

Comment by tscrim created at 2012-07-11 11:26:47

It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)


---

Comment by tscrim created at 2012-07-11 11:26:47

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-07-11 11:56:58

Replying to [comment:8 tscrim]:
> It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)
I have reopened that ticket, so they can fix their test.


---

Comment by nthiery created at 2012-07-11 14:54:35

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 tscrim]:
> > It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)
> I have reopened that ticket, so they can fix their test.

Have you read the text just above that doctest? It is precisely *documenting* this bug.

So, I am glad that you fixed that bug, but this ticket #6538 is responsible for updating the tutorial accordingly. Please merge back #12925! It's been delayed long enough.


---

Comment by tscrim created at 2012-07-13 10:15:13

Replying to [comment:10 nthiery]:
> Replying to [comment:9 jdemeyer]:
> > Replying to [comment:8 tscrim]:
> > > It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)
> > I have reopened that ticket, so they can fix their test.
> 
> Have you read the text just above that doctest? It is precisely *documenting* this bug.
> 
> So, I am glad that you fixed that bug, but this ticket #6538 is responsible for updating the tutorial accordingly. Please merge back #12925! It's been delayed long enough.

Tutorial updated accordingly.


---

Comment by nthiery created at 2012-07-13 18:33:15

> Tutorial updated accordingly.

Thanks! I am fine with this change.

Still, I am pretty sure that the underlying engine is still broken; if you can come up with an example illustrating that, please add it there!

Thanks,
                           Nicolas


---

Comment by jdemeyer created at 2012-08-08 13:04:08

Nicolas: it's not clear whether your comment should be interpreted as positive_review or needs_work?  Could you change the ticket status to either of these two?


---

Comment by nthiery created at 2012-08-08 13:23:26

Replying to [comment:13 jdemeyer]:

> Nicolas: it's not clear whether your comment should be interpreted as positive_review or needs_work?  Could you change the ticket status to either of these two?

Sorry if I was unclear. Travis: I leave that decision to you. If you have an example, please add it. Otherwise you can put a positive review under hand.

Cheers,


---

Comment by tscrim created at 2012-08-08 20:03:28

I can't find an example right now. I've tried with max_slope, min_slope, inner, outer, max_length, min_length, and multiple combinations of them and could not get any wrong results.


---

Comment by tscrim created at 2012-08-08 20:03:28

Changing status from needs_review to positive_review.


---

Attachment

Rebased to sage-5.3.beta1


---

Comment by jdemeyer created at 2012-08-14 07:02:06

Resolution: fixed


---

Comment by jhpalmieri created at 2012-08-29 17:50:09

If you're still looking for something that gives the wrong answer, use `parts_in`:

```
sage: [len(p) for p in Partitions(10, length=6, parts_in=[1,2])]
[5, 6, 7, 8, 9, 10]
sage: Partitions(10, parts_in=[1,2]).cardinality() == Partitions(10, length=6, parts_in=[1,2]).cardinality()
True
```

Another ticket?

Edit: I guess this is #12278.)


---

Comment by nthiery created at 2012-08-31 06:59:22

Replying to [comment:17 jhpalmieri]:
> If you're still looking for something that gives the wrong answer, use `parts_in`:
> {{{
> sage: [len(p) for p in Partitions(10, length=6, parts_in=[1,2])]
> [5, 6, 7, 8, 9, 10]
> sage: Partitions(10, parts_in=[1,2]).cardinality() == Partitions(10, length=6, parts_in=[1,2]).cardinality()
> True
> }}}
> Another ticket?
> 
> Edit: I guess this is #12278.)

Yup: I copy pasted this example as a comment in #12278!

However, I was looking for an example giving wrong results while only using the IntegerListsLex engine (i.e. without parts_in). Thanks though :-)
