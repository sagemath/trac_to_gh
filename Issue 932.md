# Issue 932: upgrade lcalc in sage

archive/issues_000932.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\nHi William. Before you go ahead and make a big official table like that,\nyou should upgrade to the latest lcalc. I'll be releasing that in a few\ndays. It has a more efficient zero finding routine and also gets rid of\nannoying warning message that sometimes appears when it ought not to...\nthe message might interfere with the preparation of your table. Also,\ncurrently not all digits outputed are guaranteed. For low conductor I\ndon't think that will be an issue, but as the conductor increases\nthat will be a bit relevant.\n\nI'm currently implementing something to verify the precision and adjust the\noutput accordingly.\n\nIt also has other improvements, though not relevant for the table you\nmention.\n\nMike}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/932\n\n",
    "created_at": "2007-10-19T18:58:49Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "upgrade lcalc in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/932",
    "user": "was"
}
```
Assignee: was


```

Hi William. Before you go ahead and make a big official table like that,
you should upgrade to the latest lcalc. I'll be releasing that in a few
days. It has a more efficient zero finding routine and also gets rid of
annoying warning message that sometimes appears when it ought not to...
the message might interfere with the preparation of your table. Also,
currently not all digits outputed are guaranteed. For low conductor I
don't think that will be an issue, but as the conductor increases
that will be a bit relevant.

I'm currently implementing something to verify the precision and adjust the
output accordingly.

It also has other improvements, though not relevant for the table you
mention.

Mike}}}

Issue created by migration from https://trac.sagemath.org/ticket/932





---

archive/issue_comments_005692.json:
```json
{
    "body": "I am not sure if this is going to make it for 2.8.8, but we ca at least try.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T19:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5692",
    "user": "mabshoff"
}
```

I am not sure if this is going to make it for 2.8.8, but we ca at least try.

Cheers,

Michael



---

archive/issue_comments_005693.json:
```json
{
    "body": "Mike Rubinstein says:\n\n```\nDear Colleagues,\n\nI've released a new version of lcalc.\n\nThis release fixes some bugs (so please update), has improvements to\nsome of the key\nroutines, especially for higher degree L-functions (i.e. deg >=3, and\nalso for Maass forms),\nand better handling of output precision.\n\nThe code can be downloaded from:\nhttp://pmmac03.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/\n\nPlease email me any bugs you notice.\n\nThanks,\nMike\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T17:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5693",
    "user": "mabshoff"
}
```

Mike Rubinstein says:

```
Dear Colleagues,

I've released a new version of lcalc.

This release fixes some bugs (so please update), has improvements to
some of the key
routines, especially for higher degree L-functions (i.e. deg >=3, and
also for Maass forms),
and better handling of output precision.

The code can be downloaded from:
http://pmmac03.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/

Please email me any bugs you notice.

Thanks,
Mike
```


Cheers,

Michael



---

archive/issue_comments_005694.json:
```json
{
    "body": "Hmm, see also #1626 and #449.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T17:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5694",
    "user": "mabshoff"
}
```

Hmm, see also #1626 and #449.

Cheers,

Michael



---

archive/issue_comments_005695.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-27T17:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5695",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005696.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2008-01-27T17:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5696",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_005697.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-26T00:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5697",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_005698.json:
```json
{
    "body": "This is a dupe of #1626",
    "created_at": "2008-03-26T00:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/932#issuecomment-5698",
    "user": "mabshoff"
}
```

This is a dupe of #1626
