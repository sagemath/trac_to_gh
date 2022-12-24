# Issue 7868: Factoring in fraction fields

archive/issues_007868.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona\n\nKeywords: fraction field, factorization\n\nThe following is a quote from John Cremona, \n\n    http://groups.google.com/group/sage-devel/browse_thread/thread/3638a91c0438f439\n\nI define a rational function in two variables over a finite field:\n\n\n```\nsage: R.<x,y> = GF(2)[]\nsage: f = x*y/(x+y)\nsage: f.parent()\nFraction Field of Multivariate Polynomial Ring in x, y over Finite\nField of size 2\n\n```\n\n\nI try to factor it, and get this error:\n\n\n```\nsage: f.factor()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/masgaj/.sage/temp/host_56_150/17587/_home_masgaj__sage_init_sage_0.py\nin <module>()\n\n/local/jec/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/rings/fraction_field_element.so\nin sage.rings.fraction_field_element.FractionFieldElement.factor\n(sage/rings/fraction_field_element.c:2972)()\n\n/local/jec/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so\nin sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor\n(sage/rings/polynomial/multi_polynomial_libsingular.cpp:22701)()\n\nNotImplementedError: proof = True factorization not implemented.  Call\nfactor with proof=False.\n\n```\n\n\nSo I do what I am told, but:\n\n\n```\nsage: f.factor(proof=False)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/masgaj/.sage/temp/host_56_150/17587/_home_masgaj__sage_init_sage_0.py\nin <module>()\n\nTypeError: factor() takes no keyword arguments\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7868\n\n",
    "created_at": "2010-01-07T17:07:43Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Factoring in fraction fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7868",
    "user": "spancratz"
}
```
Assignee: @aghitza

CC:  @JohnCremona

Keywords: fraction field, factorization

The following is a quote from John Cremona, 

    http://groups.google.com/group/sage-devel/browse_thread/thread/3638a91c0438f439

I define a rational function in two variables over a finite field:


```
sage: R.<x,y> = GF(2)[]
sage: f = x*y/(x+y)
sage: f.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Finite
Field of size 2

```


I try to factor it, and get this error:


```
sage: f.factor()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/17587/_home_masgaj__sage_init_sage_0.py
in <module>()

/local/jec/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/rings/fraction_field_element.so
in sage.rings.fraction_field_element.FractionFieldElement.factor
(sage/rings/fraction_field_element.c:2972)()

/local/jec/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so
in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor
(sage/rings/polynomial/multi_polynomial_libsingular.cpp:22701)()

NotImplementedError: proof = True factorization not implemented.  Call
factor with proof=False.

```


So I do what I am told, but:


```
sage: f.factor(proof=False)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/17587/_home_masgaj__sage_init_sage_0.py
in <module>()

TypeError: factor() takes no keyword arguments

```



Issue created by migration from https://trac.sagemath.org/ticket/7868





---

archive/issue_comments_068238.json:
```json
{
    "body": "Attachment [trac7868_20100107.patch](tarball://root/attachments/some-uuid/ticket7868/trac7868_20100107.patch) by spancratz created at 2010-01-07 17:14:49",
    "created_at": "2010-01-07T17:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68238",
    "user": "spancratz"
}
```

Attachment [trac7868_20100107.patch](tarball://root/attachments/some-uuid/ticket7868/trac7868_20100107.patch) by spancratz created at 2010-01-07 17:14:49



---

archive/issue_comments_068239.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-07T18:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68239",
    "user": "spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068240.json:
```json
{
    "body": "The patch I attached earlier changes the behaviour of the factoring method in fraction fields, passing on additional parameters to the factoring method of the underlying ring rather than ignoring them.\n\nI've now tested the patch (without the ``long`` option), and this did not return any test failures.\n\nSebastian",
    "created_at": "2010-01-07T18:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68240",
    "user": "spancratz"
}
```

The patch I attached earlier changes the behaviour of the factoring method in fraction fields, passing on additional parameters to the factoring method of the underlying ring rather than ignoring them.

I've now tested the patch (without the ``long`` option), and this did not return any test failures.

Sebastian



---

archive/issue_comments_068241.json:
```json
{
    "body": "Changing assignee from @aghitza to spancratz.",
    "created_at": "2010-01-07T18:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68241",
    "user": "spancratz"
}
```

Changing assignee from @aghitza to spancratz.



---

archive/issue_comments_068242.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T19:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68242",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068243.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-07T19:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68243",
    "user": "@robertwb"
}
```

Looks good to me.



---

archive/issue_comments_068244.json:
```json
{
    "body": "Well, the code looks good, but we need a test showing the behavior is fixed.",
    "created_at": "2010-01-07T19:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68244",
    "user": "@robertwb"
}
```

Well, the code looks good, but we need a test showing the behavior is fixed.



---

archive/issue_comments_068245.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-07T19:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68245",
    "user": "@robertwb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068246.json:
```json
{
    "body": "I agree with Robert's point, which I was going to make too.  But for me the code does not apply to either 4.3 or 4.3.1.apha1.  Sebastian, did you make the patch on top of your other changes to the fraction field code?  Robert, did you apply the patch?",
    "created_at": "2010-01-07T20:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68246",
    "user": "@JohnCremona"
}
```

I agree with Robert's point, which I was going to make too.  But for me the code does not apply to either 4.3 or 4.3.1.apha1.  Sebastian, did you make the patch on top of your other changes to the fraction field code?  Robert, did you apply the patch?



---

archive/issue_comments_068247.json:
```json
{
    "body": "No, I didn't actually apply it... (I've got a lot of fraction field changes that I needed to pop off first, and no, it's not applying for me either. I don't see why.) I've posted an updated one that should merge onto 4.3 fine, with the new doctest.",
    "created_at": "2010-01-07T20:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68247",
    "user": "@robertwb"
}
```

No, I didn't actually apply it... (I've got a lot of fraction field changes that I needed to pop off first, and no, it's not applying for me either. I don't see why.) I've posted an updated one that should merge onto 4.3 fine, with the new doctest.



---

archive/issue_comments_068248.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-07T20:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68248",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068249.json:
```json
{
    "body": "OOps, that second patch is empty!",
    "created_at": "2010-01-07T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68249",
    "user": "@JohnCremona"
}
```

OOps, that second patch is empty!



---

archive/issue_comments_068250.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-07T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68250",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068251.json:
```json
{
    "body": "Attachment [7868-fix.patch](tarball://root/attachments/some-uuid/ticket7868/7868-fix.patch) by @robertwb created at 2010-01-07 21:38:27\n\nreplaces previous",
    "created_at": "2010-01-07T21:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68251",
    "user": "@robertwb"
}
```

Attachment [7868-fix.patch](tarball://root/attachments/some-uuid/ticket7868/7868-fix.patch) by @robertwb created at 2010-01-07 21:38:27

replaces previous



---

archive/issue_comments_068252.json:
```json
{
    "body": "Oops...",
    "created_at": "2010-01-07T21:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68252",
    "user": "@robertwb"
}
```

Oops...



---

archive/issue_comments_068253.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-07T21:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68253",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068254.json:
```json
{
    "body": "Attachment [7868-fix.2.patch](tarball://root/attachments/some-uuid/ticket7868/7868-fix.2.patch) by @JohnCremona created at 2010-01-07 22:00:52\n\nreplaces previous",
    "created_at": "2010-01-07T22:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68254",
    "user": "@JohnCremona"
}
```

Attachment [7868-fix.2.patch](tarball://root/attachments/some-uuid/ticket7868/7868-fix.2.patch) by @JohnCremona created at 2010-01-07 22:00:52

replaces previous



---

archive/issue_comments_068255.json:
```json
{
    "body": "I deleted the lines sage: f.parent() in the patch since you omitted its output.  If this works for you: positive review.  Thanks!",
    "created_at": "2010-01-07T22:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68255",
    "user": "@JohnCremona"
}
```

I deleted the lines sage: f.parent() in the patch since you omitted its output.  If this works for you: positive review.  Thanks!



---

archive/issue_comments_068256.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T22:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68256",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068257.json:
```json
{
    "body": "Great.  This all happened rather swiftly!\n\nSebastian\n\nReplying to [comment:10 cremona]:\n> I deleted the lines sage: f.parent() in the patch since you omitted its output.  If this works for you: positive review.  Thanks!",
    "created_at": "2010-01-08T01:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68257",
    "user": "spancratz"
}
```

Great.  This all happened rather swiftly!

Sebastian

Replying to [comment:10 cremona]:
> I deleted the lines sage: f.parent() in the patch since you omitted its output.  If this works for you: positive review.  Thanks!



---

archive/issue_comments_068258.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T08:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68258",
    "user": "@rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068259.json:
```json
{
    "body": "Sorry, there's a conflict:\n\n```\npatching file sage/rings/fraction_field_element.pyx\nHunk #1 FAILED at 212\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/fraction_field_element.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh 7868-fix.2.patch\n```\n",
    "created_at": "2010-01-13T08:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68259",
    "user": "@rlmill"
}
```

Sorry, there's a conflict:

```
patching file sage/rings/fraction_field_element.pyx
Hunk #1 FAILED at 212
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/fraction_field_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 7868-fix.2.patch
```




---

archive/issue_comments_068260.json:
```json
{
    "body": "Rebase to 4.3.1.rc0",
    "created_at": "2010-01-19T12:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68260",
    "user": "spancratz"
}
```

Rebase to 4.3.1.rc0



---

archive/issue_comments_068261.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T20:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68261",
    "user": "@rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068262.json:
```json
{
    "body": "Attachment [trac7868_rb.patch](tarball://root/attachments/some-uuid/ticket7868/trac7868_rb.patch) by @rlmill created at 2010-01-19 20:04:27",
    "created_at": "2010-01-19T20:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68262",
    "user": "@rlmill"
}
```

Attachment [trac7868_rb.patch](tarball://root/attachments/some-uuid/ticket7868/trac7868_rb.patch) by @rlmill created at 2010-01-19 20:04:27



---

archive/issue_comments_068263.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T20:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68263",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068264.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T20:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7868#issuecomment-68264",
    "user": "@rlmill"
}
```

Resolution: fixed
