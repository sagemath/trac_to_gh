# Issue 8904: libsingular: memory leak in Matrix.act_on_polynomial

Issue created by migration from https://trac.sagemath.org/ticket/8904

Original creator: SimonKing

Original creation time: 2010-05-06 12:01:33

Assignee: tbd

CC:  malb

Keywords: libsingular act_on_polynomial memleak

There is a memory leak that occurs when mapping a multivariate polynomial using a matrix:

```
sage: R.<a,b>  =  QQ[]
sage: M = Matrix([[0,1],[1,0]])
sage: n = 0
sage: p = R.random_element()
sage: q = M.act_on_polynomial(p)
sage: mem = get_memory_usage()
sage: while(1):
....:     n+=1
....:     q = M.act_on_polynomial(p)
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:
801.04296875 2
801.54296875 2011
802.04296875 4738
802.54296875 7406
803.04296875 10091
803.54296875 12809
804.04296875 15495
804.54296875 18171
805.04296875 20873
805.54296875 23561
806.04296875 26251
...
```


This does not occur if one maps the polynomial by a proper morphism:

```
sage: f = R.hom([M.act_on_polynomial(t) for t in R.gens()],R)
sage: while(1):
....:     n+=1
....:     q = f(p)
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:
```





---

Comment by chapoton created at 2018-05-27 09:42:46

no longer an issue in 8.3.beta2


---

Comment by chapoton created at 2018-05-27 09:42:46

Changing status from new to needs_review.


---

Comment by SimonKing created at 2018-05-27 10:00:27

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2018-05-27 10:00:27

Replying to [comment:5 chapoton]:
> no longer an issue in 8.3.beta2

I can confirm. So, positive review with both of us as reviewers, I guess.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
