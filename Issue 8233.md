# Issue 8233: concatenation of words should preserve the data type represention when possible

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-10 16:16:17

Assignee: sage-combinat

CC:  abmasse

This concerns word represented by str, tuple and list :


```
sage: u = Word(range(10))
sage: type(u)
<class 'sage.combinat.words.word.FiniteWord_list'>
sage: type(u*u)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
```


```
sage: v = Word('asdgadsf')
sage: type(v)
<class 'sage.combinat.words.word.FiniteWord_str'>
sage: type(v*v)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
```


```
sage: v = Word((2,3,5,21,34,6))
sage: type(v)
<class 'sage.combinat.words.word.FiniteWord_tuple'>
sage: type(v*v)
<class 'sage.combinat.words.word.FiniteWord_callable_with_caching'>
```



---

Comment by slabbe created at 2010-02-11 18:27:23

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-02-25 11:05:00

Forget about this patch!


---

Attachment

Depends on #7619.


---

Attachment


---

Comment by abmasse created at 2010-03-03 08:46:02

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-03-03 08:46:02

Changing keywords from "" to "word, concatenation".


---

Comment by abmasse created at 2010-03-03 08:46:02

Tested on sage-4.3.3 after having applied ticket #7619. All tests passed, looking at the documentation with `browse_sage_doc` reveals nothing to be corrected. The improvement seems very reasonable and the code looks fine. Positive review !


---

Comment by mhansen created at 2010-03-06 08:52:26

Resolution: fixed
