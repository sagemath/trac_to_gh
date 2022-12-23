# Issue 6631: speed up is_lyndon method for words

Issue created by migration from https://trac.sagemath.org/ticket/6631

Original creator: saliola

Original creation time: 2009-07-26 22:04:26

Assignee: Franco Saliola

CC:  slabbe

Keywords: words

The current implementation of the method `is_lyndon` is too slow

```
sage: c = words.ChristoffelWord(380447,34369)
sage: c
Lower Christoffel word of slope 380447/34369 over Ordered Alphabet [0, 1]
sage: c.length()
414816
sage: time c.is_lyndon()
CPU times: user 84.15 s, sys: 0.17 s, total: 84.33 s
Wall time: 84.52 s
True
```



---

Attachment

DO NOT APPLY!


---

Comment by saliola created at 2009-07-26 22:14:50

Don't apply `trac_6631-is_lyndon.2.patch`, it is a copy of the other, and should be deleted.


---

Comment by saliola created at 2009-07-26 22:16:26

Here is the new timing: 

```
sage: c = words.ChristoffelWord(380447,34369)
sage: time c.is_lyndon()
CPU times: user 1.15 s, sys: 0.00 s, total: 1.15 s
Wall time: 1.15 s
True
```

That's much better.


---

Comment by vdelecroix created at 2009-07-27 09:53:02

The end of the loop can be simplified (there is no break statement in the loop, and we know that j==n at the end).


```
while j < n:
    [...]
else:
    return j - i == n
```


could become:


```
while j < n:
    [...]
return i == 0
```



---

Attachment

depends on #6627;


---

Comment by saliola created at 2009-07-27 10:03:20

Replying to [comment:4 vdelecroix]:
> The end of the loop can be simplified (there is no break statement in the loop, and we know that j==n at the end).
> 
> {{{
> while j < n:
>     [...]
> else:
>     return j - i == n
> }}}
> 
> could become:
> 
> {{{
> while j < n:
>     [...]
> return i == 0
> }}}

Done in the new patch. (If you give this new patch a positive review, then change 'needs review' to 'positive review'.)


---

Comment by mvngu created at 2009-08-25 00:26:15

reviewer patch: fixes typo


---

Attachment

The patch `trac_6631-reviewer.patch` fixes a typo introduced by `trac_6631-is_lyndon.patch`.


---

Comment by mvngu created at 2009-08-25 00:43:20

Merged:

 1. `trac_6631-is_lyndon.patch`
 1. `trac_6631-reviewer.patch`


---

Comment by mvngu created at 2009-08-25 00:43:20

Resolution: fixed
