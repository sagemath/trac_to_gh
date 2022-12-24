# Issue 4896: fill in missing magma --> sage conversions

archive/issues_004896.json:
```json
{
    "body": "Assignee: @williamstein\n\nMake it so all the following work:\n\n```\nsage: magma(QQ['x,y'].0).sage()\n```\n\n\nNote that a huge number of sage-->magma conversions for ring elements now work.  To find examples where the converse doesn't work, use this script:\n\n\n```\nsage: for R in sage.rings.tests.random_rings(): print R, magma(R.random_element()).sage()\n```\n\nafter applying #4779.\n\nWhen the above loop runs for \"a while\" without crashing (after applying #4779), then this ticket can be closed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4896\n\n",
    "created_at": "2008-12-31T02:33:36Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.4",
    "title": "fill in missing magma --> sage conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4896",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Make it so all the following work:

```
sage: magma(QQ['x,y'].0).sage()
```


Note that a huge number of sage-->magma conversions for ring elements now work.  To find examples where the converse doesn't work, use this script:


```
sage: for R in sage.rings.tests.random_rings(): print R, magma(R.random_element()).sage()
```

after applying #4779.

When the above loop runs for "a while" without crashing (after applying #4779), then this ticket can be closed.

Issue created by migration from https://trac.sagemath.org/ticket/4896





---

archive/issue_comments_037120.json:
```json
{
    "body": "No patch, i.e. better luck in 3.4 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T07:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37120",
    "user": "mabshoff"
}
```

No patch, i.e. better luck in 3.4 :)

Cheers,

Michael



---

archive/issue_comments_037121.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37121",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037122.json:
```json
{
    "body": "Changing component from interfaces to interfaces: optional.",
    "created_at": "2015-06-23T13:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37122",
    "user": "@jdemeyer"
}
```

Changing component from interfaces to interfaces: optional.



---

archive/issue_comments_037123.json:
```json
{
    "body": "Got\n\n```\nMultivariate Polynomial Ring in x0, x1, x2, x3, x4, x5, x6, x7 over Ring of integers modulo 30768  File \"<string>\", line 1\n    Residue class ring of integers modulo Integer(30768)['x0, x1, x2, x3, x4, x5, x6, x7'.replace('$.', 'x').replace('.', '')](dict([ ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x2'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(17090) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x2'), Integer('0x0'), Integer('0x0') ), Integer(8615) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0') ), Integer(24187) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(5374) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(27378) ) ]))\n                ^\nSyntaxError: invalid syntax\n```\n\nand\n\n```\nUnivariate Polynomial Ring in x over Ring of integers modulo 11908  File \"<string>\", line 1\n    Residue class ring of integers modulo 11908['x'.replace('$.', 'x').replace('.', '')]([ 9823, 11770, 6616 ])\n                ^\nSyntaxError: invalid syntax\n```\n",
    "created_at": "2018-06-23T08:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37123",
    "user": "@fchapoton"
}
```

Got

```
Multivariate Polynomial Ring in x0, x1, x2, x3, x4, x5, x6, x7 over Ring of integers modulo 30768  File "<string>", line 1
    Residue class ring of integers modulo Integer(30768)['x0, x1, x2, x3, x4, x5, x6, x7'.replace('$.', 'x').replace('.', '')](dict([ ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x2'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(17090) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x2'), Integer('0x0'), Integer('0x0') ), Integer(8615) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0') ), Integer(24187) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(5374) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(27378) ) ]))
                ^
SyntaxError: invalid syntax
```

and

```
Univariate Polynomial Ring in x over Ring of integers modulo 11908  File "<string>", line 1
    Residue class ring of integers modulo 11908['x'.replace('$.', 'x').replace('.', '')]([ 9823, 11770, 6616 ])
                ^
SyntaxError: invalid syntax
```




---

archive/issue_comments_037124.json:
```json
{
    "body": "Comes from\n\n```\nsage: R=Zmod(137)\nsage: magma(R)\nResidue class ring of integers modulo 137\nsage: magma(R).sage()\n  File \"<string>\", line 1\n    Residue class ring of integers modulo Integer(137)\n                ^\nSyntaxError: invalid syntax\n```\n",
    "created_at": "2018-06-23T12:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37124",
    "user": "@fchapoton"
}
```

Comes from

```
sage: R=Zmod(137)
sage: magma(R)
Residue class ring of integers modulo 137
sage: magma(R).sage()
  File "<string>", line 1
    Residue class ring of integers modulo Integer(137)
                ^
SyntaxError: invalid syntax
```




---

archive/issue_comments_037125.json:
```json
{
    "body": "Changing keywords from \"\" to \"magma\".",
    "created_at": "2018-06-23T12:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37125",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "magma".



---

archive/issue_comments_037126.json:
```json
{
    "body": "New commits:",
    "created_at": "2018-06-23T14:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37126",
    "user": "@fchapoton"
}
```

New commits:



---

archive/issue_comments_037127.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-06-23T14:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37127",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_037128.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-06-23T15:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37128",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_037129.json:
```json
{
    "body": "branch was moved to #25640",
    "created_at": "2018-06-24T11:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37129",
    "user": "@fchapoton"
}
```

branch was moved to #25640



---

archive/issue_comments_037130.json:
```json
{
    "body": "update milestone 8.3 -> 8.4",
    "created_at": "2018-08-03T19:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4896#issuecomment-37130",
    "user": "@videlec"
}
```

update milestone 8.3 -> 8.4
