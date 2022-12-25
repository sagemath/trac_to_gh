# Issue 2322: [with patch] dsage patch for 2.10.3

archive/issues_002322.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is the flattened patch. Please let me know if there are any problems applying it. It's based against 2.10.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2322\n\n",
    "created_at": "2008-02-26T18:06:30Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch] dsage patch for 2.10.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2322",
    "user": "https://github.com/yqiang"
}
```
Assignee: @williamstein

This is the flattened patch. Please let me know if there are any problems applying it. It's based against 2.10.2.

Issue created by migration from https://trac.sagemath.org/ticket/2322





---

archive/issue_comments_015408.json:
```json
{
    "body": "Patch located here:\nhttp://sage.math.washington.edu/home/yqiang/dsage-2.10.3.patch\n\nI could not attach it because it exceeded the maximum file size =)",
    "created_at": "2008-02-26T18:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15408",
    "user": "https://github.com/yqiang"
}
```

Patch located here:
http://sage.math.washington.edu/home/yqiang/dsage-2.10.3.patch

I could not attach it because it exceeded the maximum file size =)



---

archive/issue_comments_015409.json:
```json
{
    "body": "I assume that this is the patch that was reviewed by William and rlm yesterday? In case it is please have one of them add formal positive review to this so it can be merged.",
    "created_at": "2008-02-26T18:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I assume that this is the patch that was reviewed by William and rlm yesterday? In case it is please have one of them add formal positive review to this so it can be merged.



---

archive/issue_comments_015410.json:
```json
{
    "body": "Oops, wrong text box: Here we go again: It would also be nice to have a high level changelog at this ticket to indicate the changes made. I assume this also includes Timothy's patch from #2280?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-26T18:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, wrong text box: Here we go again: It would also be nice to have a high level changelog at this ticket to indicate the changes made. I assume this also includes Timothy's patch from #2280?

Cheers,

Michael



---

archive/issue_comments_015411.json:
```json
{
    "body": "For the record: Patch applies fine against my tree, so I can merge once I get the positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-26T18:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: Patch applies fine against my tree, so I can merge once I get the positive review.

Cheers,

Michael



---

archive/issue_comments_015412.json:
```json
{
    "body": "high level changelog",
    "created_at": "2008-02-26T18:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15412",
    "user": "https://github.com/yqiang"
}
```

high level changelog



---

archive/issue_comments_015413.json:
```json
{
    "body": "Attachment [dsage changelog.txt](tarball://root/attachments/some-uuid/ticket2322/dsage changelog.txt) by mabshoff created at 2008-02-26 21:19:50\n\nFrom the changelog it looks like we depend on SQLAlchemy, i.e. #2205. Is that correct?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-26T21:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [dsage changelog.txt](tarball://root/attachments/some-uuid/ticket2322/dsage changelog.txt) by mabshoff created at 2008-02-26 21:19:50

From the changelog it looks like we depend on SQLAlchemy, i.e. #2205. Is that correct?

Cheers,

Michael



---

archive/issue_comments_015414.json:
```json
{
    "body": "Yes this is correct. I couldn't find a way to specify dependencies in trac, that would be a nice feature =). For the record\n\ndsage depends on sqlalchemy which depends on setuptools.",
    "created_at": "2008-02-26T22:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15414",
    "user": "https://github.com/yqiang"
}
```

Yes this is correct. I couldn't find a way to specify dependencies in trac, that would be a nice feature =). For the record

dsage depends on sqlalchemy which depends on setuptools.



---

archive/issue_comments_015415.json:
```json
{
    "body": "Here are the exact steps needed to apply the patch and make everything work correctly:\n\n1) Apply dsage-2.10.3.patch. NOTE: Do not panic at the dirstate message. It\nwill be fixed by step 2.\n2) Remove sage/dsage/doc\n3) Remove sage/dsage/dist_functions/nodoctest.py\n4) Remove dsage_server.py from $SAGE_ROOT/local/bin",
    "created_at": "2008-03-01T23:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15415",
    "user": "https://github.com/yqiang"
}
```

Here are the exact steps needed to apply the patch and make everything work correctly:

1) Apply dsage-2.10.3.patch. NOTE: Do not panic at the dirstate message. It
will be fixed by step 2.
2) Remove sage/dsage/doc
3) Remove sage/dsage/dist_functions/nodoctest.py
4) Remove dsage_server.py from $SAGE_ROOT/local/bin



---

archive/issue_comments_015416.json:
```json
{
    "body": "Looks good to me, apply.\n\nComments:\n\n1. Every single function should have some sort of descriptive text saying what it is doing, even if it doesn't have a doctest since dsage is an exception to the rule. However, to avoid bitrot, this isn't blocking the patch.\n\n2. There are some obsolete code snippets that still use SQLite that need to be removed.",
    "created_at": "2008-03-01T23:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15416",
    "user": "https://github.com/rlmill"
}
```

Looks good to me, apply.

Comments:

1. Every single function should have some sort of descriptive text saying what it is doing, even if it doesn't have a doctest since dsage is an exception to the rule. However, to avoid bitrot, this isn't blocking the patch.

2. There are some obsolete code snippets that still use SQLite that need to be removed.



---

archive/issue_comments_015417.json:
```json
{
    "body": "NOTE:\n\nIn step 2), you actually need 'hg rm sage/dsage/doc', and in step 3), 'hg rm sage/dsage/dist_functions/nodoctest.py' from the branch root. Step 4), you just delete the file.\n\nThere is also a step 5): after everything else, apply:\n\nhttp://sage.math.washington.edu/home/rlmill/2322-step5.patch\n\nAlso, we tested everything against 2.10.3.rc0 (with SQLAlchemy installed), and the instructions worked, and all the tests passed.\n\nThis is definitely ready to merge. -- RLM",
    "created_at": "2008-03-02T00:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15417",
    "user": "https://github.com/rlmill"
}
```

NOTE:

In step 2), you actually need 'hg rm sage/dsage/doc', and in step 3), 'hg rm sage/dsage/dist_functions/nodoctest.py' from the branch root. Step 4), you just delete the file.

There is also a step 5): after everything else, apply:

http://sage.math.washington.edu/home/rlmill/2322-step5.patch

Also, we tested everything against 2.10.3.rc0 (with SQLAlchemy installed), and the instructions worked, and all the tests passed.

This is definitely ready to merge. -- RLM



---

archive/issue_comments_015418.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T17:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015419.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0 - I followed all five steps and did commit after step three.",
    "created_at": "2008-03-14T17:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2322#issuecomment-15419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0 - I followed all five steps and did commit after step three.



---

archive/issue_events_002498.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T17:47:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2322#event-2498"
}
```
