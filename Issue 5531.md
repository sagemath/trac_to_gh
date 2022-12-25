# Issue 5531: [with patch, needs review] Quaternion algebra docstring formatting needs small fixes

archive/issues_005531.json:
```json
{
    "body": "Assignee: @loefflerd\n\nIn a vanilla copy of 3.4, I get complaints from sage -docbuild because some of the docstrings in sage/algebras/quaternion_algebra.py are wrongly formatted. \n\n\n```\nWARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py:docstring of sage.algebras.quaternion_algebra.unpickle_QuaternionAlgebra_v0:4: (WARNING/2) Inline emphasis start-string without end-string.\nWARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract.conjugate:13: (WARNING/2) Inline literal start-string without end-string.\nWARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_generic:3: (WARNING/2) Literal block expected; none found.\nWARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_rational_field:4: (WARNING/2) Literal block expected; none found.\nWARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0:2: (WARNING/2) Inline emphasis start-string without end-string.\nWARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0:2: (WARNING/2) Inline emphasis start-string without end-string.\n```\n\n\nThis patch fixes that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5531\n\n",
    "created_at": "2009-03-16T17:44:59Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Quaternion algebra docstring formatting needs small fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5531",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd

In a vanilla copy of 3.4, I get complaints from sage -docbuild because some of the docstrings in sage/algebras/quaternion_algebra.py are wrongly formatted. 


```
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py:docstring of sage.algebras.quaternion_algebra.unpickle_QuaternionAlgebra_v0:4: (WARNING/2) Inline emphasis start-string without end-string.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract.conjugate:13: (WARNING/2) Inline literal start-string without end-string.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_generic:3: (WARNING/2) Literal block expected; none found.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_rational_field:4: (WARNING/2) Literal block expected; none found.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0:2: (WARNING/2) Inline emphasis start-string without end-string.
WARNING: /home/david/sage-current/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra_element.so:docstring of sage.algebras.quaternion_algebra_element.unpickle_QuaternionAlgebraElement_generic_v0:2: (WARNING/2) Inline emphasis start-string without end-string.
```


This patch fixes that.

Issue created by migration from https://trac.sagemath.org/ticket/5531





---

archive/issue_comments_042924.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-16T17:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5531#issuecomment-42924",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042925.json:
```json
{
    "body": "Attachment [quaternion_docstring_fix.patch](tarball://root/attachments/some-uuid/ticket5531/quaternion_docstring_fix.patch) by @loefflerd created at 2009-03-16 17:53:03",
    "created_at": "2009-03-16T17:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5531#issuecomment-42925",
    "user": "https://github.com/loefflerd"
}
```

Attachment [quaternion_docstring_fix.patch](tarball://root/attachments/some-uuid/ticket5531/quaternion_docstring_fix.patch) by @loefflerd created at 2009-03-16 17:53:03



---

archive/issue_comments_042926.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **quaternion_docstring_fix.patch** applied OK against Sage 3.4, doctests passed even with the `-long` option, and the reference manual builds fine. Positive review for the Sphinx formatting issues that the patch fixes.\n\n\n\nHowever, while reviewing the patch I noticed some other formatting issues. But these are addressed in ticket #5541.",
    "created_at": "2009-03-17T03:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5531#issuecomment-42926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



The patch **quaternion_docstring_fix.patch** applied OK against Sage 3.4, doctests passed even with the `-long` option, and the reference manual builds fine. Positive review for the Sphinx formatting issues that the patch fixes.



However, while reviewing the patch I noticed some other formatting issues. But these are addressed in ticket #5541.



---

archive/issue_events_012967.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-20T21:50:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5531",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5531#event-12967"
}
```



---

archive/issue_comments_042927.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T21:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5531#issuecomment-42927",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042928.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T21:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5531#issuecomment-42928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
