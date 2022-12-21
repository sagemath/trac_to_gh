# Issue 4569: problems with the Permutation constructor function

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-11-20 20:47:04

Assignee: saliola

CC:  sage-combinat

wdj pointed out in the comments to #4419:


```
{{{
sage: p = gap(Permutation('(1,2,3)'))
sage: q = gap(Permutation('()'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip>

ValueError: invalid literal for int() with base 10: ''
}}}

and this:

{{{
sage: q = gap(Permutation(()))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<snip>

TypeError: not enough arguments for format string
}}}

It seems to me you want Permutation to work like
PermutationGroupElement does here:
{{{
sage: p = gap(PermutationGroupElement('(1,2,3)'))
sage: q = gap(PermutationGroupElement('()'))
sage: gap.Group([p, q])
Group( [ (1,2,3), () ] )
sage: gap.Group([p]) == gap.Group([p, q])
True
}}}
```




---

Attachment

patched against 3.2.rc2


---

Comment by saliola created at 2008-11-20 21:51:34

After this patch:

```
sage: Permutation([()])
[1]
sage: Permutation('()')
[1]
```

which agree with PermutationGroupElement:

```
sage: PermutationGroupElement([()]).list()
[1]
sage: PermutationGroupElement('()').list()
[1]
```

and:

```
sage: p = Permutation('(1,2,3)')
sage: q = Permutation('()')
sage: gap.Group([p,q])
Group( [ (1,2,3), () ] )
sage: gap.Group([p]) == gap.Group([p, q])
True
```



---

Comment by mhansen created at 2008-11-21 14:49:36

Looks good.


---

Comment by mhansen created at 2008-11-21 14:49:36

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-21 14:49:36

Changing assignee from saliola to mhansen.


---

Comment by mabshoff created at 2008-11-21 23:43:27

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 23:43:27

Merged in Sage 3.2.1.alpha0
