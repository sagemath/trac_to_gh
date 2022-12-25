# Issue 9811: Sorting bug in fan subdivision

archive/issues_009811.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @vbraun\n\n\n```\nsage: C = Cone([(1,0,0), (0,1,0), (1,0,1), (0,1,1)])\nsage: F = Fan([C]).make_simplicial()\nsage: [cone.ambient_ray_indices() for cone in F]\n[(1, 3, 0), (1, 2, 0)]\n```\n\nWhile the output is mathematically correct, ambient ray indices are supposed to be sorted and violating this condition can lead to errors later. The attached patch adds extra sorting in the proper place. This means that polytopes constructed during subdivision can no longer be cached because of the potentially wrong vertex order, which is OK.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9812\n\n",
    "created_at": "2010-08-26T22:23:58Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Sorting bug in fan subdivision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9811",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

CC:  @vbraun


```
sage: C = Cone([(1,0,0), (0,1,0), (1,0,1), (0,1,1)])
sage: F = Fan([C]).make_simplicial()
sage: [cone.ambient_ray_indices() for cone in F]
[(1, 3, 0), (1, 2, 0)]
```

While the output is mathematically correct, ambient ray indices are supposed to be sorted and violating this condition can lead to errors later. The attached patch adds extra sorting in the proper place. This means that polytopes constructed during subdivision can no longer be cached because of the potentially wrong vertex order, which is OK.

Issue created by migration from https://trac.sagemath.org/ticket/9812





---

archive/issue_comments_096598.json:
```json
{
    "body": "Attachment [trac_9812_sorting_bug_in_fan_subdivision.patch](tarball://root/attachments/some-uuid/ticket9812/trac_9812_sorting_bug_in_fan_subdivision.patch) by @novoselt created at 2010-08-26 22:27:40",
    "created_at": "2010-08-26T22:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9811#issuecomment-96598",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9812_sorting_bug_in_fan_subdivision.patch](tarball://root/attachments/some-uuid/ticket9812/trac_9812_sorting_bug_in_fan_subdivision.patch) by @novoselt created at 2010-08-26 22:27:40



---

archive/issue_comments_096599.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T22:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9811#issuecomment-96599",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096600.json:
```json
{
    "body": "good catch!",
    "created_at": "2010-08-28T00:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9811#issuecomment-96600",
    "user": "https://github.com/vbraun"
}
```

good catch!



---

archive/issue_comments_096601.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-28T00:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9811#issuecomment-96601",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096602.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9811#issuecomment-96602",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009934.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T09:57:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9811",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9811#event-9934"
}
```
