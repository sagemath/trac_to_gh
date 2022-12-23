# Issue 1267: documentation for piecewise does not show up in notebook

archive/issues_001267.json:
```json
{
    "body": "Assignee: boothby\n\nIn the public notebook (on www.sagenb.org), when I evaluate a cell with `piecewise?`, I get this:\n\n```\nFile:        /usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/functions/piecewise.py\nType:        <type 'classobj'>\nDefinition:  piecewise(x0)\nDocstring:\n```\n\nwith no actual docstring.  (Doing the same thing from the command line does give a useful docstring.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1267\n\n",
    "created_at": "2007-11-25T15:09:41Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "documentation for piecewise does not show up in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1267",
    "user": "cwitty"
}
```
Assignee: boothby

In the public notebook (on www.sagenb.org), when I evaluate a cell with `piecewise?`, I get this:

```
File:        /usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/functions/piecewise.py
Type:        <type 'classobj'>
Definition:  piecewise(x0)
Docstring:
```

with no actual docstring.  (Doing the same thing from the command line does give a useful docstring.)


Issue created by migration from https://trac.sagemath.org/ticket/1267





---

archive/issue_comments_007942.json:
```json
{
    "body": "After some testing it turns out that cwitty is right and it does work in console mode with 2.8.14 So was is wrong and change it back.",
    "created_at": "2007-11-25T17:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7942",
    "user": "mabshoff"
}
```

After some testing it turns out that cwitty is right and it does work in console mode with 2.8.14 So was is wrong and change it back.



---

archive/issue_comments_007943.json:
```json
{
    "body": "I can confirm and replicate this problem:\n\n```\n[10:09am] was_: It does fail on my ocally-running notebook.\n[10:09am] was_: Ipython does the help on the command line.\n[10:09am] was_: *I* wrote what does the help in the notebook.\n[10:09am] DenisG_: (my locally running notebook)\n[10:09am] was_: It's separate code; I think it is is sage/server/support.py or something like that\n[10:10am] was_: And there is definitely a bug.\n```\n",
    "created_at": "2007-11-25T18:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7943",
    "user": "was"
}
```

I can confirm and replicate this problem:

```
[10:09am] was_: It does fail on my ocally-running notebook.
[10:09am] was_: Ipython does the help on the command line.
[10:09am] was_: *I* wrote what does the help in the notebook.
[10:09am] DenisG_: (my locally running notebook)
[10:09am] was_: It's separate code; I think it is is sage/server/support.py or something like that
[10:10am] was_: And there is definitely a bug.
```




---

archive/issue_comments_007944.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T00:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7944",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007945.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2007-12-06T00:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7945",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_007946.json:
```json
{
    "body": "Actually, I don't think anything wrong with the ? or ?? notation.  What was happening was roughly the following:\n\n\n```\nclass PiecewisePolynomial:\n    def __init__(self, list_of_pairs):\n        \"\"\"docstring\"\"\"\n\n    ...\n\npiecewise = PiecewisePolynomial\n```\n\n\nThe result of piecewise? was correct since PiecewisePolynomial didn't have a class docstring.",
    "created_at": "2007-12-06T00:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7946",
    "user": "mhansen"
}
```

Actually, I don't think anything wrong with the ? or ?? notation.  What was happening was roughly the following:


```
class PiecewisePolynomial:
    def __init__(self, list_of_pairs):
        """docstring"""

    ...

piecewise = PiecewisePolynomial
```


The result of piecewise? was correct since PiecewisePolynomial didn't have a class docstring.



---

archive/issue_comments_007947.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-06T00:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7947",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_007948.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T12:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7948",
    "user": "mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_007949.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T13:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7949",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007950.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T13:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1267#issuecomment-7950",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha2.
