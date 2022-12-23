# Issue 7859: bug in QQbar (easy to fix!)

archive/issues_007859.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nThe code\n\nR.<x> = AA[]\nv1 = QQbar.polynomial_root(AA.common_polynomial(x^4 + 3*x^2 + 1),\\\n CIF(RIF(-RR(2.7018838812806391e-55), RR(2.5616917931009833e-55)),\\\n RIF(RR(1.6180339887498947), RR(1.6180339887498949))))\nv2 = (2/3*v1^3 + 2/3*v1^2 + 4/3*v1 + 1).norm()\nsqrt(v2 - 1)\n\nyields the error\n\nNameError: global name 'AlgebriacNumber' is not defined\n\nApparently there is a small typo in line 3394 of the file qqbar.py\n\nBest regards,\n\n/H\u00e5kan\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7859\n\n",
    "created_at": "2010-01-06T19:45:02Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in QQbar (easy to fix!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7859",
    "user": "was"
}
```
Assignee: AlexGhitza


```
The code

R.<x> = AA[]
v1 = QQbar.polynomial_root(AA.common_polynomial(x^4 + 3*x^2 + 1),\
 CIF(RIF(-RR(2.7018838812806391e-55), RR(2.5616917931009833e-55)),\
 RIF(RR(1.6180339887498947), RR(1.6180339887498949))))
v2 = (2/3*v1^3 + 2/3*v1^2 + 4/3*v1 + 1).norm()
sqrt(v2 - 1)

yields the error

NameError: global name 'AlgebriacNumber' is not defined

Apparently there is a small typo in line 3394 of the file qqbar.py

Best regards,

/Håkan
```


Issue created by migration from https://trac.sagemath.org/ticket/7859





---

archive/issue_comments_068120.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-06T20:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68120",
    "user": "hgranath"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068121.json:
```json
{
    "body": "\n```\n\nThat's known.  And it was  fixed by an earlier version of the patch at\n#6887 which was merged in 4.3.1.alpha1.  But I now see that that fix\nhas got lost, very strange.  It will need fixing again....\n\nJohn\n```\n",
    "created_at": "2010-01-06T20:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68121",
    "user": "was"
}
```


```

That's known.  And it was  fixed by an earlier version of the patch at
#6887 which was merged in 4.3.1.alpha1.  But I now see that that fix
has got lost, very strange.  It will need fixing again....

John
```




---

archive/issue_comments_068122.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T20:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68122",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068123.json:
```json
{
    "body": "Can you add a doctest to the patch to exercise this bit of code?",
    "created_at": "2010-01-06T20:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68123",
    "user": "was"
}
```

Can you add a doctest to the patch to exercise this bit of code?



---

archive/issue_comments_068124.json:
```json
{
    "body": "new version with doctest",
    "created_at": "2010-01-06T21:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68124",
    "user": "hgranath"
}
```

new version with doctest



---

archive/issue_comments_068125.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-06T21:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68125",
    "user": "hgranath"
}
```

Attachment



---

archive/issue_comments_068126.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T21:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68126",
    "user": "hgranath"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068127.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T00:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68127",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068128.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T08:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68128",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068129.json:
```json
{
    "body": "\n```\npatching file sage/rings/qqbar.py\nHunk #2 FAILED at 3392\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/qqbar.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_7859.patch\n```\n",
    "created_at": "2010-01-13T08:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68129",
    "user": "rlm"
}
```


```
patching file sage/rings/qqbar.py
Hunk #2 FAILED at 3392
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/qqbar.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7859.patch
```




---

archive/issue_comments_068130.json:
```json
{
    "body": "This issue seems to be fixed already in 4.3.1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x> = AA[]\nsage: v1 = QQbar.polynomial_root(AA.common_polynomial(x^4 + 3*x^2 + 1),\\\n....:  CIF(RIF(-RR(2.7018838812806391e-55), RR(2.5616917931009833e-55)),\\\n....:  RIF(RR(1.6180339887498947), RR(1.6180339887498949))))\nsage: \nsage: v2 = (2/3*v1^3 + 2/3*v1^2 + 4/3*v1 + 1).norm()\nsage: sqrt(v2 - 1)\n0\n```\n",
    "created_at": "2010-02-05T21:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68130",
    "user": "zimmerma"
}
```

This issue seems to be fixed already in 4.3.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = AA[]
sage: v1 = QQbar.polynomial_root(AA.common_polynomial(x^4 + 3*x^2 + 1),\
....:  CIF(RIF(-RR(2.7018838812806391e-55), RR(2.5616917931009833e-55)),\
....:  RIF(RR(1.6180339887498947), RR(1.6180339887498949))))
sage: 
sage: v2 = (2/3*v1^3 + 2/3*v1^2 + 4/3*v1 + 1).norm()
sage: sqrt(v2 - 1)
0
```




---

archive/issue_comments_068131.json:
```json
{
    "body": "I agree.  This is fixed.  Possibly the doctest should be added, though.\n\n\n```\n~/sage/devel/sage/sage/rings% grep AlgebriacNumber *\n~/sage/devel/sage/sage/rings%\n```\n",
    "created_at": "2010-05-26T15:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68131",
    "user": "jason"
}
```

I agree.  This is fixed.  Possibly the doctest should be added, though.


```
~/sage/devel/sage/sage/rings% grep AlgebriacNumber *
~/sage/devel/sage/sage/rings%
```




---

archive/issue_comments_068132.json:
```json
{
    "body": "Attachment\n\napply only this patch",
    "created_at": "2010-06-29T09:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68132",
    "user": "davidloeffler"
}
```

Attachment

apply only this patch



---

archive/issue_comments_068133.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T09:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68133",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068134.json:
```json
{
    "body": "Here's a tiny patch (based on 4.4.4 if it matters) containing just the doctest extracted from H\u00e5kan's patch, as Jason suggested.",
    "created_at": "2010-06-29T09:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68134",
    "user": "davidloeffler"
}
```

Here's a tiny patch (based on 4.4.4 if it matters) containing just the doctest extracted from Håkan's patch, as Jason suggested.



---

archive/issue_comments_068135.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-30T07:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68135",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068136.json:
```json
{
    "body": "I'm entering a guess in the Reviewer(s) field.  Please correct it, if I'm wrong.",
    "created_at": "2010-07-20T09:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68136",
    "user": "mpatel"
}
```

I'm entering a guess in the Reviewer(s) field.  Please correct it, if I'm wrong.



---

archive/issue_comments_068137.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7859#issuecomment-68137",
    "user": "mpatel"
}
```

Resolution: fixed
