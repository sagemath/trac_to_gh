# Issue 6322: optional doctest failure -- another mistake in bordeaux lectures

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:52:53

Assignee: tbd


```
sage -t -long --optional devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/nf_galois_groups.rst", line 92:
    sage: K.galois_group(type="gap", algorithm='magma')    # optional
Expected:
    verbose...
    Galois group Transitive group number 2 of degree 3 of
    the Number Field in a with defining polynomial x^3 - 2
Got:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_nf_galois_groups.py
	 [12.4 s]
```



---

Comment by chapoton created at 2015-10-10 18:48:49

Changing status from new to needs_review.


---

Comment by chapoton created at 2015-10-10 18:48:49

Changing priority from major to minor.


---

Comment by chapoton created at 2015-10-10 18:48:49

New commits:


---

Comment by jdemeyer created at 2015-10-10 20:12:50

Did you actually test it? I don't have magma, but if you tell me that the doctest passes, I believe you.


---

Comment by chapoton created at 2015-10-10 20:34:18

I do not have magma either. Do we know somebody that has magma ?


---

Comment by jdemeyer created at 2015-10-10 21:04:05

Replying to [comment:8 chapoton]:
> I do not have magma either.

Then why do you care about this ticket???


---

Comment by git created at 2015-10-12 17:20:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-10-12 17:22:47

It appears that:

1) I do have `magma` now
2) The test requires `database_gap`

This has been tested, and needs review again.


---

Comment by chapoton created at 2015-10-17 20:06:17

ok, the tests do pass with magma and database_gap and also without both

i am not quite sure of the way to put 2 optional conditions on the same line

Jeroen, could you please set a positive review if this is correct ?


---

Comment by jdemeyer created at 2015-10-17 20:11:28

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2015-10-17 20:11:28

The usual syntax is

```
# optional - magma database_gap
```

I don't know if what you did works or not, but it's better to change it.


---

Comment by git created at 2015-10-17 20:18:00

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-10-17 20:18:37

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2015-10-17 20:18:37

done


---

Comment by jdemeyer created at 2015-10-17 20:19:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-10-18 19:11:21

Resolution: fixed
