# Issue 2227: sage-2.10.2.alpha1 -- doctest broken in sageinspect.py because I added a new option

archive/issues_002227.json:
```json
{
    "body": "Assignee: failure\n\n```\n\t [8.8 s]\nsage -t  devel/sage-main/sage/misc/sageinspect.py           **********************************************************************\nFile \"sageinspect.py\", line 412:\n    sage: sage_getdef(sage.rings.integer.Integer.factor, obj_name='factor')\nExpected:\n    \"factor(algorithm='pari', proof='True')\"\nGot:\n    \"factor(algorithm='pari', proof='True', limit='None')\"\n**********************************************************************\n1 items had failures:\n   1 of  24 in __main__.example_10\n***Test Failed*** 1 failures.\n\n```\n\nFIX -- just change the doctest -- this makes perfect sense.\n(I added a new limit option to factor).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2227\n\n",
    "created_at": "2008-02-20T07:01:40Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage-2.10.2.alpha1 -- doctest broken in sageinspect.py because I added a new option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2227",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

```
	 [8.8 s]
sage -t  devel/sage-main/sage/misc/sageinspect.py           **********************************************************************
File "sageinspect.py", line 412:
    sage: sage_getdef(sage.rings.integer.Integer.factor, obj_name='factor')
Expected:
    "factor(algorithm='pari', proof='True')"
Got:
    "factor(algorithm='pari', proof='True', limit='None')"
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_10
***Test Failed*** 1 failures.

```

FIX -- just change the doctest -- this makes perfect sense.
(I added a new limit option to factor).

Issue created by migration from https://trac.sagemath.org/ticket/2227





---

archive/issue_comments_014722.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-02-20T13:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2227#issuecomment-14722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_014723.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T13:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2227#issuecomment-14723",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014724.json:
```json
{
    "body": "Attachment [trac_2227_sageinspect_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket2227/trac_2227_sageinspect_doctest_fix.patch) by mabshoff created at 2008-02-20 13:42:45\n\nFix doctest as indicated by William",
    "created_at": "2008-02-20T13:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2227#issuecomment-14724",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2227_sageinspect_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket2227/trac_2227_sageinspect_doctest_fix.patch) by mabshoff created at 2008-02-20 13:42:45

Fix doctest as indicated by William



---

archive/issue_comments_014725.json:
```json
{
    "body": "looks good.",
    "created_at": "2008-02-20T14:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2227#issuecomment-14725",
    "user": "https://github.com/jasongrout"
}
```

looks good.



---

archive/issue_comments_014726.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T14:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2227#issuecomment-14726",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha2



---

archive/issue_comments_014727.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T14:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2227#issuecomment-14727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005308.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-20T14:36:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2227",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2227#event-5308"
}
```
