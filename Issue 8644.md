# Issue 8644: update pynac to 0.1.12

archive/issues_008644.json:
```json
{
    "body": "Assignee: tbd\n\nI released a new pynac version after applying a few upstream patches from `GiNaC`, the most important being a fix for #8565.\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.12.spkg\n\nSince these are minor changes, I don't expect any build problems. I've tested the package on \n* an up-to-date 64-bit Gentoo system (my laptop) with \n\n```\ngcc (Gentoo 4.3.4 p1.0, pie-10.1.5) 4.3.4\n```\n\n* 32-bit Debian GNU/Linux 5.0.4 (lenny)\n\n```\ngcc (Debian 4.3.2-1.1) 4.3.2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8644\n\n",
    "created_at": "2010-04-02T14:47:11Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "update pynac to 0.1.12",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8644",
    "user": "burcin"
}
```
Assignee: tbd

I released a new pynac version after applying a few upstream patches from `GiNaC`, the most important being a fix for #8565.

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.12.spkg

Since these are minor changes, I don't expect any build problems. I've tested the package on 
* an up-to-date 64-bit Gentoo system (my laptop) with 

```
gcc (Gentoo 4.3.4 p1.0, pie-10.1.5) 4.3.4
```

* 32-bit Debian GNU/Linux 5.0.4 (lenny)

```
gcc (Debian 4.3.2-1.1) 4.3.2
```


Issue created by migration from https://trac.sagemath.org/ticket/8644





---

archive/issue_comments_078399.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T14:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8644#issuecomment-78399",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078400.json:
```json
{
    "body": "Installs fine, all tests passed, works ad advertised, solves #8565. Positive review and thanks for fixing.",
    "created_at": "2010-04-09T11:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8644#issuecomment-78400",
    "user": "robert.marik"
}
```

Installs fine, all tests passed, works ad advertised, solves #8565. Positive review and thanks for fixing.



---

archive/issue_comments_078401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-09T11:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8644#issuecomment-78401",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078402.json:
```json
{
    "body": "Looks good to me too.  There is a new spkg at \n\nhttp://sage.math.washington.edu/home/mhansen/pynac-0.1.12.spkg\n\nwhich incorporates the fixes at #8753.",
    "created_at": "2010-04-27T06:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8644#issuecomment-78402",
    "user": "mhansen"
}
```

Looks good to me too.  There is a new spkg at 

http://sage.math.washington.edu/home/mhansen/pynac-0.1.12.spkg

which incorporates the fixes at #8753.



---

archive/issue_comments_078403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T18:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8644#issuecomment-78403",
    "user": "was"
}
```

Resolution: fixed
