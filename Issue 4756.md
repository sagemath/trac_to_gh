# Issue 4756: eigenmatrix_right totally broken

archive/issues_004756.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\n\n```\nsage: a = matrix(CDF,2,[1,2,4,7])\nsage: a.eigenmatrix_right()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/<ipython console> in <module>()\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenmatrix_right (sage/matrix/matrix2.c:18170)()\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.eigenmatrix_left (sage/matrix/matrix2.c:17965)()\n\nIndexError: list index out of range\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4756\n\n",
    "created_at": "2008-12-11T05:11:14Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "eigenmatrix_right totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4756",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/4756





---

archive/issue_comments_036016.json:
```json
{
    "body": "This is because the eigenvectors_left and eigenvectors_right for CDF and RDF matrices returns the data in a way that is totally incompatible with what the parent is expecting.\n\nI can make a patch for this once I have a 3.2.2alpha1 build.  Otherwise, if Jason would like to do this, I wouldn't object :-)",
    "created_at": "2008-12-11T08:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36016",
    "user": "mhansen"
}
```

This is because the eigenvectors_left and eigenvectors_right for CDF and RDF matrices returns the data in a way that is totally incompatible with what the parent is expecting.

I can make a patch for this once I have a 3.2.2alpha1 build.  Otherwise, if Jason would like to do this, I wouldn't object :-)



---

archive/issue_comments_036017.json:
```json
{
    "body": "Patch causes `left_eigenvectors()` and `right_eigenvectors()` for CDF and RDF to return eigenvalues and eigenvectors in the same format as for exact matrices.  Then eigenmatrices for these matrices behave as they should.  No attempt is made to identify eigenvalues with multiplicity greater than one.\n\nPatch is failing doctests in the modular form code right now, so will need some more work.",
    "created_at": "2010-01-19T02:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36017",
    "user": "rbeezer"
}
```

Patch causes `left_eigenvectors()` and `right_eigenvectors()` for CDF and RDF to return eigenvalues and eigenvectors in the same format as for exact matrices.  Then eigenmatrices for these matrices behave as they should.  No attempt is made to identify eigenvalues with multiplicity greater than one.

Patch is failing doctests in the modular form code right now, so will need some more work.



---

archive/issue_comments_036018.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-19T02:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36018",
    "user": "rbeezer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_036019.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-19T02:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36019",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_036020.json:
```json
{
    "body": "Self-contained patch, apply only this",
    "created_at": "2010-01-23T23:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36020",
    "user": "rbeezer"
}
```

Self-contained patch, apply only this



---

archive/issue_comments_036021.json:
```json
{
    "body": "Attachment\n\nThis patch fixes the bug and generally brings double-precision eigenvectors up-to-date.\n\n`left_eigenvectors` and `right_eigenvectors` now return their results in the same format as for exact matrices, so routines like `eigenmatrix_right` can digest the results properly.\n\nConsequently, `eigenspaces_left` was adjusted for this new format.  There was no `eigenspaces_right`, now there is.\n\nThe changed code in `modular/modform/numerical.py` simply adjusts for the new format to allow doctests to pass and is probably sub-optimal.  There is a bug nearby, so this will be addressed on #8018.\n\nDoctests:  I had some strange behavior for zero eigenvalues (ie very, very small eigenvalues), so the doctests avoid these.  For these eigenvalues, the tests would fail on a first run, but would pass on all subsequent runs (or vice-versa).  This was observed on my own machine and  boxen.math.washington.edu.  So I've avoided these eigenvalues by selecting certain ones in the doctests.\n\nDocumentation:  documentation was tested for these four functions via notebook introspection.  The rest of the file needs attention before it can go into the documentation, see #8046.",
    "created_at": "2010-01-23T23:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36021",
    "user": "rbeezer"
}
```

Attachment

This patch fixes the bug and generally brings double-precision eigenvectors up-to-date.

`left_eigenvectors` and `right_eigenvectors` now return their results in the same format as for exact matrices, so routines like `eigenmatrix_right` can digest the results properly.

Consequently, `eigenspaces_left` was adjusted for this new format.  There was no `eigenspaces_right`, now there is.

The changed code in `modular/modform/numerical.py` simply adjusts for the new format to allow doctests to pass and is probably sub-optimal.  There is a bug nearby, so this will be addressed on #8018.

Doctests:  I had some strange behavior for zero eigenvalues (ie very, very small eigenvalues), so the doctests avoid these.  For these eigenvalues, the tests would fail on a first run, but would pass on all subsequent runs (or vice-versa).  This was observed on my own machine and  boxen.math.washington.edu.  So I've avoided these eigenvalues by selecting certain ones in the doctests.

Documentation:  documentation was tested for these four functions via notebook introspection.  The rest of the file needs attention before it can go into the documentation, see #8046.



---

archive/issue_comments_036022.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T01:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36022",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036023.json:
```json
{
    "body": "Great job!\n\nI think these changes would make the code easier to read:\n\n\n```\n \t662\t        for k in range(len(spectrum)): \n \t663\t            evalue = spectrum[k][0] \n \t664\t            evector = spectrum[k][1][0] \n \t665\t            pairs.append((evalue, evector.parent().span_of_basis([evector],check=False))) \n\nchanged to\n\nfor eval,evectors in spectrum:\n    evec = evectors[0]\n    evector = evec.parent().span_of_basis([evec],check=False)\n    pairs.append((evalue, evector))\n\n```\n\n\n(similarly on lines 722-725)\n\nAlso:\n\n\n```\nB = matrix(CDF, [spectrum[i][1][0] for i in range(len(spectrum))]).transpose() \n\nchanged to\n\nB = matrix(CDF, [evecs[0] for _,evecs in spectrum]).transpose() \n\n```\n",
    "created_at": "2010-01-24T01:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36023",
    "user": "jason"
}
```

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

archive/issue_comments_036024.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-24T01:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36024",
    "user": "jason"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_036025.json:
```json
{
    "body": "Jason,\n\nThanks for helping me be more Pythonic.\n\nThe bit in the modular form module is going to be replaced in #8018 by totally different code, so I didn't change that.  First suggestion (in spirit) has been incorporated in updated patch.\n\nRob",
    "created_at": "2010-01-24T04:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36025",
    "user": "rbeezer"
}
```

Jason,

Thanks for helping me be more Pythonic.

The bit in the modular form module is going to be replaced in #8018 by totally different code, so I didn't change that.  First suggestion (in spirit) has been incorporated in updated patch.

Rob



---

archive/issue_comments_036026.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T04:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36026",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036027.json:
```json
{
    "body": "Self-contained patch, apply only this.",
    "created_at": "2010-01-24T04:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36027",
    "user": "rbeezer"
}
```

Self-contained patch, apply only this.



---

archive/issue_comments_036028.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-24T05:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36028",
    "user": "rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_036029.json:
```json
{
    "body": "Attachment\n\nI've got some doctests failing on another machine due to \"zero\" eigenvalues, so I'm going to rework some of the doctests.",
    "created_at": "2010-01-24T05:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36029",
    "user": "rbeezer"
}
```

Attachment

I've got some doctests failing on another machine due to "zero" eigenvalues, so I'm going to rework some of the doctests.



---

archive/issue_comments_036030.json:
```json
{
    "body": "Attachment\n\nSelf conatined",
    "created_at": "2010-01-24T06:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36030",
    "user": "rbeezer"
}
```

Attachment

Self conatined



---

archive/issue_comments_036031.json:
```json
{
    "body": "dot-3 patch has better doctests in it, totally avoiding \"zero\" eigenvalues and \"zero\" entries of eigenvectors.  Apply just this one patch.",
    "created_at": "2010-01-24T06:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36031",
    "user": "rbeezer"
}
```

dot-3 patch has better doctests in it, totally avoiding "zero" eigenvalues and "zero" entries of eigenvectors.  Apply just this one patch.



---

archive/issue_comments_036032.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T06:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36032",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_036033.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-22T00:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36033",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_036034.json:
```json
{
    "body": "Has this been checked on Solaris? \n\nThere's general information about building on Solaris at\n\n http://wiki.sagemath.org/solaris\n\nInformation specifically for 't2' at\n\n http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nBoth the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n\nDave",
    "created_at": "2010-02-22T00:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36034",
    "user": "drkirkby"
}
```

Has this been checked on Solaris? 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave



---

archive/issue_comments_036035.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-17T20:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36035",
    "user": "rbeezer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_036036.json:
```json
{
    "body": "Replying to [comment:10 drkirkby]:\n> Has this been checked on Solaris? \n\nHi Dave,\n\nNot that I know of.  I develop with KUbuntu.\n\nMaybe a reviewer with Solaris experience can put it through its paces.  Totally Python, so I'd guess numerical issues might be the only distinction.\n\nThanks,\nRob",
    "created_at": "2010-03-17T20:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36036",
    "user": "rbeezer"
}
```

Replying to [comment:10 drkirkby]:
> Has this been checked on Solaris? 

Hi Dave,

Not that I know of.  I develop with KUbuntu.

Maybe a reviewer with Solaris experience can put it through its paces.  Totally Python, so I'd guess numerical issues might be the only distinction.

Thanks,
Rob



---

archive/issue_comments_036037.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-04-03T07:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36037",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_036038.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T07:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36038",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036039.json:
```json
{
    "body": "Merged \"trac_4756-double-eigen.3.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36039",
    "user": "jhpalmieri"
}
```

Merged "trac_4756-double-eigen.3.patch" in 4.4.alpha0



---

archive/issue_comments_036040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4756#issuecomment-36040",
    "user": "jhpalmieri"
}
```

Resolution: fixed
