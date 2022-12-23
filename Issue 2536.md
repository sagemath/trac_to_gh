# Issue 2536: get rid of SageObject.db and SageObject.version everywhere -- these turned out to "not catch on"

Issue created by migration from https://trac.sagemath.org/ticket/2536

Original creator: was

Original creation time: 2008-03-16 00:57:20

Assignee: cwitty

CC:  mkoeppe

Hi,

I wrote db and version methods that all SageObjects have.  It seemed like a good idea at the time.  They didn't catch on -- nobody finds this interesting, etc.  I vote for completely removing them from Sage. 


---

Comment by AlexGhitza created at 2009-01-23 02:46:12

Changing type from defect to enhancement.


---

Comment by aapitzsch created at 2015-01-11 22:09:55

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-02-03 01:47:22

I realize this seems silly for something no one uses, but perhaps we should doctest these deprecations?


---

Comment by git created at 2015-02-07 23:42:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by aapitzsch created at 2015-02-07 23:44:57

Replying to [comment:7 kcrisman]:
> I realize this seems silly for something no one uses, but perhaps we should doctest these deprecations?
Added doctests.


---

Comment by kcrisman created at 2015-02-12 03:44:51

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2015-02-12 03:44:51

I'm a little surprised that doctest works since it does return a value, but I guess the `:...` covers that instead of the usual `:...:`.    Running doctests again but hopefully all is well.


---

Comment by kcrisman created at 2015-02-12 04:16:23


```
Expected:
    Help on FiniteWordPath_2d_str in module sage.combinat.words.paths object:
    ...
    Methods inherited from FiniteWordPath_2d:
    ...
    Methods inherited from FiniteWordPath_all:
    ...
    This only works on Python classes that derive from SageObject.
Got:
<stuff ending with>
     |      This only works on Python classes that derive from SageObject.
     |      
     |      TESTS::
     |      
     |          sage: v = DiGraph().version()
     |          doctest:... DeprecationWarning: version() is deprecated.
     |          See http://trac.sagemath.org/2536 for details.

----------------------------------------------------------------------
sage -t src/sage/combinat/words/paths.py  # 1 doctest failed
```

Otherwise all is well.  I guess this is my fault for asking for the deprecation warning after you did your long doctests, my apologies.


---

Comment by kcrisman created at 2015-02-12 04:16:23

Changing status from positive_review to needs_work.


---

Comment by git created at 2015-02-13 15:16:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by aapitzsch created at 2015-02-13 15:17:18

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2015-02-13 18:28:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-17 19:28:31

Resolution: fixed


---

Comment by dimpase created at 2016-05-03 19:43:14

#20376 uses `db()` for purposes of logging/debugging...
