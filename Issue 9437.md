# Issue 9437: special linear group over finite rings

Issue created by migration from https://trac.sagemath.org/ticket/9437

Original creator: vdelecroix

Original creation time: 2010-07-06 15:24:59

Assignee: AlexGhitza

CC:  vdelecroix

Keywords: group, matrix, special linear

Sage is not able to work with special linear group over finite rings (for example iterate over its element). As in the following example, the constructor accept the argument Zmod(4). But the object is not able to do anything due to call to finite field in gap. Curiously, list(G) and G.list() does not raise the same error (but both of them do).


```
sage: G = SL(2, Zmod(4))
sage: print G
sage: list(G)
TypeError                                 Traceback (most recent call last)
...
TypeError: variable names have not yet been set using self._assign_names(...)
error coercing to finite field
sage: G.list()
NameError                                 Traceback (most recent call last)
NameError: name 'ZmodnZObj' is not defined
```



---

Attachment

patch against 4.6.alpha1


---

Comment by davidloeffler created at 2010-09-23 13:46:47

For a matrix group G, the two commands `list(G)` and `G.list()` are totally different implementations; the former uses Gap to calculate the generators of G, and does the rest in Sage, while the latter just asks Gap for the list. The former works since #8970. The patch above fixes the latter, and adds doctests to prove that they both work.

It is, of course, really dumb that we have two independent implementations, but that's a job for another ticket.


---

Comment by davidloeffler created at 2010-09-23 13:46:47

Changing status from new to needs_review.


---

Comment by cremona created at 2010-10-28 19:42:30

With 4.6.rc0 the patch applies and works fine.  But look at these timings:

```
sage: G = SL(2, Zmod(4))
sage: time a = list(G)  
CPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s
Wall time: 1.69 s
sage: time b = G.list() 
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 20.60 s
```


I'm not letting that stop me giving the patch a positive review, but it suggest that the list() method should be calling whatever the other one uses!

Testing the directory matrix_gps, the file which this patch changes now takes a very long time:

```
sage -t  "sage/groups/matrix_gps/matrix_group.py"           
	 [263.9 s]
```

whereas without the patch:

```
[240.1s]
```

Is the extra time just the time of the new doctest (if so, mark it #long time), or are some other doctests now slower?


---

Comment by cremona created at 2010-10-28 19:42:30

Changing status from needs_review to needs_info.


---

Comment by davidloeffler created at 2011-01-23 10:36:55

I just remembered this ticket, which I'd forgotten about completely...

Can I propose that we have another ticket for dealing with the discrepancy between the two "list" methods? It's somewhat independent of the problem with non-finite-field base rings -- even if `G = SL(3, 17)` then `G.list()` and `list(G)` are using completely independent implementations -- so it's a preexisting problem. Hence I'm putting this back to "needs review".


---

Comment by davidloeffler created at 2011-01-23 10:36:55

Changing status from needs_info to needs_review.


---

Comment by davidloeffler created at 2011-01-24 09:27:49

In fact there is already a ticket for the discrepancy of the "list" methods: #8588.


---

Comment by davidloeffler created at 2011-01-24 09:52:21

I've done a test and the before/after timings for testing `matrix_group.py` (on selmer.warwick.ac.uk using 4.6.2.alpha1) are 25.9 s and 27.0 s. I think that's acceptable without flagging anything as #long.


---

Comment by cremona created at 2011-01-24 14:22:21

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2011-01-24 14:22:21

OK, and I checked that it still works fine with 4.6.2.alpha1.


---

Comment by jdemeyer created at 2011-01-27 14:34:21

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-27 14:34:21

This patch conflicts with #10515.  So could you please rebase this patch so that it applies on top of #10515?


---

Comment by davidloeffler created at 2011-01-27 15:23:01

rebased version


---

Attachment

Done. There's no change in the actual code of the patch, just variable names and diff context, so I'm reinstating the positive review.


---

Comment by davidloeffler created at 2011-01-27 15:24:04

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-28 08:48:31

Resolution: fixed
