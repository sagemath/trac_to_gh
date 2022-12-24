# Issue 2718: increase the default doctest timeout to 360 seconds

archive/issues_002718.json:
```json
{
    "body": "Assignee: failure\n\nE.g., issues like this:\n\n\n```\nThe athlon 32-bit linux box has the most files failing:\n   http://sage.math.washington.edu/home/was/build/tests/2.11.alpha2/Linux-meccah.log\n\n\tsage -t  devel/sage-main/sage/interfaces/psage.py\n\tsage -t  devel/sage-main/sage/interfaces/sage0.py\n\tsage -t  devel/sage-main/sage/dsage/tests/testdoc.py\n\tsage -t  devel/sage-main/sage/calculus/calculus.py\n\nAlso tut.tex fails due to the timeout. \n\nWe should raise the timeout, since calculus is a timeout issue, and\nit should be possible to test Sage even on a mere 2.1Ghz machine.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2718\n\n",
    "created_at": "2008-03-29T16:28:51Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "increase the default doctest timeout to 360 seconds",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2718",
    "user": "was"
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

archive/issue_comments_018740.json:
```json
{
    "body": "Attachment [trac_2718.patch](tarball://root/attachments/some-uuid/ticket2718/trac_2718.patch) by mabshoff created at 2008-03-29 17:21:43",
    "created_at": "2008-03-29T17:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18740",
    "user": "mabshoff"
}
```

Attachment [trac_2718.patch](tarball://root/attachments/some-uuid/ticket2718/trac_2718.patch) by mabshoff created at 2008-03-29 17:21:43



---

archive/issue_comments_018741.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-29T17:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18741",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018742.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-03-29T17:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18742",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_018743.json:
```json
{
    "body": "I tested that the patch applies and doctesting still works; I did not explicitly test that the timeout changed.\n\nLooks good.",
    "created_at": "2008-03-29T17:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18743",
    "user": "cwitty"
}
```

I tested that the patch applies and doctesting still works; I did not explicitly test that the timeout changed.

Looks good.



---

archive/issue_comments_018744.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T17:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18744",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_018745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T17:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2718",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2718#issuecomment-18745",
    "user": "mabshoff"
}
```

Resolution: fixed
