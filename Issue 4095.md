# Issue 4095: Major bug in GF(109)['x', 'y']

archive/issues_004095.json:
```json
{
    "body": "Assignee: somebody\n\nNick Alexander reported in http://groups.google.com/group/sage-devel/t/66e73453bc0b863a\n\n```\nsage: GF(109)['x', 'y'](-10)\n-10\nsage: GF(109)['x'](-10)\n99\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4095\n\n",
    "created_at": "2008-09-10T02:22:42Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Major bug in GF(109)['x', 'y']",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4095",
    "user": "mabshoff"
}
```
Assignee: somebody

Nick Alexander reported in http://groups.google.com/group/sage-devel/t/66e73453bc0b863a

```
sage: GF(109)['x', 'y'](-10)
-10
sage: GF(109)['x'](-10)
99
```


Issue created by migration from https://trac.sagemath.org/ticket/4095





---

archive/issue_comments_029542.json:
```json
{
    "body": "Michael Brickenstein wrote on [sage-devel]:\n\n```\nok, it isn't normalize, but a very small function called npWrite\n\nvoid npWrite (number &a)\n{\n\u00a0 if ((long)a > (npPrimeM >>1)) StringAppend(\"-%d\",(int)(npPrimeM-\n((long)a)));\n\u00a0 else \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0StringAppend(\"%d\",(int)((long)a));\n}\n\nThis is set to the current ring\nin numbers.cc\nn->nWrite = npWrite;\nIt should just affect the output, so I think would be okay to change it.\n```\n",
    "created_at": "2008-09-15T17:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4095#issuecomment-29542",
    "user": "@malb"
}
```

Michael Brickenstein wrote on [sage-devel]:

```
ok, it isn't normalize, but a very small function called npWrite

void npWrite (number &a)
{
  if ((long)a > (npPrimeM >>1)) StringAppend("-%d",(int)(npPrimeM-
((long)a)));
  else                          StringAppend("%d",(int)((long)a));
}

This is set to the current ring
in numbers.cc
n->nWrite = npWrite;
It should just affect the output, so I think would be okay to change it.
```




---

archive/issue_comments_029543.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4095#issuecomment-29543",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.
