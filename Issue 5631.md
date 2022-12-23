# Issue 5631: improve doctest coverage for schemes/generic/affine_space.py

Issue created by migration from https://trac.sagemath.org/ticket/5631

Original creator: AlexGhitza

Original creation time: 2009-03-29 07:59:52

Assignee: was

Keywords: doctest affine space

The attached patch improves the doctest coverage of `affine_space.py` from 45% (9 of 20) to 80% (16 of 20) and fixes a few tiny bugs along the way.



---

Comment by AlexGhitza created at 2009-03-29 08:17:35

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-03-29 08:17:44

Changing status from new to assigned.


---

Comment by was created at 2009-03-29 17:15:28

I don't understand why you deleted lines 415, 416 below:

```
414	505	    def subscheme_complement(self, X, Y): 
415	 	        X = self.subscheme(X) 
416	 	        Y = self.subscheme(Y) 
```


The way you have the code now, it subscheme_complement has nothing at all to do with self.  Why is it even a method of self as is now.  

Otherwise this patch looks very good.


---

Comment by AlexGhitza created at 2009-03-29 21:15:10

I had two problems with lines 415 and 416: (1) the doctest that I wrote wasn't working and (2) they aren't there in the corresponding method in `projective_space.py`.  If you look at the docstring that I wrote for `subscheme_complement` (and the doctest), you will notice that X and Y are already subschemes of self (so self is involved in a slightly hidden way).

I guess that one could relax the syntax so that polynomial lists can be passed to `subscheme_complement`; in the example of the doctest this would be


```
sage: A.<x, y, z> = AffineSpace(3, ZZ)
sage: A.subscheme_complement([x+y-z], [x-y+z])
```


Is this what you have in mind?


---

Comment by was created at 2009-03-30 00:06:46

> If you look at the docstring that I wrote for subscheme_complement 
> (and the doctest), you will notice that X and Y are already subschemes 
> of self (so self is involved in a slightly hidden way). 

Couldn't I do this:

```
sage: A.<x, y, z> = AffineSpace(3, ZZ)
sage: [[make an X and a Y over GF(7) say that haven't nothing to do with A]]
sage: A.subscheme_complement(X, Y)
```


Either subscheme_complement needs to check that X and Y are really subschemes of A, or it should just be a method of X, i.e.,

```
sage: X.complement(Y)
```

say, which requires that X and Y live in a common ambient space.

 -- William


---

Comment by AlexGhitza created at 2009-03-30 21:43:31

So I looked at algebraic_scheme.py and noticed that there is a method `X.exclude(Y)` which seems to want to do what you're suggesting.  It's actually broken as it is, and I doubt that it ever worked (no doctests, not used anywhere in the Sage library, and the simplest tests that I thought of didn't work).  So I'm renaming it to `X.complement(Y)` and removing `subscheme_complement()` from both `affine_space.py` and `projective_space.py`.  They are also not used anywhere.


---

Attachment


---

Comment by was created at 2009-04-10 05:28:19

Can you rebase it?  Or does it depends on something?  I can't apply it:

```
teragon:build wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch')
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5631/trac_5631.patch
Loading: [..]
cd "/Users/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/Users/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/Users/wstein/build/sage-3.4.1.rc1/devel/sage" && hg import   "/Users/wstein/.sage/temp/teragon.local/86960/tmp_1.patch"
applying /Users/wstein/.sage/temp/teragon.local/86960/tmp_1.patch
patching file sage/schemes/generic/affine_space.py
Hunk #4 FAILED at 208
Hunk #5 succeeded at 243 with fuzz 2 (offset 0 lines).
Hunk #6 FAILED at 264
2 out of 8 hunks FAILED -- saving rejects to file sage/schemes/generic/affine_space.py.rej
abort: patch failed to apply
sage: 
| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |
```



---

Attachment

apply instead of the previous patch


---

Comment by AlexGhitza created at 2009-04-10 08:24:47

Yes, there was some interaction with the ticket that fixed dimension issues.

The new patch applies to 3.4.1.rc1.


---

Comment by mabshoff created at 2009-04-12 21:33:05

Merged trac_5631_rebased.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-12 21:33:05

Resolution: fixed
