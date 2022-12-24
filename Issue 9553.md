# Issue 9553: sage -ba (build all) waits for input, making it harder to use in scripts

archive/issues_009553.json:
```json
{
    "body": "Assignee: was\n\nWhen doing \"sage -ba\" from the shell, one gets a prompt:\n\n```\n *** WARNING ***\n You are about to rebuild the entire Sage library.\n This will take a significant amount of time.\n Do you want to proceed? [y/n]\n```\n\n\nSince this waits forever for user input, it is harder to use in non-interactive scripts.  I propose to change the prompt and add a timer such that \"sage -ba\" continues anyway when nothing has been typed for 30 seconds or so.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9553\n\n",
    "created_at": "2010-07-20T08:44:27Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "sage -ba (build all) waits for input, making it harder to use in scripts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9553",
    "user": "jdemeyer"
}
```
Assignee: was

When doing "sage -ba" from the shell, one gets a prompt:

```
 *** WARNING ***
 You are about to rebuild the entire Sage library.
 This will take a significant amount of time.
 Do you want to proceed? [y/n]
```


Since this waits forever for user input, it is harder to use in non-interactive scripts.  I propose to change the prompt and add a timer such that "sage -ba" continues anyway when nothing has been typed for 30 seconds or so.

Issue created by migration from https://trac.sagemath.org/ticket/9553





---

archive/issue_comments_092076.json:
```json
{
    "body": "While looking at this bug, I discovered the -ba-force option, which is exactly what I was looking for.  So I propose a small patch to change the prompt to:\n\n```\n *** WARNING ***\n You are about to rebuild the entire Sage library.\n This will take a significant amount of time.\n (use -ba-force instead of -ba to skip this prompt.)\n Do you want to proceed? [y/n]\n```\n",
    "created_at": "2010-07-23T11:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92076",
    "user": "jdemeyer"
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

archive/issue_comments_092077.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T11:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92077",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092078.json:
```json
{
    "body": "Attachment [9553.patch](tarball://root/attachments/some-uuid/ticket9553/9553.patch) by jdemeyer created at 2010-07-23 11:13:46\n\nApply this to the local/bin branch",
    "created_at": "2010-07-23T11:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92078",
    "user": "jdemeyer"
}
```

Attachment [9553.patch](tarball://root/attachments/some-uuid/ticket9553/9553.patch) by jdemeyer created at 2010-07-23 11:13:46

Apply this to the local/bin branch



---

archive/issue_comments_092079.json:
```json
{
    "body": "Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line\n\n```\necho \" (use -ba-force instead of -ba to skip this prompt.)\" \n```\n\nshould be\n\n```\necho \" (Use -ba-force instead of -ba to skip this prompt.)\" \n```\n",
    "created_at": "2010-07-23T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92079",
    "user": "was"
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

archive/issue_comments_092080.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line\n\nAs far as I'm concerned, we could even complete remove the prompt and make -ba act like -ba-force.  I never quite understood the point of that prompt anyway.",
    "created_at": "2010-07-24T00:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92080",
    "user": "jdemeyer"
}
```

Replying to [comment:3 was]:
> Excellent idea -- I hate interactive prompts, especially ones that it isn't obvious how to get around. That said, I think this line

As far as I'm concerned, we could even complete remove the prompt and make -ba act like -ba-force.  I never quite understood the point of that prompt anyway.



---

archive/issue_comments_092081.json:
```json
{
    "body": "Attachment [trac_9553-use_the_baforce_message.patch](tarball://root/attachments/some-uuid/ticket9553/trac_9553-use_the_baforce_message.patch) by mpatel created at 2010-08-19 21:49:34\n\n\"use\" --> \"Use\".  scripts repository.  Apply only this patch.",
    "created_at": "2010-08-19T21:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92081",
    "user": "mpatel"
}
```

Attachment [trac_9553-use_the_baforce_message.patch](tarball://root/attachments/some-uuid/ticket9553/trac_9553-use_the_baforce_message.patch) by mpatel created at 2010-08-19 21:49:34

"use" --> "Use".  scripts repository.  Apply only this patch.



---

archive/issue_comments_092082.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-19T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92082",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092083.json:
```json
{
    "body": "I've attached an updated patch with William's suggested change.\n\n## To the release manager\nApply only [attachment:trac_9553-use_the_baforce_message.patch], to the scripts repository.",
    "created_at": "2010-08-19T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92083",
    "user": "mpatel"
}
```

I've attached an updated patch with William's suggested change.

## To the release manager
Apply only [attachment:trac_9553-use_the_baforce_message.patch], to the scripts repository.



---

archive/issue_comments_092084.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-31T03:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92084",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_092085.json:
```json
{
    "body": "What a ticket! I'm not sure if two reviewers are enough to merge this... :D\n\nSince despite its severity it now is, perhaps one should change the title and the description to reflect what the patch really does. ;-)",
    "created_at": "2010-08-31T05:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92085",
    "user": "leif"
}
```

What a ticket! I'm not sure if two reviewers are enough to merge this... :D

Since despite its severity it now is, perhaps one should change the title and the description to reflect what the patch really does. ;-)



---

archive/issue_comments_092086.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-08-31T07:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9553#issuecomment-92086",
    "user": "leif"
}
```

Thanks!
