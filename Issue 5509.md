# Issue 5509: Make a parametric_plot.pyx docstring a raw string because of a \times in it.

archive/issues_005509.json:
```json
{
    "body": "Assignee: was\n\nThe following documentation looks weird because the \\t in the \\times in the string gets converted to a tab.\n\n\n```\nsage: p.triangulate?\nType:\t\tbuiltin_function_or_method\nBase Class:\t<type 'builtin_function_or_method'>\nString Form:\t<built-in method triangulate of sage.plot.plot3d.parametric_surface.ParametricSurface object at 0xbb0cdec>\nNamespace:\tInteractive\nDocstring:\n    \n            Call self.eval() for all (u,v) in urange \times vrange\n            to construct this surface. \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5509\n\n",
    "created_at": "2009-03-13T14:39:51Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "Make a parametric_plot.pyx docstring a raw string because of a \\times in it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5509",
    "user": "jason"
}
```
Assignee: was

The following documentation looks weird because the \t in the \times in the string gets converted to a tab.


```
sage: p.triangulate?
Type:		builtin_function_or_method
Base Class:	<type 'builtin_function_or_method'>
String Form:	<built-in method triangulate of sage.plot.plot3d.parametric_surface.ParametricSurface object at 0xbb0cdec>
Namespace:	Interactive
Docstring:
    
            Call self.eval() for all (u,v) in urange 	imes vrange
            to construct this surface. 

```


Issue created by migration from https://trac.sagemath.org/ticket/5509





---

archive/issue_comments_042782.json:
```json
{
    "body": "Attachment [trac-5509-raw-docstring.patch](tarball://root/attachments/some-uuid/ticket5509/trac-5509-raw-docstring.patch) by jason created at 2009-03-13 14:43:59",
    "created_at": "2009-03-13T14:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42782",
    "user": "jason"
}
```

Attachment [trac-5509-raw-docstring.patch](tarball://root/attachments/some-uuid/ticket5509/trac-5509-raw-docstring.patch) by jason created at 2009-03-13 14:43:59



---

archive/issue_comments_042783.json:
```json
{
    "body": "This is a trivial patch, I know, but it was also to demonstrate the development process to a student.",
    "created_at": "2009-03-13T14:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42783",
    "user": "jason"
}
```

This is a trivial patch, I know, but it was also to demonstrate the development process to a student.



---

archive/issue_comments_042784.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheeers,\n\nMichael",
    "created_at": "2009-03-20T20:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42784",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheeers,

Michael



---

archive/issue_comments_042785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T20:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5509#issuecomment-42785",
    "user": "mabshoff"
}
```

Resolution: fixed
