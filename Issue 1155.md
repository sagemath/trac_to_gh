# Issue 1155: PermutationGroup coercion bug

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-11-12 15:24:03

Assignee: wdj

CC:  sage-combinat

Keywords: GAP, permutation group

The patch 
http://sage.math.washington.edu/home/wdj/patches/permgp-2007-11-12.hg
fixes a bug reported by Carlo H. Part of his email is pasted below:

+++++++++++++++++++++++++++++++++++++++++++++++

Hi,

I'm doing some work with groups. Using gap.Image() I can get a
permutation like this:

```
sage: x
(1,2)(3,7)(4,6)(5,8)
```

But to make a permutation group out of this element I have to enclose
the x in two sets of brackets:

```
sage: PermutationGroup([This is the Trac macro *x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x-macro))
Permutation Group with generators [(1,2)(3,7)(4,6)(5,8)]
```

On the other hand, the following command fails (see below for code and output):

```
sage: PermutationGroup([x])
```

In my mind the second version is clearer - x is a permutation so [x]
is a list of permutations and I should be able to use that to get a
group.

Should SAGE do a coercion here, or am I doing something in a strange way?

Code and output:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.11, Release Date: 2007-11-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: p = 2
sage: assert is_prime(p)
sage:
sage: F = gap.new("FreeGroup(3)")
sage:
sage: a = F.gen(1)
sage: b = F.gen(2)
sage: c = F.gen(3)
sage:
sage: rels = []
sage: rels.append( a**Integer(p) )
sage: rels.append( b**Integer(p) )
sage: rels.append( c**Integer(p) )
sage: rels.append( a*b*((b*a*c)**Integer(-1)) )
sage: rels.append( c*a*((a*c)**Integer(-1)) )
sage: rels.append( c*b*((b*c)**Integer(-1)) )
sage:
sage: N = gap.NormalClosure(F, gap.Subgroup(F, rels))
sage: niso = gap.NaturalHomomorphismByNormalSubgroupNC(F, N)
sage:
sage: x = gap.Image(niso, a)
sage: x
(1,2)(3,7)(4,6)(5,8)
sage: PermutationGroup([This is the Trac macro *x* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x-macro))
Permutation Group with generators [(1,2)(3,7)(4,6)(5,8)]
sage:
sage: PermutationGroup([x])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

```






---

Comment by cwitty created at 2007-11-27 05:08:53

This patch doesn't feel right to me; it seems like it's fixing the problem at the wrong level.  (For instance, it sometimes breaks if you try to create a permutation group from a list of generators where some of the generators are Python lists and some are Gap permutation group elements.  Maybe that's too strange a case to worry about?)

I haven't tried it, but it looks like adding a special case to gap_format() for Gap permutation group elements would also fix the problem, perhaps in a better way?


---

Comment by cwitty created at 2007-11-27 05:09:34

Also, there are no doctests in the patch.


---

Comment by mhansen created at 2007-12-06 03:47:01

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 03:47:01

Changing assignee from wdj to mhansen.


---

Comment by mhansen created at 2007-12-06 03:47:01

I've put a new patch up.


---

Attachment


---

Comment by cwitty created at 2008-01-27 02:24:29

Code looks good; doctest passes.


---

Comment by mabshoff created at 2008-01-27 02:34:37

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 02:34:37

Merged in Sage 2.10.1.rc1
