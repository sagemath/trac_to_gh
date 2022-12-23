# Issue 4756: eigenmatrix_right totally broken

Issue created by migration from https://trac.sagemath.org/ticket/4756

Original creator: was

Original creation time: 2008-12-11 05:11:14

Assignee: was

CC:  jason


```
sage: a = matrix(CDF,2,[1,2,4,7])
sage: a.eigenmatrix_right()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/wstein/sage/build/sage-3.2.2.alpha0/<ipython console> in <module>()

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenmatrix_right (sage/matrix/matrix2.c:18170)()

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenmatrix_left (sage/matrix/matrix2.c:17965)()

IndexError: list index out of range
```



---

Comment by mhansen created at 2008-12-11 08:14:42

This is because the eigenvectors_left and eigenvectors_right for CDF and RDF matrices returns the data in a way that is totally incompatible with what the parent is expecting.

I can make a patch for this once I have a 3.2.2alpha1 build.  Otherwise, if Jason would like to do this, I wouldn't object :-)


---

Comment by rbeezer created at 2010-01-19 02:45:13

Patch causes `left_eigenvectors()` and `right_eigenvectors()` for CDF and RDF to return eigenvalues and eigenvectors in the same format as for exact matrices.  Then eigenmatrices for these matrices behave as they should.  No attempt is made to identify eigenvalues with multiplicity greater than one.

Patch is failing doctests in the modular form code right now, so will need some more work.


---

Comment by rbeezer created at 2010-01-19 02:45:13

Changing status from new to needs_work.


---

Attachment


---

Comment by rbeezer created at 2010-01-23 23:30:28

Self-contained patch, apply only this


---

Attachment

This patch fixes the bug and generally brings double-precision eigenvectors up-to-date.

`left_eigenvectors` and `right_eigenvectors` now return their results in the same format as for exact matrices, so routines like `eigenmatrix_right` can digest the results properly.

Consequently, `eigenspaces_left` was adjusted for this new format.  There was no `eigenspaces_right`, now there is.

The changed code in `modular/modform/numerical.py` simply adjusts for the new format to allow doctests to pass and is probably sub-optimal.  There is a bug nearby, so this will be addressed on #8018.

Doctests:  I had some strange behavior for zero eigenvalues (ie very, very small eigenvalues), so the doctests avoid these.  For these eigenvalues, the tests would fail on a first run, but would pass on all subsequent runs (or vice-versa).  This was observed on my own machine and  boxen.math.washington.edu.  So I've avoided these eigenvalues by selecting certain ones in the doctests.

Documentation:  documentation was tested for these four functions via notebook introspection.  The rest of the file needs attention before it can go into the documentation, see #8046.


---

Comment by rbeezer created at 2010-01-24 01:14:06

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-01-24 01:38:41

Great job!

I think these changes would make the code easier to read:


```
 	662	        for k in range(len(spectrum)): 
 	663	            evalue = spectrum[k][0] 
 	664	            evector = spectrum[k][1][0] 
 	665	            pairs.append((evalue, evector.parent().span_of_basis([evector],check=False))) 

changed to

for eval,evectors in spectrum:
    evec = evectors[0]
    evector = evec.parent().span_of_basis([evec],check=False)
    pairs.append((evalue, evector))

```


(similarly on lines 722-725)

Also:


```
B = matrix(CDF, [spectrum[i][1][0] for i in range(len(spectrum))]).transpose() 

changed to

B = matrix(CDF, [evecs[0] for _,evecs in spectrum]).transpose() 

```



---

Comment by jason created at 2010-01-24 01:39:34

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-01-24 04:22:22

Jason,

Thanks for helping me be more Pythonic.

The bit in the modular form module is going to be replaced in #8018 by totally different code, so I didn't change that.  First suggestion (in spirit) has been incorporated in updated patch.

Rob


---

Comment by rbeezer created at 2010-01-24 04:22:22

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-01-24 04:22:58

Self-contained patch, apply only this.


---

Comment by rbeezer created at 2010-01-24 05:13:23

Changing status from needs_review to needs_work.


---

Attachment

I've got some doctests failing on another machine due to "zero" eigenvalues, so I'm going to rework some of the doctests.


---

Attachment

Self conatined


---

Comment by rbeezer created at 2010-01-24 06:36:25

dot-3 patch has better doctests in it, totally avoiding "zero" eigenvalues and "zero" entries of eigenvectors.  Apply just this one patch.


---

Comment by rbeezer created at 2010-01-24 06:36:25

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-22 00:16:43

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-02-22 00:16:43

Has this been checked on Solaris? 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by rbeezer created at 2010-03-17 20:57:30

Changing status from needs_info to needs_review.


---

Comment by rbeezer created at 2010-03-17 20:57:30

Replying to [comment:10 drkirkby]:
> Has this been checked on Solaris? 

Hi Dave,

Not that I know of.  I develop with KUbuntu.

Maybe a reviewer with Solaris experience can put it through its paces.  Totally Python, so I'd guess numerical issues might be the only distinction.

Thanks,
Rob


---

Comment by AlexGhitza created at 2010-04-03 07:41:35

Looks good to me.


---

Comment by AlexGhitza created at 2010-04-03 07:41:35

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:12:15

Merged "trac_4756-double-eigen.3.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:12:15

Resolution: fixed
