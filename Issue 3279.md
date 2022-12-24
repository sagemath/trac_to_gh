# Issue 3279: Sage 3.0.2.rc0: Copy dsage_* scripts from the scrips.spkg

archive/issues_003279.json:
```json
{
    "body": "Assignee: failure\n\nDue to a bug not caught in #3097 we end up with an inconsistent repo in $SAGE_LOCAL/bin:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.final/local/bin$ hg status\n! dsage_setup.py\n! dsage_worker.py\n```\n\nThe files are in the scripts.spkg:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.final/spkg/standard/sage_scripts-3.0.2.rc0$ ls -al dsage_*\n-rwxr-xr-x 1 mabshoff 1090  7479 2008-05-22 23:19 dsage_setup.py\n-rwxr-xr-x 1 mabshoff 1090 35459 2008-05-22 23:19 dsage_worker.py\n```\n\nWhen those two scripts are missing the DSage tests just hang.\n\nPatch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3279\n\n",
    "created_at": "2008-05-23T15:15:55Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Sage 3.0.2.rc0: Copy dsage_* scripts from the scrips.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3279",
    "user": "mabshoff"
}
```
Assignee: failure

Due to a bug not caught in #3097 we end up with an inconsistent repo in $SAGE_LOCAL/bin:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.final/local/bin$ hg status
! dsage_setup.py
! dsage_worker.py
```

The files are in the scripts.spkg:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.final/spkg/standard/sage_scripts-3.0.2.rc0$ ls -al dsage_*
-rwxr-xr-x 1 mabshoff 1090  7479 2008-05-22 23:19 dsage_setup.py
-rwxr-xr-x 1 mabshoff 1090 35459 2008-05-22 23:19 dsage_worker.py
```

When those two scripts are missing the DSage tests just hang.

Patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3279





---

archive/issue_comments_022684.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-23T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3279#issuecomment-22684",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022685.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-05-23T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3279#issuecomment-22685",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_022686.json:
```json
{
    "body": "Attachment [trac_3279.patch](tarball://root/attachments/some-uuid/ticket3279/trac_3279.patch) by mabshoff created at 2008-05-23 15:39:35",
    "created_at": "2008-05-23T15:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3279#issuecomment-22686",
    "user": "mabshoff"
}
```

Attachment [trac_3279.patch](tarball://root/attachments/some-uuid/ticket3279/trac_3279.patch) by mabshoff created at 2008-05-23 15:39:35



---

archive/issue_comments_022687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T16:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3279#issuecomment-22687",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022688.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc1",
    "created_at": "2008-05-23T16:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3279#issuecomment-22688",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.rc1
