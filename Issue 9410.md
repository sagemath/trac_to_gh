# Issue 9410: EC.local_data() can't handle extensions of number fields

Issue created by migration from https://trac.sagemath.org/ticket/9410

Original creator: arminstraub

Original creation time: 2010-07-02 17:40:15

Assignee: cremona

CC:  was cturner beankao

Keywords: local_data

In 4.4.4 the following code produces a ValueError:


```
sage: K.<a> = NumberField(x^2+1)
sage: L.<b> = K.extension(x^2-17)
sage: E = EllipticCurve(L, [1,1])
sage: E.local_data()
```


As a workaround, one can use absolute_field:


```
L1.<c> = L.absolute_field()
E1 = EllipticCurve(L1, [1,1])
E1.local_data()
```





---

Comment by arminstraub created at 2016-08-08 12:34:46

This seems to have been fixed since I reported this a couple of years ago, so this ticket can be closed.  Can/should I do something to flag the ticket as such?


---

Comment by cremona created at 2016-08-08 12:51:36

Choose invalid/dontfix from the Milestone menu (under "Modify Ticket").  It will the be closed.

I think it has been fixed for ages, but it hardly seems worth looking for when.  Thanks for noticing -- I'll let you follow the above instructions.


---

Comment by chapoton created at 2016-08-08 12:53:00

yes, please set to positive review with milestone "duplicate invalid wontfix"


---

Comment by arminstraub created at 2016-08-08 13:18:10

Thank you both!  I have changed the milestone as instructed.

There was no option yet to flag this as positively reviewed, so I didn't do that.  My guess is that one has to first set the ticket as "needs review" before that option becomes available.  If this should be done, please let me know.


---

Comment by chapoton created at 2016-08-08 13:31:38

Changing status from new to needs_review.


---

Comment by chapoton created at 2016-08-08 13:31:38

yes, this is a 2-step job. I did the first step for you, you can now do the second step. You could have done both yourself.


---

Comment by arminstraub created at 2016-08-08 13:35:00

Thanks!  I was hesitant to do that without understanding what will happen.  It is set to "positive review" now (with no reviewer, but I hope that is OK in such a case).


---

Comment by arminstraub created at 2016-08-08 13:35:00

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2016-08-08 13:37:10

I am not sure if we need a reviewer here, but you can add your name for safety.


---

Comment by arminstraub created at 2016-08-08 13:45:58

Done!


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
