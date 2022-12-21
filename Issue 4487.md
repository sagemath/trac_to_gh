# Issue 4487: add method to evaluate characters of permutation and matrix groups

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-11-10 00:12:42

Assignee: joyner

Currently to evaluate a character, you have to use
something indirect like 


```
sage: G = GL(2,7)
sage: z = G.center().an_element()
sage: reps = [x.Representative() for x in gap(G).ConjugacyClasses()]
sage: reps.index(gap(z))
8
sage: table = gap(G).CharacterTable().Irr()
sage: chi = table[2]
sage: chi[8]
1
```


Martin Mereb asked


```
is it possible to imlpement something like
chi(z) or chi.eval(z) or something like that?
```


This should be implemented.


---

Attachment

patch against version 3.2.rc0


---

Comment by saliola created at 2008-11-13 17:06:58

I'm attaching a patch that adds a GroupCharacter class that wraps GAP's Character function. The above can now be achieved by doing the following:


```
sage: G = GL(2,7)
sage: z = G.center().an_element()
sage: chi = G.irreducible_characters()[1]
sage: chi(z)
1
```



One problem: I don't know how to coerce the values of the characters into Sage. Is there a standard datatype for this?


---

Comment by wdj created at 2008-11-13 20:41:02

Thank you so much for adding this patch. It is wonderful!

I probably will not have time in the next day or so to referee it but can this weekend  definitely and possibly tomorrow night. However, I see a few problems. First, you are returning GAP values, but this is easy to fix:


```

sage: from sage.interfaces.gap import gfq_gap_to_sage
sage: gfq_gap_to_sage("E(7)",GF(7))
3
sage: gfq_gap_to_sage("E(8)",GF(8,"a"))
a
```


Second, and this is a matter of taste, I would name your Python class ClassFunction instead of GroupCharacter. Of course, they are the same vector space, but you can define orbital integrals and other invariants without regard to the characters, so it is just a more general name.

Third, I wonder if it would be any more work to allow any Sage ring and the value-ring of an instance of this class? (For example, polynomial-valued class functions?)

Finally, I wonder if you could also create a much more general class of ring-valued functions on a group? I don't know what use this would be off-hand but maybe one could use it in case one if not sure if the function is a class function or not?

Anyway, just a few ideas to think about if you want, but thanks again for the very useful addition.


---

Comment by saliola created at 2008-11-14 00:31:38

Right now the code just wraps GAPs commands, but it can be made to do a lot of things natively and resort to GAP for some of the more complicated stuff. I was uncertain about how to implement a few things, but I thought that this would be a good way to start the discussion. I look forward to your review.

I've been reading more about GAP's implementation, and it heavily relies on character tables. So we are probably going to want to implement those as well. In fact, every character stores the whole character table of the group (as UnderlyingCharacterTable). Should we stick closely to the GAP implementation and do the same? Arguably, this is what we should do if we want to use GAP for the heavy lifting, but I am open to suggestions.


---

Comment by wdj created at 2008-11-15 00:53:03

First, I am running sage on ubuntu 8.10 where doctesting seems to be broken, so I have not tested this.

I like this addition so much, I am going to give it a positive review once one important change is made.

This output:


```
sage: G = GL(2,3)
sage: irrs = G.irreducible_characters()
sage: chi1 = irrs[3]; chi1
Character of General Linear Group of degree 2 over Finite Field of size 3
sage: g = G.conjugacy_class_representatives()[6]
sage: chi1(g)
E(8)+E(8)^3
```

is unacceptable, IMHO, because it is easy to fix and (as the author himself noted) should be a Sage value.

In addition to the things I noted above which might be changed but don't have to be (yet or ever), is the following somewhat odd behaviour:


```
sage: len(G.conjugacy_class_representatives())
8
sage: chi2 = GroupCharacter(G, [-1, -1, -1, -1, -1, 1, -1, -1])
sage: chi2.irreducible_constituents()
[]
sage: chi2 = GroupCharacter(G, [1, 1, 1, 1, 1,1, 1, 1])
sage: chi2.irreducible_constituents()
[Character of General Linear Group of degree 2 over Finite Field of size 3]
sage: chi2 = GroupCharacter(G, [2, 2, 2, 2, 2, 2, 2, 2])
sage: chi2.irreducible_constituents()
[Character of General Linear Group of degree 2 over Finite Field of size 3]
```

It seems to be a coefficient is missing somewhere here. (I agree that this simply interfaces with GAP, but still!) Anyway, this can be fixed later and I want to minimize the required work so this can be included in Sage ASAP.


---

Comment by saliola created at 2008-11-17 10:38:41

* As suggested, I switched from GroupCharacter to ClassFunction. Note that this also changes the function being wrapped: GAP's ClassFunction instead of Character. Besides being more general, it also eliminates the odd behaviour you noticed above:

```
sage: G = GL(2,3)
sage: sage: len(G.conjugacy_class_representatives())
8
sage: chi2 = ClassFunction(G, [-1, -1, -1, -1, -1, 1, -1, -1])
sage: chi2.irreducible_constituents()
[Character of General Linear Group of degree 2 over Finite Field of size 3,
 Character of General Linear Group of degree 2 over Finite Field of size 3,
 Character of General Linear Group of degree 2 over Finite Field of size 3,
 Character of General Linear Group of degree 2 over Finite Field of size 3,
 Character of General Linear Group of degree 2 over Finite Field of size 3,
 Character of General Linear Group of degree 2 over Finite Field of size 3]
sage: chi2 = ClassFunction(G, [1, 1, 1, 1, 1,1, 1, 1])
sage: chi2.irreducible_constituents()
[Character of General Linear Group of degree 2 over Finite Field of size 3]
sage: chi2 = ClassFunction(G, [2, 2, 2, 2, 2, 2, 2, 2])
sage: chi2.irreducible_constituents()
[Character of General Linear Group of degree 2 over Finite Field of size 3]
```


 * I also fixed it so that Sage values are output instead of GAP elements. Thanks for pointing out gfq_gap_to_sage. I fixed this by adding a _base_ring data attribute that is set to the appropriate Cyclotomic Field (like is done in the character_table method). This should also make it possible to extend the code to work with values in arbitrary sage rings.

```
sage: G = GL(2,3)
sage: chi = G.irreducible_characters()[3]
sage: g = G.conjugacy_class_representatives()[6]
sage: chi(g)
zeta8^3 + zeta8
```


 * Unfortunately, though, it seems that Cyclotomic field elements aren't converted to GAP elements correctly, so using them as values won't work.

```
sage: G = GL(2,3)
sage: z = CyclotomicField(8).an_element; z
zeta8
sage: values = [2, 1, -2, -1, 0, -z^3 - z, z^3 + z, 0]
sage: xi = gap.ClassFunction(G, values); xi
ClassFunction( CharacterTable( GL(2,3) ),
[ 2, 1, -2, -1, 0, (-1*zeta8-1*zeta8^3), (zeta8+zeta8^3), 0 ] )
sage: ClassFunction(G, values)
Traceback: ...
```

I think this might be a bug:

```
sage: K = CyclotomicField(8)
sage: z = K.an_element; z
zeta8
sage: K(gap.E(8))
zeta8
sage: K(gap.E(8)) == z
True
sage: gap(z)
(zeta8)
sage: gap.E(8) == gap(z)
False
sage: gap(z)**4
!-1
```

I'm not sure what !-1 means. Any ideas?


---

Attachment

do NOT apply group_characters_4487.patch


---

Comment by saliola created at 2008-11-17 10:40:52

Only apply the latest patch (class_functions_4487.patch).


---

Comment by wdj created at 2008-11-18 19:37:52

Applies cleanly to 3.2.rc1, passes sage -testall. Code looks good. Thanks Franco!


---

Comment by mabshoff created at 2008-11-21 09:36:09

This patch does not pass doctests with 3.2:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0$ ./sage -t -long devel/sage/sage/groups/class_function.py 
sage -t -long devel/sage/sage/groups/class_function.py      
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/groups/class_function.py", line 335:
    sage: chi.restrict(H)
Expected:
    Character of Subgroup of SymmetricGroup(5) generated by [(1,2,3), (1,2), (4,5)]
Got:
    Character of Subgroup of SymmetricGroup(5) generated by [(4,5), (1,2), (1,2,3)]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/groups/class_function.py", line 348:
    sage: xi = H.trivial_character(); xi
Expected:
    Character of Subgroup of SymmetricGroup(5) generated by [(1,2,3), (1,2), (4,5)]
Got:
    Character of Subgroup of SymmetricGroup(5) generated by [(4,5), (1,2), (1,2,3)]
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_21
   1 of   7 in __main__.example_22
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/tmp/.doctest_class_function.py
         [6.8 s]
exit code: 1024
```


I am not quite sure what is going on here, but I guess we need to sort the generators at some point.

Cheers,

Michael


---

Comment by saliola created at 2008-11-21 13:55:51

fixes the broken doctests; apply on top of class_functions_4487.patch


---

Attachment

Hello Michael,

The __repr__ for this class just returns "Character of" plus the string representation of the group. So perhaps something changed in subgroup between 3.2.rc1 and 3.2?

Anyhow, I posted a patch to correct the docstring. Apply on top of class_functions_4487.patch.

Franco


---

Comment by mhansen created at 2008-11-21 15:46:18

Yep, William added a patch late in the 3.2 game which adds some canonicalization of the generators of a permutation group (by default).  So, just changing the doctests is all that's needed.

+1


---

Comment by mabshoff created at 2008-11-21 19:15:22

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 19:15:22

Merged class_functions_4487.patch and class_functions_4487-part2.patch in Sage 3.2.1.alpha0
