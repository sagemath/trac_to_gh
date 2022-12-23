# Issue 3695: factor?? improved

Issue created by migration from https://trac.sagemath.org/ticket/3695

Original creator: certik

Original creation time: 2008-07-21 18:37:49

Assignee: gfurnish

See the patch.


---

Attachment

REFEREE:

Looks good. It is also safe to apply to sage-3.0.6 even since it contains no new doctests and no new source code.


---

Comment by mabshoff created at 2008-07-21 18:59:01

Merged in Sage 3.0.6.rc0


---

Comment by mabshoff created at 2008-07-21 18:59:01

Resolution: fixed


---

Comment by cremona created at 2008-07-21 19:44:30

I was not quick enough to catch this before it got merged.  I think that for integers it is a little misleading to describe the output as a sorted list of pairs (p,e): it is a more sophisticated structure:

```
sage: n=-100          
sage: f=factor(n)     
sage: type(f)
<class 'sage.structure.factorization.Factorization'>
```

which has a number of associated methods:

```
sage: f.
f.base_ring       f.dumps           f.prod            f.simplify        f.value
f.category        f.expand          f.rename          f.sort            f.version
f.db              f.is_commutative  f.reset_name      f.unit            
f.dump            f.plot            f.save            f.unit_part     
```

It is true that you can get a list of pairs (p,e):

```
sage: list(f)
[(2, 2), (5, 2)]
```

but that misses the unit part:

```
sage: f.unit()
-1
```

as well as three different ways of recovering the factored integer (prod, expand, value).


---

Comment by certik created at 2008-07-21 19:49:52

Thanks John for noticing. I just copied the old docstring for integers, assuming it was correct. So I think this patch is not a regression.


---

Comment by cremona created at 2008-07-21 19:54:05

Replying to [comment:4 certik]:
> Thanks John for noticing. I just copied the old docstring for integers, assuming it was correct. So I think this patch is not a regression.

No, I was not accusing you of breaking anything!

As factorization of integers is something which new users (e.g. in elementary number theory classes) will want to do -- and something which Sage does very well -- I think it is worth improving the docstring for integers. 

I'll add a new patch (to be applied after yours) in a few minutes.


---

Comment by cremona created at 2008-07-21 20:13:28

Extra documentation added as promised.

I know this is not the first time I have edited this docstring;  sorry not to have done it well enough last time!


---

Comment by mabshoff created at 2008-07-21 20:26:08

There is a slight typo in John's patch:

```
A Factorization contains bothe the 
```


Cheers,

Michael


---

Attachment

Replying to [comment:7 mabshoff]:
> There is a slight typo in John's patch:
> {{{
> A Factorization contains bothe the 
> }}}
> 
> Cheers,
> 
> Michael


I fixed that by text-editing the patch file and re-uploading it in place of the original (of mine).  I hope that works....


---

Comment by malb created at 2008-07-21 20:42:17

I only looked ad John's patch and it looks good.


---

Comment by mabshoff created at 2008-07-21 20:48:54

Replying to [comment:8 cremona]:
> 
> I fixed that by text-editing the patch file and re-uploading it in place of the original (of mine).  I hope that works....

Hi John,

that is perfectly fine and the patch did apply as expected.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 20:50:54

Merged factor_docstring_extra.patch in Sage 3.0.6.rc0
