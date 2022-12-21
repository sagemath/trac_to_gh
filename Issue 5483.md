# Issue 5483: [with preliminary patch; not ready for review; request comments] Add explain_pickle module; allow overriding class lookup for unpickling

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-11 07:12:13

Assignee: cwitty

CC:  was

explain_pickle is an unpickler (intended to be totally compatible with the cPickle unpickler) that produces Sage source code, which can then be evaluated by sage_eval.  This is useful to see exactly how the unpickle process works.  For example:


```
sage: explain_pickle(dumps(3))

pg_make_integer = unpickle_global('sage.rings.integer', 'make_integer')
pg_make_integer('3')
sage: explain_pickle(dumps(3), in_current_sage=True)

from sage.rings.integer import make_integer
make_integer('3')
```


I think the code works, but I'm not done writing documentation and doctests.


---

Comment by nthiery created at 2009-04-16 16:59:42

I am not technically qualified to review this, patch it has been in the sage-combinat queue for a couple weeks, and has proven really useful! So +1 from Florent and myself.


---

Comment by mabshoff created at 2009-04-16 21:18:49

Carl: Can you change the summary in case this patch is ready for review?

I changed it so that this ticket is picked up by the right report.

Cheers,

Michael


---

Attachment

I finally managed to finish writing the doctests (and fixed a few bugs in the process).


---

Comment by mabshoff created at 2009-05-19 20:28:21

The new file(s) should get added to the reference manual so that people actually can read about them ;).

Cheers,

Michael


---

Comment by nthiery created at 2009-05-22 00:34:20

Changing keywords from "" to "pickling".


---

Comment by nthiery created at 2009-05-22 00:34:20

I have been using this patch on a regular basis without any issue. It is extremely useful, and very well and thoroughly documented.

The code itself is for the most part straightforward, yet pretty technical.
By its nature of the code, the included systematic unit tests should catch most potential bugs.
Checking the tests themselves would require a thorough knowledge of the cpickle protocol which I do not have. But which I trust Carl to have.
The included integration test (comparing the result with cPickle on all the sage pickle jar) is a positive sign.
Also this code is mainly intended for interactive users, so remaining bugs in them should not cause a threat to the rest of the Sage library.
Besides, this patch is a blocker for the category integration.

I am about to attach a short patch fixing some ReST stuff, and adding explain_pickle to the reference manual as recommended by Michael.

For all those reason, I would give my two thumbs up for a positive review. And for advertising this cool tool beyond the Sage world.

William: what do you think?


---

Attachment

Oral comment by William: no reason not to integrate this. Positive Review.


---

Comment by mhansen created at 2009-06-01 05:24:01

I get the failure at http://sage.pastebin.com/m4bec1638

Carl, is it trivial?


---

Comment by cwitty created at 2009-06-02 20:14:12

This appears to be a difference in Python's repr(), possibly between Python 2.5.2 (from Sage 3.4.2 on my laptop, where I developed the patch) and Python 2.5.4 (from Sage 4.0 on sage.math).

Python 2.5.2:

```
>>> v = ([],)
>>> v[0].append(v)
>>> repr(v)
'([([...],)],)'
```


Python 2.5.4:

```
>>> v = ([],)
>>> v[0].append(v)
>>> repr(v)
'([(...)],)'
```


I don't have time to experiment further right now, but I would suggest changing the expected output to the new version, and if it's consistent across all the test platforms then chalk it up to a change in Python and call it good.


---

Comment by mhansen created at 2009-06-03 20:52:01

Resolution: fixed


---

Comment by mhansen created at 2009-06-03 20:52:01

I fixed the doctest.

Merged in 4.0.1.rc0.
