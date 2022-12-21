# Issue 1691: [with patch] old bug in pari.gen __setitem__ code

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-01-05 08:53:04

Assignee: craigcitro

CC:  craigcitro@gmail.com carl.witty@gmail.com

There's an old bug in the __setitem__ code for pari gen objects:


```
x = pari("[[1,2],3]") ; x[0][0] = 500 ; x
```


would give you back a list with nonsense where the 500 should go. The issue was a memory management one. In general, whenever a pari GEN is allocated, if we want it to be preserved, there ultimately has to be *some* python object pointing to it somewhere. What would happen in this case is that x[0][0] = 500 became x.__getitem__(0).__setitem__(0,500), and the return value from x.__getitem__(0) would store a pointer to the GEN containing 500. However, after the __setitem__ was finished, the object returned by __getitem__ was deallocated, and thus our GEN no longer had any python object pointing to it, and it was itself deallocated. 

So, ultimately, we need to do a bit more memory management. Here's the fix I implemented (which came out of some conversation with Carl Witty during Bug Day ... 7?), and which is really just a more complete version of something already in place. Namely, pari gens sometimes have a _refers_to dictionary, which in the case of a t_VEC or t_MAT, stores references to the gens pointing to the GENs stored there. I've mostly just beefed up this system. 

I added two new fields, _GEN_owner and _owner_set. The idea is this: any time you create a gen that's not the only gen pointing to its GEN, we need to make sure that everyone knows when that GEN gets updated. So when we create a gen that's not the unique one pointing to its GEN, we set its _owner_set to 1, and _GEN_owner to the other gen pointing to its GEN. 

Since that reads like something out of "Who's on First," let's give an example: we'll pretend for a moment that _owner_set, _GEN_owner, and _refers_to are def'd instead of cdef'd, and give a mock sage session explaining an example:


```
sage: x = pari([0,1,2])
sage: x._owner_set
0
sage: x._refers_to
{0: 0, 1: 1, 2: 2}
sage: y = pari([3,4])
sage: y._owner_set 
0
sage: x[0] = y ; x
[[3, 4], 1, 2]
sage: x[0]._owner_set
1
sage: x[0] is y
False
sage: x[0]._GEN_owner is y
True
sage: x[0][0] = 123 ; x
[[123, 4], 1, 2]
sage: y
[123, 4]
```


So this does what we want. There's one somewhat frustrating thing that can happen, though. In the above example, we're allocating each element of the list, so our _refers_to gets set just as we'd like. However, it's possible that not every GEN has a gen pointing to it. That is:


```
sage: x = pari("[[1,2],3,4]") ; x._refers_to
{}
```


This is annoying for us -- it means that we don't have our reference tracking working with such an object until the user tries to refer to a piece of it. So, when you try to create a new_ref to an object, and it's never been referenced before, we first make and store a reference to it as we would have done at allocation.

While I was doing this, I sped up pari coercion a bit here and there ... here's two examples:

Before:

```
sage: ls = [2,3]

sage: time for _ in range(100000): x = pari(ls)
CPU times: user 4.84 s, sys: 1.05 s, total: 5.89 s
Wall time: 6.40

sage: foo = True

sage: time for _ in range(100000): x = pari(foo)
CPU times: user 1.25 s, sys: 0.01 s, total: 1.26 s
Wall time: 1.35
```


After:

```
sage: ls = [2,3]

sage: time for _ in range(100000): x = pari(ls)
CPU times: user 2.56 s, sys: 0.89 s, total: 3.45 s
Wall time: 3.90

sage: foo = True

sage: time for _ in range(100000): x = pari(foo)
CPU times: user 0.73 s, sys: 0.01 s, total: 0.73 s
Wall time: 0.80
```





---

Comment by craigcitro created at 2008-01-05 09:00:40

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2008-01-06 05:28:36

I think I understand what this patch is doing.  It seems excessively complicated and possibly broken.

1) Sometimes _GEN_owner refers to another gen with the same value as self; sometimes it refers to another gen (a matrix or vector) such that self is an element of _GEN_owner.  This is quite confusing.

I think the latter case is the only important case; then _GEN_owner should be renamed to _GEN_parent.

In the former case, instead of creating multiple gen elements with the same value, and setting _GEN_owner, it should just use the original gen.  So:

```
                    return P.new_ref((<gen>x).g,x)
```

would become

```
                    return x
```


2) There need to be more comments describing these fields.

3) (less important): It seems that ._owner_set is true iff ._GEN_owner is not None; I recommend removing this field and just checking ._GEN_owner (or, in the rewritten patch, ._GEN_parent), to save memory at a (probably) negligible cost in time.


---

Comment by craigcitro created at 2008-01-14 12:46:21

I've completely thrown out the old patch and written a new fix for this. I was talking this through with Robert Bradshaw, and he pointed out that since so much of the trouble comes from lots of references to the same GEN, why not get rid of that? That is, we now demand that the following general rule is true: there is at most one sage gen pointing to any given Pari GEN. There are still multiple gens pointing to the parts of a single GEN (i.e. x[0], x[1], etc), but never to the same GEN. This greatly simplifies things, and the code seems to work well. All the timings above are still valid with the new patch.

I also changed forcecopy to gcopy in gen.pyx, and commented out forcecopy in decl.pxi. It turns out that forcecopy is deprecated, and isn't even mentioned in the Pari manual anymore, and gcopy replaces it. In fact, looking at the Pari sources we ship with 2.9.3, forcecopy is declared by #define forcecopy gcopy, so there's no reason to have it around anyway, since it will likely disappear completely from Pari at some point.

I am running a -testall overnight, so I can't guarantee there are no doctest failures, but the rings/ directory and libs/pari/ both doctest clean, which is a good start. I'll fix any doctest failures I find tomorrow.


---

Attachment


---

Comment by cwitty created at 2008-01-15 03:14:14

Looks good to me!  (patch looks good, testall passes)

Apply only 1691v2.patch.


---

Comment by mabshoff created at 2008-01-15 03:19:44

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 03:19:44

1691v2.patch only merged in Sage 2.10.alpha3
