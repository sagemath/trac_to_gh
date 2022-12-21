# Issue 2460: some issues with factorization.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-10 16:02:43

Assignee: somebody

Various people worked on factorization.py and unfortunately ignored some implicit 
assumptions in what that code is supposed to do.  In particular, this function

```
    def base_ring(self):
        if len(self) > 0:
            return self[0][0].parent()
        else:
            return self.unit().parent()
```

assumes that (1) ever element has the same parent, and (2) the parent is a ring.
Neither assumption need be satisfied.   

This is_commutative function then relies on base_ring working.  
Here's an example of this leading to *wrong* answers:

```
sage: R.<x,y> = FreeAlgebra(QQ,2)
sage: Factorization([(3,1), (x,2), (y,3), (x,1), (y,2)])
3 * x^3 * y^5
```


Proposal: Simply call Sequence on the list of bases in the factorization
to get a new list where the basis lie in a common university.  Then refine
is_commutative to mean that the universe is a commuative ring, and only then
commute factors automatically.

Second, after the above is resolved, the sort function for comparison 
should call universe() (not base_ring) and use some sensible defaults,
before resorting to that mess of code in the current sort method. 




---

Comment by was created at 2008-03-10 16:10:24

Changing status from new to assigned.


---

Comment by was created at 2008-03-10 16:10:24

Changing assignee from somebody to was.


---

Comment by gfurnish created at 2008-03-10 16:22:25

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-10 16:22:25

Changing status from assigned to new.


---

Comment by gfurnish created at 2008-03-10 16:22:34

Changing status from new to assigned.


---

Attachment


---

Comment by gfurnish created at 2008-03-10 16:33:57

There is a possibility that fixing commutativity may other things.


---

Comment by gfurnish created at 2008-03-10 17:12:58

Changing assignee from gfurnish to was.


---

Comment by gfurnish created at 2008-03-10 17:12:58

Changing status from assigned to new.


---

Comment by gfurnish created at 2008-03-10 17:12:58

There are non-trivial issues involved with fixing this (namely, moving things to the universe causes issues with repr and commutes, and I can't find a way to fix those issues without refactoring other code to make this work well, so this should probably see some discussion.


---

Comment by craigcitro created at 2008-06-20 04:46:32

Resolution: invalid


---

Comment by mabshoff created at 2008-06-23 05:56:22

Hi Carig,

not to be prickly Pete, but can give a reason why this was invalidated?

Cheers,

Michael


---

Comment by was created at 2008-06-27 20:20:25

Resolution changed from invalid to 


---

Comment by was created at 2008-06-27 20:20:25

Changing status from closed to reopened.


---

Comment by was created at 2008-06-27 20:20:25

Woah -- I incorrectly thought this had long since been fixed.  NOT.

```
sage: R.<x,y> = FreeAlgebra(QQ,2)
sage: sage: Factorization([(3,1), (x,2), (y,3), (x,1), (y,2)])
3 * x^3 * y^5
```



---

Comment by mabshoff created at 2008-07-03 07:08:33

Ok, moving this back to a current milestone so that it can be seen :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 11:02:33

William, 

can you be the editor of this patch? Feel free to bounce it back to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 11:02:33

Changing keywords from "" to "editor_wstein".


---

Comment by cremona created at 2008-08-22 17:35:50

Looking at factorization.py I was all ready to fix all the problems I could see -- using Sequence to get a common universe for the bases on construction, cache this base_ring, only allow operations between factorizations with the same base_ring, and so on.

But then I saw what appeared to be a totally weird example:


```
sage: F = Factorization([(ZZ^3, 2), (ZZ^2, 5)], cr=True); F
(Ambient free module of rank 2 over the principal ideal domain Integer Ring)^5 * 
(Ambient free module of rank 3 over the principal ideal domain Integer Ring)^2            
```

This bears no relation at all to what I thought the Factorization class was for.  Doing a search_src showed that this is designed in to support splitting of modular symbols spaces (and similar).

This leaves a question almost certainly for William:  is it really sensible to have one class serve both as the structure to hold "prime factorizations" for UFDs and other rings, as well as to hold lists of subspaces with multiplicities?

If so, perhaps we need to refactor this to have a base class which just handles the basics, with (at least) 2 derived classes, one for rings factorizations and one for additive decompositions?

John

# I have added this posting to trac#2460 too.


---

Comment by cremona created at 2008-08-23 16:09:43

I think the issues raised here have all been dealt with by the patches I put up at #3927 (which started out as a separate enhancement, hence the new ticket).  In particular the good parts of the patch attached to this ticket have been used there.

I suggest that this ticket be closed, with a link to #3927 instead.


---

Comment by mhansen created at 2008-11-14 08:52:38

Resolution: fixed


---

Comment by mhansen created at 2008-11-14 08:52:38

I think that this can be closed as well due to #3927.
