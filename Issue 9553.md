# Issue 9553: Mention 'sage -ba-force' in the 'sage -ba' prompt

archive/issues_009553.json:
```json
{
    "body": "Assignee: @williamstein\n\nRunning `sage -ba` from the shell gives\n\n```\n *** WARNING ***\n You are about to rebuild the entire Sage library.\n This will take a significant amount of time.\n Do you want to proceed? [y/n]\n```\n\nSince this waits forever for user input, it is harder to use in non-interactive scripts.  However, there is `sage -ba-force`, which does not wait.  This ticket just adds a note about `-ba-force` to the prompt above.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9553\n\n",
    "closed_at": "2010-08-31T03:20:35Z",
    "created_at": "2010-07-20T08:44:27Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Mention 'sage -ba-force' in the 'sage -ba' prompt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9553",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

Running `sage -ba` from the shell gives

```
 *** WARNING ***
 You are about to rebuild the entire Sage library.
 This will take a significant amount of time.
 Do you want to proceed? [y/n]
```

Since this waits forever for user input, it is harder to use in non-interactive scripts.  However, there is `sage -ba-force`, which does not wait.  This ticket just adds a note about `-ba-force` to the prompt above.

Issue created by migration from https://trac.sagemath.org/ticket/9553





---

archive/issue_comments_091922.json:
```json
{
    "body": "While looking at this bug, I discovered the -ba-force option, which is exactly what I was looking for.  So I propose a small patch to change the prompt to:\n\n```\n *** WARNING ***\n You are about to rebuild the entire Sage library.\n This will take a significant amount of time.\n (use -ba-force instead of -ba to skip this prompt.)\n Do you want to proceed? [y/n]\n```",
    "created_at": "2010-07-23T11:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91922",
    "user": "https://github.com/jdemeyer"
}
```

While looking at this bug, I discovered the -ba-force option, which is exactly what I was looking for.  So I propose a small patch to change the prompt to:

```
 *** WARNING ***
 You are about to rebuild the entire Sage library.
 This will take a significant amount of time.
 (use -ba-force instead of -ba to skip this prompt.)
 Do you want to proceed? [y/n]
```



---

archive/issue_comments_091923.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T11:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91923",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091924.json:
```json
{
    "body": "Attachment [9553.patch](tarball://root/attachments/some-uuid/ticket9553/9553.patch) by @jdemeyer created at 2010-07-23 11:13:46\n\nApply this to the local/bin branch",
    "created_at": "2010-07-23T11:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91924",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9553.patch](tarball://root/attachments/some-uuid/ticket9553/9553.patch) by @jdemeyer created at 2010-07-23 11:13:46

Apply this to the local/bin branch



---

archive/issue_comments_091925.json:
```json
{
    "body": "Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line\n\n```\necho \" (use -ba-force instead of -ba to skip this prompt.)\" \n```\nshould be\n\n```\necho \" (Use -ba-force instead of -ba to skip this prompt.)\" \n```",
    "created_at": "2010-07-23T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91925",
    "user": "https://github.com/williamstein"
}
```

Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line

```
echo " (use -ba-force instead of -ba to skip this prompt.)" 
```
should be

```
echo " (Use -ba-force instead of -ba to skip this prompt.)" 
```



---

archive/issue_comments_091926.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line\n\n\nAs far as I'm concerned, we could even complete remove the prompt and make -ba act like -ba-force.  I never quite understood the point of that prompt anyway.",
    "created_at": "2010-07-24T00:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91926",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:3 was]:
> Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line


As far as I'm concerned, we could even complete remove the prompt and make -ba act like -ba-force.  I never quite understood the point of that prompt anyway.



---

archive/issue_comments_091927.json:
```json
{
    "body": "Attachment [trac_9553-use_the_baforce_message.patch](tarball://root/attachments/some-uuid/ticket9553/trac_9553-use_the_baforce_message.patch) by @qed777 created at 2010-08-19 21:49:34\n\n\"use\" --> \"Use\".  scripts repository.  Apply only this patch.",
    "created_at": "2010-08-19T21:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91927",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9553-use_the_baforce_message.patch](tarball://root/attachments/some-uuid/ticket9553/trac_9553-use_the_baforce_message.patch) by @qed777 created at 2010-08-19 21:49:34

"use" --> "Use".  scripts repository.  Apply only this patch.



---

archive/issue_comments_091928.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-19T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91928",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023779.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-19T21:52:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9553#event-23779"
}
```



---

archive/issue_comments_091929.json:
```json
{
    "body": "I've attached an updated patch with William's suggested change.\n\n## To the release manager\nApply only [attachment:trac_9553-use_the_baforce_message.patch], to the scripts repository.",
    "created_at": "2010-08-19T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91929",
    "user": "https://github.com/qed777"
}
```

I've attached an updated patch with William's suggested change.

## To the release manager
Apply only [attachment:trac_9553-use_the_baforce_message.patch], to the scripts repository.



---

archive/issue_comments_091930.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-31T03:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91930",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023780.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-31T03:20:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9553#event-23780"
}
```



---

archive/issue_events_023781.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-31T03:32:20Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9553#event-23781"
}
```



---

archive/issue_events_023782.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-31T03:32:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9553#event-23782"
}
```



---

archive/issue_comments_091931.json:
```json
{
    "body": "What a ticket! I'm not sure if two reviewers are enough to merge this... :D\n\nSince despite its severity it now is, perhaps one should change the title and the description to reflect what the patch really does. ;-)",
    "created_at": "2010-08-31T05:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91931",
    "user": "https://github.com/nexttime"
}
```

What a ticket! I'm not sure if two reviewers are enough to merge this... :D

Since despite its severity it now is, perhaps one should change the title and the description to reflect what the patch really does. ;-)



---

archive/issue_comments_091932.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-08-31T07:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-91932",
    "user": "https://github.com/nexttime"
}
```

Thanks!
