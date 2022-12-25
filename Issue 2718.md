# Issue 2718: increase the default doctest timeout to 360 seconds

archive/issues_002718.json:
```json
{
    "body": "Assignee: failure\n\nE.g., issues like this:\n\n```\nThe athlon 32-bit linux box has the most files failing:\n   http://sage.math.washington.edu/home/was/build/tests/2.11.alpha2/Linux-meccah.log\n\n\tsage -t  devel/sage-main/sage/interfaces/psage.py\n\tsage -t  devel/sage-main/sage/interfaces/sage0.py\n\tsage -t  devel/sage-main/sage/dsage/tests/testdoc.py\n\tsage -t  devel/sage-main/sage/calculus/calculus.py\n\nAlso tut.tex fails due to the timeout. \n\nWe should raise the timeout, since calculus is a timeout issue, and\nit should be possible to test Sage even on a mere 2.1Ghz machine.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2718\n\n",
    "created_at": "2008-03-29T16:28:51Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "increase the default doctest timeout to 360 seconds",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2718",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

E.g., issues like this:

```
The athlon 32-bit linux box has the most files failing:
   http://sage.math.washington.edu/home/was/build/tests/2.11.alpha2/Linux-meccah.log

	sage -t  devel/sage-main/sage/interfaces/psage.py
	sage -t  devel/sage-main/sage/interfaces/sage0.py
	sage -t  devel/sage-main/sage/dsage/tests/testdoc.py
	sage -t  devel/sage-main/sage/calculus/calculus.py

Also tut.tex fails due to the timeout. 

We should raise the timeout, since calculus is a timeout issue, and
it should be possible to test Sage even on a mere 2.1Ghz machine.
```

Issue created by migration from https://trac.sagemath.org/ticket/2718





---

archive/issue_comments_018701.json:
```json
{
    "body": "Attachment [trac_2718.patch](tarball://root/attachments/some-uuid/ticket2718/trac_2718.patch) by mabshoff created at 2008-03-29 17:21:43",
    "created_at": "2008-03-29T17:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18701",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2718.patch](tarball://root/attachments/some-uuid/ticket2718/trac_2718.patch) by mabshoff created at 2008-03-29 17:21:43



---

archive/issue_comments_018702.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-29T17:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18702",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018703.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-03-29T17:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_018704.json:
```json
{
    "body": "I tested that the patch applies and doctesting still works; I did not explicitly test that the timeout changed.\n\nLooks good.",
    "created_at": "2008-03-29T17:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18704",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I tested that the patch applies and doctesting still works; I did not explicitly test that the timeout changed.

Looks good.



---

archive/issue_events_006343.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T17:33:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2718#event-6343"
}
```



---

archive/issue_comments_018705.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T17:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T17:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
