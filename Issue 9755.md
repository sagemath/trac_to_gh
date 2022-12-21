# Issue 9755: Symmetric Function coercion issue

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2010-08-17 15:27:40

Assignee: jbandlow

CC:  sage-combinat

Keywords: symmetric functions

The following was reported to me by Nicolas Thiéry and Lenny Tevlin.


```
R.<q,t> = ZZ[]
R = FractionField(R)
P = MacdonaldPolynomialsP(R,q,t) 
Q = HallLittlewoodQ(R,t) # or Q or P (Qp = H)
Ph=HallLittlewoodP(R,t)
SF = SymmetricFunctions(R)
SF.inject_shorthands()
Q(s.one())

Traceback (click to the left of this block for traceback)
...
AttributeError: 'int' object has no attribute 'subs'
```

The same error occurs with `Ph(s.one())`, although `P(s.one())` works.


---

Comment by jbandlow created at 2010-08-19 19:16:15

Ready for review.


---

Comment by jbandlow created at 2010-08-19 19:16:15

Changing status from new to needs_review.


---

Comment by jbandlow created at 2010-08-19 19:28:19

Note for combinat people: I've put this patch in the 'needs review' section of the queue.


---

Comment by mhansen created at 2010-09-17 00:53:46

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-09-17 00:53:46

Looks good to me.


---

Comment by mpatel created at 2010-09-18 07:53:51

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-18 07:53:51

Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?


---

Attachment


---

Comment by jbandlow created at 2010-09-18 14:29:09

Replying to [comment:4 mpatel]:
> Could someone make the commit string a bit more descriptive, e.g., `#9755: Fix coercion problem for Hall-Littlewood polynomials`?

Oops, sorry about that.  Fixed.


---

Comment by jbandlow created at 2010-09-18 14:29:09

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-09-18 14:42:19

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-18 20:36:56

Could you move `#9755: Fix...` to the first line of the commit string?  Otherwise, `hg log` gives, e.g.,

```
changeset:   14948:0b3960059b6c
tag:         qtip
tag:         trac_9755_hall_littlewood_coercions-jb.patch
tag:         tip
user:        Jason Bandlow <...>
date:        Thu Aug 19 15:08:26 2010 -0400
summary:     [mq]: trac_9755_hall_littlewood_coercions-jb.patch
```



---

Attachment


---

Comment by jbandlow created at 2010-09-18 21:54:07

Sorry.  How's the new version (I forgot to overwrite the old one)?


---

Comment by mpatel created at 2010-09-18 22:13:21

Replying to [comment:8 jbandlow]:
> Sorry.  How's the new version (I forgot to overwrite the old one)?

No worries.  V2 looks good.  Thanks!


---

Comment by mpatel created at 2010-09-29 04:25:03

Resolution: fixed
