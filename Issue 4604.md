# Issue 4604: Graphics() should work in 3d as a valid empty object

archive/issues_004604.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graphics, 3d\n\nFrom sage-support (and this has bugged me too):\n\n\nI'm not sure if this is a bug or just something I'm misunderstanding,\nbut for 2D graphics I can write code like this.\n\n```\ng = Graphics()\ng += line( [ [-1,-1], [1,1] ] )\ng.show()\n```\n\nBut in 3D if I do either\n\n```\ng = Graphics()\ng += sphere( (1,1,1), 2 )\ng.show()\n```\n\nor\n\n```\ng = sage.plot.plot3d.base.Graphics3dGroup()\ng += sphere( (1,1,1), 2 )\ng.show()\n```\n\nI get the error: \n\n```\nValueError: min() arg is an empty sequence\n```\n\n\nIs there something I'm missing on how to create a graphics object and\nadd 3D graphics to it like the way it's done in 2D? \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4604\n\n",
    "created_at": "2008-11-24T17:37:26Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Graphics() should work in 3d as a valid empty object",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4604",
    "user": "mhampton"
}
```
Assignee: was

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

archive/issue_comments_034509.json:
```json
{
    "body": "Attachment [trac_4604.patch](tarball://root/attachments/some-uuid/ticket4604/trac_4604.patch) by wcauchois created at 2010-01-16 23:49:52\n\nbased on sage 4.3.1.alpha1",
    "created_at": "2010-01-16T23:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34509",
    "user": "wcauchois"
}
```

Attachment [trac_4604.patch](tarball://root/attachments/some-uuid/ticket4604/trac_4604.patch) by wcauchois created at 2010-01-16 23:49:52

based on sage 4.3.1.alpha1



---

archive/issue_comments_034510.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T23:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34510",
    "user": "wcauchois"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034511.json:
```json
{
    "body": "Robert and I confirmed this bug has been fixed in Sage 4.3. The attached patch implements a doctest for Graphics that implements this.",
    "created_at": "2010-01-16T23:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34511",
    "user": "wcauchois"
}
```

Robert and I confirmed this bug has been fixed in Sage 4.3. The attached patch implements a doctest for Graphics that implements this.



---

archive/issue_comments_034512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34512",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034513.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-17T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34513",
    "user": "timdumol"
}
```

LGTM.



---

archive/issue_comments_034514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4604#issuecomment-34514",
    "user": "rlm"
}
```

Resolution: fixed
