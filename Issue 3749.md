# Issue 3749: Request for a method "is_cyclic" for groups in SAGE

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-07-31 14:01:47

Assignee: joyner

It appears that there is no method is_cyclic for groups in SAGE; this is a command that MAGMA does have, and one which I think is fairly basic. It would be nice if this was included in a version of SAGE.


---

Comment by mabshoff created at 2008-07-31 14:03:23

Please remember to assign a default milestone.

Cheers,

Michael


---

Comment by wdj created at 2008-07-31 14:09:20

It's there:


```
sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
sage: G.is_cyclic()
False
sage:        
```



---

Comment by ljpk created at 2008-07-31 15:22:52

It isn't there for AbelianGroup:


```
F = AbelianGroup(3,[2]*3)
F.is_cyclic()
```


gives


```
Traceback (click to the left for traceback)
...
AttributeError: 'AbelianGroup_class' object has no attribute 'is_cyclic'
```



---

Comment by wdj created at 2008-07-31 16:07:50

I could easily create one (and I'd be happy to) but I am concerned with interfering with David Roe's rewrite of the AbelianGroup class. One way to do it (which might break with the new class) is to just look at the invariants. The other way, which is probably unbreakable (though slower, especially for larger groups) is to convert to a permutation group (using the permutation_group method in the AbelianGroup class) and then apply is_cyclic. 
I'd prefer hearing comments from others before going ahead with one of these.


---

Comment by was created at 2008-12-11 06:01:55

Don't worry about what David Roe is doing -- this ticket has been idle for nearly 6 months.    And definitely *DON'T* convert to a permutation group -- that's crazy -- you should use the invariants.


---

Attachment

based on 3.2.2.alpha1


---

Comment by wdj created at 2008-12-11 13:36:19

The attached patch passes sage -t and seems to do the job.


---

Comment by was created at 2008-12-11 23:05:26

REFEREE REPORT:

This implementation is wrong and inefficient.

1. Wrong -- the group Z/2 + Z/4 is cyclic.

```
sage: AbelianGroup([2,4]).is_cyclic()
True
```



2. Inefficient -- even if it were right, the actual way it is coded is inefficient, since once you find a duplicate you would be done.  No need to iterate through the whole loop then check a flag at the end.


---

I just noticed that the function elementary_divisors on finite abelian groups isn't documented, in that it doesn't say what it does.   Since it could be ambiguous I wish it were documented. 

I think A.is_cyclic() should be true if and only if every element of the output of elementary_divisors is coprime.  Given that factoring prime powers is fast, the following should be a reasonable is_cyclic function (and it's only 2 lines!):

```
sage: def is_cyclic(A):
    v = [a.factor()[0][0] if a else 0 for a in A.elementary_divisors()]
    return len(v) == len(set(v))
```


This works on finite groups:

```
sage: is_cyclic(AbelianGroup([3,5]))
True
sage: is_cyclic(AbelianGroup([2,4]))
False
sage: is_cyclic(AbelianGroup([2,2]))
False
sage: is_cyclic(AbelianGroup([6]))
True
sage: is_cyclic(AbelianGroup([15,1,21]))
False
```


This fails on infinite groups since the function elementary_divisors itself has a bug on infinite groups!

```
sage: AbelianGroup([0,5]).elementary_divisors()
...
ArithmeticError: Prime factorization of 0 not defined.
```


I think the above should return [0,5].

That said, it is disturbing that elementary_divisors isn't documented, and moreover the choice of definition is inconsistent with the one for matrices over ZZ (made by pari, actually):

```
sage: a = matrix(ZZ, 3, [0,0,0, 0,5,0, 0,0,3]) ; a
[0 0 0]
[0 5 0]
[0 0 3]
sage: a.elementary_divisors()
[1, 15, 0]
sage: AbelianGroup([5,3]).elementary_divisors()
[3, 5]
```


So elementary_divisors for matrices gives invariants d_i where d_1 | d_2 | ..., 
With that choice of elementary divisors definition, the is_cyclic function would be easy:

```
def is_cyclic(A):
    return len(A.elementary_divisors()) <= 1
```


I think the elementary_divisors function for abelian groups could be "cheesily" fixed for now by just defining things in terms of matrices:

```
sage: def elementary_divisors(A):
....:     v = A.invariants()
....:     return diagonal_matrix(ZZ,v).elementary_divisors()
....: 
sage: elementary_divisors(AbelianGroup([5,3]))
[1, 15]
sage: elementary_divisors(AbelianGroup([0,0,5,3]))
[1, 15, 0, 0]
```

This obviously sucks because of the waste of memory (a matrix takes more), but is good because at least it is definitely *correct* and consistent, and I think correct and consistent is more important than speed.  We can fix the speed later once this consistency is established and tested. 

Summary: 
1. Change elementary_divisors to use matrices for consistency and correctness, and fix all corresponding doctests.

2. Change is_cyclic to just be "len(self.elementary_divisors()) <= 1", and add much better doctests for is_cyclic, e.g, testing infinite groups and Z/2 x Z/3, etc.


---

Comment by was created at 2008-12-11 23:20:54

Robert Miller points that there is an easy algorithm for computing the elementary divisors d1, d2, d3, of a finite abelian group, where elementary divisors means d1 | d2 | d3 | ...

Just factor the numbers a_i that define the abelian group.  Then the biggest d_i is the product of the maximum prime powers dividing some a_j.  I.e., d_i is the product of p^v, where v = max(ord_p(a_j) for all j).  Then divide out all those p^v's, and repeat to compute d_{i-1}.


---

Attachment

Apply other patch first. Based on 3.2.2.alpha1


---

Comment by wdj created at 2008-12-12 02:10:51

Followed instructions almost to the letter. (I think the code for 


```
def elementary_divisors...
```


given above needed a minor change.) Passes sage -t. I will report problems with sage -testall. (This takes a long time on my machine ubuntu 8.10 machine currently.) Hope it is okay to post the patch first.


---

Comment by was created at 2008-12-12 17:37:29

* Is this statement that is in the docs still true? "Thus we see that the "invariants" are not the invariant factors but the "elementary divisors" (in the terminology of Rotman [R])."

 * It doesn't make sense to include in the docs that paragraph about how to compute the elementary divisors, because we didn't implement that algorithm.  It would make sense to include that paragraph as a comment and say -- when somebody wants to speed this code up, please implement this algorithm.

 * Is this actually necessary:

```
 	665	        if 1 in edivs: 
 	666	            edivs.remove(1) 
```

Since I think that the only possible way 1 can be in evids is if evids = [1], in which case the group is trivial, hence cyclic.


---

Comment by wdj created at 2008-12-12 23:28:59

In reply to 


```
Is this actually necessary:

 	665	        if 1 in edivs: 
 	666	            edivs.remove(1) 
```


As elementary_divisors is implemented:


```
sage: J = AbelianGroup([2,3])
sage: J.invariants()
[2, 3]
sage: J.elementary_divisors()
[1, 6]
```


But we probably should have 

```
sage: J = AbelianGroup([2,3])
sage: J.invariants()
[2, 3]
sage: J.elementary_divisors()
[6]
```


since you want the elementary divisor of AbelianGroup([2,3]) to be the same as that of AbelianGroup([6]). 

I'll try to fix this too.


---

Comment by wdj created at 2008-12-12 23:51:20

The others should be applied first. Based on 3.2.2.alpha1


---

Attachment

I think this last patch fixes things the way you suggested. Also, both abelian_groups.py and dual_abelian_groups.py pass sage -t now.


---

Comment by cremona created at 2009-01-18 18:14:15

Review:   I have been avoiding reviewing this for ages since I hate the whole abelian groups code so much that every time I look at it I want to rewrite it from scratch, but am never going to have the time.  But that is silly.

This code (after applying all three patches in succession to 3.2.3) gives correct answers now for both elementary_divisors() and is_cyclic(), as far as I can see.  So it can pass.


---

Comment by mabshoff created at 2009-01-19 06:28:32

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 06:28:32

Merged all three patches in Sage 3.3.alpha0
