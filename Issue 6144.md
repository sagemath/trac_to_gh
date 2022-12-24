# Issue 6144: Pynac doesn't simplify exp(x)*exp(2*x) to exp(3*x)

archive/issues_006144.json:
```json
{
    "body": "CC:  was\n\n\n```\nsage: exp(x)*exp(2*x)\ne^(2*x)*e^x\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6144\n\n",
    "created_at": "2009-05-28T05:27:18Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "Pynac doesn't simplify exp(x)*exp(2*x) to exp(3*x)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6144",
    "user": "mhansen"
}
```
CC:  was


```
sage: exp(x)*exp(2*x)
e^(2*x)*e^x
```


Issue created by migration from https://trac.sagemath.org/ticket/6144





---

archive/issue_comments_049048.json:
```json
{
    "body": "GiNaC doesn't do this either:\n\n\n```\n> exp(x)*exp(2*x);\nexp(2*x)*exp(x)\n```\n\n\nI'll try to play with the mul::eval method in pynac to do this. The main problem is doing it without compromising speed.\n\nCheers,\n\nBurcin",
    "created_at": "2009-05-28T10:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49048",
    "user": "burcin"
}
```

GiNaC doesn't do this either:


```
> exp(x)*exp(2*x);
exp(2*x)*exp(x)
```


I'll try to play with the mul::eval method in pynac to do this. The main problem is doing it without compromising speed.

Cheers,

Burcin



---

archive/issue_comments_049049.json:
```json
{
    "body": "Attachment [trac_6144-exp_simplify.patch](tarball://root/attachments/some-uuid/ticket6144/trac_6144-exp_simplify.patch) by burcin created at 2009-06-04 09:49:49",
    "created_at": "2009-06-04T09:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49049",
    "user": "burcin"
}
```

Attachment [trac_6144-exp_simplify.patch](tarball://root/attachments/some-uuid/ticket6144/trac_6144-exp_simplify.patch) by burcin created at 2009-06-04 09:49:49



---

archive/issue_comments_049050.json:
```json
{
    "body": "Attachment [trac_6144-pynac_depends.patch](tarball://root/attachments/some-uuid/ticket6144/trac_6144-pynac_depends.patch) by burcin created at 2009-06-04 10:10:03\n\nNew pynac package here fixes the exp simplification:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.spkg\n\nAttached patches fix doctests, and change module_list.py to rebuild the sage/symbolic/* modules if the package is updated.\n\nThis package also contains a fix for #6163, so these tickets should be merged together.",
    "created_at": "2009-06-04T10:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49050",
    "user": "burcin"
}
```

Attachment [trac_6144-pynac_depends.patch](tarball://root/attachments/some-uuid/ticket6144/trac_6144-pynac_depends.patch) by burcin created at 2009-06-04 10:10:03

New pynac package here fixes the exp simplification:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.spkg

Attached patches fix doctests, and change module_list.py to rebuild the sage/symbolic/* modules if the package is updated.

This package also contains a fix for #6163, so these tickets should be merged together.



---

archive/issue_comments_049051.json:
```json
{
    "body": "Attachment [trac_6144-review.patch](tarball://root/attachments/some-uuid/ticket6144/trac_6144-review.patch) by mhansen created at 2009-06-05 01:52:53",
    "created_at": "2009-06-05T01:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49051",
    "user": "mhansen"
}
```

Attachment [trac_6144-review.patch](tarball://root/attachments/some-uuid/ticket6144/trac_6144-review.patch) by mhansen created at 2009-06-05 01:52:53



---

archive/issue_comments_049052.json:
```json
{
    "body": "Burcin's changes look good to me.  There was one doctest failure that I fixed and put in trac_6144-review.patch",
    "created_at": "2009-06-05T01:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49052",
    "user": "mhansen"
}
```

Burcin's changes look good to me.  There was one doctest failure that I fixed and put in trac_6144-review.patch



---

archive/issue_comments_049053.json:
```json
{
    "body": "All looks good to me!  I'm glad this is fixed, I updated the number field tests and was disappointed with the previous behaviour.",
    "created_at": "2009-06-05T01:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49053",
    "user": "ncalexan"
}
```

All looks good to me!  I'm glad this is fixed, I updated the number field tests and was disappointed with the previous behaviour.



---

archive/issue_comments_049054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-05T02:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49054",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049055.json:
```json
{
    "body": "Merged in 4.0.1.rc2.",
    "created_at": "2009-06-05T02:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6144#issuecomment-49055",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc2.
