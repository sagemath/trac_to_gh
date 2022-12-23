# Issue 3253: f.jacob() used to work to compute jacobian ideal. Now it doesn't

archive/issues_003253.json:
```json
{
    "body": "Assignee: was\n\nCC:  alexghitza\n\nThe code {{{ # file = singularlocus1.sage\nK = QQ\nR.<x,y,z> = PolynomialRing(K)\nf = x^3 + y^3 + z^3\nJ = f.jacob()*R # Jacobian ideal\nd = J.dimension()\nprint \"f =\", f\nprint \"dimension(Jacobian ideal of f) =\", d\nprint \"projective dimension of singular locus of f =\", d-1 }}}\ngenerates an error:\n\n[chiquito:jc] sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0, Release Date: 2008-04-21                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: load \"singularlocus1.sage\"\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/carlson/.sage/temp/chiquito.lan/9508/_Users_carlson_docs_chiquito__Research_CIMAT_Lectures_sageprogs_singularlocus1_sage_0.py in <module>()\n      7 R = PolynomialRing(K,names=('x', 'y', 'z')); (x, y, z,) = R._first_ngens(Integer(3))\n      8 f = x**Integer(3) + y**Integer(3) + z**Integer(3)\n----> 9 J = f.jacob()*R # Jacobian ideal\n     10 d = J.dimension()\n     11 print \"f =\", f\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'jacob'\nWARNING: Failure executing file: </Users/carlson/.sage/temp/chiquito.lan/9508/_Users_carlson_docs_chiquito__Research_CIMAT_Lectures_sageprogs_singularlocus1_sage_0.py>\n\n\nIt seems that f.jacob() no longer exists.  (for a while it didn't, then it did, now it doesn')\n\nIssue created by migration from https://trac.sagemath.org/ticket/3253\n\n",
    "created_at": "2008-05-18T03:43:31Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "f.jacob() used to work to compute jacobian ideal. Now it doesn't",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3253",
    "user": "jxxcarlson"
}
```
Assignee: was

CC:  alexghitza

The code {{{ # file = singularlocus1.sage
K = QQ
R.<x,y,z> = PolynomialRing(K)
f = x^3 + y^3 + z^3
J = f.jacob()*R # Jacobian ideal
d = J.dimension()
print "f =", f
print "dimension(Jacobian ideal of f) =", d
print "projective dimension of singular locus of f =", d-1 }}}
generates an error:

[chiquito:jc] sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0, Release Date: 2008-04-21                         |
| Type notebook() for the GUI, and license() for information.        |
sage: load "singularlocus1.sage"
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/carlson/.sage/temp/chiquito.lan/9508/_Users_carlson_docs_chiquito__Research_CIMAT_Lectures_sageprogs_singularlocus1_sage_0.py in <module>()
      7 R = PolynomialRing(K,names=('x', 'y', 'z')); (x, y, z,) = R._first_ngens(Integer(3))
      8 f = x**Integer(3) + y**Integer(3) + z**Integer(3)
----> 9 J = f.jacob()*R # Jacobian ideal
     10 d = J.dimension()
     11 print "f =", f

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.multi_polynomial_libsingular' object has no attribute 'jacob'
WARNING: Failure executing file: </Users/carlson/.sage/temp/chiquito.lan/9508/_Users_carlson_docs_chiquito__Research_CIMAT_Lectures_sageprogs_singularlocus1_sage_0.py>


It seems that f.jacob() no longer exists.  (for a while it didn't, then it did, now it doesn')

Issue created by migration from https://trac.sagemath.org/ticket/3253





---

archive/issue_comments_022502.json:
```json
{
    "body": "Hi Jim,\n\nin 2.10.3-rc4 jacob() was changed to gradient() - see #2425 for details. We do not yet have a proper procedure to deprecate/rename functions like that, i.e. the old version would print a warning for a couple months and then be removed. I hope this fixes the issue for you.\n\nI will bring the deprecation issue up on sage-devel again since last time we didn't really have an end result from the discussion and as more people that don't follow development too closely use Sage we want to avoid breaking their code needlessly and if we have to change names it should be clear what caused it and suggest a fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T12:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22502",
    "user": "mabshoff"
}
```

Hi Jim,

in 2.10.3-rc4 jacob() was changed to gradient() - see #2425 for details. We do not yet have a proper procedure to deprecate/rename functions like that, i.e. the old version would print a warning for a couple months and then be removed. I hope this fixes the issue for you.

I will bring the deprecation issue up on sage-devel again since last time we didn't really have an end result from the discussion and as more people that don't follow development too closely use Sage we want to avoid breaking their code needlessly and if we have to change names it should be clear what caused it and suggest a fix.

Cheers,

Michael



---

archive/issue_comments_022503.json:
```json
{
    "body": "What should we do with this ticket? I vote for closing as wontfix since it would be strange to add a jacob method again with a deprecation warning, wouldn't it?",
    "created_at": "2008-08-18T17:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22503",
    "user": "malb"
}
```

What should we do with this ticket? I vote for closing as wontfix since it would be strange to add a jacob method again with a deprecation warning, wouldn't it?



---

archive/issue_comments_022504.json:
```json
{
    "body": "I just encountered this issue myself. I have no problem with what f.gradient() does, but I would like to also have a command f.jacobian_ideal() that returns the ideal rather than the list of partial derivatives. (And I think f.jacobian_ideal() is a better name than f.jacob(), since I think the Sage model is to have long but descriptive names rather than concise but cryptic names for functions.)\n\nSince the original issue from this ticket is resolved, I'm reclassifying this from \"major defect\" to \"minor enhancement\".",
    "created_at": "2008-08-27T14:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22504",
    "user": "kedlaya"
}
```

I just encountered this issue myself. I have no problem with what f.gradient() does, but I would like to also have a command f.jacobian_ideal() that returns the ideal rather than the list of partial derivatives. (And I think f.jacobian_ideal() is a better name than f.jacob(), since I think the Sage model is to have long but descriptive names rather than concise but cryptic names for functions.)

Since the original issue from this ticket is resolved, I'm reclassifying this from "major defect" to "minor enhancement".



---

archive/issue_comments_022505.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-27T14:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22505",
    "user": "kedlaya"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_022506.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-08-27T14:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22506",
    "user": "kedlaya"
}
```

Changing priority from major to minor.



---

archive/issue_comments_022507.json:
```json
{
    "body": "The patch implements Kiran's request.",
    "created_at": "2008-08-27T22:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22507",
    "user": "AlexGhitza"
}
```

The patch implements Kiran's request.



---

archive/issue_comments_022508.json:
```json
{
    "body": "This function should not be implemented for `sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular` but for `sage.rings.polynomial.multi_polynomial.MPolynomial`. The former inherits from the later. I suppose that'd also mean to move `gradient` to `MPolynomial`.",
    "created_at": "2008-08-27T23:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22508",
    "user": "malb"
}
```

This function should not be implemented for `sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular` but for `sage.rings.polynomial.multi_polynomial.MPolynomial`. The former inherits from the later. I suppose that'd also mean to move `gradient` to `MPolynomial`.



---

archive/issue_comments_022509.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-28T03:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22509",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_022510.json:
```json
{
    "body": "Ah, I thought this might come up.  I have replaced the patch with a new one, where I have put a very simple-minded gradient() function in MPolynomial, but it is of course quite a bit slower than the specialized one for MPolynomial_libsingular, so I don't want to remove the latter.  The function jacobian_ideal() is now in MPolynomial.\n\nBTW, if anyone has ideas on how to make the generic gradient() faster in MPolynomial, I would happily implement them.",
    "created_at": "2008-08-28T03:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22510",
    "user": "AlexGhitza"
}
```

Ah, I thought this might come up.  I have replaced the patch with a new one, where I have put a very simple-minded gradient() function in MPolynomial, but it is of course quite a bit slower than the specialized one for MPolynomial_libsingular, so I don't want to remove the latter.  The function jacobian_ideal() is now in MPolynomial.

BTW, if anyone has ideas on how to make the generic gradient() faster in MPolynomial, I would happily implement them.



---

archive/issue_comments_022511.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-08-28T10:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22511",
    "user": "malb"
}
```

Looks good.



---

archive/issue_comments_022512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T12:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22512",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022513.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T12:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3253#issuecomment-22513",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2
