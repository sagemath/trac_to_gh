# Issue 4698: [with patch, needs review] a single make_element function for pickling is hard to maintain

archive/issues_004698.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robertwb @williamstein\n\nAll subclasses of `sage.structure.element.Element` end up using `sage.structure.element.make_element` for unpickling. This design is very hard to maintain, especially when trying to keep backward compatibility with older pickles. \n\nPython's pickling protocol via `__getstate__()` and `__setstate__()` moves the implementation of pickling/unpickling to the subclasses. [1] Attached patch changes sage.structure.element.Element to use this protocol.\n\n[1] http://www.python.org/doc/2.5/lib/pickle-inst.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/4698\n\n",
    "created_at": "2008-12-04T23:04:26Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review] a single make_element function for pickling is hard to maintain",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4698",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @robertwb @williamstein

All subclasses of `sage.structure.element.Element` end up using `sage.structure.element.make_element` for unpickling. This design is very hard to maintain, especially when trying to keep backward compatibility with older pickles. 

Python's pickling protocol via `__getstate__()` and `__setstate__()` moves the implementation of pickling/unpickling to the subclasses. [1] Attached patch changes sage.structure.element.Element to use this protocol.

[1] http://www.python.org/doc/2.5/lib/pickle-inst.html

Issue created by migration from https://trac.sagemath.org/ticket/4698





---

archive/issue_comments_035322.json:
```json
{
    "body": "Attachment [trac_4698-pickle.patch](tarball://root/attachments/some-uuid/ticket4698/trac_4698-pickle.patch) by @williamstein created at 2008-12-06 22:28:38\n\nI fully doctested this on sage.math and it worked perfectly. \n\nI read the code and it looks good, and like a nice solution.  Bravo.",
    "created_at": "2008-12-06T22:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4698#issuecomment-35322",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4698-pickle.patch](tarball://root/attachments/some-uuid/ticket4698/trac_4698-pickle.patch) by @williamstein created at 2008-12-06 22:28:38

I fully doctested this on sage.math and it worked perfectly. 

I read the code and it looks good, and like a nice solution.  Bravo.



---

archive/issue_events_004943.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-07T08:07:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4698",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4698#event-4943"
}
```



---

archive/issue_comments_035323.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha1",
    "created_at": "2008-12-07T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4698#issuecomment-35323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha1



---

archive/issue_comments_035324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4698#issuecomment-35324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
