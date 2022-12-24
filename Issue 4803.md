# Issue 4803: improvements to the polyhedra module documentation

archive/issues_004803.json:
```json
{
    "body": "Assignee: sbarthelemy\n\nCC:  mhampton\n\nThe attached patch corrects some imprecisions in the polyhedra module documentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4803\n\n",
    "created_at": "2008-12-15T09:50:23Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "improvements to the polyhedra module documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4803",
    "user": "sbarthelemy"
}
```
Assignee: sbarthelemy

CC:  mhampton

The attached patch corrects some imprecisions in the polyhedra module documentation.

Issue created by migration from https://trac.sagemath.org/ticket/4803





---

archive/issue_comments_036404.json:
```json
{
    "body": "Attachment [11113.patch](tarball://root/attachments/some-uuid/ticket4803/11113.patch) by sbarthelemy created at 2008-12-15 09:57:16",
    "created_at": "2008-12-15T09:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36404",
    "user": "sbarthelemy"
}
```

Attachment [11113.patch](tarball://root/attachments/some-uuid/ticket4803/11113.patch) by sbarthelemy created at 2008-12-15 09:57:16



---

archive/issue_comments_036405.json:
```json
{
    "body": "There are a couple typos in this proposed documentation change:\n\n\"minkowsky sum\" should be \"Minkowski sum\"\n\"positive (aka conic) combination\" should be \"positive (aka convex) combination\"\n\n(unless there is a meaning of conic combination that I don't know).\n\nThe Fukuda reference is good, it would be better to add a \"REFERENCES\" section since eventually such sections might be searched for and organized.\n\nThanks for working on this!\nMarshall Hampton",
    "created_at": "2008-12-15T10:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36405",
    "user": "mhampton"
}
```

There are a couple typos in this proposed documentation change:

"minkowsky sum" should be "Minkowski sum"
"positive (aka conic) combination" should be "positive (aka convex) combination"

(unless there is a meaning of conic combination that I don't know).

The Fukuda reference is good, it would be better to add a "REFERENCES" section since eventually such sections might be searched for and organized.

Thanks for working on this!
Marshall Hampton



---

archive/issue_comments_036406.json:
```json
{
    "body": "Changing component from algebra to geometry.",
    "created_at": "2008-12-15T10:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36406",
    "user": "mhampton"
}
```

Changing component from algebra to geometry.



---

archive/issue_comments_036407.json:
```json
{
    "body": "Here is a new patch, against the previous\n\n> \"minkowsky sum\" should be \"Minkowski sum\"\n\nI fixed that thanks\n\n> \"positive (aka conic) combination\" should be \"positive (aka convex) combination\"\n> (unless there is a meaning of conic combination that I don't know).\n\nsee http://en.wikipedia.org/wiki/Conical_combination\n\nDattorro [1] uses \"conic hull\" instead of \"conical hull\". Fukuda uses noneg(ray1, ray2,...). I don't know which term is better. In the new patch I chose \"conic hull\", change it to what sounds best to you, english speakers.\n\n> The Fukuda reference is good, it would be better to add a \"REFERENCES\" section since eventually such sections might be searched for and organized.\n\nYou're right, fixed in the patch\n\n> Thanks for working on this!\n\nThanks for the feedback!\n\nS\u00e9bastien\n\n[1] http://meboo.convexoptimization.com/BOOK/convexgeometry.pdf",
    "created_at": "2008-12-15T11:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36407",
    "user": "sbarthelemy"
}
```

Here is a new patch, against the previous

> "minkowsky sum" should be "Minkowski sum"

I fixed that thanks

> "positive (aka conic) combination" should be "positive (aka convex) combination"
> (unless there is a meaning of conic combination that I don't know).

see http://en.wikipedia.org/wiki/Conical_combination

Dattorro [1] uses "conic hull" instead of "conical hull". Fukuda uses noneg(ray1, ray2,...). I don't know which term is better. In the new patch I chose "conic hull", change it to what sounds best to you, english speakers.

> The Fukuda reference is good, it would be better to add a "REFERENCES" section since eventually such sections might be searched for and organized.

You're right, fixed in the patch

> Thanks for working on this!

Thanks for the feedback!

Sébastien

[1] http://meboo.convexoptimization.com/BOOK/convexgeometry.pdf



---

archive/issue_comments_036408.json:
```json
{
    "body": "Attachment [11114.patch](tarball://root/attachments/some-uuid/ticket4803/11114.patch) by mabshoff created at 2008-12-15 11:08:01",
    "created_at": "2008-12-15T11:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36408",
    "user": "mabshoff"
}
```

Attachment [11114.patch](tarball://root/attachments/some-uuid/ticket4803/11114.patch) by mabshoff created at 2008-12-15 11:08:01



---

archive/issue_comments_036409.json:
```json
{
    "body": "Great, I think with those changes it should go in.  Its unclear to me what the best term is for the \"conic hull\" but that can be tweaked later.",
    "created_at": "2008-12-16T14:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36409",
    "user": "mhampton"
}
```

Great, I think with those changes it should go in.  Its unclear to me what the best term is for the "conic hull" but that can be tweaked later.



---

archive/issue_comments_036410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-17T14:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36410",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036411.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc1",
    "created_at": "2008-12-17T14:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4803#issuecomment-36411",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc1
