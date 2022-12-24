# Issue 3553: Update eclib to eclib-20080310.p4.spkg

archive/issues_003553.json:
```json
{
    "body": "Assignee: cremona\n\nThere's a newly patched version here:\n\nhttp://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20080310.p4.spkg\n\nJohn Cremona removed some unused LiDiA code since it no longer builds. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3553\n\n",
    "created_at": "2008-07-05T20:42:22Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Update eclib to eclib-20080310.p4.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3553",
    "user": "mabshoff"
}
```
Assignee: cremona

There's a newly patched version here:

http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20080310.p4.spkg

John Cremona removed some unused LiDiA code since it no longer builds. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3553





---

archive/issue_comments_025131.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-05T21:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3553#issuecomment-25131",
    "user": "mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_025132.json:
```json
{
    "body": "The spkg was based on eclib-20080310.p3.spkg without my fixes to SPKG.txt and the current spkg also did not have a changelog in SPKG.txt. I added back the changes for p3 and also wrote a new entry for p4. In addition the hg repo in src had uncommitted changes:\n\n```\neclib-20080310.p4/src$ hg status\nM procs/gf.h\nM procs/interface.h\nM procs/marith.cc\nM procs/marith.h\nM procs/mptest.cc\nM procs/mptest.out\n```\n\nI checked those in in John's name. Builds fine for me.\n\nJohn: the updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/eclib-20080310.p4.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-07-05T22:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3553#issuecomment-25132",
    "user": "mabshoff"
}
```

The spkg was based on eclib-20080310.p3.spkg without my fixes to SPKG.txt and the current spkg also did not have a changelog in SPKG.txt. I added back the changes for p3 and also wrote a new entry for p4. In addition the hg repo in src had uncommitted changes:

```
eclib-20080310.p4/src$ hg status
M procs/gf.h
M procs/interface.h
M procs/marith.cc
M procs/marith.h
M procs/mptest.cc
M procs/mptest.out
```

I checked those in in John's name. Builds fine for me.

John: the updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/eclib-20080310.p4.spkg

Cheers,

Michael



---

archive/issue_comments_025133.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-05T22:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3553#issuecomment-25133",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025134.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-05T22:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3553#issuecomment-25134",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
