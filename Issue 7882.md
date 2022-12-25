# Issue 7882: Macaulay2 interface breaks on examples

archive/issues_007882.json:
```json
{
    "body": "Assignee: @williamstein\n\nPresent version of Macaulay2 interface breaks on\n\n```\nmacaulay2(\"help matrix\")\n```\n\nalthough\n\n```\nmacaulay2.help(\"matrix\")\n```\n\ndoes work fine.\n\nThe problem is that pexpect detects input prompts inside of examples. The patch changes the input prompt to get matches only in the beginning of lines.\n\nThe interface still breaks if you try to print input prompts at the beginning of the line, but that is probably a rare situation...\n\nIssue created by migration from https://trac.sagemath.org/ticket/7882\n\n",
    "created_at": "2010-01-09T20:02:02Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Macaulay2 interface breaks on examples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7882",
    "user": "https://github.com/novoselt"
}
```
Assignee: @williamstein

Present version of Macaulay2 interface breaks on

```
macaulay2("help matrix")
```

although

```
macaulay2.help("matrix")
```

does work fine.

The problem is that pexpect detects input prompts inside of examples. The patch changes the input prompt to get matches only in the beginning of lines.

The interface still breaks if you try to print input prompts at the beginning of the line, but that is probably a rare situation...

Issue created by migration from https://trac.sagemath.org/ticket/7882





---

archive/issue_comments_068391.json:
```json
{
    "body": "Attachment [Macaulay2_prompt_only_in_the_beginning_of_lines.patch](tarball://root/attachments/some-uuid/ticket7882/Macaulay2_prompt_only_in_the_beginning_of_lines.patch) by @novoselt created at 2010-01-09 20:02:48",
    "created_at": "2010-01-09T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68391",
    "user": "https://github.com/novoselt"
}
```

Attachment [Macaulay2_prompt_only_in_the_beginning_of_lines.patch](tarball://root/attachments/some-uuid/ticket7882/Macaulay2_prompt_only_in_the_beginning_of_lines.patch) by @novoselt created at 2010-01-09 20:02:48



---

archive/issue_comments_068392.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68392",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068393.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-11T20:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68393",
    "user": "https://github.com/novoselt"
}
```

Resolution: duplicate



---

archive/issue_events_018845.json:
```json
{
    "actor": "https://github.com/novoselt",
    "created_at": "2010-01-11T20:58:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7882#event-18845"
}
```



---

archive/issue_comments_068394.json:
```json
{
    "body": "Ticket #7897 fixes this in a better way.",
    "created_at": "2010-01-11T20:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68394",
    "user": "https://github.com/novoselt"
}
```

Ticket #7897 fixes this in a better way.



---

archive/issue_events_018846.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-12T01:52:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7882#event-18846"
}
```
