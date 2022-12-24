# Issue 2283: the coercion code (in __mul__) should call __rmul__ when left or right is not coercible to a Sage element

archive/issues_002283.json:
```json
{
    "body": "Assignee: robertwb\n\nIn this example the last print statement goes boom, but should work fine.\n\n\n```\nclass Foo:\n   def __rmul__(self, left):\n      return 'hello'\n\nH = Foo()\nprint int(3)*H\nprint 3*H\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2283\n\n",
    "created_at": "2008-02-23T22:32:25Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "the coercion code (in __mul__) should call __rmul__ when left or right is not coercible to a Sage element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2283",
    "user": "was"
}
```
Assignee: robertwb

In this example the last print statement goes boom, but should work fine.


```
class Foo:
   def __rmul__(self, left):
      return 'hello'

H = Foo()
print int(3)*H
print 3*H
```




Issue created by migration from https://trac.sagemath.org/ticket/2283





---

archive/issue_comments_015145.json:
```json
{
    "body": "Attachment [coercion-rmul.patch](tarball://root/attachments/some-uuid/ticket2283/coercion-rmul.patch) by jason created at 2008-02-27 20:56:09",
    "created_at": "2008-02-27T20:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15145",
    "user": "jason"
}
```

Attachment [coercion-rmul.patch](tarball://root/attachments/some-uuid/ticket2283/coercion-rmul.patch) by jason created at 2008-02-27 20:56:09



---

archive/issue_comments_015146.json:
```json
{
    "body": "Currently, (before this patch), if a class did\n\n\n```\n_r_action = __rmul__\n```\n\n\nthings would work since the coercion model looks for an _r_action function as a last resort.  This patch just makes this line unnecessary by having the coercion system also look for an __rmul__ function (which is standard python; see http://docs.python.org/ref/numeric-types.html)\n\nApparently this patch is controversial to at least one person, so it probably ought to be discussed.",
    "created_at": "2008-02-27T21:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15146",
    "user": "jason"
}
```

Currently, (before this patch), if a class did


```
_r_action = __rmul__
```


things would work since the coercion model looks for an _r_action function as a last resort.  This patch just makes this line unnecessary by having the coercion system also look for an __rmul__ function (which is standard python; see http://docs.python.org/ref/numeric-types.html)

Apparently this patch is controversial to at least one person, so it probably ought to be discussed.



---

archive/issue_comments_015147.json:
```json
{
    "body": "disclaimer: I don't know much at all about the coercion system; the above statements are from observations made in running examples.",
    "created_at": "2008-02-27T21:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15147",
    "user": "jason"
}
```

disclaimer: I don't know much at all about the coercion system; the above statements are from observations made in running examples.



---

archive/issue_comments_015148.json:
```json
{
    "body": "Attachment [coercion-rmul2.patch](tarball://root/attachments/some-uuid/ticket2283/coercion-rmul2.patch) by jason created at 2008-02-28 04:47:54\n\ncredit goes to gfurnish for noticing and helping track down the segfault that the original patch introduced!\n\nApply coercion-rmul2.patch instead of coercion-rmul.patch",
    "created_at": "2008-02-28T04:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15148",
    "user": "jason"
}
```

Attachment [coercion-rmul2.patch](tarball://root/attachments/some-uuid/ticket2283/coercion-rmul2.patch) by jason created at 2008-02-28 04:47:54

credit goes to gfurnish for noticing and helping track down the segfault that the original patch introduced!

Apply coercion-rmul2.patch instead of coercion-rmul.patch



---

archive/issue_comments_015149.json:
```json
{
    "body": "(and gfurnish also knew how to fix the error causing the segfault!)",
    "created_at": "2008-02-28T04:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15149",
    "user": "jason"
}
```

(and gfurnish also knew how to fix the error causing the segfault!)



---

archive/issue_comments_015150.json:
```json
{
    "body": "The patches above apply to 2.10.2.",
    "created_at": "2008-02-28T04:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15150",
    "user": "jason"
}
```

The patches above apply to 2.10.2.



---

archive/issue_comments_015151.json:
```json
{
    "body": "Looks good to me. Thanks guys!",
    "created_at": "2008-02-28T05:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15151",
    "user": "was"
}
```

Looks good to me. Thanks guys!



---

archive/issue_comments_015152.json:
```json
{
    "body": "Merged coercion-rmul2.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15152",
    "user": "mabshoff"
}
```

Merged coercion-rmul2.patch in Sage 2.10.3.rc0



---

archive/issue_comments_015153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2283#issuecomment-15153",
    "user": "mabshoff"
}
```

Resolution: fixed
