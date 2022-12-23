# Issue 9785: Subsets(list, submultiset=True): wrong output

Issue created by migration from https://trac.sagemath.org/ticket/9786

Original creator: mmezzarobba

Original creation time: 2010-08-23 12:57:41

Assignee: sage-combinat

CC:  hivert brunellus jason

Keywords: multiset


```
sage: S = Subsets(['a','a','b','b'], 2, submultiset=True); S.list()
[['a', 'a'], ['a', 'b'], ['b', 'b']]
sage: S = Subsets(['a','b','a','b'], 2, submultiset=True); S.list()
[['a', 'a'], ['a', 'a'], ['a', 'a']]
```



---

Comment by brunellus created at 2011-12-12 20:36:33

I think the problem is that the _indices list was created before input sorting, so after the sort its elements pointed to the wrong locations. For example in the case ["a", "b", "a", "b"] indices looked like [0, 1] what corresponds to the original data (0->a, 1->b), but after the sort the content of _s was ["a", "a", "b", "b"], so 0 and 1 both pointed to "a".


---

Comment by brunellus created at 2011-12-12 20:36:33

Changing status from new to needs_review.


---

Comment by mhansen created at 2011-12-18 13:26:47

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by jdemeyer created at 2011-12-22 13:06:08

Resolution: fixed
