# Issue 6427: Fix doctest failures in sage-4.1.alpha1

archive/issues_006427.json:
```json
{
    "body": "Assignee: tba\n\nThe following occur in sage-4.1.alpha1:\n\n```\nThe following tests failed:\n\n        sage -t -long devel/sage/doc/fr/tutorial/programming.rst # 1 doctests failed\n        sage -t -long devel/sage/sage/misc/darwin_utilities.pyx # 3 doctests failed\n----------------------------------------------------------------------\n```\n\nthey're both really easy fixes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6427\n\n",
    "created_at": "2009-06-26T18:05:01Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Fix doctest failures in sage-4.1.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6427",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tba

The following occur in sage-4.1.alpha1:

```
The following tests failed:

        sage -t -long devel/sage/doc/fr/tutorial/programming.rst # 1 doctests failed
        sage -t -long devel/sage/sage/misc/darwin_utilities.pyx # 3 doctests failed
----------------------------------------------------------------------
```

they're both really easy fixes.

Issue created by migration from https://trac.sagemath.org/ticket/6427





---

archive/issue_comments_051517.json:
```json
{
    "body": "Attachment [6427-doctest.patch](tarball://root/attachments/some-uuid/ticket6427/6427-doctest.patch) by boothby created at 2009-06-26 18:09:01",
    "created_at": "2009-06-26T18:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6427#issuecomment-51517",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [6427-doctest.patch](tarball://root/attachments/some-uuid/ticket6427/6427-doctest.patch) by boothby created at 2009-06-26 18:09:01



---

archive/issue_comments_051518.json:
```json
{
    "body": "The change to module_list.py is wrong.  If you do that, then Sage won't build on OS X 10.4, and will waste time/space on non-OS X.  It's critical to only build that module if we're on OS X >= 10.5, since it isn't implemented for any other platform.  the other part of the patch is fine.",
    "created_at": "2009-06-26T18:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6427#issuecomment-51518",
    "user": "https://github.com/williamstein"
}
```

The change to module_list.py is wrong.  If you do that, then Sage won't build on OS X 10.4, and will waste time/space on non-OS X.  It's critical to only build that module if we're on OS X >= 10.5, since it isn't implemented for any other platform.  the other part of the patch is fine.



---

archive/issue_comments_051519.json:
```json
{
    "body": "I think the right change is to make the doctests in darwin_utilities.pyx marked \n\n```\n# optional - osx\n```",
    "created_at": "2009-06-26T18:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6427#issuecomment-51519",
    "user": "https://github.com/williamstein"
}
```

I think the right change is to make the doctests in darwin_utilities.pyx marked 

```
# optional - osx
```



---

archive/issue_events_015153.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-02T06:16:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6427",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6427#event-15153"
}
```



---

archive/issue_comments_051520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T06:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6427#issuecomment-51520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051521.json:
```json
{
    "body": "This is fixed in Sage 4.3.2.alpha1:\n\n```\n[mvngu@mod sage-4.3.2.alpha1]$ ./sage -t -long devel/sage/doc/fr/tutorial/programming.rst\nsage -t -long \"devel/sage/doc/fr/tutorial/programming.rst\"  \n\t [4.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.7 seconds\n[mvngu@mod sage-4.3.2.alpha1]$ ./sage -t -long devel/sage/sage/misc/darwin_utilities.pyx\nsage -t -long \"devel/sage/sage/misc/darwin_utilities.pyx\"   \n\t [4.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.0 seconds\n```\nI'm closing this ticket as fixed.",
    "created_at": "2010-02-02T06:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6427#issuecomment-51521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This is fixed in Sage 4.3.2.alpha1:

```
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -t -long devel/sage/doc/fr/tutorial/programming.rst
sage -t -long "devel/sage/doc/fr/tutorial/programming.rst"  
	 [4.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.7 seconds
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -t -long devel/sage/sage/misc/darwin_utilities.pyx
sage -t -long "devel/sage/sage/misc/darwin_utilities.pyx"   
	 [4.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.0 seconds
```
I'm closing this ticket as fixed.
