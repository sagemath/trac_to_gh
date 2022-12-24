# Issue 2075: very serious bug in modules over QQ[x] -- they shouldn't "work" (solution fix defn of echelon form over QQ[x] to raise NotImplementedError)

archive/issues_002075.json:
```json
{
    "body": "Assignee: was\n\nE.g., this is DEFINITELY WRONG -- it directly contradicts how things work over ZZ, and leads to major bugs in the free module code.   This must be changed ASAP.    There can be a method that returns the echelon form over the fraction field, but it must have a different name. \n\n```\nsage: R.<x> = QQ[]\nsage: a = matrix(R, 2, 3, [x,x^2,1,1+x, 1,x])\nsage: a.echelon_form()\n[                             1                              0    (-x^3 + 1)/(-x^3 - x^2 + x)]\n[                             0                              1 (x^2 - x - 1)/(-x^3 - x^2 + x)]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2075\n\n",
    "created_at": "2008-02-06T09:58:01Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "very serious bug in modules over QQ[x] -- they shouldn't \"work\" (solution fix defn of echelon form over QQ[x] to raise NotImplementedError)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2075",
    "user": "was"
}
```
Assignee: was

E.g., this is DEFINITELY WRONG -- it directly contradicts how things work over ZZ, and leads to major bugs in the free module code.   This must be changed ASAP.    There can be a method that returns the echelon form over the fraction field, but it must have a different name. 

```
sage: R.<x> = QQ[]
sage: a = matrix(R, 2, 3, [x,x^2,1,1+x, 1,x])
sage: a.echelon_form()
[                             1                              0    (-x^3 + 1)/(-x^3 - x^2 + x)]
[                             0                              1 (x^2 - x - 1)/(-x^3 - x^2 + x)]
```


Issue created by migration from https://trac.sagemath.org/ticket/2075





---

archive/issue_comments_013420.json:
```json
{
    "body": "It is the default behaviour of Sage to return the echelon form over fraction fields \n\n\n```\n#matrix2.pyx\nif not (R == ZZ or R.is_field()):\n    try:\n        E = self.matrix_over_field()\n    except TypeError:\n        raise NotImplementedError, \"Echelon form not implemented over '%s'.\"%R\n```\n\n\nso this is much more general.\n\nNote, that there is a specialised implementation for multivariate polynomials though:\n\n\n```\nsage: R.<x> = MPolynomialRing(QQ,1)\nsage: a = matrix(R, 2, 3, [x,x^2,1,1+x, 1,x])\nsage: a.echelon_form() # default as above\n[                             1                              0    (-x^3 + 1)/(-x^3 - x^2 + x)]\n[                             0                              1 (x^2 - x - 1)/(-x^3 - x^2 + x)]\n\nsage: a.echelon_form('row_reduction')\n[         x + 1              1              x]\n[-x^3 - x^2 + x              0       -x^3 + 1]\n\nsage: a.echelon_form('bareiss')\n[          x       x + 1           1]\n[          0 x^2 - x - 1     x^3 - 1]\n```\n",
    "created_at": "2008-02-06T10:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13420",
    "user": "malb"
}
```

It is the default behaviour of Sage to return the echelon form over fraction fields 


```
#matrix2.pyx
if not (R == ZZ or R.is_field()):
    try:
        E = self.matrix_over_field()
    except TypeError:
        raise NotImplementedError, "Echelon form not implemented over '%s'."%R
```


so this is much more general.

Note, that there is a specialised implementation for multivariate polynomials though:


```
sage: R.<x> = MPolynomialRing(QQ,1)
sage: a = matrix(R, 2, 3, [x,x^2,1,1+x, 1,x])
sage: a.echelon_form() # default as above
[                             1                              0    (-x^3 + 1)/(-x^3 - x^2 + x)]
[                             0                              1 (x^2 - x - 1)/(-x^3 - x^2 + x)]

sage: a.echelon_form('row_reduction')
[         x + 1              1              x]
[-x^3 - x^2 + x              0       -x^3 + 1]

sage: a.echelon_form('bareiss')
[          x       x + 1           1]
[          0 x^2 - x - 1     x^3 - 1]
```




---

archive/issue_comments_013421.json:
```json
{
    "body": "> It is the default behaviour of Sage to return the echelon form over fraction fields\n\nWell that's TERRIBLE, and needs to be changed ASAP.  It is completely wrong / inconsistent.",
    "created_at": "2008-02-06T20:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13421",
    "user": "was"
}
```

> It is the default behaviour of Sage to return the echelon form over fraction fields

Well that's TERRIBLE, and needs to be changed ASAP.  It is completely wrong / inconsistent.



---

archive/issue_comments_013422.json:
```json
{
    "body": "We ought to sort this out before 2.10.2 is released.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T23:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13422",
    "user": "mabshoff"
}
```

We ought to sort this out before 2.10.2 is released.

Cheers,

Michael



---

archive/issue_comments_013423.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-02-14T23:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13423",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_013424.json:
```json
{
    "body": "There is a nice notion of normal form for matrices over F[x] for any field F which plays a similar role in the theory of modules over such rings to that played by Hermite normal form over Z.  Reduction to that form can be as useful as LLL reduction for Z-lattices.  It has various names including \"weak Popov form\".  It is very easy to implement, atleast naively.  I have used it successfully where F is a finte field (in an application to find rational points on curves defined over F(x)).  However when F is (for example) Q the naive implementation would be about as useful as the Euclidean algorithm for two polynomials in Q[x] -- in fact the algorithm directly generalises this too.  I mean: it is not useful since intermediate expression swell kills it performance-wise.\n\n What's the conclusion?   That there is no simple answer to what is the best form of normal form for matrices over rings.\n\n Can William explain where this is used in the free module code and what the resulting problems are?  If so I might be able to help.  But is this really a blocker for 2.20.2?",
    "created_at": "2008-02-17T22:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13424",
    "user": "cremona"
}
```

There is a nice notion of normal form for matrices over F[x] for any field F which plays a similar role in the theory of modules over such rings to that played by Hermite normal form over Z.  Reduction to that form can be as useful as LLL reduction for Z-lattices.  It has various names including "weak Popov form".  It is very easy to implement, atleast naively.  I have used it successfully where F is a finte field (in an application to find rational points on curves defined over F(x)).  However when F is (for example) Q the naive implementation would be about as useful as the Euclidean algorithm for two polynomials in Q[x] -- in fact the algorithm directly generalises this too.  I mean: it is not useful since intermediate expression swell kills it performance-wise.

 What's the conclusion?   That there is no simple answer to what is the best form of normal form for matrices over rings.

 Can William explain where this is used in the free module code and what the resulting problems are?  If so I might be able to help.  But is this really a blocker for 2.20.2?



---

archive/issue_comments_013425.json:
```json
{
    "body": "YES, this is a blocker.  If you create a free module over QQ[x] with given generators, it replaces the generators by a basis coming from the rows of the \"echelon form\" of the matrix.  It is terrible if the elements in this echelon form aren't even in the QQ[x] span of the original matrix.",
    "created_at": "2008-02-17T22:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13425",
    "user": "was"
}
```

YES, this is a blocker.  If you create a free module over QQ[x] with given generators, it replaces the generators by a basis coming from the rows of the "echelon form" of the matrix.  It is terrible if the elements in this echelon form aren't even in the QQ[x] span of the original matrix.



---

archive/issue_comments_013426.json:
```json
{
    "body": "Attachment [sage-2075.patch](tarball://root/attachments/some-uuid/ticket2075/sage-2075.patch) by malb created at 2008-02-21 20:04:10\n\nSome minor issues:\n\n* in docstring of `_echelonize_ring` `NotImplemenetedError` should get `\\code{`}\n* does `self.dense_matrix()` return `self` if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first\n* What is the status of \"`#not very useful?`\" is that a note to self to fix this or for the user?\n* \"#This code is by Me\" that should be William Stein\n* Erocal Burcin -> Burcin Erocal\n\nExcept those minor things the code looks good. Note, I didn't attempt to apply the patch yet.",
    "created_at": "2008-02-21T20:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13426",
    "user": "malb"
}
```

Attachment [sage-2075.patch](tarball://root/attachments/some-uuid/ticket2075/sage-2075.patch) by malb created at 2008-02-21 20:04:10

Some minor issues:

* in docstring of `_echelonize_ring` `NotImplemenetedError` should get `\code{`}
* does `self.dense_matrix()` return `self` if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first
* What is the status of "`#not very useful?`" is that a note to self to fix this or for the user?
* "#This code is by Me" that should be William Stein
* Erocal Burcin -> Burcin Erocal

Except those minor things the code looks good. Note, I didn't attempt to apply the patch yet.



---

archive/issue_comments_013427.json:
```json
{
    "body": "* in docstring of _echelonize_ring NotImplemenetedError should get \\code{}\n\nYes.\n\n* does self.dense_matrix() return self if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first\n\nYes, it returns self. \n\n* What is the status of \"#not very useful?\" is that a note to self to fix this or for the user?\n\nIt looks WRONG to me.  Shouldn't the second row be removed?!\n\n* \"#This code is by Me\" that should be William Stein\n\nOK.\n\n* Erocal Burcin -> Burcin Erocal \n\nOK. \n\nAny chance you could make the changes you suggest above?  I have to a bunch\nof other stuff today, and don't want to hold up rc1.",
    "created_at": "2008-02-21T20:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13427",
    "user": "was"
}
```

* in docstring of _echelonize_ring NotImplemenetedError should get \code{}

Yes.

* does self.dense_matrix() return self if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first

Yes, it returns self. 

* What is the status of "#not very useful?" is that a note to self to fix this or for the user?

It looks WRONG to me.  Shouldn't the second row be removed?!

* "#This code is by Me" that should be William Stein

OK.

* Erocal Burcin -> Burcin Erocal 

OK. 

Any chance you could make the changes you suggest above?  I have to a bunch
of other stuff today, and don't want to hold up rc1.



---

archive/issue_comments_013428.json:
```json
{
    "body": "fixes most minor issues",
    "created_at": "2008-02-21T20:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13428",
    "user": "malb"
}
```

fixes most minor issues



---

archive/issue_comments_013429.json:
```json
{
    "body": "Attachment [sage-2075.2.patch](tarball://root/attachments/some-uuid/ticket2075/sage-2075.2.patch) by malb created at 2008-02-21 20:50:32\n\n`sage-2075.2.patch` fixes:\n* in docstring of _echelonize_ring NotImplemenetedError should get \\code{} \n* \"#This code is by Me\" that should be William Stein \n* Erocal Burcin -> Burcin Erocal\n\nLeft over:\n* \"does self.dense_matrix() return self if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first  -> Yes, it returns self.\" So it needs no fix\n* \"What is the status of \"#not very useful?\" is that a note to self to fix this or for the user?  ->  It looks WRONG to me. Shouldn't the second row be removed?!\"\n  rowred only considers constants for reduction, not very useful for most applications indeed.\n\nI say apply. If we don't like rowred the way it is, we should (a) rename it and/or (b) fix it in another ticket.",
    "created_at": "2008-02-21T20:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13429",
    "user": "malb"
}
```

Attachment [sage-2075.2.patch](tarball://root/attachments/some-uuid/ticket2075/sage-2075.2.patch) by malb created at 2008-02-21 20:50:32

`sage-2075.2.patch` fixes:
* in docstring of _echelonize_ring NotImplemenetedError should get \code{} 
* "#This code is by Me" that should be William Stein 
* Erocal Burcin -> Burcin Erocal

Left over:
* "does self.dense_matrix() return self if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first  -> Yes, it returns self." So it needs no fix
* "What is the status of "#not very useful?" is that a note to self to fix this or for the user?  ->  It looks WRONG to me. Shouldn't the second row be removed?!"
  rowred only considers constants for reduction, not very useful for most applications indeed.

I say apply. If we don't like rowred the way it is, we should (a) rename it and/or (b) fix it in another ticket.



---

archive/issue_comments_013430.json:
```json
{
    "body": "William, if you redo the patch you should also remove the last hunk since it has already been merged via some other patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T21:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13430",
    "user": "mabshoff"
}
```

William, if you redo the patch you should also remove the last hunk since it has already been merged via some other patch.

Cheers,

Michael



---

archive/issue_comments_013431.json:
```json
{
    "body": "Merged sage-2075.2.patch in Sage 2.10.2.rc0.",
    "created_at": "2008-02-22T01:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13431",
    "user": "mabshoff"
}
```

Merged sage-2075.2.patch in Sage 2.10.2.rc0.



---

archive/issue_comments_013432.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T01:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2075#issuecomment-13432",
    "user": "mabshoff"
}
```

Resolution: fixed
