# Issue 3623: Factory and pickling framework (part of coercion branch)

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-07-09 08:03:41

Assignee: robertwb

Uniqueness of parents makes Sage operate much more smoothly. This leads to an enormous amount of nearly identical caching code scattered throughout the library. This factory handles all the caching for you, and also provides a good pickling mechanism. 


---

Comment by robertwb created at 2008-07-09 08:16:34

Code documented and works great/passes tests. Just need some doctests in factory.pyx (perhaps via a fake test class?)


---

Comment by anakha created at 2008-09-06 15:54:02

Needs to be rebased against 3.1.2.alpha4:


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-2.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-2.patch?format=raw
Loading: [....]
cd "/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage" && hg import   "/Users/anakha/.sage/temp/fullmetal.umn/58245/tmp_1.patch"
applying /Users/anakha/.sage/temp/fullmetal.umn/58245/tmp_1.patch
patching file sage/modules/free_module.py
Hunk #1 FAILED at 157
Hunk #2 FAILED at 261
2 out of 2 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
abort: patch failed to apply
```


Otherwise, I like this very much after having gone through the pain of implementing a unique factory for a parent already, I would have wasted a week less if this had already been in sage.


---

Comment by robertwb created at 2008-09-08 16:26:21

Thanks. I'll rebase this as soon as 3.1.2 comes out (as I doubt this ticket will make it into there).


---

Attachment


---

Attachment


---

Attachment

All four patches rebased.


---

Attachment


---

Comment by was created at 2008-11-28 21:36:39

Hi Robert,

This bitrotted again.  Sorry!

```
was`@`sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-1.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-1.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/14985/tmp_0.patch"
applying /home/was/.sage/temp/sage/14985/tmp_0.patch
patching file setup.py
Hunk #1 FAILED at 533
1 out of 1 hunk FAILED -- saving rejects to file setup.py.rej
abort: patch failed to apply
sage: 
```

| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
Can you rebase it an email me asap so this can get properly refereed and *not* bitrot again.


---

Comment by robertwb created at 2008-12-02 12:37:34

patches 1-5 folded and rebased onto 3.2.1


---

Attachment

OK, this is once again rebased.


---

Comment by mabshoff created at 2008-12-02 15:46:15

The patch applies cleanly against 3.2.1 and together with #4276 I am seeing two doctest failures:

```
sage -t -long "devel/sage/sage/structure/coerce.pyx"        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx", line 862:
    sage: V is W
Expected:
    False
Got:
    True
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx", line 865:
    sage: cm.coercion_maps(V, W)
Expected:
    (None,
     Call morphism:
      From: Vector space of dimension 3 over Rational Field
      To:   Vector space of dimension 3 over Rational Field)
Got:
    (None, None)
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx", line 870:
    sage: cm.coercion_maps(W, V)
Expected:
    (None,
     Call morphism:
      From: Vector space of dimension 3 over Rational Field
      To:   Vector space of dimension 3 over Rational Field)
Got:
    (None, Free module morphism defined by the matrix
    [1 0 0]
    [0 1 0]
    [0 0 1]
    Domain: Vector space of dimension 3 over Rational Field
    Codomain: Vector space of dimension 3 over Rational Field)
**********************************************************************
1 items had failures:
   3 of  21 in __main__.example_15
***Test Failed*** 3 failures.
```

I guess the first one is worrying while the rest is mostly a printing issue.

The other failure is:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_number_field.py", line 667:
    sage: [E.tamagawa_exponent(P) for P in K(11).support()]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[7]>", line 1, in <module>
        [E.tamagawa_exponent(P) for P in K(Integer(11)).support()]###line 667:
    sage: [E.tamagawa_exponent(P) for P in K(11).support()]
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 675, in tamagawa_exponent
        return self.local_data(P, proof).tamagawa_exponent()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 401, in local_data
        return self._get_local_data(P,proof)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 418, in _get_local_data
        self._local_data[P] = EllipticCurveLocalData(self, P, proof)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 140, in __init__
        self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 528, in _tate
        r = -pinv(12*c4) * (c6 + b2 * c4)
      File "element.pyx", line 1074, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:8580)
      File "coerce.pyx", line 697, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5808)
    TypeError: unsupported operand parent(s) for '*': 'Maximal Order in Number Field in a with defining polynomial x^2 + 11' and 'Number Field in a with defining polynomial x^2 + 11'
**********************************************************************
```


Cheers,

Michael


---

Attachment

apply after 3623-3.2.1-all.patch


---

Comment by robertwb created at 2008-12-02 20:20:23

OK, I fixed the doctests in coerce.pyx. The issue was that loads(dumps(V)) wasn't returning a new object anymore (this is *good*) so it wasn't testing what I wanted to test (equal but not identical parents). 

The other one is almost certainly due to #4276, looking into that now.


---

Comment by mabshoff created at 2008-12-02 21:05:39

3623-fix.patch does indeed fix the problem and seem to not have any side effects, i.e. the doctest failure in ell_number_field.py is still there. No additional doctests did fail.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 11:56:59

Ok, since 3623-all-3.2.1.patch and 3623-fix.patch + the two patches from #4276 make all tests pass I am giving this a positive review. There might still be issues here, so if anyone does take a closer look please open another ticket. The cost of this bitrotting is too high, so if this blows up there is only me and not Robert to blame.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 11:57:20

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-04 11:57:20

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 12:00:49

One last remark: A couple doctests for the various "create_key" methods would be nice, but that can be done via a new ticket.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-04 20:09:04

Thanks you. This one is a real pain to rebase, and I've wanted to use it elsewhere too. 

Note that Mike Hansen did look at these during Sage Days 10, and the response was generally positive (though not formal).
