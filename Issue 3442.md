# Issue 3442: is_normal for permutation groups gives wrong answer

Issue created by migration from https://trac.sagemath.org/ticket/3442

Original creator: wjp

Original creation time: 2008-06-16 22:37:41

Assignee: joyner

The example in the docstring for `is_normal` in `sage/groups/perm_gps/permgroup.py` in sage-3.0.3.alpha2 is wrong.


```

        Return True if the group self is a normal subgroup of other.

        EXAMPLES:
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_normal(H)
            True
```


(Aside: isn't it more natural to let H be a subgroup of G instead of the other way around?)

G is not a normal subgroup of H since conjugation by (1,2,3,4,5) does not map G to G.

Other example:

```
sage: G = SymmetricGroup(3); G.1
(1,2)
sage: H = G.subgroup( [ G.1 ] )
sage: H.is_normal(G)
True
```



---

Comment by wdj created at 2008-06-16 23:31:07

Yes, the documentation is wrong (the function is okay). My fault. Sorry.


```
gap> G := Group([(1,2,3)(4,5)]);
Group([ (1,2,3)(4,5) ])
gap> H := Group([(1,2,3)(4,5), (1,2,3,4,5)]);
Group([ (1,2,3)(4,5), (1,2,3,4,5) ])
gap> IsNormal(H,G);
false
```

The docstring should read


```
Return True if the group other is a normal subgroup of self.

EXAMPLES: 
    sage: G = PermutationGroup(['(1,2,3)(4,5)'])
    sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
    sage: H.is_normal(G)
    False
```



---

Comment by wdj created at 2008-06-17 17:40:12

docstring patch bases on 3.0.3.rc0


---

Attachment

A patch for this docstring error is posted which is based on sage-3.0.3.rc0. 

Install and sage -testall passed for sage-3.0.3.rc0. Also, this patch passed using sage -t. However, running sage -testall on this patch resulted in a lock-up on padic_lseries.py. I'll try again but think this is an unrelated issue.

I could create another patch which does reordering of the methods alphabetically (as was done earlier). However, it seems I'm the only one who cares, so unless someone yells, I'll drop that idea.


---

Comment by wdj created at 2008-06-17 19:55:42

I reran sage -testall and all tests passed on this patch.


---

Comment by wjp created at 2008-06-17 21:09:30

Wouldn't not changing the function itself mean that now is_normal claims that S_5 is normal in `< (1,2,3)(4,5) >`, even though it isn't even a subgroup?


---

Comment by wdj created at 2008-06-17 23:26:02

According to the GAP documentation for the function IsNormal (which is what is_normal wraps):


```
IsNormal( G, U ) O

returns true if the group G normalizes the group U and false otherwise.

A group G normalizes a group U if and only if for every g ∈ G and u ∈ U the element ug is a member of U. Note that U need not be a subgroup of G. 
```


So the docstring, as corrected in the patch, is correct but does not tell the full story. Do you think it should be further elaborated?


---

Comment by wjp created at 2008-06-19 07:26:09

I think naming the current function '`normalizes`' would be better. A new `is_normal` function could then check if 'self' is a normal subgroup of 'other' (by doing `self.is_subgroup(other) and other.normalizes(self)` ?). This would be more consistent with how `is_subgroup`, `is_subring`, `is_subspace` order their arguments, IMO.


---

Comment by wdj created at 2008-06-19 11:05:33

again, based on 3.0.3.rc0. Should be applied after 9860.


---

Attachment

Done. Please apply 9860 then 9861 to sage-3.0.3.rc0 to get the behavior you requested.


---

Comment by craigcitro created at 2008-06-20 05:06:04

Changing keywords from "" to "editor_mhansen".


---

Attachment


---

Comment by wjp created at 2008-06-20 19:19:29

I've added a third patch (apply after 9860 and 9861) that swaps the arguments to `is_normal`.

It makes `H.is_normal(G)` mean: H is a normal subgroup of G.

(This is consistent with functions like `is_subgroup`, `is_subspace`.)


---

Comment by malb created at 2008-07-02 20:42:10

I give the last patch a positive review, wjp gave the prior patches a positive review -> *positive review*.


---

Comment by mabshoff created at 2008-07-03 03:24:23

Merged all three patches in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-03 03:24:23

Resolution: fixed
