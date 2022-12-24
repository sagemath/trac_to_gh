# Issue 5616: speed regression with fast_callable

archive/issues_005616.json:
```json
{
    "body": "Assignee: cwitty\n\nBefore (vanilla 3.4)\n\n\n```\nsage: var('x,y')\n(x, y)\nsage: time P = parametric_plot3d((x, y, x*y), (x, -10, 10), (y, -10, 10), plot_points=(500,500))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: time P.triangulate()\nCPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s\nWall time: 0.08 s\n```\n\n\nafter (3.4 + #5093)\n\n\n```\nsage: sage: var('x,y')\n(x, y)\nsage: sage: time P = parametric_plot3d((x, y, x*y), (x, -10, 10), (y, -10, 10), plot_points=(500,500))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: sage: time P.triangulate()\nCPU times: user 0.28 s, sys: 0.02 s, total: 0.30 s\nWall time: 0.30 s\n```\n\n\nI think this is due to there not being an interface to evaluate fast_callable objects without passing through Python. Perhaps a \n\n\n```\ncdef int call_c(void* args, void* ret) except -1\n```\n\n\nmethod should be attached to the generic interpreter wrapper class (to be overridden by the subclasses), and those with specific knowledge about the various implementations could then use this interface (e.g. RDF passes double*). \n\nIssue created by migration from https://trac.sagemath.org/ticket/5616\n\n",
    "created_at": "2009-03-26T08:31:17Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "speed regression with fast_callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5616",
    "user": "@robertwb"
}
```
Assignee: cwitty

Before (vanilla 3.4)


```
sage: var('x,y')
(x, y)
sage: time P = parametric_plot3d((x, y, x*y), (x, -10, 10), (y, -10, 10), plot_points=(500,500))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time P.triangulate()
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.08 s
```


after (3.4 + #5093)


```
sage: sage: var('x,y')
(x, y)
sage: sage: time P = parametric_plot3d((x, y, x*y), (x, -10, 10), (y, -10, 10), plot_points=(500,500))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: sage: time P.triangulate()
CPU times: user 0.28 s, sys: 0.02 s, total: 0.30 s
Wall time: 0.30 s
```


I think this is due to there not being an interface to evaluate fast_callable objects without passing through Python. Perhaps a 


```
cdef int call_c(void* args, void* ret) except -1
```


method should be attached to the generic interpreter wrapper class (to be overridden by the subclasses), and those with specific knowledge about the various implementations could then use this interface (e.g. RDF passes double*). 

Issue created by migration from https://trac.sagemath.org/ticket/5616





---

archive/issue_comments_043853.json:
```json
{
    "body": "Attachment [trac5616-fast-callable-gen-pxd.patch](tarball://root/attachments/some-uuid/ticket5616/trac5616-fast-callable-gen-pxd.patch) by cwitty created at 2009-03-28 20:27:47",
    "created_at": "2009-03-28T20:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43853",
    "user": "cwitty"
}
```

Attachment [trac5616-fast-callable-gen-pxd.patch](tarball://root/attachments/some-uuid/ticket5616/trac5616-fast-callable-gen-pxd.patch) by cwitty created at 2009-03-28 20:27:47



---

archive/issue_comments_043854.json:
```json
{
    "body": "Attachment [trac5616-fast-callable-cdef-interface.patch](tarball://root/attachments/some-uuid/ticket5616/trac5616-fast-callable-cdef-interface.patch) by cwitty created at 2009-03-28 20:28:15",
    "created_at": "2009-03-28T20:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43854",
    "user": "cwitty"
}
```

Attachment [trac5616-fast-callable-cdef-interface.patch](tarball://root/attachments/some-uuid/ticket5616/trac5616-fast-callable-cdef-interface.patch) by cwitty created at 2009-03-28 20:28:15



---

archive/issue_comments_043855.json:
```json
{
    "body": "The attached patches should fix this problem.  (Apply both patches, in order.)\n\nI split the fix into two logically separate pieces.  The first only generates .pxd files for the fast_callable interpreters; this should have no observable effect.  The second adds a .call_c() cdef method to the interpreters.  (Each interpreter has its own call_c, rather than inheriting a common method as Robert suggested; I did it this way because I like typechecking.)\n\nThe second patch also modifies parametric_surface.pyx to take advantage of the call_c() method when generating the surface.  I left the old code in as well; this means you can benchmark fast_eval vs. fast_callable by setting sage.ext.fast_eval.new_fast_float to False/True.\n\nThese patches depend on #5622.",
    "created_at": "2009-03-28T20:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43855",
    "user": "cwitty"
}
```

The attached patches should fix this problem.  (Apply both patches, in order.)

I split the fix into two logically separate pieces.  The first only generates .pxd files for the fast_callable interpreters; this should have no observable effect.  The second adds a .call_c() cdef method to the interpreters.  (Each interpreter has its own call_c, rather than inheriting a common method as Robert suggested; I did it this way because I like typechecking.)

The second patch also modifies parametric_surface.pyx to take advantage of the call_c() method when generating the surface.  I left the old code in as well; this means you can benchmark fast_eval vs. fast_callable by setting sage.ext.fast_eval.new_fast_float to False/True.

These patches depend on #5622.



---

archive/issue_comments_043856.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-28T20:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43856",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043857.json:
```json
{
    "body": "Excellent. Yes, generating specific pxd files with typed call_c methods is a better way to go. Code is good and this completely resolves the issue.",
    "created_at": "2009-03-29T10:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43857",
    "user": "@robertwb"
}
```

Excellent. Yes, generating specific pxd files with typed call_c methods is a better way to go. Code is good and this completely resolves the issue.



---

archive/issue_comments_043858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T06:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43858",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043859.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T06:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5616#issuecomment-43859",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael
