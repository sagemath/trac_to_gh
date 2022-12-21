# Issue 5165: make padded_list use prec by default

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-02-03 05:59:54

Assignee: AlexGhitza

Consider this situation:


```
sage: f = ModularForms(28,2).q_expansion_basis()[-1]
sage: f
q^7 + O(q^20)
```


At this point, I would like to be able to do f.padded_list() and have this take f.prec() as default parameter.  It's not a big deal, but it would be more convenient than having to type f.padded_list(f.prec()).  There might be other situations (power series in general, for instance?) where this change could also be made.

I'll have a patch up for this soon.


---

Comment by AlexGhitza created at 2010-01-03 10:20:18

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-03 10:20:18

In fact, `padded_list` is actually inherited from power series.

See the attached patch.


---

Attachment


---

Comment by davidloeffler created at 2010-04-05 14:57:26

Looks fine to me.


---

Comment by davidloeffler created at 2010-04-05 14:57:26

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 05:19:57

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 05:19:57

Merged in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 06:05:03

(The change in the description was accidental.)
