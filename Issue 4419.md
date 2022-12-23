# Issue 4419: [with patch, needs review] conversion of Permutations to GAP not implemented

Issue created by migration from https://trac.sagemath.org/ticket/4419

Original creator: mhansen

Original creation time: 2008-11-02 00:17:11

Assignee: mhansen

CC:  sage-combinat

The following fails 

```
sage: p = gap(Permutation('(1,2,3)'))
sage: q = gap(Permutation([()]))
sage: gap.Group([p, q])
```

because 

```
sage: gap(Permutation((1,2,3)))
[ 2 3 1 ]
```



---

Attachment

I don't see how this fixes the original problem. I get this:


```
sage: p = gap(Permutation('(1,2,3)'))                                                                                              
sage: q = gap(Permutation('()'))                                                                                       
---------------------------------------------------------------------------                                            
ValueError                                Traceback (most recent call last)
<snip>


ValueError: invalid literal for int() with base 10: ''
```


and this:


```
sage: q = gap(Permutation(()))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<snip>

TypeError: not enough arguments for format string
```


It seems to me you want Permutation to work like
PermutationGroupElement does here:

```
sage: p = gap(PermutationGroupElement('(1,2,3)'))
sage: q = gap(PermutationGroupElement('()'))
sage: gap.Group([p, q])
Group( [ (1,2,3), () ] )
sage: gap.Group([p]) == gap.Group([p, q])
True
```

Is that correct?


---

Comment by mhansen created at 2008-11-02 03:07:06

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-02 03:07:06

Actually, the original issue was this:


```
sage: p = gap(Permutation('(1,2,3)'))
sage: q = gap(Permutation([()]))
sage: gap.Group([p, q])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
```


Those things that you encountered are "bugs" in the constructor of Permutation.  I always construct Permutations from their list notation.


---

Comment by saliola created at 2008-11-20 20:41:28

This patch should get a positive review because it fixes the conversion to gap problem:


```
sage: p = Permutation('(1,2,3)')
sage: q = Permutation([()])
sage: gap.Group([p,q])
Group( [ (1,2,3), () ] )
```


The other issues noticed by wdj are problems with the Permutations constructor function, and I will open a new ticket for them.


---

Comment by saliola created at 2008-11-20 20:47:59

The new ticket is here: #4569


---

Comment by mabshoff created at 2008-11-21 10:56:12

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 10:56:12

Merged in Sage 3.2.1.alpha0
