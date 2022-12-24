# Issue 3716: [with spkg, needs review] add GINV as experimental/optional package

archive/issues_003716.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @burcin\n\nFrom the Ginv website (http://invo.jinr.ru/ginv/index.html)\n\"The open source software GINV implements the Gr\u00f6bner bases method for systems of equations. GINV is a C++ module of Python designed for constructing Gr\u00f6bner bases of ideals and modules in polynomial, differential and difference rings. Gr\u00f6bner bases are constructed by involutive algorithms. GINV is an open source software. The source codes, the installation package for Python, documentation in Russian and English are available on the Web page http://invo.jinr.ru\"\n\nThe package has a pretty good reputation for fast GBs over QQ. It also is reported to have a fast multivariate GCD over QQ and GF(q) and GBs over ZZ.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3716\n\n",
    "created_at": "2008-07-23T19:32:57Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with spkg, needs review] add GINV as experimental/optional package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3716",
    "user": "@malb"
}
```
Assignee: mabshoff

CC:  @burcin

From the Ginv website (http://invo.jinr.ru/ginv/index.html)
"The open source software GINV implements the Gröbner bases method for systems of equations. GINV is a C++ module of Python designed for constructing Gröbner bases of ideals and modules in polynomial, differential and difference rings. Gröbner bases are constructed by involutive algorithms. GINV is an open source software. The source codes, the installation package for Python, documentation in Russian and English are available on the Web page http://invo.jinr.ru"

The package has a pretty good reputation for fast GBs over QQ. It also is reported to have a fast multivariate GCD over QQ and GF(q) and GBs over ZZ.

Issue created by migration from https://trac.sagemath.org/ticket/3716





---

archive/issue_comments_026371.json:
```json
{
    "body": "The SPKG is here:\n\n   http://sage.math.washington.edu/home/malb/spkgs/ginv-1.9-20080723.spkg",
    "created_at": "2008-07-23T19:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3716#issuecomment-26371",
    "user": "@malb"
}
```

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/ginv-1.9-20080723.spkg



---

archive/issue_comments_026372.json:
```json
{
    "body": "There are some small issues, all of which I fixed:\n\n* .hgignore is missing and patches/setup.py was not under revision control\n* the dependencies in SPKG.txt were from M2 it seems - ginv only depends on gmp\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T17:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3716#issuecomment-26372",
    "user": "mabshoff"
}
```

There are some small issues, all of which I fixed:

* .hgignore is missing and patches/setup.py was not under revision control
* the dependencies in SPKG.txt were from M2 it seems - ginv only depends on gmp

Positive review.

Cheers,

Michael



---

archive/issue_comments_026373.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3716#issuecomment-26373",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026374.json:
```json
{
    "body": "Merged in the optinal repo in Sage 3.0.6.final",
    "created_at": "2008-07-29T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3716#issuecomment-26374",
    "user": "mabshoff"
}
```

Merged in the optinal repo in Sage 3.0.6.final
