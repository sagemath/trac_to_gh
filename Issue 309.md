# Issue 309: rationals enumeration not  monotone in height.

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-03-05 18:37:50

Assignee: somebody

While the new `Rationals().__iter__ method` is really nice and quick, I realized there is one drawback: The enumeration is not completely wrt increasing height:


```
from itertools import islice,imap

def idifference(iter):
    B = iter.next()
    for b in iter:
      yield b-B
      B=b

def height(x):
  return x.height()

[(n,min(idifference(imap(height,islice(Rationals(),Integer(2)**n))))) for n in range(Integer(1),Integer(19))]
```


yields


```
[(1, 0),
 (2, 0),
 (3, 0),
 (4, 0),
 (5, -1),
 (6, -2),
 (7, -3),
 (8, -5),
 (9, -8),
 (10, -13),
 (11, -21),
 (12, -34),
 (13, -55),
 (14, -89),
 (15, -144),
 (16, -233),
 (17, -377),
 (18, -610)]
```


so the jumps in height actually do get big. Many people will expect that if a certain number occurs in the enumeration, then all numbers of smaller height have also appeared. Therefore, we should perhaps have a choice of algorithm (since the present formula (sage 2.2) is so cool, I think it should be left in, but perhaps not as default enumeration order).

On the other hand, I realize that nobody will be using this routine anyway, so any change to this routine is essentially a waste of time.



---

Comment by AlexGhitza created at 2008-09-01 05:35:09

As a thought experiment, I implemented the naive algorithm for enumerating the rationals according to the height.  To my surprise, it seems to have the same speed as the version implemented by Nils (which is not monotone in height, hence this ticket -- see below for sample timings).  So I think we should just use the naive algorithm, which is in the attached patch.  It seemed a shame to throw out Nils' code so I just commented it out and fixed its references.

with old code:

```
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**4): a = lst.next()                               
CPU times: user 0.12 s, sys: 0.00 s, total: 0.12 s
Wall time: 0.12 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**5): a = lst.next()                               
CPU times: user 0.64 s, sys: 0.00 s, total: 0.64 s
Wall time: 0.64 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**6): a = lst.next()                               
CPU times: user 5.96 s, sys: 0.03 s, total: 5.99 s
Wall time: 5.99 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**7): a = lst.next()                               
CPU times: user 59.47 s, sys: 0.21 s, total: 59.68 s
Wall time: 59.68 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**8): a = lst.next()                               
CPU times: user 599.76 s, sys: 1.95 s, total: 601.71 s
Wall time: 601.92 s
```


with new code:

```
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**4): a = lst.next()                               
CPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**5): a = lst.next()                               
CPU times: user 0.64 s, sys: 0.01 s, total: 0.65 s
Wall time: 0.65 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**6): a = lst.next()                               
CPU times: user 5.88 s, sys: 0.06 s, total: 5.94 s
Wall time: 5.94 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**7): a = lst.next()                               
CPU times: user 58.68 s, sys: 0.58 s, total: 59.26 s
Wall time: 59.28 s
sage: lst = itertools.islice(Rationals(), 10**8)                               
sage: time for _ in range(10**8): a = lst.next()                               
CPU times: user 587.97 s, sys: 6.62 s, total: 594.59 s
Wall time: 594.65 s
```



---

Comment by AlexGhitza created at 2008-09-01 09:13:53

Changing assignee from somebody to AlexGhitza.


---

Comment by AlexGhitza created at 2008-09-01 10:03:36

Changing status from new to assigned.


---

Comment by cremona created at 2008-09-01 20:05:30

I prefer this, and would definitely want to use it in preference to the clever one.  In fact I do exactly the same thing somewhere in the modular symbols code in eclib...

It would be nice to make it easier for users to create iterators to (say) loop through all rationals up to a certain height, without having to resort to "import itertools" magic.  Something like this:

```
   for q in qrange(H):
       # do something with q
```

which would loop through all rationals of height <H.

Anyway, this patch applies fine to 3.1.2.alpha3, but doctesting rational_field.py threw up this for me:

```
File "/home/john/sage-3.1.2.alpha3/tmp/rational_field.py", line 287:
    sage: [a for a in itertools.islice(Rationals(),10)]
Expected:
    [0, 1, -1, 1/2, -1/2, 2, -2, 1/3, -1/3, 3/2]
Got:
    [0, 1, -1, 1/2, -1/2, 2, -2, 1/3, -1/3, 3]
```



---

Comment by AlexGhitza created at 2008-09-01 22:44:41

Thanks for looking at this, John.

I don't know enough about Python iterators at the moment to implement the more user-friendly version, but I do agree with you.

The doctest failure makes no sense, because if you look at the patch it clearly removes the line with the first 10 rationals and replaces it with the first 17 rationals.  Something must have gone wrong when you applied the patch?


---

Comment by mabshoff created at 2008-09-01 23:42:08

I applied and tested the patch with alpha3 on x86-64 linux and 32 bit OSX and cannot reproduce the failure? Maybe something went wrong with the merge as Alex suspected?

Cheers,

Michael


---

Attachment

mhansen gave me a crash course on iterators and I have implemented a method QQ.range_by_height().  John's request from above becomes then


```
sage: for q in QQ.range_by_height(3):                                          
....:     print q                                                              
....:                                                                          
0
1
-1
1/2
-1/2
2
-2
```


I have replaced the old patch with one that contains this method as well.


---

Comment by mabshoff created at 2008-09-02 03:51:58

With Alex's old patch I am actually seeing one doctest failure in interact:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha4$ ./sage -t -long devel/sage/sage/server/notebook/interact.py
sage -t -long devel/sage/sage/server/notebook/interact.py   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha4/tmp/interact.py", line 2556:
    sage: sage.server.notebook.interact.list_of_first_n(QQ, 10)
Expected:
    [0, 1, -1, 1/2, -1/2, 2, -2, 1/3, -1/3, 3/2, -3/2]
Got:
    [0, 1, -1, 1/2, -1/2, 2, -2, 1/3, -1/3, 3, -3]
**********************************************************************
```


I am trying the new patch now, but I expect the same result.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-02 04:25:11

With the new patch I get:

```
sage -t -long devel/sage/sage/server/notebook/interact.py   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha4/tmp/interact.py", line 2556:
    sage: sage.server.notebook.interact.list_of_first_n(QQ, 10)
Expected:
    [0, 1, -1, 1/2, -1/2, 2, -2, 1/3, -1/3, 3/2, -3/2]
Got:
    [0, 1, -1, 1/2, -1/2, 2, -2, 1/3, -1/3, 3, -3]
**********************************************************************
```


Cheers,

Michael


---

Attachment

apply on top of 309-rational_iter_height.patch and the patch from #4037


---

Comment by AlexGhitza created at 2008-09-02 04:53:26

The doctest in interact.py needs a trivial fix.  The second patch file puts this in, but it has to be applied after the patch from #4037.


---

Comment by cremona created at 2008-09-02 08:28:29

Brilliant!   I'm impressed with the way my suggested enhancement was added so well and so quickly!

I successfully applied both patches after the one from #4037, which also has a positive review, and everything works fine.


---

Comment by mabshoff created at 2008-09-02 09:36:42

Resolution: fixed


---

Comment by mabshoff created at 2008-09-02 09:36:42

Merged both patches in Sage 3.1.2.alpha4
