# Issue 4248: aspect_ratio is buggy in plot3d

archive/issues_004248.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: aspect_ratio, plot3d\n\n`aspect_ratio` doesn't obey its documentation.  If I type\n\n```\nsage: var('x y')\nsage: Q = plot3d(sin(x+y), (-3,3), (-2,2))\nsage: Q.show(aspect_ratio=[1,1,1])\n```\n\nthen I get what I expect: the x-, y-, and z-axes are given the same scale, so ratio of the length of the x-axis to the length of the y-axis is 3:2.  But if I do\n\n```\nsage: Q.show(aspect_ratio=[1,1,2])\n```\n\nthen suddenly the y-axis goes from -4 to 4, and the ratio of the lengths of the x- and y-axes is 3:4 (so the aspect_ratio in the two dimensions x and y is [2,1] instead of [1,1]).\n\nHere is a web page with pictures showing the problem:\n[http://www.math.washington.edu/~palmieri/Sage/ar.html](http://www.math.washington.edu/~palmieri/Sage/ar.html)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4248\n\n",
    "created_at": "2008-10-06T23:01:06Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "aspect_ratio is buggy in plot3d",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4248",
    "user": "jhpalmieri"
}
```
Assignee: somebody

Keywords: aspect_ratio, plot3d

`aspect_ratio` doesn't obey its documentation.  If I type

```
sage: var('x y')
sage: Q = plot3d(sin(x+y), (-3,3), (-2,2))
sage: Q.show(aspect_ratio=[1,1,1])
```

then I get what I expect: the x-, y-, and z-axes are given the same scale, so ratio of the length of the x-axis to the length of the y-axis is 3:2.  But if I do

```
sage: Q.show(aspect_ratio=[1,1,2])
```

then suddenly the y-axis goes from -4 to 4, and the ratio of the lengths of the x- and y-axes is 3:4 (so the aspect_ratio in the two dimensions x and y is [2,1] instead of [1,1]).

Here is a web page with pictures showing the problem:
[http://www.math.washington.edu/~palmieri/Sage/ar.html](http://www.math.washington.edu/~palmieri/Sage/ar.html)


Issue created by migration from https://trac.sagemath.org/ticket/4248





---

archive/issue_comments_030883.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-20T19:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4248#issuecomment-30883",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_030884.json:
```json
{
    "body": "I'm attaching a patch.  Some comments:\n\n1. the only significant change is the removal of the line\n\n```\nif i != longest_side: \n```\n\nand the ensuing change in indentation.\n\n2. the variable `new_box`, defined at the beginning of the old code, wasn't used anywhere, so I deleted it.\n\n3. my other changes are basically cosmetic.",
    "created_at": "2008-10-20T20:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4248#issuecomment-30884",
    "user": "jhpalmieri"
}
```

I'm attaching a patch.  Some comments:

1. the only significant change is the removal of the line

```
if i != longest_side: 
```

and the ensuing change in indentation.

2. the variable `new_box`, defined at the beginning of the old code, wasn't used anywhere, so I deleted it.

3. my other changes are basically cosmetic.



---

archive/issue_comments_030885.json:
```json
{
    "body": "Positive review.  I was surprised by the bad coverage in plot/plot3d/base.pyx, its only 5%, but fixing that is way beyond the scope of this patch.  This seems to fix the noted problem and passes what few tests there are in base.pyx.",
    "created_at": "2008-10-22T19:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4248#issuecomment-30885",
    "user": "mhampton"
}
```

Positive review.  I was surprised by the bad coverage in plot/plot3d/base.pyx, its only 5%, but fixing that is way beyond the scope of this patch.  This seems to fix the noted problem and passes what few tests there are in base.pyx.



---

archive/issue_comments_030886.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-25T21:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4248#issuecomment-30886",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030887.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-25T21:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4248#issuecomment-30887",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1
