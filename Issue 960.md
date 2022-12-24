# Issue 960: reconsider how floating point values are printed

archive/issues_000960.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n some f-p values are printed like integers, which may confuse the user\n (especially if one copies them with the mouse):\n sage: 2.0^46\n 70368744177664.0\n sage: 2.0^47\n 140737488355328\n I would expect '140737488355328.' or '1.40737488355328e14' in the 2nd case.\n By the way, typing 140737488355328.0 outputs itself, which is inconsistent,\n since 140737488355328.0-2.0^47 gives 0.0000000000000000.\n\n Compare also:\n sage: 2.0^99\n 633825300114115000000000000000\n sage: 2.0^100\n 1.26765060022823e30\n\nMy 2 cents,\nPaul Z.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/960\n\n",
    "created_at": "2007-10-21T12:41:39Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "reconsider how floating point values are printed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/960",
    "user": "was"
}
```
Assignee: somebody


```
 some f-p values are printed like integers, which may confuse the user
 (especially if one copies them with the mouse):
 sage: 2.0^46
 70368744177664.0
 sage: 2.0^47
 140737488355328
 I would expect '140737488355328.' or '1.40737488355328e14' in the 2nd case.
 By the way, typing 140737488355328.0 outputs itself, which is inconsistent,
 since 140737488355328.0-2.0^47 gives 0.0000000000000000.

 Compare also:
 sage: 2.0^99
 633825300114115000000000000000
 sage: 2.0^100
 1.26765060022823e30

My 2 cents,
Paul Z.
```


Issue created by migration from https://trac.sagemath.org/ticket/960





---

archive/issue_comments_005850.json:
```json
{
    "body": "The inconsistency mentioned is because of the automagic behavior of decimal literals, where longer literals get more bits:\n\n```\nsage: (2.0^47).prec()\n53\nsage: (140737488355328.0).prec()\n56\n```\n\n\nMaybe this magic behavior should be removed, or somehow modified to be less confusing?  (Although I have no idea how to make it less confusing.)\n\nSee also #962, for problems with the current implementation of the precision extension.",
    "created_at": "2007-10-21T15:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/960#issuecomment-5850",
    "user": "cwitty"
}
```

The inconsistency mentioned is because of the automagic behavior of decimal literals, where longer literals get more bits:

```
sage: (2.0^47).prec()
53
sage: (140737488355328.0).prec()
56
```


Maybe this magic behavior should be removed, or somehow modified to be less confusing?  (Although I have no idea how to make it less confusing.)

See also #962, for problems with the current implementation of the precision extension.



---

archive/issue_comments_005851.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-10-23T22:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/960#issuecomment-5851",
    "user": "malb"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_005852.json:
```json
{
    "body": "Attachment [mpfr.patch](tarball://root/attachments/some-uuid/ticket960/mpfr.patch) by mhansen created at 2007-10-24 00:31:09\n\nI've attached a patch that makes sure that all real numbers include a \".\" so that they don't get confused with integers.\n\nHere is the behavior after the patch\n\n```\nsage:  2.0^47\n140737488355328.\nsage:  2.0^46\n70368744177664.0\nsage:  2.0^99\n633825300114115000000000000000.\nsage:  2.0^100\n1.26765060022823e30\nsage: 140737488355328.\n140737488355328.\nsage: a = 2.0^47\nsage: a\n140737488355328.\nsage: a.prec()\n53\nsage: b = 140737488355328.\nsage: b.prec()\n53\n```\n",
    "created_at": "2007-10-24T00:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/960#issuecomment-5852",
    "user": "mhansen"
}
```

Attachment [mpfr.patch](tarball://root/attachments/some-uuid/ticket960/mpfr.patch) by mhansen created at 2007-10-24 00:31:09

I've attached a patch that makes sure that all real numbers include a "." so that they don't get confused with integers.

Here is the behavior after the patch

```
sage:  2.0^47
140737488355328.
sage:  2.0^46
70368744177664.0
sage:  2.0^99
633825300114115000000000000000.
sage:  2.0^100
1.26765060022823e30
sage: 140737488355328.
140737488355328.
sage: a = 2.0^47
sage: a
140737488355328.
sage: a.prec()
53
sage: b = 140737488355328.
sage: b.prec()
53
```




---

archive/issue_comments_005853.json:
```json
{
    "body": "Changing assignee from cwitty to mhansen.",
    "created_at": "2007-10-25T06:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/960#issuecomment-5853",
    "user": "cwitty"
}
```

Changing assignee from cwitty to mhansen.



---

archive/issue_comments_005854.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T02:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/960#issuecomment-5854",
    "user": "cwitty"
}
```

Resolution: fixed
