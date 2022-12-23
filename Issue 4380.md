# Issue 4380: Memory Leak in libsingular

Issue created by migration from https://trac.sagemath.org/ticket/4380

Original creator: SimonKing

Original creation time: 2008-10-29 09:27:48

Assignee: malb

Keywords: memory leak libsingular

At http://groups.google.com/group/sage-support/browse_thread/thread/b997f95c1e2503e0/5db5f9e7d4c8faf2 was discussion about a memory leak. I found a reasonably short bit of code that triggers the leak.

In `test.pyx`:

```
from sage.all import copy

def Test(I):
    R=I.ring()
    p=R.random_element()
    J0=list(I.reduced_basis())
    while(1):
        J = copy(J0)
        for i in range(100):
            q=p.reduce(J)
            J.append(q)
```


Apparently the memory consumption should not grow, since `J` returns to its original state after finishing the `for` loop. However, the following `Sage` session is leaking (i.e., the memory consumption grows rapidly, and after a few seconds 1GB are filled up):

```
sage: attach test.pyx
Compiling /home/king/Projekte/f5/test.pyx...
sage: from sage.rings.ideal import Cyclic
sage: R=PolynomialRing(QQ,'x',5)
sage: I=Cyclic(R).homogenize()
sage: Test(I)
```


The `while` loop comprises
 1. copying of a Sequence (`J0`) of `MPolynomial_libsingular`
 2. reduction of `MPolynomial_libsingular`
 3. appending to a Sequence.

In one of these three steps must be the leak. I suspect it is the reduction and will try to verify it.



---

Comment by SimonKing created at 2008-10-29 09:30:02

Sorry, it is not copying a _Sequence_ but a _list_. But that shouldn't matter.


---

Comment by SimonKing created at 2008-10-29 10:33:46

... and the line `J.append(q)` (that would occur, e.g., in a Groebner basis computation) is not needed either. Replacing `Test(I)` by the following code triggers the leak as well:


```
def Test(I):
    R=I.ring()
    p=R.random_element()
    J=list(I.reduced_basis())
    while(1):
        q=p.reduce(J)
```



---

Comment by SimonKing created at 2008-10-29 11:24:54

The patch `libsingularLeak.patch` partially solves the problem.

I observed that when a coercion error occurs an intermediately generated ideal `_I` is explicitly destroyed with `id_Delete(&_I,r)`. But when there is no error and the result is returned, then `_I` is not deleted. But I think it should.

With the patch, the above `Test(I)` still shows an increase of memory, but a rather moderate increase. So, it seems to be a partial solution of the problem, but more needs to be done.


---

Comment by mabshoff created at 2008-10-29 11:30:11

Simon,

nice work. If you find any more issues please open a new ticket, so that this patch can be merged. I will review this patch shortly.

Cheers,

Michael


---

Attachment

Fixing the leak, after a suggestion of malb


---

Comment by SimonKing created at 2008-10-29 12:16:58

Since the announced review of Michael didn't come yet, I hope it is ok that I changed the patch according to a suggestion of malb, without opening a new ticket. 

The new patch seems to fix it completely.


---

Comment by mabshoff created at 2008-10-29 12:18:35

Replying to [comment:5 SimonKing]:
> Since the announced review of Michael didn't come yet, I hope it is ok that I changed the patch according to a suggestion of malb, without opening a new ticket. 

Yep, I am testing that patch now.

> The new patch seems to fix it completely.

:)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-29 12:22:12

This patch also seems to fix the problem with sr.py consuming vast amounts of memory, but I will do some independent testing first.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-29 12:47:48

Replying to [comment:7 mabshoff]:
> This patch also seems to fix the problem with sr.py consuming vast amounts of memory, but I will do some independent testing first.

Unfortunately it doesn't fix the segfault (see #3758), but the amount of memory allocated goes down significantly already.

> Cheers,
> 
> Michael

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-29 12:55:51

Valgrinds clean, passes doctests, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-29 12:56:49

Resolution: fixed


---

Comment by mabshoff created at 2008-10-29 12:56:49

Merged in Sage 3.2alpha2
