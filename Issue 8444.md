# Issue 8444: Memleak in conversion for univariate polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/8444

Original creator: SimonKing

Original creation time: 2010-03-05 12:41:29

Assignee: tbd

Keywords: univariate polynomial ring coercion

At [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a145a02c8d379b11), Ben Linowitz reported a problem with memory. Apparently it boils down to the following problem:


```
sage: R.<x> = QQ[]
sage: M = get_memory_usage()
sage: for n in range(50000):
....:     Mnew = get_memory_usage()
....:     if Mnew > M:
....:         print n, Mnew-M
....:         M=Mnew
....:     a = R(1)
....:
0 1.51171875
6673 0.12890625
8785 0.12890625
10897 0.12890625
13009 0.12890625
15121 0.12890625
17233 0.12890625
19345 0.12890625
21457 0.12890625
23569 0.12890625
25681 0.12890625
27793 0.12890625
29905 0.12890625
32017 0.12890625
34129 0.12890625
36241 0.12890625
38353 0.12890625
40465 0.12890625
42577 0.12890625
44689 0.12890625
46801 0.12890625
48913 0.12890625
```

This is with sage 4.3.3 on sage.math.

So, the first 6673 everything is good. Then, after 2112 rounds there is a leak of (if I did not miscompute) 135168 Byte.

This does not occur for multivariate rings:


```
sage: R.<x,y> = QQ[]
sage: M = get_memory_usage()
sage: for n in range(50000):
....:     Mnew = get_memory_usage()
....:     if Mnew > M:
....:         print n, Mnew-M
....:         M=Mnew
....:     a = R(1)
....:
0 1.5
```



---

Comment by mhampton created at 2010-03-05 14:32:06

Changing priority from major to critical.


---

Comment by mhampton created at 2010-03-05 22:40:35

Sage-4.3.3 does not have this problem on my mac running 10.6.2.


---

Comment by SimonKing created at 2010-03-05 23:24:08

For the record:

Gonzalo Tornaria stated at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/6de8c4287495d9d3):

  "I think this is caused by a duplicate _sig_on in the bottom part of

pari.`__call__`."


---

Attachment

fix memory leak due to dup call to _sig_on


---

Comment by tornaria created at 2010-03-11 04:42:37

Changing keywords from "univariate polynomial ring coercion" to "univariate polynomial ring coercion, pari, sig_on".


---

Comment by tornaria created at 2010-03-11 04:42:37

Changing status from new to needs_review.


---

Comment by tornaria created at 2010-03-11 04:42:37

The attached patch seems to fix the memleak. I worked on top of 4.3.3; all tests pass with this patch, and the snippet in the ticket description goes through without extra allocations:

```
sage: R.<x> = QQ[]
sage: M = get_memory_usage()
sage: for n in range(50000):
....:     Mnew = get_memory_usage()
....:     if Mnew > M:
....:         print n, Mnew-M
....:         M=Mnew
....:     a = R(1)
....:     
0 1.6015625
sage: 
```


Here's the full commit log which explains the patch:

#8444: fix memory leak due to dup call to `_sig_on` in the bottom part of `PariInstance.__call__`

At the bottom of `PariInstance.__call__` both `_sig_on` (first) and `_sig_str`
(later) are used. In fact, both count as calls to `_sig_on` (actually `_sig_on` is
equivalent to `_sig_str(NULL)`) and these are _not_ reentrant, i.e. nesting is not
supported (anyway, there's only one implicit `_sig_off` in the call to new_gen).

A double `_sig_on`, as defined in `interrupt.h`, is usually equivalent to a single
one -- however, for the pari library these macros are overrided as `_pari_sig_on`
(defined in `misc.h` and `pari_err.h`) adding a call to pari's own error catching
function.  Calling the `err_catch()` function twice without the corresponding
call to `err_leave()` results in a memory leak which is reported in #8444.

The patch is one-liner: removing the first `_sig_on` fixes the memory leak.

Note: this line was added by changeset `10536:423520e7d069` as part of a large
effort to add lots of missing calls to `_sig_on` in pari interface. However, I
think in this case it was just an oversight because the already existing call to
`_sig_on` was only implicit in the call to `_sig_str`.


---

Comment by zimmerma created at 2010-03-15 21:36:55

Dear Gonzalo,

great work! It is very important to fix such issues, thanks a lot.

Paul


---

Comment by zimmerma created at 2010-03-15 21:36:55

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:52:54

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:52:54

Merged "trac_8444.fix_pari_memleak.patch" into 4.4.alpha0.
