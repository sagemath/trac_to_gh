# Issue 5664: Bugs in PermutationGroup_subgroup.__cmp__

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-04-02 06:39:32

Assignee: tbd

Keywords: comparison subgroup

At http://groups.google.com/group/sage-support/browse_thread/thread/533747d48a1f29eb?hl=en
it was reported that comparision of subgroups of permutation groups does not work as expected:


```
sage: G = SymmetricGroup(4)
sage: H = G.subgroup([G((1,2,3))])
sage: K = G.subgroup([G((2,3,1))]) 
sage: G((1,2,3))==G((2,3,1))
True
sage: K==H
False
```


Even worse, comparison may raise an error -- afaik, the Python specification says that `__cmp__` is not supposed to raise errors:

```
sage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])
sage: G==G2
True
sage: G2==G
Traceback (most recent call last):
...
AttributeError: 'SymmetricGroup' object has no attribute 'ambient_group'
```


So, `==` is not a symmetric relation.

Of course, G==G2 invokes G.__cmp__(G2), which tests whether G and G2 are the same as PermutationGroup_generic.
In contrast, G2==G tests whether G2 and G are the same as PermutationGroup_subgroup.

So, what do people want?
 1. A symmetric relation? Then K.__cmp__() should invoke PermutationGroup_generic.__cmp__().
 2. Or should K.__cmp__(H) test whether K and H are subgroups of the same PermutationGroup, and then continue with testing whether K and H are subgroup of each other?

Note that the with 1., == would test whether K and H are isomorphic abstract groups, which is the job of K.is_isomorphic(H). 

Therefore, I am in favour of 2. 

But then: 
 * What should be returned if neither H is a subgroup of K nor K is a subgroup of H?
 * What should be returned if H is subgroup of G1 and K is subgroup of G2, with H contained in K contained in G2 contained in G1? Currently, K.__cmp__(H) would  -1 in this case (hence, H<K although K is contained in H!). Example:
 {{{
sage: G=SymmetricGroup(6)
sage: G1=G.subgroup([G((1,2,3,4,5)),G((1,2))])
sage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])
sage: K=G2.subgroup([G1((1,2,3))])
sage: H=G1.subgroup([G2(())])
sage: H<K
False
sage: K<H
True
}}}

So, the trivial group in G1 is considered greater than a non-trivial group in G2, because G1>G2.

So, before working on a patch, I'd like to get people's opinion on what is a good specification of 'comparison of subgroups'.


---

Comment by SimonKing created at 2009-04-02 06:47:32

Changing assignee from tbd to SimonKing.


---

Comment by wdj created at 2009-04-02 09:31:22

Based on how I think mathematicians would most likely use this, I'm in favor of 1. 

In any case, I don't agree that "with 1., == would test whether K and H are isomorphic abstract groups". The code is


```
        if not isinstance(right, PermutationGroup_generic):
            return -1
        return right._gap_().__cmp__(self._gap_())
```

which seems to be a wrapper for GAP's equality. Does that seem right to you?


---

Comment by wdj created at 2009-04-02 09:31:22

Changing component from algebra to group_theory.


---

Comment by SimonKing created at 2009-04-02 09:41:25

Hi,

Replying to [comment:3 wdj]:
> Based on how I think mathematicians would most likely use this, I'm in favor of 1. 
> 
> In any case, I don't agree that "with 1., == would test whether K and H are isomorphic abstract groups". The code is
> 
> {{{
>         if not isinstance(right, PermutationGroup_generic):
>             return -1
>         return right._gap_().__cmp__(self._gap_())
> }}}
> which seems to be a wrapper for GAP's equality. Does that seem right to you?

Right. My (apparently wrong) assumption was that gap tests for isomorphism.
So, my reason for supporting 1. broke.

However, who did implement (I guess overloaded) the `__cmp__` method of PermutationGroup_generic for PermutationGroup_subgroup? What was the original reason for taking into account the ambient group?

Cheers,
    Simon


---

Comment by wdj created at 2009-04-02 10:37:21

> However, who did implement (I guess overloaded) the __cmp__ method of 
> PermutationGroup?_generic for PermutationGroup?_subgroup? What was the 
> original reason for taking into account the ambient group?

I think that was my stupid idea. I don't remember what I was thinking, sorry.
Maybe an {{{is_equal}} (as subgroups) was what I was thinking, though I'm
not sure how useful that is, given == and {{{ambient_group}} are existing methods.


---

Comment by SimonKing created at 2009-04-02 12:30:19

I just observed another detail that I found strange.

Note that in `PermutationGroup_generic.__cmp__(self,right)`, the return value is `right._gap_().__cmp__(self._gap_())`, not `self._gap_().__cmp__(right._gap_())`.

By consequence, we have 

```
sage: G = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: H = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments ())](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G<H
True
```


Is this something that we want? I also ask on the mailing list, as this seems fundamental to me.


---

Comment by SimonKing created at 2009-04-02 13:07:22

I have a suggestion for a fix.

 1. For comparing PermutationGroup_generic, rely on gap, without reversion of the output.
 2. For ``PermutationGroup_subgroup.__cmp__(self,other)``:
    a) Compare self and other as PermutationGroup_generic. If they are not equal, return the result.
    b) Otherwise, return the comparison of the ambient group of self with the ambient group of other (or with other, itself, if it is not given as a subgroup).

I had to modify the doc-test example of ``PermutationGroup_generic.__cmp__``. And then, we have:

```
sage: G=SymmetricGroup(6)
sage: G1=G.subgroup([G((1,2,3,4,5)),G((1,2))])
sage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])
sage: K=G2.subgroup([G2((1,2,3))])
sage: H=G1.subgroup([G1(())])
sage: H<K
True
sage: K<H
False
sage: H2=G2.subgroup([G2(())])
sage: H<H2
True     # because the ambient group of H is a subgroup of the ambient group of H2

sage: G = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: H = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments ())](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G<H
False

sage: G = SymmetricGroup(4)
sage: H = G.subgroup([G((1,2,3))])
sage: K = G.subgroup([G((2,3,1))])
sage: H==K
True

# Here comes an oddity
sage: G = SymmetricGroup(4)
sage: H = G.subgroup([G((1,2,3)),G((1,2))])
sage: K = SymmetricGroup(3)
sage: K < H
False  # this is comparison as PermutationGroup_generic
sage: K == H
True
sage: H < K
False 
sage: H == K
False
```

The last example is comparison as PermutationGroup_subgroup, and comes from the fact that the ambient group of K (which is assumed to be K itself) is strictly smaller than the ambient group of H.

Does this way of comparison makes kind of sense?


---

Comment by wdj created at 2009-04-02 13:40:08

> Does this way of comparison makes kind of sense?

Not in my opinion. If H, K are permutation groups, then
H == K should return True iff H=k (as sets)
H<K should return True iff H is a subset of K.

Does your patch do this?


---

Comment by SimonKing created at 2009-04-02 21:45:09

Replying to [comment:9 wdj]:
> > Does this way of comparison makes kind of sense?
> 
> Not in my opinion. If H, K are permutation groups, then
> H == K should return True iff H=k (as sets)
> H<K should return True iff H is a subset of K.
> 
> Does your patch do this?

Apparently not.

My way of thinking was like this: The present implementation took into account that we do not talk about permutation groups but about _subgroups_ of permutation groups. With this in mind, it is natural to have K==H if and only if K is the same permutation group as H, and _in addition_ the ambient groups coincide.

One question on gap: Assume that K is a _proper_ subgroup of H; would `K._gap_()<H._gap_()` return True?

If the answer to the preceding question is 'Yes' then my patch provides the following:
 * If K is a _proper_ subgroup of H, then K<H.
 * If K and H coincide as permutation groups and the ambient group of K is a proper subgroup of the ambient group of H, then K<H
 * K==H only if K coincides with H (as permutation groups) and _in addition_ the ambient groups coincide.

But of course it is also a very natural thing (and probably what algebraists would expect from K<H) to just test whether one group is subgroup of the other. If this is what `K._gap_()<H._gap_()` does, then it is easy to implement (tomorrow, when I'll have better internet access; now is about the 5th attempt to submit my comment...).


---

Comment by wdj created at 2009-04-04 17:47:36

Almost a positive review.

Seems to apply fine to 3.4 and test okay.

The problem is with the docstrings. The docstring for __cmp__
in the subgroup class defines H but never uses it. Plase

(a) improve the docstring for __cmp__
in the subgroup class to include instances of the behavious discussed above

(b) please add your name to the AUTHOR list at the top

A positive review after that.


---

Comment by SimonKing created at 2009-04-18 14:08:18

The new version of the patch should apply to sage-3.4.1.rc3 -- it is formed by two change sets, I hope it works...

I added myself to the list of authors, and I added more doc tests (similar to the things discussed above).

Cheers,
    Simon


---

Comment by wdj created at 2009-04-19 00:42:21

How is this behaviour (after your patch is attached) explained?


```
sage: G1 = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G2 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2,3),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G1 > G2
False
sage: G = SymmetricGroup(5)
sage: G1 = G.subgroup([G([(1,2,3),(4,5)]),G((3,4))])
sage: G2 = G.subgroup([G([(1,2,3),(4,5)])])
sage: G1 > G2
False
```



The outout is True for both without your patch.


---

Comment by SimonKing created at 2009-04-20 11:41:37

Replying to [comment:14 wdj]:
> How is this behaviour (after your patch is attached) explained?

This is since comparison in gap apparently has nothing to do with the subgroup structure. 

Without my patch, `PermutationGroup.__cmp__(self, right)` returns 

```
right._gap_().__cmp__(self._gap_())
```

which means that the trivial group may be _bigger_ than a non-trivial group:

```
# without my patch
sage: G = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: H = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments ())](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G<H
True
```


This example is the reason why I suggested to let `PermutationGroup.__cmp__(self, right)` return

```
self._gap_().__cmp__(right._gap_())
```


But then, your example gives a strange result. I think gap is to blame for this.

So, our choice is: 
 * Either we want that the trivial group is _greater_ than the cyclic group of order two; nasty!!
 * or `PermutationGroup([[(1,2,3),(4,5)],[(3,4)]]) < PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2,3),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))`; nasty as well!
 * or `G.__cmp__(H)` for PermutationGroups should do the following:
   1. Test if G is a subgroup of H; if yes, return -1
   2. Test if H is a subgroup of G; if yes, return +1
   3. Now, G and H are mutually not subgroups. Then, return whatever gap provides.

The last option seems best to me, from a mathematical point of view. However, the subgroup test might be long. 

What do you think?


---

Comment by wdj created at 2009-04-20 12:25:19

Is the previous behaviour (without the patch) only wrong in the special case of the
trivial group? If so, can't that case just be treated separately using an if/then
statement?


```
sage: G = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: H = PermutationGroup([[(1,2)],[(2,3)]])
sage: G<H1             # correct 
True
sage: H2 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,3))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G<H2             # correct 
False
sage: H2 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: G<H2             # incorrect 
True
```



---

Comment by SimonKing created at 2009-04-20 12:36:07

Replying to [comment:16 wdj]:
> Is the previous behaviour (without the patch) only wrong in the special case of the
> trivial group? If so, can't that case just be treated separately using an if/then
> statement?

Well, you know Gap better than I...

What does the Gap reference say? I tried to find something, but there was no index entry that sounded relevant (the nearest was "Comparison of Permutations", but not "Comparison of Permutation Groups").


---

Comment by wdj created at 2009-04-20 13:18:27

I searched the Gap reference manual and couldn't find it either.
(Emailed gap support though and will let you know...)

Maybe we should just use IsSubgroup (I thought < called that method but I guess not):


```
sage: G = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: gG = gap(G)
sage: H1 = PermutationGroup([[(1,2)],[(2,3)]])
sage: gH1 = gap(H1)
sage: bool(gH1.IsSubgroup(gG))             # correct 
True
sage: H2 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,3))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: bool(gH2.IsSubgroup(gG))             # correct 
False
sage: H3 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: gH3 = gap(H3)
sage: bool(gH3.IsSubgroup(gG))             # correct 
False
```


Thoughts?


---

Comment by SimonKing created at 2009-04-20 19:09:35

Replying to [comment:18 wdj]:
> I searched the Gap reference manual and couldn't find it either.
> (Emailed gap support though and will let you know...)

Since, according to the email support, the comparison is by some lexicographic order of the list of elements, it is perhaps no surprise that the "<"-relation of Gap does not behave well with respect to subgroups.

> Maybe we should just use IsSubgroup (I thought < called that method but I guess not):

As much as I understand the sorting of Gap, we would have 
 G is proper subgroup of H <=> |G|<|H| and (G<H in Gap's '<'-order)

So, rather than calling IsSubgroup, we might consider to use Order(G); I guess this is cached and thus faster.

Would this work (and is the cacheing-thing true)?

Cheers,
    Simon


---

Comment by SimonKing created at 2009-04-20 19:12:12

Sorry, I was writing too quickly (have to leave office very soon...):

Replying to [comment:19 SimonKing]:
> Since, according to the email support, the comparison is by some lexicographic order of the list of elements, it is perhaps no surprise that the "<"-relation of Gap does not behave well with respect to subgroups.
> 
...
> As much as I understand the sorting of Gap, we would have 
>  G is proper subgroup of H <=> |G|<|H| and (G<H in Gap's '<'-order)

Of course it is not!

So, I agree that IsSubgroup is the way to go.


---

Attachment

Bug fixes and doc tests for `PermutationGroup_generic.__cmp__` and `PermutationGroup_subgroup.__cmp__`


---

Comment by SimonKing created at 2009-04-21 08:01:32

The new patch (relative to sage-3.4.1.rc3) now relies on gap's `IsSubgroup`.

Hence, the examples discussed above now work as expected, `__cmp___` extends the subgroup lattice:
 * If G is subgroup of H then G<H
 * If neither G is subgroup of H nor H is subgroup of G, then, in order to give any answer at all, return whatever gap suggests.

However, there is a price to pay. The result is not an ordering!

```
sage: H1 = PermutationGroup([[(1,2)],[(5,6)]])
sage: H2 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (3,4))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: H3 = PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2))](https://trac.sagemath.org/wiki/WikiMacros#-macro))
# H1,H2 are mutually not subgroups, and H2,H3 are mutually not subgroups
sage: H1 < H2 # according to Gap's ordering
True
sage: H2 < H3 # according to Gap's ordering
True
sage: H3 < H1 # since H3 is a subgroup of H1
True
```


So, really our choices are:
 1. Return gap's ordering -- which has nothing to do with subgroups. Nasty
 2. Do as suggested in my new patch -- then we don't have transitivity. Nasty
 3. Invest an enormous amount of work into finding a total ordering on permutation groups that extends the subgroup lattice.

Since I doubt that 3. is mathematically possible (and even if it is, it would probably be unfeasible), I think we should chose 2.

What do you think?

Sidenote:
Working on this patch, I found that the method `is_subgroup()` does not rely on gap's `IsSubgroup`. Instead, it tests if any element of the first group is element of the second group. 
And the element containment test (G.has_element(g)) also does not directly rely on Gap. Instead, the list of all elements of G is created (but not cached), and it is tested whether g is on this list.

It seems to me that `IsSubgroup` is much faster than {{{is_subgroup}}, hence I suggest that the latter should be rewritten. But this will be a different ticket.


---

Comment by SimonKing created at 2009-04-21 09:37:15

Replying to [comment:21 SimonKing]:
> The new patch (relative to sage-3.4.1.rc3) now relies on gap's `IsSubgroup`.
...
> It seems to me that `IsSubgroup` is much faster than {{{is_subgroup}}, hence I suggest that the latter should be rewritten. But this will be a different ticket.

Done, the ticket is #5844 -- [with patch, needs review], hint hint...

To my surprise, after applying #5844, `is_subgroup` seems _faster_ then `IsSubgroup`. Hence, as soon as #5844 is merged, I suggest to change `IsSubgroup` into `is_subgroup` and avoid the call to Gap.

I do not change the tag into [with patch, needs work], since the present patch fixes a bug and does _not_ depend on #5844. The change after inclusion of #5844 is only about performance, and should probably be on a different ticket.


---

Comment by wdj created at 2009-04-21 10:19:12

Thanks. I'll look at both these, #5844 and #5664. Unfortunately I have a lot of grading to do first but hopefully will get to them today.


---

Comment by wdj created at 2009-04-25 12:46:05

Applies in 3.4.1.rc3 on top of the patch from #5844. 
Passes tests (there were however a lot of unrelated failures)
and does what it claims to do. Thanks for working 
on this Simon!

I will also run tests on this patch using 3.4.2.a0 and report back.


---

Comment by wdj created at 2009-04-25 17:36:54

Applies to 3.4.2.a0 on a ubuntu amd64 8.10 machine and passes all tests.


---

Comment by mabshoff created at 2009-05-13 19:04:49

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 19:04:49

Resolution: fixed
