# Issue 8305: Improve documentation of Monsky-Washnitzer code

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2010-02-19 03:34:22

Assignee: cremona

CC:  jpflori

Keywords: Monsky-Washnitzer, elliptic curves, hyperelliptic curves

The code in schemes/elliptic_curves/monsky_washnitzer.py largely dates from a time (early 2007) before Sage documentation and doctesting standards had been codified. As a result, its coverage is terrible (26 of 107).

It may also be worth a mild refactor: since it now applies more generally to hyperelliptic curves, it probably should be under schemes/hyperelliptic_curves.


---

Comment by robertwb created at 2010-02-20 08:54:26

The patch at #7926 brings coverage up to 50% (though I didn't make it to documenting the really interesting stuff).


---

Comment by kedlaya created at 2010-02-20 14:57:44

OK, so this ticket should stay on ice until someone (e.g., me) has a chance to review #7926. Besides the documentation, there is also the issue of moving the MW code from elliptic to hyperelliptic where it belongs.


---

Comment by kedlaya created at 2010-02-20 14:57:44

Changing assignee from cremona to kedlaya.


---

Attachment

first patch, with coverage reaching 67%


---

Comment by chapoton created at 2013-08-23 16:40:27

after some more work, coverage is almost 77%


---

Comment by chapoton created at 2013-10-01 19:37:06

after some more work, coverage is now 83%


---

Attachment


---

Comment by chapoton created at 2013-10-14 19:33:28

after some more work, coverage is now 85%


---

Comment by chapoton created at 2014-01-05 13:00:29

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-01-05 13:00:29

maybe this can be considered as a good first step towards 100% ?
----
New commits:


---

Comment by kedlaya created at 2014-01-07 23:08:24

An excellent step, yes! Good work.

I've spun off tickets #15645 and #15646 to track the remaining issues on this ticket (100% coverage and refactoring).


---

Comment by kedlaya created at 2014-01-07 23:08:24

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-09 06:43:30

Fill in the reviewer name...


---

Comment by vbraun created at 2014-01-10 07:29:50

Resolution: fixed
