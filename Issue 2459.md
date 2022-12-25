# Issue 2459: Fix GSL_DISABLE_DEPRECAED macro in setup.py

archive/issues_002459.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrancois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that:\n\n```\nIn sage-2.10.3.rc3 in the top setup.py at line 430 we have:\ndefine_macros = [('GSL_DISABLE_DEPRECAED','1')]\nFor those who can't spot it, it miss a 'T'. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2459\n\n",
    "created_at": "2008-03-10T14:58:39Z",
    "labels": [
        "component: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Fix GSL_DISABLE_DEPRECAED macro in setup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Francois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that:

```
In sage-2.10.3.rc3 in the top setup.py at line 430 we have:
define_macros = [('GSL_DISABLE_DEPRECAED','1')]
For those who can't spot it, it miss a 'T'. 
```


Issue created by migration from https://trac.sagemath.org/ticket/2459





---

archive/issue_comments_016614.json:
```json
{
    "body": "Changing component from Cygwin to build.",
    "created_at": "2008-03-10T14:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from Cygwin to build.



---

archive/issue_events_005794.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-10T14:59:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2459#event-5794"
}
```



---

archive/issue_comments_016615.json:
```json
{
    "body": "Attachment [2459.hg](tarball://root/attachments/some-uuid/ticket2459/2459.hg) by @dfdeshom created at 2008-03-14 05:42:31",
    "created_at": "2008-03-14T05:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16615",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2459.hg](tarball://root/attachments/some-uuid/ticket2459/2459.hg) by @dfdeshom created at 2008-03-14 05:42:31



---

archive/issue_comments_016616.json:
```json
{
    "body": "I've attached a patch that fixes this typo. `real_double_vector` (the module to be built in line 430) built fine and passed all doctests.",
    "created_at": "2008-03-14T05:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16616",
    "user": "https://github.com/dfdeshom"
}
```

I've attached a patch that fixes this typo. `real_double_vector` (the module to be built in line 430) built fine and passed all doctests.



---

archive/issue_events_005795.json:
```json
{
    "actor": "https://github.com/dfdeshom",
    "created_at": "2008-03-14T05:45:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2459#event-5795"
}
```



---

archive/issue_events_005796.json:
```json
{
    "actor": "https://github.com/dfdeshom",
    "created_at": "2008-03-14T05:45:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2459#event-5796"
}
```



---

archive/issue_comments_016617.json:
```json
{
    "body": "Patch looks good to me and does the right thing.",
    "created_at": "2008-03-15T07:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me and does the right thing.



---

archive/issue_comments_016618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T08:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16618",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005797.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T08:07:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2459#event-5797"
}
```



---

archive/issue_comments_016619.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-15T08:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2459#issuecomment-16619",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
