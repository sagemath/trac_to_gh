# Issue 5803: [with patch, needs review] Upgrade Cython to 0.11.1

archive/issues_005803.json:
```json
{
    "body": "Assignee: mabshoff\n\nSpkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/5803\n\n",
    "created_at": "2009-04-16T08:38:38Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, needs review] Upgrade Cython to 0.11.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5803",
    "user": "https://github.com/robertwb"
}
```
Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/5803





---

archive/issue_comments_045463.json:
```json
{
    "body": "Attachment [5803-cython-0.11.1.patch](tarball://root/attachments/some-uuid/ticket5803/5803-cython-0.11.1.patch) by @robertwb created at 2009-04-16 08:44:53",
    "created_at": "2009-04-16T08:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5803#issuecomment-45463",
    "user": "https://github.com/robertwb"
}
```

Attachment [5803-cython-0.11.1.patch](tarball://root/attachments/some-uuid/ticket5803/5803-cython-0.11.1.patch) by @robertwb created at 2009-04-16 08:44:53



---

archive/issue_comments_045464.json:
```json
{
    "body": "Ok, positive review on the spkg. I did a number of cleanups and added a proper SPKG.txt changelog entry that Robert has been skipping forever. In the ultimate move of irony I also deleted the .hg repo inside the src repo (given the current discussion on the cython mailing list). That way the size of the spkg decreased by 3.5 MB :)\n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/alpha0/cython-0.11.1.p0.spkg\n\nRobert: Please base future spkgs on this one since I have cleaned up this spkg before. You have then based it on the a non-clean spkg and last time I let it slide, but it won't happen again and I will give it a non-positive review :)\n\nDoctesting the patch right now, but changing the review in anticipation.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T07:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5803#issuecomment-45464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, positive review on the spkg. I did a number of cleanups and added a proper SPKG.txt changelog entry that Robert has been skipping forever. In the ultimate move of irony I also deleted the .hg repo inside the src repo (given the current discussion on the cython mailing list). That way the size of the spkg decreased by 3.5 MB :)

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/alpha0/cython-0.11.1.p0.spkg

Robert: Please base future spkgs on this one since I have cleaned up this spkg before. You have then based it on the a non-clean spkg and last time I let it slide, but it won't happen again and I will give it a non-positive review :)

Doctesting the patch right now, but changing the review in anticipation.

Cheers,

Michael



---

archive/issue_comments_045465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T08:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5803#issuecomment-45465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-24T08:13:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5803",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5803#event-6052"
}
```



---

archive/issue_comments_045466.json:
```json
{
    "body": "Merged patch and spkg into Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5803#issuecomment-45466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged patch and spkg into Sage 3.4.2.alpha0.

Cheers,

Michael
