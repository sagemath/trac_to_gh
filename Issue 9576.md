# Issue 9576: Allow the operator & for submodule intersections.

Issue created by migration from https://trac.sagemath.org/ticket/9576

Original creator: fmaltey

Original creation time: 2010-07-22 07:45:59

Assignee: jason, was

Keywords: operator & for submodule intersection

There is already the operatror & for Sets intersections : S1 & S2.

There is also the operator + for submodules sum : F+G.

I propose to expand the operator & over submodules and subspaces,
and add theses lines in free_modules.py


```
## allow the "intersection" operator & for submodules.
 
     def __and__ (self, other) : return self.intersection (other)
```



---

Comment by git created at 2017-10-16 07:34:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pmenegat created at 2017-10-16 07:38:02

Changing status from new to needs_review.


---

Comment by sbrandhorst created at 2017-10-16 07:40:40

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-10-22 17:23:29

Resolution: fixed
