# Issue 4521: Trivial permutation group enumeration bug

Issue created by migration from https://trac.sagemath.org/ticket/4521

Original creator: kohel

Original creation time: 2008-11-14 09:05:07

Assignee: joyner

CC:  saliola mhansen knsam

1. This gives an error:

sage: G = PermutationGroup([])
sage: G.list()

2. Permutation group should take an argument for the degree, e.g.:

sage: G = PermutationGroup([],degree=4)

3. Permutation group should set the degree correctly:

sage: G = PermutationGroup([[]])
sage: 
sage: G.list()
[()]
sage: G.degree()
1
sage: G = PermutationGroup([This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro))
sage: G.degree()
1

The first group should have degree 0. 

3. Degree 0 should really be supported or 
we will have difficulties with automorphism 
groups of boundary cases.  Currently this 
gives an error:

sage: SymmetricGroup(0)

Certainly these examples should go into the 
docstrings.
Most of these can be trivially fixed, but 
it would be good if someone could review 
permutation groups with a view to catching 
these problems before they arise.


---

Comment by saliola created at 2008-11-20 23:49:47

I took a quick look at the code today and I've come away with a bunch of questions.

(1) Can you post the definition of degree? In the current code, degree it is set equal to largest_moved_point, which grabs the value from gap's LargestMovedPoint if it isn't properly set. But this doesn't seem to agree with some of the things mentioned above.

(2) Which group should the following command return?

```
sage: G = PermutationGroup([],degree=4)
```


(3) The following two groups are isomorphic:

```
sage: G = PermutationGroup([[]]) 
sage: G = PermutationGroup([ [1] ])
```

This is because

```
sage: PermutationGroupElement([]).list()
[1]
sage: PermutationGroupElement([1]).list()
[1]
```

So I'm not sure why one group should have degree 0 while the other does not.

(4) What should the degrees of SymmetricGroup(0) and SymmetricGroup(1) be? Should SymmetricGroup(0) == SymmetricGroup(1)?

I think these are all my questions for now.


---

Comment by knsam created at 2013-02-19 16:49:10

Changing status from new to needs_info.


---

Comment by knsam created at 2013-02-19 17:09:29

I have not looked into any standard references on the permutation groups, but, I'd think that degree of a permutation group should be the cardinality of the maximal set on which the group acts transitively. I'll try to look into the references tomorrow in the library. 

This seems to resolve a couple of things, about the degree. I really don't know what should (2) return, perhaps an error? :)


---

Comment by vdelecroix created at 2019-10-28 14:44:40

This is a bug

```
sage: PermutationGroupElement([]).list()
[1]
```

`PermutationGroupElement([])` should really be the unique permutation of the empty set.


---

Comment by vdelecroix created at 2019-10-28 14:48:59

Changing status from needs_info to needs_work.


---

Comment by embray created at 2020-01-06 14:10:03

Ticket retargeted after milestone closed


---

Comment by mkoeppe created at 2020-04-14 19:41:51

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.
