# Issue 5459: Notebook and worksheet autosave intervals, excessive snapshots

archive/issues_005459.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  chapoton\n\nKeywords: notebook worksheet autosave snapshots\n\nThere is a notebook configuration item indexed by 'save_interval'.  This can be set at the sage command line by instantiating a notebook object (call it \"nb\") and issuing commands like \n`nb.conf()['save_interval'] = int(3600)`   This value seems to be used by server/notebook/twist.py to make backup copies of nb.sobj.  It seems to make a snapshot of a worksheet as a side-effect, without any check if the snapshot is different from previous snapshots.  This is speculation, since I could not decipher what triggers twist.py to check and do such a save.  Also, experimentally, I see that it happens \"automatically\", even if the worksheets and notebook are left untouched.\n\nThere is also a per-user 'autosave_interval'  This can be accessed through code like `nb.user(\"admin\")['autosave_interval']` and can also be set from the drop-down box in the \"Settings\" area of the notebook (to be 1,3,5,7,9 minutes only).  The use of this seems a bit odd.  Any edit (but only edits) in the worksheet triggers a possible snapshot save.  First, the time since the last save is checked against the user autosave_interval.  If not enough time has elapsed, it exits, otherwise it continues towards a snapshot save.  It then checks to see if the worksheet has changed.  But it must have changed, since only edits trigger the routine.  Then it writes a snapshot.\n\nSo in summary, a new snapshot every period given by 'save_interval' which is not obviously user-configurable.  No check on if the snapshot is different.  Every edit triggers a possible snapshot, it happens only if time exceeds user's autosave_interval, which can be set by the user to limited number of values.\n\nThis may be an imperfect understanding of the situation, but I think it is confusing for a user and potentially filling up disk space and/or degrading performance.  So there's some room for improvement in how this works.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5459\n\n",
    "created_at": "2009-03-09T03:54:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Notebook and worksheet autosave intervals, excessive snapshots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5459",
    "user": "rbeezer"
}
```
Assignee: somebody

CC:  chapoton

Keywords: notebook worksheet autosave snapshots

There is a notebook configuration item indexed by 'save_interval'.  This can be set at the sage command line by instantiating a notebook object (call it "nb") and issuing commands like 
`nb.conf()['save_interval'] = int(3600)`   This value seems to be used by server/notebook/twist.py to make backup copies of nb.sobj.  It seems to make a snapshot of a worksheet as a side-effect, without any check if the snapshot is different from previous snapshots.  This is speculation, since I could not decipher what triggers twist.py to check and do such a save.  Also, experimentally, I see that it happens "automatically", even if the worksheets and notebook are left untouched.

There is also a per-user 'autosave_interval'  This can be accessed through code like `nb.user("admin")['autosave_interval']` and can also be set from the drop-down box in the "Settings" area of the notebook (to be 1,3,5,7,9 minutes only).  The use of this seems a bit odd.  Any edit (but only edits) in the worksheet triggers a possible snapshot save.  First, the time since the last save is checked against the user autosave_interval.  If not enough time has elapsed, it exits, otherwise it continues towards a snapshot save.  It then checks to see if the worksheet has changed.  But it must have changed, since only edits trigger the routine.  Then it writes a snapshot.

So in summary, a new snapshot every period given by 'save_interval' which is not obviously user-configurable.  No check on if the snapshot is different.  Every edit triggers a possible snapshot, it happens only if time exceeds user's autosave_interval, which can be set by the user to limited number of values.

This may be an imperfect understanding of the situation, but I think it is confusing for a user and potentially filling up disk space and/or degrading performance.  So there's some room for improvement in how this works.


Issue created by migration from https://trac.sagemath.org/ticket/5459





---

archive/issue_comments_042391.json:
```json
{
    "body": "Upstream https://github.com/sagemath/sagenb/issues/233\n\nThere has been a lot of change and this is more or less disabled.  But still very worth fixing.",
    "created_at": "2014-09-18T02:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5459#issuecomment-42391",
    "user": "kcrisman"
}
```

Upstream https://github.com/sagemath/sagenb/issues/233

There has been a lot of change and this is more or less disabled.  But still very worth fixing.



---

archive/issue_comments_042392.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5459#issuecomment-42392",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042393.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5459#issuecomment-42393",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_042394.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5459#issuecomment-42394",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042395.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-25T15:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5459#issuecomment-42395",
    "user": "chapoton"
}
```

Resolution: invalid
