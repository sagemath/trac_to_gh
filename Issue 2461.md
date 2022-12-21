# Issue 2461: vector norms should have a reasonable default

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-03-10 18:05:31

Assignee: somebody

v.norm() should work without any arguments, returning the (standard) Euclidean norm. 


---

Attachment


---

Comment by AlexGhitza created at 2008-03-11 02:21:22

I was in the process of refereeing this, and realized that Robert's changes to the doctests uncovered a fairly serious bug in the code for norm():


```
sage: v = vector([1, 2, -3])
sage: v.norm(Infinity)
2
sage: v.norm(1)
0
```


Both of these are wrong, due to the fact that whoever wrote the norm() function (I think it was me, actually) forgot to take absolute values of the entries of the vector before computing the norm.

I fixed this and put up a new patch that incorporates both this fix and Robert's improvements.


---

Attachment


---

Comment by cwitty created at 2008-03-14 01:26:56

Looks good, testall passes.

Apply vector-norms_replace.patch; when writing release notes, note that this patch combines work by robertwb and `AlexGhitza`.


---

Comment by mabshoff created at 2008-03-14 02:27:28

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 02:27:28

Merged in Sage 2.10.4.alpha0
