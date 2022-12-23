# Issue 4383: composition_series() returns no generators for trivial subgroup

Issue created by migration from https://trac.sagemath.org/ticket/4383

Original creator: rbeezer

Original creation time: 2008-10-30 04:02:58

Assignee: somebody

Keywords: composition series, generators

At the tail end of a composition series of a group, the trivial subgroup has no generators, rather than the identity permutation as a generator.  This appears unacceptable to GAP for subsequent computations.

On 3.1.4 built from source on x86.


```
sage: G=CyclicPermutationGroup(2)
sage: comps
```



```
[Permutation Group with generators [(1,2)],
 Permutation Group with generators []]
```



```
sage: comps[1].order()
```



```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/rob/.sage/sage_notebook/worksheets/admin/48/code/5.py", line 7, in <module>
    comps[_sage_const_1 ].order()
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 770, in order
    return Integer(self._gap_().Size())
  File "sage_object.pyx", line 270, in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2442)
  File "sage_object.pyx", line 246, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2186)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
    return cls(self, x, name=name)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1283, in __init__
    raise TypeError, x
TypeError: Gap produced error output
Error, usage: Group(<gen>,...), Group(<gens>), Group(<gens>,<id>)

   executing $sage6:=Group([]);;
```



---

Comment by rbeezer created at 2008-10-30 04:06:41

First bit of code above lost the middle line, which should read


```
sage: comps=G.composition_series()
```



---

Comment by wdj created at 2008-10-30 19:15:06

I'm guessing that this this ticket is not named accurately. 

It appears the problem isn't with the composition series but with the order function:


```
sage: G = PermutationGroup([])
sage: G.order()
ERROR: An unexpected error occurred while tokenizing input
<snip>
```

This will possibly raise the issue of whether the trivial group should be PermutationGroup([]) (as it is now) or PermutationGroup([()]) (for which order works). According to Rotman, the group whose generating set is the empty set is the trivial group, so I think they way we have it is fine. Therefore, I elected to simply fix this bug in the order method. 
Patch attached is based on sage-3.2.alpha1 and pases sage -t.


---

Attachment

based on 3.2.alpha1


---

Comment by mabshoff created at 2008-10-30 19:19:03

This patch needs a doctest.

Please also stick with the standard tags for patches.

Cheers,

Michael


---

Comment by wdj created at 2008-10-30 19:55:16

Sorry - I added a doctest in the 2nd patch. I could not figure out what I did wrong with the tags (whatever they are - I could not find them in http://wiki.sagemath.org/TracGuidelines, but could have easily missed something).


---

Attachment

based on 3.2.alpha1 - apply after the first patch


---

Comment by rbeezer created at 2008-10-31 02:40:21

I agree that a constructor with an empty list should be interpreted as the trivial subgroup, but it seems that passing this to GAP will cause an error.  On 3.1.4 I get a different error message than David, which suggests that GAP doesn't like the construction.

Calling other commands on a group with no generators (such as exponent() or is_simple() or derived_series()), yields an error similar (or identical) to the one from a call to order().

Furthermore, it appears that until recently composition_series() returned a trivial subgroup with the identity element as a generator for the tail end of the series.  For example, see sample output in [3364](http://trac.sagemath.org/sage_trac/ticket/3364).

It seems to me that having the output of one command be acceptable to all subsequent commands is preferable.  The experiment below suggests to me that GAP doesn't like an empty list of generators.



```
sage: gap.eval("G := Group(())")
'Group(())'

sage: gap.eval("G := Group()")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/rob/.sage/sage_notebook/worksheets/admin/48/code/17.py", line 6, in <module>
    gap.eval("G := Group()")
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 404, in eval
    s = Expect.eval(self, x)
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 937, in eval
    return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
  File "/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 627, in _eval_line
    raise RuntimeError, message
RuntimeError: Gap produced error output
Error, usage: Group(<gen>,...), Group(<gens>), Group(<gens>,<id>)

   executing G := Group();
```



---

Comment by wdj created at 2008-10-31 10:05:44

(a) Maybe I'm wrong, I see this as a different issue form the bug you opened the ticket for. 
(b) It seems you are suggesting that all the methods should work for groups constructed using both PermutationGroup([()]) and PermutationGroup([]), and give the same result. This seems reasonable to me. However, it seems like it should be opened as a separate ticket, which a suitably descriptive title.


---

Comment by rbeezer created at 2008-10-31 14:17:20

With regards to (b), I'm suggesting the opposite.  Seems easier, and more consistent, to return composition_series() to its previous behavior, rather than having it generate objects that subsequently GAP cannot digest.  In other words, adjust only the behavior of composition_series().   I am NOT suggesting that all the methods acting on groups be adjusted to accept a trivial subgroup specified with no generators.

So I guess I'm suggesting more broadly that an empty list of generators not be possible (even if it makes sense mathematically).  I don't have enough experience with the other parts of Sage to know how it is handled for other objects (like rings).  But if GAP isn't happy with an empty list, then I think the effort should be made to make sure the output of methods for groups produces items appropriate as input to other commands using GAP to do their work.  Or maybe the interface to GAP should convert empty lists to a list with the identity?  That would be another solution.

One possibility would be to have the constructors for groups recognize and convert an empty list of generators into a list holding just the identity permutation.  But again, I don't have enough experience to know if this would be feasible or desirable.

Rob


---

Comment by wdj created at 2008-11-01 02:07:51

This last patch seems to do what you want.


---

Comment by rbeezer created at 2008-11-01 19:21:19

Thanks, David.

Rob


---

Comment by was created at 2008-11-28 22:37:53

REFEREE REPORT:

Huh?  


* trac_4383-order-trivial-permgp.patch + trac_4383-order-trivial-permgp2.patch  make some sense to me with the second patch fixing a bug introduced in the first and adding doctests.

* trac_4383-order-trivial-permgp3.patch looks to me like exactly the same (?) as the first buggy patch!  So maybe you forgot to attach the right patch?

Please clarify and ping me.


---

Attachment


---

Comment by was created at 2008-11-29 01:49:47

REPORT:

Looks good.   Mabshoff, apply the following patches in order (to 3.2.1.alpha):


```
trac_4383-order-trivial-permgp.patch 
trac_4383-order-trivial-permgp2.patch
trac_4383-order-trivial-permgp3-REBASE.patch
```



---

Attachment


---

Comment by mabshoff created at 2008-11-29 02:27:23

One trivial doctesting failure is to fix:

```
sage -t -long "devel/sage/sage/combinat/designs/incidence_structures.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha3/devel/sage/sage/combinat/designs/incidence_structures.py", line 174:
    sage: G = BD.automorphism_group(); G
Expected:
    Permutation Group with generators []
Got:
    Permutation Group with generators [()]
```



---

Comment by was created at 2008-11-29 02:34:07

Another doctest failure:

```
File "/home/was/build/sage-3.2.1.alpha1/devel/sage-review/sage/combinat/designs/incidence_structures.py", line 174:
    sage: G = BD.automorphism_group(); G
Expected:
    Permutation Group with generators []
Got:
    Permutation Group with generators [()]
```



---

Attachment


---

Comment by mabshoff created at 2008-11-29 03:31:41

Resolution: fixed


---

Comment by mabshoff created at 2008-11-29 03:31:41

Merged

```
trac_4383-order-trivial-permgp.patch 
trac_4383-order-trivial-permgp2.patch
trac_4383-order-trivial-permgp3-REBASE.patch
trac_4383-order-trivial-permgp4.patch
```

in Sage 3.2.1.rc0

Cheers,

Michael
