# Issue 3277: context for calculus assumptions

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-05-23 08:15:57

Assignee: gfurnish

CC:  mmezzarobba charpent

one should be able to do something like

```
with assumptions(x<0):
    ...
```


where assume() and forget() would be called on the entering and exiting of the block. This could probably be cleanly done with maxima's contexts. 


---

Comment by gfurnish created at 2008-05-23 19:41:14

I'm going to implement passing of assumptions into functions, so much of this can be done as an addon to that (with some global assumption list)


---

Comment by kcrisman created at 2009-01-29 16:42:40

See also #780 and #1163 for discussions of assumption issues.


---

Comment by kcrisman created at 2012-02-14 14:17:34

See also [this ask.sagemath.org question](http://ask.sagemath.org/question/1154/piecewise-assumptions-for-integration), which would love this.  Note that [Maxima does support contexts](http://maxima.sourceforge.net/docs/manual/en/maxima_11.html#contexts).


---

Comment by kcrisman created at 2012-02-14 14:17:34

Changing keywords from "" to "assume".


---

Comment by mkoeppe created at 2020-07-06 00:59:02

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-06 00:59:02

This was implemented in #24119. Should be closed as a dup


---

Comment by @DaveWitteMorris created at 2020-07-06 01:05:53

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2020-07-06 11:33:20

NO WAY!  Thanks to Emmanuel for that!


---

Comment by charpent created at 2020-07-06 11:46:49

Replying to [comment:7 kcrisman]:
> NO WAY!  Thanks to Emmanuel for that!

I may be dense but ... What do you mean by "NO WAY!" ? Do you think that this ticket should be treated separately from #24119 ?


---

Comment by kcrisman created at 2020-07-10 14:49:57

> > NO WAY!  Thanks to Emmanuel for that!
> 
> I may be dense but ... What do you mean by "NO WAY!" ? Do you think that this ticket should be treated separately from #24119 ?

Sorry, an Americanism - it means, "I don't believe this amazing thing that has happened!"  Purely a phrase of thankfulness and surprise.


---

Comment by slelievre created at 2020-08-22 07:10:24

Resolution: fixed
