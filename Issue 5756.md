# Issue 5756: improve coverage of rings/morphism.pyx

Issue created by migration from https://trac.sagemath.org/ticket/5756

Original creator: was

Original creation time: 2009-04-11 17:24:57

Assignee: mabshoff

CC:  robertwb




---

Comment by was created at 2009-04-11 21:10:09

BUGS FOUND:

1. bug in __cmp__

```
10:56 < wstein-5756> Wow, I was reading the __cmp__ for ring lifting maps.
10:56 < wstein-5756> Check out this bug:
10:56 < wstein-5756> Zmod(8).lift() == Zmod(10).lift()
10:56 < wstein-5756> True
10:56 < wstein-5756> Any two lifting maps are always equal.
10:56 < wstein-5756> Ouch.
```


2. Another bug related to __cmp__:   #5758 (weird "hello")

3. __nonzero__ is wrong for ring morphisms, since Sage does have the 0 ring where 0 == 1, so this code was wrong:

```
    def __nonzero__(self):
        return True
```


4. Calling .lift() on a morphism returns None.  This is a bug that was caused by cythonizing morphism.pyx:

```
sage: R.<x,y> = QQ[]; R.hom([x,x]).lift() is None
True
```



---

Comment by was created at 2009-04-11 23:28:37

BUGS FOUND:
5. im_gens() returns a mutable list, which makes it trivial to *break* a morphism after it is created:

```
sage: R.<x,y> = QQ[]
sage: f = R.hom([x,x+y])
sage: f(x)
x
sage: f.im_gens()[0] = 5
sage: f.im_gens()
[5, x + y]
sage: f(x)
5
```



---

Attachment


---

Comment by cremona created at 2009-04-12 11:07:36

Starting to review this, which is in itself non-trivial!

There is some strange terminology here.  I'm not sure what a "Set-theoretic ring endomorphism of Integer Ring" is meant to be, let alone a "set-theoretic ring".  I think that what is meant is (in the first case) a map between rings which is not a ring homomorphism, such as a section of a surjective map.

Also the term "lift" is used for such a section, i.e. if f:R-->S is the surjective ring hom and h:S-->R is a section (so f(h(s))==s for all s in S) then the map h is being called a lift, where I would say that the element h(s) is a lift of s.  And "cover"?   Here R is being called a cover of S?

I think it would be helpful if somewhere in this file this terminology is defined since not all of it is so standard...

A more proper review will follow.


---

Comment by mabshoff created at 2009-04-15 03:58:40

Robert: In case you are reviewing this - all doctest in my rc3 merge tree with this patch applied pass.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-15 23:06:58

I agree that the notation could be made more consistent, but this patch simply documents what is there (which is good) and fixes some bugs. 

One thing I noticed, which is not just common to this patch, is that when we return a list that we don't want people to change (e.g. im_gens) we (hopefully) make a copy. This is why tuples were invited, shouldn't we just be using those instead?


---

Comment by mabshoff created at 2009-04-16 02:47:45

Replying to [comment:6 robertwb]:
> I agree that the notation could be made more consistent, but this patch simply documents what is there (which is good) and fixes some bugs. 

Yeah, getting it in should be the main goal here and now.

> One thing I noticed, which is not just common to this patch, is that when we return a list that we don't want people to change (e.g. im_gens) we (hopefully) make a copy. This is why tuples were invited, shouldn't we just be using those instead?

*implemented_ instead of *invited_' I assume? 

Either way, can you please open a followup ticket so that this doesn't get lost.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 02:54:51

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 02:54:51

Resolution: fixed


---

Comment by robertwb created at 2009-04-16 07:22:20

I meant invented...

Followup at #5802, perhaps there should be a followup to John Cremona's comments as well.
