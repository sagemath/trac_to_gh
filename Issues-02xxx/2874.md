# Issue 2874: [with patch, positive review] add tests for type E root system, correct some misinformation in root_system.py, add Justin Walker credit

archive/issues_002874.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nThis patch was written with Justin Walker, who originally coded the exceptional group root systems based on data from Bourbaki. The patch does 3 things.\n\n(1) Replaces self.dim with self.rank in AmbientLattice_e and corrects some related misinformation in a comment in the file. (The a comment in the file formerly said that E6 had rank 5.)\n\n(2) Adds tests. We checked the dimensions of the fundamental representations against what they are supposed to be (from another source), which is a convincing test that all the root data are correct.\n\n(3) Adds a credit for Justin in the file. This was my idea since I know Justin worked hard on getting the exceptional groups coded but if it is controversial it can be taken down.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2874\n\n",
    "closed_at": "2008-04-11T01:39:27Z",
    "created_at": "2008-04-11T00:55:08Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] add tests for type E root system, correct some misinformation in root_system.py, add Justin Walker credit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2874",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

This patch was written with Justin Walker, who originally coded the exceptional group root systems based on data from Bourbaki. The patch does 3 things.

(1) Replaces self.dim with self.rank in AmbientLattice_e and corrects some related misinformation in a comment in the file. (The a comment in the file formerly said that E6 had rank 5.)

(2) Adds tests. We checked the dimensions of the fundamental representations against what they are supposed to be (from another source), which is a convincing test that all the root data are correct.

(3) Adds a credit for Justin in the file. This was my idea since I know Justin worked hard on getting the exceptional groups coded but if it is controversial it can be taken down.



Issue created by migration from https://trac.sagemath.org/ticket/2874





---

archive/issue_comments_019703.json:
```json
{
    "body": "Attachment [rootsystem.patch](tarball://root/attachments/some-uuid/ticket2874/rootsystem.patch) by @dwbump created at 2008-04-11 00:56:36",
    "created_at": "2008-04-11T00:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2874#issuecomment-19703",
    "user": "https://github.com/dwbump"
}
```

Attachment [rootsystem.patch](tarball://root/attachments/some-uuid/ticket2874/rootsystem.patch) by @dwbump created at 2008-04-11 00:56:36



---

archive/issue_comments_019704.json:
```json
{
    "body": "Yep, Justin should definitely get credit for the exceptional groups.\n\nLooks good to me.",
    "created_at": "2008-04-11T01:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2874#issuecomment-19704",
    "user": "https://github.com/mwhansen"
}
```

Yep, Justin should definitely get credit for the exceptional groups.

Looks good to me.



---

archive/issue_comments_019705.json:
```json
{
    "body": "Dan, \n\nplease post mercurial patches in the future. You need to use export instead of diff. That way you get properly credited in the log as author of the patch. Let me know if you have any more questions.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-11T01:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2874#issuecomment-19705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Dan, 

please post mercurial patches in the future. You need to use export instead of diff. That way you get properly credited in the log as author of the patch. Let me know if you have any more questions.

Cheers,

Michael



---

archive/issue_comments_019706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-11T01:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2874#issuecomment-19706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006569.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-11T01:39:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2874",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2874#event-6569"
}
```



---

archive/issue_comments_019707.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-11T01:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2874#issuecomment-19707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4
