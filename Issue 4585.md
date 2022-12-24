# Issue 4585: "sage -upgrade" shall call the "sage-starts" script

archive/issues_004585.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn a system where \"root\" upgrades incrementally a system-wide Sage installation, and only \"normal\" users ever run Sage, there might be trouble.\n\nMore precisely, the rights to create the \"sage-flags.txt\" file --- or also the \"sage-location.txt\" file --- might not be owned by the normal user.\n\nEven if this would be only a corner case, the obvious fix (run \"sage-starts\" once during sage -upgrade\") does not hurt anybody, hence this ticket. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4585\n\n",
    "created_at": "2008-11-22T22:46:31Z",
    "labels": [
        "build",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"sage -upgrade\" shall call the \"sage-starts\" script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4585",
    "user": "GeorgSWeber"
}
```
Assignee: mabshoff

On a system where "root" upgrades incrementally a system-wide Sage installation, and only "normal" users ever run Sage, there might be trouble.

More precisely, the rights to create the "sage-flags.txt" file --- or also the "sage-location.txt" file --- might not be owned by the normal user.

Even if this would be only a corner case, the obvious fix (run "sage-starts" once during sage -upgrade") does not hurt anybody, hence this ticket. 

Issue created by migration from https://trac.sagemath.org/ticket/4585





---

archive/issue_comments_034381.json:
```json
{
    "body": "Changing assignee from mabshoff to GeorgSWeber.",
    "created_at": "2008-11-22T22:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34381",
    "user": "GeorgSWeber"
}
```

Changing assignee from mabshoff to GeorgSWeber.



---

archive/issue_comments_034382.json:
```json
{
    "body": "Hmmm,\n\nit's better to call the \"sage-location\" script directly, because starting Sage as \"root\" will create certain files/directories (.sage/...) in root's home directory, which is avoidable.",
    "created_at": "2008-11-23T08:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34382",
    "user": "GeorgSWeber"
}
```

Hmmm,

it's better to call the "sage-location" script directly, because starting Sage as "root" will create certain files/directories (.sage/...) in root's home directory, which is avoidable.



---

archive/issue_comments_034383.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34383",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034384.json:
```json
{
    "body": "`sage-location` is run when doing `sage --upgrade`.",
    "created_at": "2013-05-19T13:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34384",
    "user": "jdemeyer"
}
```

`sage-location` is run when doing `sage --upgrade`.



---

archive/issue_comments_034385.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34385",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034386.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-21T07:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34386",
    "user": "jdemeyer"
}
```

Resolution: worksforme
