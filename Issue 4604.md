# Issue 4604: Graphics() should work in 3d as a valid empty object

archive/issues_004604.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphics, 3d\n\nFrom sage-support (and this has bugged me too):\n\n\nI'm not sure if this is a bug or just something I'm misunderstanding,\nbut for 2D graphics I can write code like this.\n\n```\ng = Graphics()\ng += line( [ [-1,-1], [1,1] ] )\ng.show()\n```\n\nBut in 3D if I do either\n\n```\ng = Graphics()\ng += sphere( (1,1,1), 2 )\ng.show()\n```\n\nor\n\n```\ng = sage.plot.plot3d.base.Graphics3dGroup()\ng += sphere( (1,1,1), 2 )\ng.show()\n```\n\nI get the error: \n\n```\nValueError: min() arg is an empty sequence\n```\n\n\nIs there something I'm missing on how to create a graphics object and\nadd 3D graphics to it like the way it's done in 2D? \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4604\n\n",
    "created_at": "2008-11-24T17:37:26Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Graphics() should work in 3d as a valid empty object",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

Keywords: graphics, 3d

From sage-support (and this has bugged me too):


I'm not sure if this is a bug or just something I'm misunderstanding,
but for 2D graphics I can write code like this.

```
g = Graphics()
g += line( [ [-1,-1], [1,1] ] )
g.show()
```

But in 3D if I do either

```
g = Graphics()
g += sphere( (1,1,1), 2 )
g.show()
```

or

```
g = sage.plot.plot3d.base.Graphics3dGroup()
g += sphere( (1,1,1), 2 )
g.show()
```

I get the error: 

```
ValueError: min() arg is an empty sequence
```


Is there something I'm missing on how to create a graphics object and
add 3D graphics to it like the way it's done in 2D? 



Issue created by migration from https://trac.sagemath.org/ticket/4604





---

archive/issue_comments_034442.json:
```json
{
    "body": "Attachment [trac_4604.patch](tarball://root/attachments/some-uuid/ticket4604/trac_4604.patch) by wcauchois created at 2010-01-16 23:49:52\n\nbased on sage 4.3.1.alpha1",
    "created_at": "2010-01-16T23:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34442",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac_4604.patch](tarball://root/attachments/some-uuid/ticket4604/trac_4604.patch) by wcauchois created at 2010-01-16 23:49:52

based on sage 4.3.1.alpha1



---

archive/issue_comments_034443.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T23:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34443",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034444.json:
```json
{
    "body": "Robert and I confirmed this bug has been fixed in Sage 4.3. The attached patch implements a doctest for Graphics that implements this.",
    "created_at": "2010-01-16T23:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34444",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Robert and I confirmed this bug has been fixed in Sage 4.3. The attached patch implements a doctest for Graphics that implements this.



---

archive/issue_comments_034445.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34445",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034446.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-17T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34446",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_events_010460.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T00:40:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4604#event-10460"
}
```



---

archive/issue_comments_034447.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34447",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
