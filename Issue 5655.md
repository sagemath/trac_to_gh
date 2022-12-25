# Issue 5655: [with patch, needs review] Improved enumeration of vertices and 0-dimensional faces

archive/issues_005655.json:
```json
{
    "body": "Assignee: mhampton\n\nCurrent behaviour of 0-dimensional faces of LatticePolytope's is a bit confusing:\n\n```\nsage: ReflexivePolytope(2,0).faces(dim=0)\n[[2], [1], [0]]\n```\n\nThis means that the 0-th 0-dimensional face of this polytope is spanned by the 2-nd vertex. (The reason behind this is that poly.x orders faces according to facets containing them.)\n\nThe patch adds a line of code sorting the 0-dimensional faces so that the 0-th 0-dimensional face is spanned by the 0-th vertex.\n\nWhile this is quite trivial, I found the current enumeration very confusing when it is necessary to keep track of face correspondenses for several related polytopes. (In fact, I was unable to keep track of it correctly and instead made this change as an easier solution.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5655\n\n",
    "created_at": "2009-04-01T02:55:09Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Improved enumeration of vertices and 0-dimensional faces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5655",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

Current behaviour of 0-dimensional faces of LatticePolytope's is a bit confusing:

```
sage: ReflexivePolytope(2,0).faces(dim=0)
[[2], [1], [0]]
```

This means that the 0-th 0-dimensional face of this polytope is spanned by the 2-nd vertex. (The reason behind this is that poly.x orders faces according to facets containing them.)

The patch adds a line of code sorting the 0-dimensional faces so that the 0-th 0-dimensional face is spanned by the 0-th vertex.

While this is quite trivial, I found the current enumeration very confusing when it is necessary to keep track of face correspondenses for several related polytopes. (In fact, I was unable to keep track of it correctly and instead made this change as an easier solution.)

Issue created by migration from https://trac.sagemath.org/ticket/5655





---

archive/issue_comments_044139.json:
```json
{
    "body": "Attachment [11805.patch](tarball://root/attachments/some-uuid/ticket5655/11805.patch) by @novoselt created at 2009-04-01 02:55:19",
    "created_at": "2009-04-01T02:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5655#issuecomment-44139",
    "user": "https://github.com/novoselt"
}
```

Attachment [11805.patch](tarball://root/attachments/some-uuid/ticket5655/11805.patch) by @novoselt created at 2009-04-01 02:55:19



---

archive/issue_comments_044140.json:
```json
{
    "body": "There is some danger that this will break old code; otherwise I approve of the changes and I have tested that they seem to work correctly.\n\nI believe that the polytope code, both here and in polyhedra.py, is still in a relatively immature state and that it is better for us to improve it than worry too much about backwards compatibility.  Currently not many people are using it heavily, so I think this sort of change in behavior is OK - only very fragile code would be affected by this.",
    "created_at": "2009-04-13T19:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5655#issuecomment-44140",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

There is some danger that this will break old code; otherwise I approve of the changes and I have tested that they seem to work correctly.

I believe that the polytope code, both here and in polyhedra.py, is still in a relatively immature state and that it is better for us to improve it than worry too much about backwards compatibility.  Currently not many people are using it heavily, so I think this sort of change in behavior is OK - only very fragile code would be affected by this.



---

archive/issue_comments_044141.json:
```json
{
    "body": "Ok, can either one of you add a not to what changed at\n\n  http://wiki.sagemath.org/sage-3.4.1\n\nso that we can point people to that in case they complain?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T01:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5655#issuecomment-44141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, can either one of you add a not to what changed at

  http://wiki.sagemath.org/sage-3.4.1

so that we can point people to that in case they complain?

Cheers,

Michael



---

archive/issue_comments_044142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T01:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5655#issuecomment-44142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044143.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T01:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5655#issuecomment-44143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
