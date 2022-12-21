# Issue 3130: permgps: added normal_subgroups and fixed image and kernel

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-05-08 03:57:46

Assignee: joyner

CC:  cwitty

Why SAGE doesn't support the computation of normal subgroups has been raised on sage-support. I needed it myself for a research problem so, added it. While constructing an example for the docstring, it dawned on me that image and kernel still only return a string. William Stein and David Kohel suggested that be fixed, maybe 2 years ago now, so I added that. While doctesting, I discovered that derived_series and friends is a random computation. (Very odd that a docstring failure hasn't been triggered until now.) Anyway, some "# random" comments were added to fix that.
Finally, I rearranged the PermutationGroup class methods in a more alphabetical order for easier reading.

Passes sage -testall. The diff file is huge but only because of the reordering of the methods. Really, it is a fairly simple pach.



---

Attachment

permgp.py+permgp_morphism.py patch based on 3.0.1


---

Comment by bump created at 2008-05-29 16:04:23

This is not a review but I can review this patch. Here are a few preliminary comments.

The effect of the patch is obscured by the fact that the methods in PermutationGroup_generic have been reordered. The new order first places methods whose names start with underscore at the top, and then begins alphabetical order. However the alphabetical order breaks down after quotient_group. I get the impression that alphabetization of the methods was started but not completed. There are merits to alphabetical ordering of the methods but there are also disadvantages. For example, largest_moved_point and smallest_moved_point are no longer adjacent.

The patch affects (favorably) the examples at the head of permgroup_morphism.py. Many of the methods in this short file have no docstring and no doctests. It might be good to take this opportunity to add docstrings and doctests to these methods.

The patch addresses finding normal subgroups of a permutation group by adding a new method.
This might be an occasion to address a problem with the normalizer method. One is more
likely to want the normalizer of a subgroup than of an element. Currently the latter is implemented and the former not. See:

http://groups.google.com/group/sage-devel/browse_thread/thread/a62aa2fc980375c3/e405621898a4f8d3?hl=en&lnk=gst&q=normalizer#e405621898a4f8d3

The normalizer_method should first test whether the parameter g is an element or itself a group. For example:


```
    def normalizer(self,g):
        """
        Returns the normalizer of g in self.

        EXAMPLES:
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: g = G.random_element(); g
            (1,3)
            sage: G.normalizer(g)
            Group( [ (1,3), (2,4) ] )
            sage: g = G([(1,2,3,4)])
            sage: G.normalizer(g)
            Group( [ (1,2,3,4), (1,3)(2,4), (2,4) ] )

        """
        if g in self:
            N = self._gap_().Normalizer(str(g))
        else:
            N = self._gap_().Normalizer(gap(g).name()) 
        return N
```


I will review the patch within the next few days but in the meantime I'm offering these preliminary comments.


---

Comment by wdj created at 2008-05-29 16:12:02

I agree with everything said. I'm not looking forward to having to rebase this, but hopefully I can do that and fix whatever problems Dan finds at the same time.


---

Attachment


---

Attachment


---

Comment by bump created at 2008-05-29 20:39:00

I uploaded two patches called 9670-factored-a.patch and 9670-factored-b.patch.

The union of these two patches is exactly David's patch 9670.patch.

The first patch 9670-factored-a.patch only reorders the methods of PermutationGroup_generic
into exactly the order of David's patch (except omitting the new method normal_subgroups).
It is guaranteed to have no effect, because no code is changed aside from this reordering.

The second patch goes on top. Importing these two patches is equivalent to David's patch.

The purpose of this exercise is to show exactly what David's patch does. The second patch
9670-factored-b.patch shows the changed and new code.


---

Comment by wdj created at 2008-05-29 23:37:54

I just want to add that this applies cleanly to 3.0.2 and 3.0.3.alpha0 (thanks Dan!) and passes sage -testall on sage 3.0.2. I am currently testing it on 3.0.3.alpha0. If it passes (and I assume it will) then I'll add the functionality to normalizer suggested by Dan above and posta new patch based on 3.0.3.alpha0.


---

Comment by bump created at 2008-05-30 02:54:56

If you are revising the patch, how about adding docstrings and tests in permgrp_morphism.py?

Dan


---

Attachment

patch based on 3.0.3.alpha0


---

Comment by wdj created at 2008-05-30 03:45:37

I modified normalizer almost as suggested about (the version above returned a GAP Group; the one in the latext patch returns a SAGE PermutationGroup). Also, I straightened out the organization to the methods are now really in alphabetical order.

Passes sage -testall.

I don't think I should review this but if you twist my arm, I'll give it a positive review:-)


---

Comment by bump created at 2008-05-30 14:23:59

I'll review it. (Maybe not until tomorrow.)


---

Comment by bump created at 2008-05-30 19:02:40

The contents of the patch are as follows.

(1) Methods of PermutationGroup_generic are alphabetized.

(2) A comment on the Suzuki and Ree groups was moved to the file
permgroup_named.py, where it properly belongs.

(3) Certain tests are commented # random output.

(4) A method normal_subgroup() of PermutationGroup_generic is added.

(5) The method normalizer() of PermutationGroup_generic is enhanced.
Previously only the normalizer of an element was implemented; now
you can get the normalizer of a subgroup.

(5) In permgroup_morphism.py PermutationGroupMorphism_im_gens gets
correct kernel and image methods.

I have looked at the patch carefully and tested it and found it good.
I recommend merging it. Merge 9670.patch and 9792.patch.


---

Comment by mabshoff created at 2008-05-31 06:44:49

I am concerned about the added #random to doctests. Since we see GAP's random seed these doctests should be reproducible and it should be unneeded. I am CCing cwitty on the ticket - he might have some explanation or might know where the bug lurks [in case these is one].

Cheers,

Michael


---

Comment by wdj created at 2008-05-31 11:31:25

I'm not sure what Michael's comment means. I just have the following observation to report which might be relevant. Consider for example the "random output" comment in:


```
    def composition_series(self):
        """
        Return the composition series of this group as a list of
        permutation groups.

        EXAMPLES:
        These computations use pseudo-random numbers, so we set the
        seed for reproducible testing.
            sage: set_random_seed(0)
            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
            sage: G.composition_series()    # random output
            [Permutation Group with generators [(1,2,3)(4,5), (3,4)],
             Permutation Group with generators [(1,5)(3,4), (1,5)(2,3), (1,5,4)],
             Permutation Group with generators [()]]
```

The output of the block

```
sage: set_random_seed(0)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.composition_series()  
```

is, when entered repeatedly,  not constant. However, once you enter the first 2 lines and then 

```
sage: G.composition_series()  
```

repeatedly, the answer is always the same.

It seems to me that "# random output" is to help the *reader* of the code recognize that their output might be different than the output given in the docstring. If that is the case, then for readability, it seems that some sort of comment on the random nature of the output should stay in the documentation somewhere. Does this seem reasonable?


---

Comment by was created at 2008-05-31 13:51:54

1. I think the fact that one sets the random seed in the doctest should be indication enough to the reader.

2. There is absolutely no reason the composition series is random.  Why not return it in a deterministic order?


---

Comment by wdj created at 2008-05-31 13:58:27


```
2. There is absolutely no reason the composition series is random. Why not return it in a deterministic order? 
```

The order is not the issue.. The generators are randomly determined.


---

Comment by wdj created at 2008-05-31 19:22:20

In any case, I am confused as to what to do. Do I wait for cwitty to comment, or just remove the "# random output" lines in the cases when the random seed is set (then post a new patch), or ... ?


---

Comment by cwitty created at 2008-05-31 20:10:58

Any function that calls a GAP function that uses random numbers should set the GAP random number seed, as explained in the following excerpt from randstate.pyx:

```
\item[GAP] If you are calling code in GAP that uses random numbers,
call \method{set_seed_gap} at the beginning of your function, like this:
\begin{verbatim}
from sage.misc.randstate import current_randstate
...

    current_randstate().set_seed_gap()
\end{verbatim}

Fetch the current \class{randstate} with \code{current_randstate()} in 
every function that wants to use it; don't cache it globally or 
in a class.  (Such caching would break \method{set_random_seed}).
```


You can see several uses of this idiom in permgroup.py.


---

Comment by wdj created at 2008-06-02 01:12:29

Okay, but it isn't clear to me that GAP is calling GAP's random numbers. 
In http://www.gap-system.org/Manuals/doc/htm/ref/CHAP028.htm#SSEC006.2
it's stated that

"The method used by GAP to obtain random elements may depend on the type object."

Is it true that the random method used to obtain generators of the terms in the CompositionSeries (and DerivedSeries, and friends) depends on the same seed used to generate random numbers? If this is not known, then I don't see why one uses the randstate.pyx function in permgroup.py. 

In any case, I am still unsure if I am supposed to submit a new patch or not.


---

Comment by cwitty created at 2008-06-02 17:10:17

"Is it true that the random method ... depends on the same seed used to generate random numbers?"

I think it's very likely to be true (for practical purposes, there seems to be a single global random number generator in GAP).  Did you check that the "# random" cases you added were actually random (that is, that they gave different answers on different doctest runs)?  With our current approach to doctesting pseudo-random numbers, slight modifications to the code could easily result in changing the results of the doctests to a new, consistent value.

I think it's worth removing as many "# random" from the Sage doctests as possible (which is why I bothered to write randstate.pyx), but I don't think there's any formal policy forbidding new "# random" doctests (even if they are easily fixable).


---

Comment by wdj created at 2008-06-02 21:17:06

Forgive my questions but I'm still confused. You asked

"Did you check that the "# random" cases you added were actually random (that is, that they gave different answers on different doctest runs)?"

I'm not sure if this answers your question but here are two consecutive runs which set the seed and give different answers. Is that what you mean?


```
sage: set_random_seed(0)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.composition_series()

[Permutation Group with generators [(1,2,3)(4,5), (3,4)],
 Permutation Group with generators [(1,5)(3,4), (1,5)(2,3), (1,5,4)],
 Permutation Group with generators [()]]
sage: set_random_seed(0)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G.composition_series()

[Permutation Group with generators [(1,2,3)(4,5), (3,4)],
 Permutation Group with generators [(1,5)(3,4), (1,5)(2,4), (2,4)(3,5)],
 Permutation Group with generators [()]]
```



---

Comment by cwitty created at 2008-06-04 16:33:35

OK, this seems to be a general problem with randstate; I can reproduce similar problems in Sage 3.0.2.  I'm going to open a new ticket for the randstate bug; since the randstate issues have nothing to do with this patch, I'm going to reinstate bump's positive review.


---

Comment by cwitty created at 2008-06-04 16:53:34

(See #3364 for the new randstate ticket.)


---

Comment by mabshoff created at 2008-06-04 21:22:12

9670.patch no longer merges cleanly because of the following hunk:

```
`@``@` -402,21 +372,6 `@``@` class PermutationGroup_generic(group.Fin
                 return PermutationGroupElement(x._gap_(), self, check = False)
         raise TypeError, "no implicit coercion of element into permutation group"

-    def list(self):
-        """
-        Return list of all elements of this group.
-
-        EXAMPLES:
-            sage: G = PermutationGroup([[(1,2,3,4)], [(1,2)]])
-            sage: G.list()
-            [(), (3,4), (2,3), (2,3,4), (2,4,3), (2,4), (1,2), (1,2)(3,4), (1,2,3), (1,2,3,4), (1,2,4,3), (1,2,4), (1,3,2), (1,3,4,2), (1,3), (1,3,4), (1,3)(2,4), (1,3,2,4), (1,4,3,2), (1,4,2), (1,4,3), (1,4), (1,4,2,3), (1,4)(2,3)]
-        """
-        from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
-        X = self._gap_().Elements()
-        n = X.Length()
-        return [PermutationGroupElement(X[i], self, check = False)
-                            for i in range(1,n+1)]
-
```

This is because of the fixes by William at #3353. This patch will need to be rebased against 3.0.3.alpha1 once it is out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-04 21:28:16

Looking at 9670.patch the problem might be limited to the actual moving of the list(self) function. Replacing that version with the one written by William might be enough. I did not look at the second patch, so there might be more problems there. 

David: For the record since you asked: Rebasing does not mean copying over the old files into the 3.0.3.alpha1 and then exporting again. You need to merge all the fixes including the moving of the new list(self) function. It would also be good if you posted a single new patch.

Cheers,

Michael


---

Comment by bump created at 2008-06-05 13:36:31

Since the patch must be rebased let me point out that the patch would be easier to evaluate it would be better if the patch were factored into two parts, one of which only reorders the methods of `PermutationGroup_generic` and the other part containing the actual changes. Observe that I factored David's original patch this way (see above) and found it necessary to do so in order to understand what the patch actually does. I did not repeat this exercise on the second part of the patch.


---

Comment by wdj created at 2008-06-07 13:35:39

I'm trying to rebase but don't know how to merge. When I try to apply the old patch I get


```
wdj`@`hera:~/sagefiles/sage-3.0.3.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: permgp
sage: hg_sage.apply("/home/wdj/sagefiles/9792.patch")
cd "/home/wdj/sagefiles/sage-3.0.3.alpha1/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.0.3.alpha1/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.0.3.alpha1/devel/sage" && hg import   "/home/wdj/sagefiles/9792.patch"
applying /home/wdj/sagefiles/9792.patch
patching file sage/groups/perm_gps/permgroup.py
Hunk #1 FAILED at 60
Hunk #3 succeeded at 686 with fuzz 2 (offset -146 lines).
Hunk #4 succeeded at 724 with fuzz 2 (offset -146 lines).
Hunk #5 FAILED at 1365
Hunk #6 FAILED at 1780
Hunk #7 succeeded at 1831 with fuzz 1 (offset -22 lines).
3 out of 8 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej
abort: patch failed to apply
```

The methods in file permgroup.py.rej make no sense to me:
| SAGE Version 3.0.3.alpha1, Release Date: 2008-06-04                |
| Type notebook() for the GUI, and license() for information.        |

```
--- permgroup.py
+++ permgroup.py
`@``@` -61,7 +61,8 `@``@` AUTHOR:
     - William Stein (2007-07): put is_isomorphic back (and make it better)
     - David Joyner (2007-08): fixed bugs in composition_series, upper/lower_central_series, 
                               derived_series,
-    - David Joyner (2008-05): added normal_subgroups  (requested feature)
+    - David Joyner (2008-05): added normal_subgroups (requested feature), some rearrangement,
+                              modified normalizer
  
 REFERENCES:
     Cameron, P., Permutation Groups. New York: Cambridge University Press, 1999.
`@``@` -1289,171 +1367,6 `@``@` class PermutationGroup_generic(group.Fin
         from permgroup_morphism import PermutationGroupMorphism_im_gens
         return PermutationGroupMorphism_im_gens(self, right, srcs, dsts)
 
-    def molien_series(self):
-        r"""
-        Returns the Moien series of a transtive permutation group.
-        The function
-        $$
-        M(x) = (1/|G|)\sum_{g\in G} det(1-x*g)^(-1)
-        $$
-        is sometimes called the "Molien series" of G.
-        GAP's \code{MolienSeries} is associated to a character of a group G.
-        How are these related? A group G, given as a permutation 
-        group on n points, has a "natural" representation of 
-        dimension n, given by permutation matrices. The Molien series 
-        of G is the one associated to that permutation representation of 
-        G using the above formula. Character values then count fixed 
-        points of the corresponding permutations. 
-        
-        EXAMPLES:
-            sage: G = SymmetricGroup(5)
-            sage: G.molien_series()                              # requires optional gap_packages
-            1/(-x^15 + x^14 + x^13 - x^10 - x^9 - x^8 + x^7 + x^6 + x^5 - x^2 - x + 1)
-            sage: G = SymmetricGroup(3)
-            sage: G.molien_series()                              # requires optional gap_packages
-            1/(-x^6 + x^5 + x^4 - x^2 - x + 1)
-
-        """
-        G = self
-        GG = G._gap_init_()
-        gap.eval("pi := NaturalCharacter( %s )"%GG)
-        gap.eval("cc := ConstituentsOfCharacter( pi )")
-        M = gap.eval("M := MolienSeries(Sum(cc))")
-        R = PolynomialRing(RationalField(),"x")
-	x = R.gen()
-        nn = gap.eval("NumeratorOfRationalFunction(M)")
-        dd = gap.eval("DenominatorOfRationalFunction(M)")
-        FF = FractionField(R)
-        return FF(nn.replace("_1",""))/FF(dd.replace("_1",""))
-    
-    def normal_subgroups(self):
-        """
-        Return the normal subgroups of this group as a (sorted in increasing
-        order) list of permutation groups.
-
-        The normal subgroups of $H = PSL(2,7)xPSL(2,7)$ are $1$, two copies
-        of $PSL(2,7)$ and $H$ itself, as the following example shows.
-        EXAMPLES:
-            sage: G = PSL(2,7)
-            sage: D = G.direct_product(G)
-            sage: H = D[0]
-            sage: NH = H.normal_subgroups()
-            sage: len(NH)
-            4
-            sage: NH[1].is_isomorphic(G)
-            True
-            sage: NH[2].is_isomorphic(G)
-            True
-
-        """
-        ans = []
-        NS = self._gap_().NormalSubgroups()
-        n = NS.Length()
-        for i in range(1,n+1):
-            ans.append(PermutationGroup(NS[i].GeneratorsOfGroup()))
-        return ans
-
-    def normalizer(self,g):
-        """
-        Returns the normalizer of g in self.
-
-        EXAMPLES:
-            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
-            sage: g = G.random_element(); g
-            (1,3)
-            sage: G.normalizer(g)
-            Group( [ (1,3), (2,4) ] )
-            sage: g = G([(1,2,3,4)])
-            sage: G.normalizer(g)
-            Group( [ (1,2,3,4), (1,3)(2,4), (2,4) ] )
-
-        """
-        N = self._gap_().Normalizer(str(g))
-        return N
-
-    def poincare_series(self, p=2, n=10):
-        """
-        Returns the Poincare series of G mod p (p must be a prime), for n>1 
-        large. In other words, if you input a finite group G, a prime p, 
-        and a positive integer n, it returns a quotient of polynomials 
-        f(x)=P(x)/Q(x) whose coefficient of $x^k$ equals the rank of the 
-        vector space $H_k(G,ZZ/pZZ)$, for all k in the range $1\leq k \leq n$. 
-        
-        REQUIRES:
-            GAP package HAP (in gap_packages-*.spkg).
-
-        EXAMPLES: 
-            sage: G = SymmetricGroup(5)
-            sage: G.poincare_series(2,10)                              # requires optional gap_packages
-            (x^2 + 1)/(x^4 - x^3 - x + 1)
-            sage: G = SymmetricGroup(3)
-            sage: G.poincare_series(2,10)                              # requires optional gap_packages
-            1/(-x + 1)
-
-        AUTHORS:
-            David Joyner and Graham Ellis
-        """
-        gap.eval('RequirePackage("HAP")')
-        from sage.rings.arith import is_prime
-        if not (p == 0 or is_prime(p)):
-            raise ValueError, "p must be 0 or prime"
-        G = self
-        GG = G._gap_init_()
-        ff = gap.eval("ff := PoincareSeriesPrimePart(%s,%s,%s)"%(GG,p,n))
-        R = PolynomialRing(RationalField(),"x")
-	x = R.gen()
-        nn = gap.eval("NumeratorOfRationalFunction(ff)")
-        dd = gap.eval("DenominatorOfRationalFunction(ff)")
-        FF = FractionField(R)
-        return FF(nn)/FF(dd)
-
-    def smallest_moved_point(self):
-        """
-        Return the smallest point moved by a permutation in this group.
-        
-        EXAMPLES:
-            sage: G = PermutationGroup([[(3,4)], [(2,3,4)]])
-            sage: G.smallest_moved_point()
-            2
-            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
-            sage: G.smallest_moved_point()
-            1
-        """
-        try:
-            return self.__smallest_moved_point
-        except AttributeError:
-            n = Integer(self._gap_().SmallestMovedPoint())
-        self.__smallest_moved_point = n
-        return n
-
-    def sylow_subgroup(self, p):
-        """
-        Returns a Sylow p-subgroups of the finite group G, where p is
-        a prime. This is a p-subgroup of G whose index in G is coprime to p.
-        Wraps the GAP function SylowSubgroup.
-
-        EXAMPLES:
-            sage: G = PermutationGroup(['(1,2,3)', '(2,3)'])
-            sage: G.sylow_subgroup(2)
-            Permutation Group with generators [(2,3)]
-            sage: G.sylow_subgroup(5)
-            Permutation Group with generators [()]
-
-        """
-        from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
-        G = self
-        gap.eval("G := %s"%G._gap_init_())
-        gap.eval("Ssgp := SylowSubgroup(G, %s);"%p)
-        gap.eval("gens := GeneratorsOfGroup( Ssgp );")
-        N = Integer(gap.eval("N := Length(gens);"))
-        if N>0:
-            gens = [PermutationGroupElement(gap.eval("gens[%s];"%j)) for j in range(1,N+1)]
-            H = PermutationGroup(gens)
-        else:
-            H = PermutationGroup([()])
-        return H
-
-        
     ######################  Boolean tests #####################
     
     def is_abelian(self):
`@``@` -1704,54 +1617,6 `@``@` class PermutationGroup_generic(group.Fin
         ans = self._gap_().IsTransitive()
         return ans.bool()
     
-    ############## Series ######################
-    
-    def composition_series(self):
-        """
-        Return the composition series of this group as a list of
-        permutation groups.
-
-        EXAMPLES:
-        These computations use pseudo-random numbers, so we set the
-        seed for reproducible testing.
-            sage: set_random_seed(0)
-            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
-            sage: G.composition_series()    # random output
-            [Permutation Group with generators [(1,2,3)(4,5), (3,4)],
-             Permutation Group with generators [(1,5)(3,4), (1,5)(2,3), (1,5,4)],
-             Permutation Group with generators [()]]
-
-        """
-        current_randstate().set_seed_gap()
-        ans = []
-        DS = self._gap_().CompositionSeries()
-        n = DS.Length()
-        for i in range(1,n+1):
-            ans.append(PermutationGroup(DS[i].GeneratorsOfGroup()))
-        return ans
-
-    def derived_series(self):
-        """
-        Return the derived series of this group as a list of
-        permutation groups.
-
-        EXAMPLES:
-        These computations use pseudo-random numbers, so we set the
-        seed for reproducible testing.
-            sage: set_random_seed(0)
-            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
-            sage: G.derived_series()    # random output
-            [Permutation Group with generators [(1,2,3)(4,5), (3,4)], 
-             Permutation Group with generators [(1,5)(3,4), (1,5)(2,4), (2,4)(3,5)]]
-        """
-        current_randstate().set_seed_gap()
-        ans = []
-        DS = self._gap_().DerivedSeries()
-        n = DS.Length()
-        for i in range(1,n+1):
-            ans.append(PermutationGroup(DS[i].GeneratorsOfGroup()))
-        return ans
-    
     def lower_central_series(self):
         """
         Return the lower central series of this group as a list of
```


Why would these be rejected? AFAIK, they have nothing to do with the list(self) function. In any case, I don't know what to do with these. The link http://hgbook.red-bean.com/hgbookch12.html simply says "it is usually best to fix up the rejected hunks", but that isn't very specific. These passes sage -testall before, so I don't know what there is to fix.


---

Comment by wdj created at 2008-06-07 18:51:17

Perhaps I'm misreading something, but it seems like the files size before William's patch http://trac.sagemath.org/sage_trac/ticket/3353 is 72K and now it is 80K. So, I'm leary of just taking my file and replacing the list method by William's. Maybe I should just completely redo the entire thing? To me that would be more straightforward than dealing with hg-rejected methods. If I should do this, should I also start a new ticket?


---

Comment by bump created at 2008-06-08 12:24:51

It seems to me that the patch has to be redone but without starting a new ticket. I'd prefer to see just the changes to the methods without alphabetizing. That way the effect of the patch is clear. A separate patch putting the methods in alphabetical order could be a separate ticket. I think it is good practice if code-cleanup patches (such as realphabetizing, tab removal, etc.) do the cleanup but have no other effect. Especially realphabetizing the methods should not be mixed with actual code changes since one can't tell that a method hasn't been changed when it is moved to another spot. This was a problem when I reviewed the patch.


---

Comment by mabshoff created at 2008-06-09 00:47:13

I agree with Dan: Post a new patch that adds normal_subgroups and fixes image and kernel only against 3.0.3.a1. Then open a new ticket that sorts all the functions alphabetically.

Cheers,

Michael


---

Comment by wdj created at 2008-06-09 02:17:35

Please apply both of these patches. The 2 pass sage -testall. There is no alphabetical resorting in this patch.


---

Attachment

this and 9807 are based on sage 3.0.3alpha1


---

Attachment

I went through the patch (9807.patch+9808.patch) and it looks good to me. It is
exactly what was discussed before without the realphabetizing.

I hope that this ticket is closed before 3364. When 3364 is closed maybe someone
can come back and remove the # random output comments this patch adds.


---

Comment by mabshoff created at 2008-06-09 06:19:34

Resolution: fixed


---

Comment by mabshoff created at 2008-06-09 06:19:34

Merged in Sage 3.0.3.alpha2
