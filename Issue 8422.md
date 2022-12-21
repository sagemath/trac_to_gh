# Issue 8422: ChainPoset in broken for small input

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-03-02 17:54:52

Assignee: sage-combinat

Keywords: ChainPoset

For n>2 the answer is correct: 

```
sage: Posets.ChainPoset(3).size()
3
sage: Posets.ChainPoset(4).size()
4
sage: Posets.ChainPoset(5).size()
5
```

However:

```
sage: Posets.ChainPoset(2).size()
1
sage: Posets.ChainPoset(1).size()
...
ValueError: not valid poset data.
```



---

Comment by hivert created at 2010-03-02 18:13:37

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2010-03-04 21:58:01

Changing assignee from sage-combinat to hivert.


---

Comment by nborie created at 2010-03-04 22:50:41

patch apply, doctests passed, documentation ok.

Positive review from me.


---

Comment by nborie created at 2010-03-04 22:50:41

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 08:50:21

Resolution: fixed
