# Issue 9593: spring layout does not converge on some graphs

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2010-07-24 18:32:43

Assignee: jason, ncohen, rlm

CC:  rlm chapoton

Try the following in 4.5.2.alpha0 (or after applying #9532):

```
sage: G = graphs.PetersenGraph()
sage: set_random_seed(0); G.plot(layout='spring', iterations=10000)
sage: set_random_seed(0); G.plot(layout='spring', iterations=10001)
```

I get very different-looking graphs.  (If you go back and try with iterations=10000 again, you get the same graph again, showing that #9532 did make it reproducible, at least.)

Maybe some constants need tweaking?

I think this may be causing the problem reported in the first comment on #9584.


---

Comment by leif created at 2010-07-24 20:15:05

Replying to [ticket:9593 cwitty]:
> I think this may be causing the problem reported in the first comment on #9584.

Carl, should we fix that one here (numeric noise causing doctest failure)?


---

Comment by cwitty created at 2010-07-24 22:08:03

The story so far: #9532 tried to make spring layout reproducible (and added tests to see that it was reproducible), but it wasn't enough and so the layout is actually not reproducible across platforms.  Before #9532, spring layout was totally non-reproducible.

So in my opinion, the correct thing to do for the next release is just to remove the failing doctest.  Spring layout wasn't reproducible before, so nobody can be depending on it being reproducible; and it isn't now, so there's no point in a test that verifies that it is reproducible.  The patch that removes the doctest should not go on this ticket (removing the doctest is not part of fixing layout convergence).  When this ticket is fixed, the doctest (or a similar one) should be added, to show that spring layout then does become reproducible.


---

Comment by leif created at 2010-07-24 22:50:21

Ok, I'll open a new ticket that simply adds a `# random` to that doctest.


---

Comment by leif created at 2010-07-25 19:53:08

Replying to [comment:3 leif]:
> Ok, I'll open a new ticket that simply adds a `# random` to that doctest.

Oh, I completely forgot to add this here: The related _doctest error_ in Sage 4.5.2.alpha0 is now #9594, which already has positive review. (The comment in the patch links back to _this_ ticket, which I found more appropriate, since the `# random` tag can hopefully be removed again once we have _reproducible_ spring layout.)


---

Comment by jmantysalo created at 2016-07-15 20:48:50

Changing status from new to needs_review.


---

Comment by jmantysalo created at 2016-07-15 20:48:50

I think that this one has just forgotten to be closed. Frédéric, please click positive_review if you agree.


---

Comment by chapoton created at 2016-07-15 20:57:03

ok, let us close that


---

Comment by chapoton created at 2016-07-15 20:57:03

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix
