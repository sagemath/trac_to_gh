# Issue 5509: [with patch, positive review] Make a parametric_plot.pyx docstring a raw string because of a \times in it.

archive/issues_005509.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following documentation looks weird because the \\t in the \\times in the string gets converted to a tab.\n\n```\nsage: p.triangulate?\nType:builtin_function_or_method\nBase Class:<type 'builtin_function_or_method'>\nString Form:<built-in method triangulate of sage.plot.plot3d.parametric_surface.ParametricSurface object at 0xbb0cdec>\nNamespace:Interactive\nDocstring:\n\n            Call self.eval() for all (u,v) in urange times vrange\n            to construct this surface. \n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5509\n\n",
    "closed_at": "2009-03-20T20:35:06Z",
    "created_at": "2009-03-13T14:39:51Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] Make a parametric_plot.pyx docstring a raw string because of a \\times in it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5509",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The following documentation looks weird because the \t in the \times in the string gets converted to a tab.

```
sage: p.triangulate?
Type:builtin_function_or_method
Base Class:<type 'builtin_function_or_method'>
String Form:<built-in method triangulate of sage.plot.plot3d.parametric_surface.ParametricSurface object at 0xbb0cdec>
Namespace:Interactive
Docstring:

            Call self.eval() for all (u,v) in urange times vrange
            to construct this surface. 

```

Issue created by migration from https://trac.sagemath.org/ticket/5509





---

archive/issue_comments_042699.json:
```json
{
    "body": "Attachment [trac-5509-raw-docstring.patch](tarball://root/attachments/some-uuid/ticket5509/trac-5509-raw-docstring.patch) by @jasongrout created at 2009-03-13 14:43:59",
    "created_at": "2009-03-13T14:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42699",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5509-raw-docstring.patch](tarball://root/attachments/some-uuid/ticket5509/trac-5509-raw-docstring.patch) by @jasongrout created at 2009-03-13 14:43:59



---

archive/issue_comments_042700.json:
```json
{
    "body": "This is a trivial patch, I know, but it was also to demonstrate the development process to a student.",
    "created_at": "2009-03-13T14:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42700",
    "user": "https://github.com/jasongrout"
}
```

This is a trivial patch, I know, but it was also to demonstrate the development process to a student.



---

archive/issue_events_012908.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-20T20:35:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5509#event-12908"
}
```



---

archive/issue_comments_042701.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheeers,\n\nMichael",
    "created_at": "2009-03-20T20:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42701",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheeers,

Michael



---

archive/issue_comments_042702.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T20:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42702",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
