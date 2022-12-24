# Issue 6782: Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/calculus.rst

archive/issues_006782.json:
```json
{
    "body": "Assignee: burcin\n\nOn Solaris (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThu Aug 20 20:02:37 BST 2009\ndsage-trial tmp directory doesn't exist - creating ...\nThis script will run the unit tests for DSage\n```\n\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n<SNIP>\n\n```\nFile \"/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/calculus.rst\", line 117:\n    sage: maxima(f).powerseries(x,0)\nExpected:\n    ('sum((-1)^i2*2^(2*i2)*bern(2*i2)*x^(2*i2)/(i2*(2*i2)!),i2,1,inf))/2\nGot:\n    'sum((-1)^i2*2^(2*i2-1)*bern(2*i2)*x^(2*i2)/(i2*(2*i2)!),i2,1,inf)\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6782\n\n",
    "created_at": "2009-08-20T21:29:19Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Doctest failure in sage-4.1.1/devel/sage/doc/en/constructions/calculus.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6782",
    "user": "drkirkby"
}
```
Assignee: burcin

On Solaris (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
<SNIP>

```
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/doc/en/constructions/calculus.rst", line 117:
    sage: maxima(f).powerseries(x,0)
Expected:
    ('sum((-1)^i2*2^(2*i2)*bern(2*i2)*x^(2*i2)/(i2*(2*i2)!),i2,1,inf))/2
Got:
    'sum((-1)^i2*2^(2*i2-1)*bern(2*i2)*x^(2*i2)/(i2*(2*i2)!),i2,1,inf)

```



Issue created by migration from https://trac.sagemath.org/ticket/6782





---

archive/issue_comments_055896.json:
```json
{
    "body": "Changing assignee from burcin to AlexGhitza.",
    "created_at": "2009-08-20T23:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55896",
    "user": "AlexGhitza"
}
```

Changing assignee from burcin to AlexGhitza.



---

archive/issue_comments_055897.json:
```json
{
    "body": "This one is trivial; see attached patch.",
    "created_at": "2009-08-20T23:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55897",
    "user": "AlexGhitza"
}
```

This one is trivial; see attached patch.



---

archive/issue_comments_055898.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-20T23:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55898",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055899.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55899",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055900.json:
```json
{
    "body": "Attachment [trac_6782.patch](tarball://root/attachments/some-uuid/ticket6782/trac_6782.patch) by AlexGhitza created at 2009-08-20 23:10:09\n\napply after spkg's at #6564 and #6699",
    "created_at": "2009-08-20T23:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55900",
    "user": "AlexGhitza"
}
```

Attachment [trac_6782.patch](tarball://root/attachments/some-uuid/ticket6782/trac_6782.patch) by AlexGhitza created at 2009-08-20 23:10:09

apply after spkg's at #6564 and #6699



---

archive/issue_comments_055901.json:
```json
{
    "body": "The log was generated with Maxima 5.19.1, not 5.19.0, so I'm changing the title slightly to reflect this.",
    "created_at": "2009-08-21T05:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55901",
    "user": "drkirkby"
}
```

The log was generated with Maxima 5.19.1, not 5.19.0, so I'm changing the title slightly to reflect this.



---

archive/issue_comments_055902.json:
```json
{
    "body": "Are these mathematically equivalent? It seems to me the factor in the numerator has changed from (2*i2) to (2*i2-1) and denominator from 2 to 1. That seems a different result to me. \n\nI tried what I **think** the test is doing in Mathematica and got:\n\n\n```\nIn[7]:= f=Log[Sin[x]/x]\n\n            Sin[x]\nOut[7]= Log[------]\n              x\n\nIn[8]:=  Series[f,{x,0,12}]\n\n          2    4      6      8       10           12\n        -x    x      x      x       x        691 x           13\nOut[8]= --- - --- - ---- - ----- - ------ - ---------- + O[x]\n         6    180   2835   37800   467775   3831077250\n\nIn[9]:=\n```\n\n\nI've no idea what's right or not. \n\nDave",
    "created_at": "2009-08-21T07:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55902",
    "user": "drkirkby"
}
```

Are these mathematically equivalent? It seems to me the factor in the numerator has changed from (2*i2) to (2*i2-1) and denominator from 2 to 1. That seems a different result to me. 

I tried what I **think** the test is doing in Mathematica and got:


```
In[7]:= f=Log[Sin[x]/x]

            Sin[x]
Out[7]= Log[------]
              x

In[8]:=  Series[f,{x,0,12}]

          2    4      6      8       10           12
        -x    x      x      x       x        691 x           13
Out[8]= --- - --- - ---- - ----- - ------ - ---------- + O[x]
         6    180   2835   37800   467775   3831077250

In[9]:=
```


I've no idea what's right or not. 

Dave



---

archive/issue_comments_055903.json:
```json
{
    "body": "The difference is `2^(2*i2)/2` versus `2^(2*i2-1)`.  Yes, they are the same.",
    "created_at": "2009-08-21T09:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55903",
    "user": "AlexGhitza"
}
```

The difference is `2^(2*i2)/2` versus `2^(2*i2-1)`.  Yes, they are the same.



---

archive/issue_comments_055904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T10:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55904",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055905.json:
```json
{
    "body": "This is fixed by #6699.",
    "created_at": "2009-09-02T10:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6782#issuecomment-55905",
    "user": "mvngu"
}
```

This is fixed by #6699.
