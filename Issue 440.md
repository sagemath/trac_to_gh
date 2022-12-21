# Issue 440: Integer.__index__() currently goes via a python long

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-08-18 18:25:28

Assignee: somebody

Currently `Integer.__index__()` goes via a python long. In most cases the result should be just a python int, and it should be much faster to go directly there.

Probably the best way to implement this is to first call `mpz_size(x.value)` to check the size in words; if the size is one, then construct a python int directly; otherwise go to a long.

Even better might be to write another version of `mpz_get_pylong` which can produce a python int when that's feasible, or a long if it's not.



---

Comment by dmharvey created at 2007-08-18 18:26:36

oops I forgot to mention the above comment is for sage 2.8


---

Comment by dmharvey created at 2007-08-18 19:01:42

Here's a profile, on sage.math, sage 2.8.1:


```
sage: L = [None] * 10
sage: index = Integer(5)
sage: timeit x = L[index]
1000000 loops, best of 3: 690 ns per loop
sage: timeit x = L[index]
1000000 loops, best of 3: 691 ns per loop
```


Let's see if we can do better than that...


---

Comment by dmharvey created at 2007-08-18 20:14:58

I'm about to attach a patch for this, here is the new profile:


```
sage: L = [None] * 10
sage: index = Integer(5)
sage: timeit x = L[index]
1000000 loops, best of 3: 331 ns per loop
```



---

Attachment

adds new mpz_get_pyintlong function, change some calls in Integer class to use this function


---

Comment by was created at 2007-08-18 20:55:25

Resolution: fixed
