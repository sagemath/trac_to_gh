# Issue 7420: Fix uncaught infinite loop in coercion discovery

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-11-10 00:45:07

Assignee: mhansen

CC:  sage-combinat robertwb

Keywords: coercion

#5597 or #5598 introduced a potential infinite loop (and segfault) upon coercion discovery on a cyclic graph. The first occurence of such a graph was with the newly refactored symmetric functions.

The attached patch fixes this. By the way, it uses a dictionary rather than a list to hold the marks used (register_pair) to detect cycles.

The category patches #5981 depend on this!!!


---

Attachment


---

Comment by nthiery created at 2009-11-10 00:50:38

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-11-10 00:50:38

I reviewed the change, and it looks good.

Robert: please double check; I don't guarantee that all the invariants are preserved.


---

Comment by mhansen created at 2009-11-10 05:36:52

Another option is to wrap that coerce_map_from call in a _register_pair try/except block.


---

Comment by robertwb created at 2009-11-10 07:08:06

Yes, calling _register_pair would work here, even a helper is_registered function might be better than using _coerce_test_dict directly. 

Also, instead of 


```
                connection = None 
                if EltPair(mor._domain, S, "coerce") not in _coerce_test_dict: 
                    connecting = mor._domain.coerce_map_from(S)
                if connecting is not None: 
```


it might be clearer to do 


```
                if EltPair(mor._domain, S, "coerce") not in _coerce_test_dict: 
                    connecting = mor._domain.coerce_map_from(S)
                    if connecting is not None: 
                        ...

```



---

Comment by nthiery created at 2009-11-11 08:29:12

This is a variant of the previous patch, using register_pair


---

Attachment

Replying to [comment:3 robertwb]:
> Yes, calling _register_pair would work here

I gave it a shot, and this works almost fine: all sage tests pass; except that for jack polynomials. Looking at it, it appears that the coercion model is picking a path which is *really* far from the shortest (see the attached log). The previous version was doing reasonably. This sounds like a pure piece of luck though, since in both cases, the strategy seems to be depth first search + limited selection among the first conversions found.

Robert, Mike: from here, I see two options:
 - Either you spot something stupid I did in the second version of the patch, and then we go for it after fixing it.
 - Or we go for the first version of the patch for the moment (after applying Robert's suggestion for better indentation)

In both cases, after the category patches are in, we should definitely rewrite the coercion lookup to use a breath first search.


---

Attachment

Log showing a *long* conversion path


---

Comment by nthiery created at 2009-11-11 08:51:41

I should mention: the error appearing in the log comes from the having the coercion go through
jack polynomials at t=-1; apparently, the scalar product is then non positive, which causes the error. I have to check the literature. Maybe we should forbid t=-1, or at least not declare the corresponding broken coercions.


---

Comment by mhansen created at 2009-11-13 04:48:52

I'm going to move this to 4.3 where it's more relevant.


---

Comment by robertwb created at 2009-11-14 07:27:20

I'd say at this point go for the first version of the patch, but with an eye towards improving things in the multiple paths case. (A breath first search sounds like a good idea, but could be more expensive if paths "all the way down" have already been explored. Also, there's the notion of assigning a cost to a morphism which has not been exploited.)


---

Comment by mhansen created at 2009-11-17 05:27:55

I'll merge the first patch, and then look into a better solution.


---

Comment by mhansen created at 2009-11-17 05:27:55

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 05:42:30

Resolution: fixed
