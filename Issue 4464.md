# Issue 4464: devel/sage/sage/combinat/root_system/weyl_characters.py test (too) long

archive/issues_004464.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: test, long\n\nJaap,\n\ncan you please open a ticket for that one. I suspect that we don't\nhave anything tested via long or that the tests aren't properly marked\n\"#long time\". This one has popped up so often that we really ought to\nfix it once and for all since you hit it every time.\n\n[...]\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4464\n\n",
    "created_at": "2008-11-07T17:58:33Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "title": "devel/sage/sage/combinat/root_system/weyl_characters.py test (too) long",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4464",
    "user": "jsp"
}
```
Assignee: mabshoff

Keywords: test, long

Jaap,

can you please open a ticket for that one. I suspect that we don't
have anything tested via long or that the tests aren't properly marked
"#long time". This one has popped up so often that we really ought to
fix it once and for all since you hit it every time.

[...]

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4464





---

archive/issue_comments_032968.json:
```json
{
    "body": "I think the file weyl_characters.py should be converted to Cython. The single most computationally intensive thing is the Freudenthal multiplicity formula (which is invoked a lot).",
    "created_at": "2008-11-08T12:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4464#issuecomment-32968",
    "user": "bump"
}
```

I think the file weyl_characters.py should be converted to Cython. The single most computationally intensive thing is the Freudenthal multiplicity formula (which is invoked a lot).



---

archive/issue_comments_032969.json:
```json
{
    "body": "Replying to [comment:1 bump]:\n> I think the file weyl_characters.py should be converted to Cython. The single most computationally intensive thing is the Freudenthal multiplicity formula (which is invoked a lot).\n\nHi Dan,\n\nthat sounds fine to me, but we should do that on another ticket post Sage 3.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T00:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4464#issuecomment-32969",
    "user": "mabshoff"
}
```

Replying to [comment:1 bump]:
> I think the file weyl_characters.py should be converted to Cython. The single most computationally intensive thing is the Freudenthal multiplicity formula (which is invoked a lot).

Hi Dan,

that sounds fine to me, but we should do that on another ticket post Sage 3.2.

Cheers,

Michael



---

archive/issue_comments_032970.json:
```json
{
    "body": "#5721 fixed this.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T22:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4464#issuecomment-32970",
    "user": "mabshoff"
}
```

#5721 fixed this.

Cheers,

Michael



---

archive/issue_comments_032971.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T22:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4464#issuecomment-32971",
    "user": "mabshoff"
}
```

Resolution: fixed
