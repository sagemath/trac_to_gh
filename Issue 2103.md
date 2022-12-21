# Issue 2103: equivalence classes of cusps for congruence subgroups

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-02-08 07:46:52

Assignee: was

CC:  alexghitza craigcitro cremona m.t.aranes@warwick.ac.uk

Given a congruence subgroup G, return a list of representatives for the G-equivalence classes of cusps.

Sample wished-for session:


```
sage: C = Cusps
sage: G = Gamma0(5)
sage: C(G)
[Infinity, 0]
```




---

Comment by davidloeffler created at 2008-09-21 18:27:34

I'd also like this. I'll have a go at it.


---

Comment by davidloeffler created at 2008-09-21 18:27:34

Changing assignee from was to davidloeffler.


---

Attachment

patch against 3.1.2


---

Comment by davidloeffler created at 2008-09-22 19:28:48

The above patch adds a cusps() method for all congruence subgroups; this accepts an optional boolean keyword argument "bdmap". 

If "bdmap" is true, then the method creates the space of modular symbols for the congruence subgroup and calls the .cusps() method on this, which triggers computation of the boundary map; the existing code for computing the boundary map also gives the set of cusps as a side-effect. They aren't computed in reduced form, though, so we reduce them and pass them back to the user.

If "bdmap" is false (the default), the method finds all cusps by directly calculating the appropriate list of rational numbers -- there are two hidden helper methods, one to do this for Gamma0 and another for Gamma1 and GammaH. This is *much* faster than computing the boundary map if N is large. 

I've also added a reduce_cusp method, which is essentially a wrapper around Craig Citro's _reduce_cusp method but throws away the extra output of a sign, since that's not so important
outside the specific context of modular symbol boundary maps.

In the course of fixing this, I've also made some other changes: I found that existing code gives
{{{ 
sage: Gamma1(11) == GammaH(11, [])
False
sage: Gamma0(11) == GammaH(11, [2])
False
}}}
despite the fact that in both cases the two groups are the same.

Hence I've adjusted things so that Gamma0 and Gamma1 inherit from GammaH, and use the GammaH __cmp__ methods. Things are now much more consistent, but there was a slight side-effect of breaking a doctest in abvar/abvar.py as the sort order of congruence subgroups has changed -- there is no way to avoid this, because at the moment we have the following: 

```
sage: Gamma1(11) < Gamma0(11)
False
sage: GammaH(11, []) < GammaH(11, [2])
True
```


I know that having cusps() as a method of congruence subgroups isn't the syntax originally proposed, but I don't like the idea of using Cusps_class.__call__(). If anyone feels strongly about this I'll happily add methods to Cusps_class so one can say

```
sage: Cusps.orbit_reps(Gamma1(11))
...
```

or whatever.


---

Comment by cremona created at 2008-09-23 11:33:00

I've added myself on the CC list for this.  My student Maite Aranes is in the process of implementing cusps for general number fields, by the way, but I have not yet made a ticket for it.


---

Comment by mvngu created at 2008-10-27 12:18:03

For the patch *2103.patch*, here's a possible fix for improving the documentation:



```
-Since Gamma0(N) always, contains the matrix -1, this always
+Since Gamma0(N) always contains the matrix -1, this always
```

After applying that diff, you'd get:

```
Return True precisely if this subgroup contains the matrix -1. 

Since Gamma0(N) always contains the matrix -1, this always 
returns True.
```



---

Comment by cremona created at 2008-10-27 12:50:51


```
applying /local/jec/2103.patch
patching file sage/modular/congroup.py
Hunk #3 FAILED at 589
1 out of 10 hunks FAILED -- saving rejects to file sage/modular/congroup.py.rej
abort: patch failed to apply
```


Same on both 3.1.4 and 3.2.apha0.  David, could you rebase this?  Then I'll review it.

While I'm here: am I right in thinking that there's quite a lot of code which is just moved from one place to another?  (Judging by the amount of red and blue I see when viewing the patch).

I certainly like the code from looking at it by eye but it needs to be able to be applied...

My guess is that the code for giving a complete set of cusp representatives is not very efficient, but I also think it unlikely that that function would be needed for large N anyway.  I never wrote down explicit representatives even for Gamma_0(N), but think that you should have all a/d where 0<d|N and a runs through invertible residues mod gcd(d,N/d) lifted to be coprime to d.


---

Attachment

rebased to 3.1.4 (also works in 3.2.alpha1)


---

Comment by davidloeffler created at 2008-10-28 11:22:17

It was conflicting with mhansen's changeset 10648, deprecating is_blah() functions. I've uploaded a new patch (also incorporating mvngu's docstring fix), which was created under 3.1.4 and seems to apply fine to 3.2.alpha1 as well.


---

Comment by davidloeffler created at 2008-10-28 11:22:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-28 17:33:28

FYI: With the patch applied against 3.2.alpha1+merges all doctests with -long pass.

A couple docstrings and doctests are missing for

 * def dimension_modular_forms_H(X, k=2) in line 1488 of sage/modular/dims.py
 * def dimension_modular_forms_H(X, k=2) in line 1534 of sage/modular/dims.py

Mathematically I am not qualified to review :)

Cheers,

Michael


---

Attachment


---

Comment by davidloeffler created at 2008-10-28 18:33:42

Oops! The same function appears twice in dims.py, with identical code both times -- that was silly of me. I have recreated the patch with only one copy of dimension_modular_forms_H, and added a doctest for it.


---

Comment by craigcitro created at 2008-10-28 20:05:00

Ok, I'm in the process of reviewing this -- I'll have it done in a little bit.


---

Attachment

This is an excellent patch. 

In addition to adding the requested functionality, this patch performs some long-needed cleanup to the class hierarchy in `congroup.py`. In particular, `Gamma0` and `Gamma1` now inherit from `GammaH`, as makes sense. I should note that it might be a good project for someone to look at the code in `congroup.py`, and see how much of the code for `Gamma0` and `Gamma1` could be moved up to/unified with code in `GammaH`. 

I've added a small patch to apply on top of `2103-new.patch` which cleans up a few things. Most of it is documentation touch-ups. I replaced the `__cmp__` methods for `Gamma0` and `Gamma1` which the original patch removed, and rewrote them to do comparison without ever generating the corresponding lists of elements. 

Someone should look over my additional patch, but after that, this is ready to go.


---

Comment by cremona created at 2008-10-29 09:51:40

Craig's additional patch looks good to me;  though I don't have time at the moment to check that everything works properly.


---

Comment by cremona created at 2008-10-29 12:05:30

1. Note that only the last two patches should be applied: 2103-new.patch and trac-2103-pt2.patch
    2. They apply cleanly to 3.2.alpha1
    3. All tests in sage/modular pass

I am happy to give this a positive review, reinforcing Craig's.


---

Comment by mabshoff created at 2008-10-29 13:47:45

Resolution: fixed


---

Comment by mabshoff created at 2008-10-29 13:47:45

Merged in Sage 3.2.alpha2
