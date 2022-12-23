# Issue 2170: sage's integer.pyx digits function sucks in the base 10 case

Issue created by migration from https://trac.sagemath.org/ticket/2170

Original creator: was

Original creation time: 2008-02-15 07:59:32

Assignee: somebody

The digits function should be rewritten to have a special
case in the base 10 case, since as illustrated below
it is currently **WAY** slower than just doing str(...) on 
the input number!


```
sage: a = 3^100000
sage: time w = a.digits(base=10)
CPU times: user 1.00 s, sys: 0.01 s, total: 1.01 s
Wall time: 1.01
sage: time v = list(reversed(str(a)))
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
sage: v[:10]
['1', '0', '0', '0', '0', '0', '2', '2', '5', '5']
sage: w[:10]
[1, 0, 0, 0, 0, 0, 2, 2, 5, 5]
```




---

Comment by zimmerma created at 2008-02-15 13:55:42

Together with Laurent Imbert, we propose the attached patch. This solves the case where
the base is >= 10.

```
sage: a = 3^100000
sage: time w = a.digits(base=10)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.01
```



---

Attachment


---

Comment by was created at 2008-02-15 16:43:42

REVIEW: The patch needs to be changed to only use the mpz string trick when the base is  small enough to work with GMP.   Right now we have:

Before patch:

```
sage: a = 9939082340
sage: a.digits(512)
[100, 302, 26, 74]
```


After patch:

```
sage: a = 9939082340
sage: a.digits(10)
['0', '4', '3', '2', '8', '0', '9', '3', '9', '9']
sage: a.digits(32)
['4', '3', 'n', 'k', '6', '8', '9']
sage: a.digits(62)
['g', 'L', 'N', 'd', 'q', 'A']
sage: a.digits(63)
------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by robertwb created at 2008-02-19 19:04:27


```
l = <object> PyString_FromString(str_out) 
```


could simply read 


```
l = str_out
```


and Cython will do the string conversion for you. This looks like it was copied from `Integer.str()` and should be changed there as well. 

It certainly needs to be fixed to handle the base > 62 case, and this patch changes the semantics of the function as well, so I don't think it should be applied as is.


---

Attachment

Attached is a revised patch, fixing the issues reported by the reviewers (whom we thank):

```
sage: a = 9939082340
sage: a.digits(512)
[100, 302, 26, 74]
sage: a.digits(10)
[0, 4, 3, 2, 8, 0, 9, 3, 9, 9]
sage: a = 3^100000
sage: time w = a.digits(base=10)
CPU times: user 0.12 s, sys: 0.00 s, total: 0.12 s
Wall time: 0.11
sage: w[:10]
[1, 0, 0, 0, 0, 0, 2, 2, 5, 5]
```

We also made the change suggested by Robert (in Integer.str() too).
The new digits() function is faster for 10 <= base <= 62, but not as fast as in the 1st (wrong)
patch; the bottleneck seems to be the map(make_integer, l) call.


---

Comment by was created at 2008-02-25 14:39:52

> Attached is a revised patch,

This patch seems to be identical to the original patch.


---

Attachment

> This patch seems to be identical to the original patch.

Sorry for that. The new one (8683.patch) should be the correct one.


---

Comment by jbmohler created at 2008-03-01 18:36:29

I applied 8312.patch and 8683.patch (in that order) to a vanilla 2.10.2.  I may be losing my mind, but it sure appears to me that the patched version is actually *slower* than 2.10.2.  I would also point out that there is no point in declaring 'l' as a 'cdef object' -- that's the cython default.    I also think that " = PyList_New(0)" allocates a python list that is never used (just overwritten later).

As to the original bug, it seems quite intrinsic to me that digits would be slower than str.  The digits method needs to create individual python objects for each and every digit, str does not.  There's a frikkin lot of memory allocation going on there.  With that in mind, I'm not at all convinced that the bug is even fixable at all.


---

Comment by jbmohler created at 2008-03-01 19:43:10

Oh, I see, upon more reflection.  I see that my idea of "big" wasn't quite big enough.  Once, we have a really big number, this patch becomes effective.

Here's what I observe for moderate numbers:

```
# vanilla 2.10.2
sage: a = 28356982659^15
sage: %timeit w = a.digits(base=10)
10000 loops, best of 3: 67 Âµs per loop
```



```
# Patched version
sage: a = 28356982659^15
sage: %timeit w = a.digits(base=10)
10000 loops, best of 3: 136 Âµs per loop
```


I do see that my memory allocation comment is entirely incorrect though.  I'm still a bit disturbed though.  Why should we suddenly get slower at 63?  Can't we extract gmp's algorithm for larger bases?  Part of the reason for my questions is that I want to use the digits method for mpoly factoring and it has some issues with large bases.

Modulo my comments above about the variable 'l', I think this is a good patch for the moment and should be included.  I do think there is a better answer in the long-term for larger bases though.


---

Comment by jbmohler created at 2008-03-02 03:04:20

Well, I guess I should've waited to post the first two after I thought about this a bit more.  :)

I now have some serious reservations about this patch:

1)  It actually makes small cases slower.  (See above)

2)  It doesn't handle negatives correctly (what is correct?) -- we need a doc-test to clarify intent here.


```
sage: n=-20385
sage: n.digits(100)  # this is what used to occur with negatives
[-85, -3, -2]
sage: n.digits(10)  # the last zero comes from '-' in the string?
[5, 8, 3, 0, 2, 0]
```


3)  The version that runs with a non-None digits parameter is still slow.

4)  A big base (bigger than 62) is still slow.

5)  I now have cold feet about the 'PyMem_Free'.  Shouldn't it be 'free' since presumably gmp allocated with 'malloc'?  Or, did we hack gmp?  Or, doesn't it matter?

Now, this raises some questions in my mind.  What should happen with negatives when digits are specified?


---

Comment by jbmohler created at 2008-03-02 05:53:39

With apologies to zimmerma and Laurent Imbert for stealing their thunder, I attached a patch to #2362 which fixes that bug and this bug.


---

Comment by mabshoff created at 2008-04-03 19:25:33

Resolution: fixed


---

Comment by mabshoff created at 2008-04-03 19:25:33

As Joel pointed out in IRC this ticket can be closed as fixed since his patches at #2363 [that have been merged] fix the issue.

Cheers,

Michael
