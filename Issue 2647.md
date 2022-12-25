# Issue 2647: [with spkg; positive review] Fixed Debian support for linbox

archive/issues_002647.json:
```json
{
    "body": "Assignee: @timabbott\n\nApparently the debian support for linbox didn't make it into the 1.1.5 spkg whenever that was created.  Since the linbox spkg had a bunch of uncommitted changes, I've put the relevant files (with some fixes I needed to do anyway) in a new spkg; the only things changed from the old 1.1.5rc2.p4 spkg should be dist/ and spkg-debian:\n\nhttp://sage.math.washington.edu/home/tabbott/linbox-1.1.5rc2.p5.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/2647\n\n",
    "closed_at": "2008-03-22T21:01:49Z",
    "created_at": "2008-03-22T16:55:32Z",
    "labels": [
        "component: debian-package"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with spkg; positive review] Fixed Debian support for linbox",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2647",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

Apparently the debian support for linbox didn't make it into the 1.1.5 spkg whenever that was created.  Since the linbox spkg had a bunch of uncommitted changes, I've put the relevant files (with some fixes I needed to do anyway) in a new spkg; the only things changed from the old 1.1.5rc2.p4 spkg should be dist/ and spkg-debian:

http://sage.math.washington.edu/home/tabbott/linbox-1.1.5rc2.p5.spkg

Issue created by migration from https://trac.sagemath.org/ticket/2647





---

archive/issue_comments_018163.json:
```json
{
    "body": "Hi Tim,\n\nthe updated SPKG at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha1/linbox-1.1.5rc2.p6.spkg\n\nincludes the Debian code, cleans up SPKG.txt and commits all changes to the repo.\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T21:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2647#issuecomment-18163",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Tim,

the updated SPKG at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha1/linbox-1.1.5rc2.p6.spkg

includes the Debian code, cleans up SPKG.txt and commits all changes to the repo.

Positive review.

Cheers,

Michael



---

archive/issue_events_006198.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-22T21:01:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2647",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2647#event-6198"
}
```



---

archive/issue_comments_018164.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T21:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2647#issuecomment-18164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_events_006199.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-22T21:01:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2647",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2647#event-6199"
}
```



---

archive/issue_comments_018165.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T21:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2647#issuecomment-18165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
