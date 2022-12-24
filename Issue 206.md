# Issue 206: Graphic.append() does not update xmin, xmax etc.

archive/issues_000206.json:
```json
{
    "body": "Assignee: was\n\nIf I add a bunch of graphics primitives to a Graphic object using the Graphic append() method, the `__xmax`, `__xmin`, `__ymax`, `__ymin` attributes are not updated. Therefore when I try to plot the graphic, nothing shows up. Code for the correct behaviour can be found in the `Graphic.__add__()` method.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/206\n\n",
    "created_at": "2007-01-23T04:46:27Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "Graphic.append() does not update xmin, xmax etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/206",
    "user": "dmharvey"
}
```
Assignee: was

If I add a bunch of graphics primitives to a Graphic object using the Graphic append() method, the `__xmax`, `__xmin`, `__ymax`, `__ymin` attributes are not updated. Therefore when I try to plot the graphic, nothing shows up. Code for the correct behaviour can be found in the `Graphic.__add__()` method.


Issue created by migration from https://trac.sagemath.org/ticket/206





---

archive/issue_comments_000923.json:
```json
{
    "body": "Changing assignee from was to rlm.",
    "created_at": "2007-08-18T16:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-923",
    "user": "rlm"
}
```

Changing assignee from was to rlm.



---

archive/issue_comments_000924.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T20:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-924",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_000925.json:
```json
{
    "body": "http://sage.math.washington.edu/home/rlmill/xmin.patch",
    "created_at": "2007-08-18T20:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-925",
    "user": "rlm"
}
```

http://sage.math.washington.edu/home/rlmill/xmin.patch



---

archive/issue_comments_000926.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-18T21:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-926",
    "user": "rlm"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_000927.json:
```json
{
    "body": "The correct behaviour is not quite that in Graphic.__add__(), since this is adding two Graphics objects. The reason for this bug is that primitives don't usually remember their xmin/max values, and if they do it's inconsistent.",
    "created_at": "2007-08-18T21:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-927",
    "user": "rlm"
}
```

The correct behaviour is not quite that in Graphic.__add__(), since this is adding two Graphics objects. The reason for this bug is that primitives don't usually remember their xmin/max values, and if they do it's inconsistent.



---

archive/issue_comments_000928.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-08-18T21:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-928",
    "user": "rlm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_000929.json:
```json
{
    "body": "After a massive amount of discussion, we decided that there should be no Graphic.append method.  It just doesn't even make sense.   So we removed it and closed this bug.",
    "created_at": "2007-08-19T01:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-929",
    "user": "was"
}
```

After a massive amount of discussion, we decided that there should be no Graphic.append method.  It just doesn't even make sense.   So we removed it and closed this bug.



---

archive/issue_comments_000930.json:
```json
{
    "body": "Changing assignee from rlm to agc.",
    "created_at": "2007-08-19T01:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-930",
    "user": "was"
}
```

Changing assignee from rlm to agc.



---

archive/issue_comments_000931.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2007-08-19T01:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-931",
    "user": "was"
}
```

Changing status from reopened to new.



---

archive/issue_comments_000932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T01:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/206#issuecomment-932",
    "user": "was"
}
```

Resolution: fixed
