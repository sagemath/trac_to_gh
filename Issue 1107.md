# Issue 1107: [with patch] add minkowski bound function for number fields

archive/issues_001107.json:
```json
{
    "body": "Assignee: @williamstein\n\nAdd computation of Minkowski bound to number fields (very simple). \n\nIssue created by migration from https://trac.sagemath.org/ticket/1107\n\n",
    "created_at": "2007-11-05T21:29:44Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] add minkowski bound function for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1107",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Add computation of Minkowski bound to number fields (very simple). 

Issue created by migration from https://trac.sagemath.org/ticket/1107





---

archive/issue_events_002968.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-16T11:56:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1107#event-2968"
}
```



---

archive/issue_comments_006677.json:
```json
{
    "body": "The patch is good.",
    "created_at": "2007-11-18T09:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6677",
    "user": "https://github.com/robertwb"
}
```

The patch is good.



---

archive/issue_comments_006678.json:
```json
{
    "body": "The patch no longer applies cleanly:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/devel/sage$ hg import minkowski.patch\napplying minkowski.patch\npatching file sage/rings/rational_field.py\nHunk #1 succeeded at 298 with fuzz 2 (offset 23 lines).\nHunk #2 FAILED at 362\nHunk #3 FAILED at 370\nHunk #4 FAILED at 378\n3 out of 4 hunks FAILED -- saving rejects to file sage/rings/rational_field.py.rej\nabort: patch failed to apply\n```\n\n\nCheers,\n\nMichaell",
    "created_at": "2007-11-19T21:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6678",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch no longer applies cleanly:

```
mabshoff@sage:/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/devel/sage$ hg import minkowski.patch
applying minkowski.patch
patching file sage/rings/rational_field.py
Hunk #1 succeeded at 298 with fuzz 2 (offset 23 lines).
Hunk #2 FAILED at 362
Hunk #3 FAILED at 370
Hunk #4 FAILED at 378
3 out of 4 hunks FAILED -- saving rejects to file sage/rings/rational_field.py.rej
abort: patch failed to apply
```


Cheers,

Michaell



---

archive/issue_comments_006679.json:
```json
{
    "body": "\n```\ncwitty: williamstein, did you notice mabshoff's comment on your #1107 patch?  Evidently it no longer applies.\n[9:13pm] williamstein: Thanks.  \n[9:16pm] williamstein: actually it's fine -- the one hunk that doesn't get applied with 1107 doesn't apply because it is already applied in the current sage.\n[9:16pm] williamstein: So it's OK.  Just ignore the one hunk that fails. \n```\n",
    "created_at": "2007-11-27T05:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6679",
    "user": "https://github.com/williamstein"
}
```


```
cwitty: williamstein, did you notice mabshoff's comment on your #1107 patch?  Evidently it no longer applies.
[9:13pm] williamstein: Thanks.  
[9:16pm] williamstein: actually it's fine -- the one hunk that doesn't get applied with 1107 doesn't apply because it is already applied in the current sage.
[9:16pm] williamstein: So it's OK.  Just ignore the one hunk that fails. 
```




---

archive/issue_comments_006680.json:
```json
{
    "body": "\n```\n\n[9:17pm] cwitty: The three hunks that don't get applied, you mean?  (Judging from mabshoff's comment.)\n[9:20pm] williamstein: Yes, that's what I meant.  Thanks.\n```\n",
    "created_at": "2007-11-27T05:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6680",
    "user": "https://github.com/williamstein"
}
```


```

[9:17pm] cwitty: The three hunks that don't get applied, you mean?  (Judging from mabshoff's comment.)
[9:20pm] williamstein: Yes, that's what I meant.  Thanks.
```




---

archive/issue_comments_006681.json:
```json
{
    "body": "Attachment [minkowski.patch](tarball://root/attachments/some-uuid/ticket1107/minkowski.patch) by @williamstein created at 2007-11-27 05:48:08\n\nThis is rebased against 2.8.15",
    "created_at": "2007-11-27T05:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6681",
    "user": "https://github.com/williamstein"
}
```

Attachment [minkowski.patch](tarball://root/attachments/some-uuid/ticket1107/minkowski.patch) by @williamstein created at 2007-11-27 05:48:08

This is rebased against 2.8.15



---

archive/issue_comments_006682.json:
```json
{
    "body": "OK, I rebased it so I get credit :-)",
    "created_at": "2007-11-27T05:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6682",
    "user": "https://github.com/williamstein"
}
```

OK, I rebased it so I get credit :-)



---

archive/issue_comments_006683.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-11-29T22:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6683",
    "user": "https://github.com/robertwb"
}
```

Looks good to me.



---

archive/issue_comments_006684.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6684",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_006685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1107#issuecomment-6685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002969.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T11:30:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1107",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1107#event-2969"
}
```
