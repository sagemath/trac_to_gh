# Issue 7882: Macaulay2 interface breaks on examples

archive/issues_007882.json:
```json
{
    "body": "Assignee: was\n\nPresent version of Macaulay2 interface breaks on\n\n\n```\nmacaulay2(\"help matrix\")\n```\n\n\nalthough\n\n\n```\nmacaulay2.help(\"matrix\")\n```\n\n\ndoes work fine.\n\nThe problem is that pexpect detects input prompts inside of examples. The patch changes the input prompt to get matches only in the beginning of lines.\n\nThe interface still breaks if you try to print input prompts at the beginning of the line, but that is probably a rare situation...\n\nIssue created by migration from https://trac.sagemath.org/ticket/7882\n\n",
    "created_at": "2010-01-09T20:02:02Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Macaulay2 interface breaks on examples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7882",
    "user": "novoselt"
}
```
Assignee: was

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

archive/issue_comments_068509.json:
```json
{
    "body": "Attachment [Macaulay2_prompt_only_in_the_beginning_of_lines.patch](tarball://root/attachments/some-uuid/ticket7882/Macaulay2_prompt_only_in_the_beginning_of_lines.patch) by novoselt created at 2010-01-09 20:02:48",
    "created_at": "2010-01-09T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68509",
    "user": "novoselt"
}
```

Attachment [Macaulay2_prompt_only_in_the_beginning_of_lines.patch](tarball://root/attachments/some-uuid/ticket7882/Macaulay2_prompt_only_in_the_beginning_of_lines.patch) by novoselt created at 2010-01-09 20:02:48



---

archive/issue_comments_068510.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68510",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068511.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-11T20:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68511",
    "user": "novoselt"
}
```

Resolution: duplicate



---

archive/issue_comments_068512.json:
```json
{
    "body": "Ticket #7897 fixes this in a better way.",
    "created_at": "2010-01-11T20:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7882#issuecomment-68512",
    "user": "novoselt"
}
```

Ticket #7897 fixes this in a better way.
