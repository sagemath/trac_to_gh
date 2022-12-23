# Issue 7119: Redundant minus sign in PolyDict polynomial

archive/issues_007119.json:
```json
{
    "body": "Assignee: Kwankyu Lee\n\nThere is a tiny bug in the polydict implementation of multivariate\npolynomial ring. \n\n\n```\nsage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict\nsage: R.<x,y>=MPolynomialRing_polydict(GF(2),2,order='lex')\nsage: R\nMultivariate Polynomial Ring in x, y over Finite Field of size 2\nsage: f=x+y\nsage: f.lt()\n-x\nsage: f.lm()\n-x\n```\n\n\nThe minus sign in \"-x\" is redundant\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7119\n\n",
    "created_at": "2009-10-05T04:49:57Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "Redundant minus sign in PolyDict polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7119",
    "user": "klee"
}
```
Assignee: Kwankyu Lee

There is a tiny bug in the polydict implementation of multivariate
polynomial ring. 


```
sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict
sage: R.<x,y>=MPolynomialRing_polydict(GF(2),2,order='lex')
sage: R
Multivariate Polynomial Ring in x, y over Finite Field of size 2
sage: f=x+y
sage: f.lt()
-x
sage: f.lm()
-x
```


The minus sign in "-x" is redundant


Issue created by migration from https://trac.sagemath.org/ticket/7119





---

archive/issue_comments_059011.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-10-05T04:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59011",
    "user": "klee"
}
```

Changing status from new to assigned.



---

archive/issue_comments_059012.json:
```json
{
    "body": "Attachment\n\nThe patch corrects the bug.",
    "created_at": "2009-10-05T04:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59012",
    "user": "klee"
}
```

Attachment

The patch corrects the bug.



---

archive/issue_comments_059013.json:
```json
{
    "body": "Changing assignee from Kwankyu Lee to klee.",
    "created_at": "2009-10-05T04:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59013",
    "user": "klee"
}
```

Changing assignee from Kwankyu Lee to klee.



---

archive/issue_comments_059014.json:
```json
{
    "body": "I think a doctest should be added for the case that the patch fixes. ~ adam",
    "created_at": "2009-10-10T10:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59014",
    "user": "awebb"
}
```

I think a doctest should be added for the case that the patch fixes. ~ adam



---

archive/issue_comments_059015.json:
```json
{
    "body": "Attachment\n\nThe new patch includes doctests and a bugfix of the patch itself.\n\nMartin says:\n\nAlex Ghitza wrote a patch to fix printing of multivariate polynomials in\ngeneral\n\n  http://trac.sagemath.org/sage_trac/ticket/6551\n\nwhich might contain your fix. However, it needs some work before it can go in.\n\n\nHowever, it seems to me that Alex Ghitza's patch is independent with the current patch.",
    "created_at": "2009-10-12T08:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59015",
    "user": "klee"
}
```

Attachment

The new patch includes doctests and a bugfix of the patch itself.

Martin says:

Alex Ghitza wrote a patch to fix printing of multivariate polynomials in
general

  http://trac.sagemath.org/sage_trac/ticket/6551

which might contain your fix. However, it needs some work before it can go in.


However, it seems to me that Alex Ghitza's patch is independent with the current patch.



---

archive/issue_comments_059016.json:
```json
{
    "body": "The present bug results from the class PolyDict in sage/rings/polynomial/\npolydict.pyx rests upon \"zero\" optional parameter, which defaults to\ninteger 0, to decide the characteristic of the parent ring when its\nobject is printed. On the other hand, f.lt() does not set the \"zero\"\nparameter in sage/rings/polynomial/multi_polynomial_element.py. \n\nI think patching the polydict.pyx so as not to rely on the \"zero\" paramter might be better way to correct the bug. But this is out of my reach.",
    "created_at": "2009-10-12T08:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59016",
    "user": "klee"
}
```

The present bug results from the class PolyDict in sage/rings/polynomial/
polydict.pyx rests upon "zero" optional parameter, which defaults to
integer 0, to decide the characteristic of the parent ring when its
object is printed. On the other hand, f.lt() does not set the "zero"
parameter in sage/rings/polynomial/multi_polynomial_element.py. 

I think patching the polydict.pyx so as not to rely on the "zero" paramter might be better way to correct the bug. But this is out of my reach.



---

archive/issue_comments_059017.json:
```json
{
    "body": "What does the TESTS: label do? When I build the reference the Test section is also included. In which case, why not just add to the Examples section (separated by a line with a :: to start a new section)?\n\nI think it would be easier to use something like:\n\n```\nsage: R.<x,y>=PolynomialRing(GF(2),2,order='lex')\nsage: f=x+y\nsage: f.lt()\nx\n```\n\n\nThen you don't need the long import statement.  What do you think?\n\nAdam",
    "created_at": "2009-10-12T11:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59017",
    "user": "awebb"
}
```

What does the TESTS: label do? When I build the reference the Test section is also included. In which case, why not just add to the Examples section (separated by a line with a :: to start a new section)?

I think it would be easier to use something like:

```
sage: R.<x,y>=PolynomialRing(GF(2),2,order='lex')
sage: f=x+y
sage: f.lt()
x
```


Then you don't need the long import statement.  What do you think?

Adam



---

archive/issue_comments_059018.json:
```json
{
    "body": "suggested changes",
    "created_at": "2009-10-12T11:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59018",
    "user": "awebb"
}
```

suggested changes



---

archive/issue_comments_059019.json:
```json
{
    "body": "Attachment\n\nI added a \"suggested changes\" patch just to clarify. ~ Adam",
    "created_at": "2009-10-12T11:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59019",
    "user": "awebb"
}
```

Attachment

I added a "suggested changes" patch just to clarify. ~ Adam



---

archive/issue_comments_059020.json:
```json
{
    "body": "Hi Adam,\n\nThe bug is in the polydict engine of multivariate polynomial rings. So your doctest does not check the bug.\n\nAbout the tests section in the docstring, see this thread in sage-devel: http://groups.google.com/group/sage-devel/browse_frm/thread/2c86e8b59d670502\n\nTo summarize, your \"suggested changes\" should be reverted.\n\nKwankyu",
    "created_at": "2009-10-13T02:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59020",
    "user": "klee"
}
```

Hi Adam,

The bug is in the polydict engine of multivariate polynomial rings. So your doctest does not check the bug.

About the tests section in the docstring, see this thread in sage-devel: http://groups.google.com/group/sage-devel/browse_frm/thread/2c86e8b59d670502

To summarize, your "suggested changes" should be reverted.

Kwankyu



---

archive/issue_comments_059021.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-13T06:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59021",
    "user": "awebb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059022.json:
```json
{
    "body": "Hi,\n\nThat all sounds fine to me. In that case my suggested patch can be ignored. If you know how, you can delete it. In any case, trac_#7119.patch would be the correct patch to apply.\n\nCheers,\n\nAdam",
    "created_at": "2009-10-13T06:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59022",
    "user": "awebb"
}
```

Hi,

That all sounds fine to me. In that case my suggested patch can be ignored. If you know how, you can delete it. In any case, trac_#7119.patch would be the correct patch to apply.

Cheers,

Adam



---

archive/issue_comments_059023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T15:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7119#issuecomment-59023",
    "user": "mhansen"
}
```

Resolution: fixed
