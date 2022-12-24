# Issue 3838: Element access for RElement

archive/issues_003838.json:
```json
{
    "body": "Assignee: SimonKing\n\nCC:  alexghitza\n\nKeywords: r interface, element access\n\nOn [http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en](http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en), Alexandr Batalshikov pointed out that\n\n```\n> v = c(3,5,9,1)\n> v[c(2,3)]\n[1] 5 9 \n```\n\nworks in R, but the corresponding statement in Sage does not:\n\n```\nsage: v = r.c(3,5,9,1)\nsage: n = r.c(2,3)\nsage: v[n]\n[1] 3\n```\n\n\nI believe this is a defect. With the attached patch, the following works:\n\n```\nsage: v = r.c(3,5,9,1)\nsage: n = r.c(2,3)\nsage: v[n]\n[1] 5 9\nsage: v[-2]\n[1] 3 9 1\nsage: v['c(2,3)']\n[1] 5 9\nsage: v[2,4,3]\n[1] 5 1 9\nsage: v[2]\n[1] 5\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3838\n\n",
    "created_at": "2008-08-13T17:27:21Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Element access for RElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3838",
    "user": "SimonKing"
}
```
Assignee: SimonKing

CC:  alexghitza

Keywords: r interface, element access

On [http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en](http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en), Alexandr Batalshikov pointed out that

```
> v = c(3,5,9,1)
> v[c(2,3)]
[1] 5 9 
```

works in R, but the corresponding statement in Sage does not:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 3
```


I believe this is a defect. With the attached patch, the following works:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 5 9
sage: v[-2]
[1] 3 9 1
sage: v['c(2,3)']
[1] 5 9
sage: v[2,4,3]
[1] 5 1 9
sage: v[2]
[1] 5
```



Issue created by migration from https://trac.sagemath.org/ticket/3838





---

archive/issue_comments_027289.json:
```json
{
    "body": "Patch relative to 3.1.alpha0",
    "created_at": "2008-08-13T17:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27289",
    "user": "SimonKing"
}
```

Patch relative to 3.1.alpha0



---

archive/issue_comments_027290.json:
```json
{
    "body": "Attachment [RElementAccess.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccess.patch) by mabshoff created at 2008-08-13 17:29:16",
    "created_at": "2008-08-13T17:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27290",
    "user": "mabshoff"
}
```

Attachment [RElementAccess.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccess.patch) by mabshoff created at 2008-08-13 17:29:16



---

archive/issue_comments_027291.json:
```json
{
    "body": "Attachment [RElementAccess2.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccess2.patch) by SimonKing created at 2008-08-13 20:00:50\n\nCorrection for the first patch",
    "created_at": "2008-08-13T20:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27291",
    "user": "SimonKing"
}
```

Attachment [RElementAccess2.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccess2.patch) by SimonKing created at 2008-08-13 20:00:50

Correction for the first patch



---

archive/issue_comments_027292.json:
```json
{
    "body": "I just realized that it is not a good idea to make `v[2,3]` return a vector, because if `v` is an array, `v[2,3]` should return a single entry of the array.\n\nThe new patch (that should be applied after the first one) takes this into account. Now we have:\n\n```\nsage: v = r.c(3,5,9,1)\nsage: n = r.c(2,3)\nsage: v[n]\n[1] 5 9\nsage: v[-n]\n[1] 3 1\n```\n\nas above, and\n\n```\nsage: m = r.array('1:3', r.c(2,4))\nsage: m\n     [,1] [,2] [,3] [,4]\n[1,]    1    3    2    1\n[2,]    2    1    3    2\nsage: m[1,2]\n[1] 3\nsage: m[n]\n[1] 2 3\n```\n\n\nI think this is better than the first approach, but still allows to use an RElement as index.",
    "created_at": "2008-08-13T20:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27292",
    "user": "SimonKing"
}
```

I just realized that it is not a good idea to make `v[2,3]` return a vector, because if `v` is an array, `v[2,3]` should return a single entry of the array.

The new patch (that should be applied after the first one) takes this into account. Now we have:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 5 9
sage: v[-n]
[1] 3 1
```

as above, and

```
sage: m = r.array('1:3', r.c(2,4))
sage: m
     [,1] [,2] [,3] [,4]
[1,]    1    3    2    1
[2,]    2    1    3    2
sage: m[1,2]
[1] 3
sage: m[n]
[1] 2 3
```


I think this is better than the first approach, but still allows to use an RElement as index.



---

archive/issue_comments_027293.json:
```json
{
    "body": "hi, I like the second approach, but just for the sake of completeness and with the future in mind: could you add a doctest for accessing elements of a three dimensional array? I know they can happen and i think it would be good to cover them.",
    "created_at": "2008-08-13T22:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27293",
    "user": "schilly"
}
```

hi, I like the second approach, but just for the sake of completeness and with the future in mind: could you add a doctest for accessing elements of a three dimensional array? I know they can happen and i think it would be good to cover them.



---

archive/issue_comments_027294.json:
```json
{
    "body": "Attachment [RElementAccess3.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccess3.patch) by SimonKing created at 2008-08-14 06:53:45\n\nTo be applied after the two previous patches",
    "created_at": "2008-08-14T06:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27294",
    "user": "SimonKing"
}
```

Attachment [RElementAccess3.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccess3.patch) by SimonKing created at 2008-08-14 06:53:45

To be applied after the two previous patches



---

archive/issue_comments_027295.json:
```json
{
    "body": "Replying to [comment:3 schilly]:\n> hi, I like the second approach, but just for the sake of completeness and with the future in mind: could you add a doctest for accessing elements of a three dimensional array? I know they can happen and i think it would be good to cover them.\n\nNo problem, that works already with the previous version:\n\n```\nsage: m = r.array('1:3', r.c(2,4,2))\nsage: m\n, , 1\n     [,1] [,2] [,3] [,4]\n[1,]    1    3    2    1\n[2,]    2    1    3    2\n\n, , 2\n     [,1] [,2] [,3] [,4]\n[1,]    3    2    1    3\n[2,]    1    3    2    1\n\nsage: m[1,2,2]\n[1] 2\nsage: m[1,3,2]\n[1] 1\n```\n\n\nI changed the doc-tests accordingly (by the third patch).\n\nHowever, i just realize that mixing integer and r.c does not work:\n\n```\nsage: m = r.array('1:3', r.c(2,4,2))\nsage: r(m.name()+'[1,c(1,2),1]')\n[1] 1 3    # the output how it should be\nsage: m[1,r.c(1,2),1]\n[1] 2      # wrong output\n```\n\n\nI'll work on this problem.",
    "created_at": "2008-08-14T07:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27295",
    "user": "SimonKing"
}
```

Replying to [comment:3 schilly]:
> hi, I like the second approach, but just for the sake of completeness and with the future in mind: could you add a doctest for accessing elements of a three dimensional array? I know they can happen and i think it would be good to cover them.

No problem, that works already with the previous version:

```
sage: m = r.array('1:3', r.c(2,4,2))
sage: m
, , 1
     [,1] [,2] [,3] [,4]
[1,]    1    3    2    1
[2,]    2    1    3    2

, , 2
     [,1] [,2] [,3] [,4]
[1,]    3    2    1    3
[2,]    1    3    2    1

sage: m[1,2,2]
[1] 2
sage: m[1,3,2]
[1] 1
```


I changed the doc-tests accordingly (by the third patch).

However, i just realize that mixing integer and r.c does not work:

```
sage: m = r.array('1:3', r.c(2,4,2))
sage: r(m.name()+'[1,c(1,2),1]')
[1] 1 3    # the output how it should be
sage: m[1,r.c(1,2),1]
[1] 2      # wrong output
```


I'll work on this problem.



---

archive/issue_comments_027296.json:
```json
{
    "body": "Attachment [RElementAccessNew.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccessNew.patch) by SimonKing created at 2008-08-14 07:17:12\n\nReplaces all previous patches",
    "created_at": "2008-08-14T07:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27296",
    "user": "SimonKing"
}
```

Attachment [RElementAccessNew.patch](tarball://root/attachments/some-uuid/ticket3838/RElementAccessNew.patch) by SimonKing created at 2008-08-14 07:17:12

Replaces all previous patches



---

archive/issue_comments_027297.json:
```json
{
    "body": "Replying to [comment:4 SimonKing]:\n> I'll work on this problem.\n\nThe most recent patch replaces all previous patches and should apply to 3.1.alpha0. Here is the new feature:\n\n```\nsage: m = r.array('1:3', r.c(2,4,2))\nsage: m\n, , 1\n     [,1] [,2] [,3] [,4]\n[1,]    1    3    2    1\n[2,]    2    1    3    2\n\n, , 2\n     [,1] [,2] [,3] [,4]\n[1,]    3    2    1    3\n[2,]    1    3    2    1\nsage: m[1,r.c(1,2),1]\n[1] 1 3\nsage: m[1,r.c(1,3),r.c(1,2)]\n     [,1] [,2]\n[1,]    1    3\n[2,]    2    1\n```\n\n\nThe doctests provide examples for that type of usage.",
    "created_at": "2008-08-14T07:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27297",
    "user": "SimonKing"
}
```

Replying to [comment:4 SimonKing]:
> I'll work on this problem.

The most recent patch replaces all previous patches and should apply to 3.1.alpha0. Here is the new feature:

```
sage: m = r.array('1:3', r.c(2,4,2))
sage: m
, , 1
     [,1] [,2] [,3] [,4]
[1,]    1    3    2    1
[2,]    2    1    3    2

, , 2
     [,1] [,2] [,3] [,4]
[1,]    3    2    1    3
[2,]    1    3    2    1
sage: m[1,r.c(1,2),1]
[1] 1 3
sage: m[1,r.c(1,3),r.c(1,2)]
     [,1] [,2]
[1,]    1    3
[2,]    2    1
```


The doctests provide examples for that type of usage.



---

archive/issue_comments_027298.json:
```json
{
    "body": "applies to 3.1.3.alpha0",
    "created_at": "2008-09-23T07:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27298",
    "user": "AlexGhitza"
}
```

applies to 3.1.3.alpha0



---

archive/issue_comments_027299.json:
```json
{
    "body": "Merged RElementAccessNew.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T10:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27299",
    "user": "mabshoff"
}
```

Merged RElementAccessNew.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_027300.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T10:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3838#issuecomment-27300",
    "user": "mabshoff"
}
```

Resolution: fixed
