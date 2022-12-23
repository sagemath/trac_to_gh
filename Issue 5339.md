# Issue 5339: update README.txt to reflect what platforms we currently supporting building sage with

archive/issues_005339.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  drkirkby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5339\n\n",
    "created_at": "2009-02-22T18:52:08Z",
    "labels": [
        "distribution",
        "major",
        "enhancement"
    ],
    "title": "update README.txt to reflect what platforms we currently supporting building sage with",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5339",
    "user": "was"
}
```
Assignee: mabshoff

CC:  drkirkby



Issue created by migration from https://trac.sagemath.org/ticket/5339





---

archive/issue_comments_041135.json:
```json
{
    "body": "Better luck in Sage 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5339#issuecomment-41135",
    "user": "mabshoff"
}
```

Better luck in Sage 3.4.1.

Cheers,

Michael



---

archive/issue_comments_041136.json:
```json
{
    "body": "This is also relevant (from David Kirkby):\n\n```\nLooking at the top level README.txt in sage-3.4.2.alpha0, there are a\ncouple of things about Solaris of note. The first is minor - the second\nless so.\n\n1) At one point its called Solaris, and another SOLARIS. After finding\n'Solaris' at the top, I did a search (using vi as the editor) and found\nlittle reference to it. Later I see the operating system referred to as\nSOLARIS. It might be worth using the same case, or at least referring to\nit as 'Solaris' in the 'SOLARIS' section, in case someone does a\ncase-sensitive search.\n\n2) More importantly, one reads:\n-----------\n    SOLARIS:\n      It is reportedly possible, but not recommended yet (see below).\n      A fully supported port is planned.\n-----------\n\nBut there is NOTHING below that point in the README.txt about Solaris -\ndespite the \"see below\" in there.\n\nIt would be worth either putting what information was planned about\nSolaris in the README.txt, or making a 'Solaris.txt' with what\ninformation is needed. Obviously a link to the tool chain would be worth\nputting. \n```\n",
    "created_at": "2009-04-29T03:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5339#issuecomment-41136",
    "user": "mabshoff"
}
```

This is also relevant (from David Kirkby):

```
Looking at the top level README.txt in sage-3.4.2.alpha0, there are a
couple of things about Solaris of note. The first is minor - the second
less so.

1) At one point its called Solaris, and another SOLARIS. After finding
'Solaris' at the top, I did a search (using vi as the editor) and found
little reference to it. Later I see the operating system referred to as
SOLARIS. It might be worth using the same case, or at least referring to
it as 'Solaris' in the 'SOLARIS' section, in case someone does a
case-sensitive search.

2) More importantly, one reads:
-----------
    SOLARIS:
      It is reportedly possible, but not recommended yet (see below).
      A fully supported port is planned.
-----------

But there is NOTHING below that point in the README.txt about Solaris -
despite the "see below" in there.

It would be worth either putting what information was planned about
Solaris in the README.txt, or making a 'Solaris.txt' with what
information is needed. Obviously a link to the tool chain would be worth
putting. 
```




---

archive/issue_comments_041137.json:
```json
{
    "body": "Should I close this as a \"duplicate\" of #9487?",
    "created_at": "2010-08-07T04:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5339#issuecomment-41137",
    "user": "mpatel"
}
```

Should I close this as a "duplicate" of #9487?



---

archive/issue_comments_041138.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Should I close this as a \"duplicate\" of #9487?\n\nYes, that seems reasonable. Technically #9487 is a duplicate of this, but there's more useful information on #9487. This has also at least partially been fixed by another ticket, so I would close it. \n\nDave",
    "created_at": "2010-08-07T10:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5339#issuecomment-41138",
    "user": "drkirkby"
}
```

Replying to [comment:3 mpatel]:
> Should I close this as a "duplicate" of #9487?

Yes, that seems reasonable. Technically #9487 is a duplicate of this, but there's more useful information on #9487. This has also at least partially been fixed by another ticket, so I would close it. 

Dave



---

archive/issue_comments_041139.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-07T10:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5339#issuecomment-41139",
    "user": "mpatel"
}
```

Resolution: duplicate
