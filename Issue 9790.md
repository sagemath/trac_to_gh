# Issue 9790: Fix documentation for weave in the "numerical_sage" document

archive/issues_009790.json:
```json
{
    "body": "Assignee: mvngu\n\n\n```\nimport weave\nfrom weave import converters\n```\n\n\nshould be\n\n\n```\nfrom scipy.weave import converters\n```\n\n\nSee http://ask.sagemath.org/question/56/error-while-trying-to-import-weave#comment-213\n\nIssue created by migration from https://trac.sagemath.org/ticket/9791\n\n",
    "created_at": "2010-08-24T01:38:43Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Fix documentation for weave in the \"numerical_sage\" document",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9790",
    "user": "https://github.com/mwhansen"
}
```
Assignee: mvngu


```
import weave
from weave import converters
```


should be


```
from scipy.weave import converters
```


See http://ask.sagemath.org/question/56/error-while-trying-to-import-weave#comment-213

Issue created by migration from https://trac.sagemath.org/ticket/9791





---

archive/issue_comments_095962.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-25T15:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95962",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Changing status from new to needs_review.



---

archive/issue_events_024557.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-25T17:04:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9790#event-24557"
}
```



---

archive/issue_comments_095963.json:
```json
{
    "body": "Standard indentation in Sage is 4 spaces, so I think there is no reason to change that.",
    "created_at": "2011-01-25T17:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95963",
    "user": "https://github.com/jdemeyer"
}
```

Standard indentation in Sage is 4 spaces, so I think there is no reason to change that.



---

archive/issue_comments_095964.json:
```json
{
    "body": "I have a new patch, keeping indentation and adding a `sage:` prompt so at least the `import` statements are tested.",
    "created_at": "2011-01-25T17:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95964",
    "user": "https://github.com/jdemeyer"
}
```

I have a new patch, keeping indentation and adding a `sage:` prompt so at least the `import` statements are tested.



---

archive/issue_comments_095965.json:
```json
{
    "body": "Could you also correct\n\n```\n\t\"\"\"\n\n       code=\"\"\"\n```\n\nIt should probably be something like\n\n```\n       code=\"\"\" \"\"\"\n```\n\n\nThe link to the weave tutorial (at the end) doesn't work. Maybe you can fix this, too.",
    "created_at": "2011-01-25T17:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95965",
    "user": "https://github.com/a-andre"
}
```

Could you also correct

```
	"""

       code="""
```

It should probably be something like

```
       code=""" """
```


The link to the weave tutorial (at the end) doesn't work. Maybe you can fix this, too.



---

archive/issue_comments_095966.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-25T17:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95966",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095967.json:
```json
{
    "body": "Apologies, there is an indentation problem, it's just that you fixed it the wrong way.",
    "created_at": "2011-01-25T17:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95967",
    "user": "https://github.com/jdemeyer"
}
```

Apologies, there is an indentation problem, it's just that you fixed it the wrong way.



---

archive/issue_comments_095968.json:
```json
{
    "body": "This file is a mess, there is more clean-up to do.",
    "created_at": "2011-01-25T17:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95968",
    "user": "https://github.com/jdemeyer"
}
```

This file is a mess, there is more clean-up to do.



---

archive/issue_comments_095969.json:
```json
{
    "body": "Attachment [9791.patch](tarball://root/attachments/some-uuid/ticket9791/9791.patch) by @jdemeyer created at 2011-01-25 17:52:04\n\nReplaces previous patch",
    "created_at": "2011-01-25T17:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95969",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9791.patch](tarball://root/attachments/some-uuid/ticket9791/9791.patch) by @jdemeyer created at 2011-01-25 17:52:04

Replaces previous patch



---

archive/issue_comments_095970.json:
```json
{
    "body": "I can't find an updated weave tutorial, so I just removed the link for now.",
    "created_at": "2011-01-25T17:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95970",
    "user": "https://github.com/jdemeyer"
}
```

I can't find an updated weave tutorial, so I just removed the link for now.



---

archive/issue_comments_095971.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-01-25T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95971",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_095972.json:
```json
{
    "body": "Replying to [comment:6 jdemeyer]:\n> This file is a mess, there is more clean-up to do.\n\nReplying to [comment:5 jdemeyer]:\n> Apologies, there is an indentation problem, it's just that you fixed it the wrong way. \n\nI wanted just to post that ^^\n\nThe thing with the \n\n\n\n```\n\"\"\"\n\ncode=\"\"\"\n```\n\n\nis correct since it belongs to the support_code\n\nI add a new patch with that thing corrected + a new updated link.\nI added some blank lines into the 3rd code snippet for a little optical clan up.\n\n\nAt least all examples should work now.",
    "created_at": "2011-01-25T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95972",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Replying to [comment:6 jdemeyer]:
> This file is a mess, there is more clean-up to do.

Replying to [comment:5 jdemeyer]:
> Apologies, there is an indentation problem, it's just that you fixed it the wrong way. 

I wanted just to post that ^^

The thing with the 



```
"""

code="""
```


is correct since it belongs to the support_code

I add a new patch with that thing corrected + a new updated link.
I added some blank lines into the 3rd code snippet for a little optical clan up.


At least all examples should work now.



---

archive/issue_comments_095973.json:
```json
{
    "body": "Corrected version",
    "created_at": "2011-01-25T17:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95973",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Corrected version



---

archive/issue_comments_095974.json:
```json
{
    "body": "Attachment [trac_9791_updatet_blitz_docu.2.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.2.patch) by maldun created at 2011-01-25 18:13:05\n\nCorrected a small error\n\nSo I think we need review again ^^",
    "created_at": "2011-01-25T18:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95974",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Attachment [trac_9791_updatet_blitz_docu.2.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.2.patch) by maldun created at 2011-01-25 18:13:05

Corrected a small error

So I think we need review again ^^



---

archive/issue_comments_095975.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-25T18:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95975",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_095976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-26T09:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95976",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095977.json:
```json
{
    "body": "Sorry, I hadn't seen `\"\"\"` after `support_code`.\n\nThanks, everything looks good now.",
    "created_at": "2011-01-26T09:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95977",
    "user": "https://github.com/a-andre"
}
```

Sorry, I hadn't seen `"""` after `support_code`.

Thanks, everything looks good now.



---

archive/issue_comments_095978.json:
```json
{
    "body": "Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to \"combine\" both our patches?",
    "created_at": "2011-01-26T22:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95978",
    "user": "https://github.com/jdemeyer"
}
```

Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?



---

archive/issue_comments_095979.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-26T22:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95979",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095980.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to \"combine\" both our patches?\n\nOk I double checked, and have to admit that I oversaw the optical clean up you did. I think a merge will be the best then =)",
    "created_at": "2011-01-27T00:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95980",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Replying to [comment:11 jdemeyer]:
> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?

Ok I double checked, and have to admit that I oversaw the optical clean up you did. I think a merge will be the best then =)



---

archive/issue_comments_095981.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-27T11:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95981",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095982.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to \"combine\" both our patches?\n\nOk found some time to do the merge myself. I simply applied your patch and added my changes + a small change =)",
    "created_at": "2011-01-27T11:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95982",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Replying to [comment:11 jdemeyer]:
> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?

Ok found some time to do the merge myself. I simply applied your patch and added my changes + a small change =)



---

archive/issue_comments_095983.json:
```json
{
    "body": "Attachment [trac_9791_updatet_blitz_docu.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.patch) by maldun created at 2011-01-27 11:46:39\n\nLatest version that merges all changes together",
    "created_at": "2011-01-27T11:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95983",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Attachment [trac_9791_updatet_blitz_docu.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.patch) by maldun created at 2011-01-27 11:46:39

Latest version that merges all changes together



---

archive/issue_comments_095984.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-27T12:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95984",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095985.json:
```json
{
    "body": "Fixed commit message, apply only this",
    "created_at": "2011-01-28T09:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95985",
    "user": "https://github.com/jdemeyer"
}
```

Fixed commit message, apply only this



---

archive/issue_comments_095986.json:
```json
{
    "body": "Attachment [trac_9791_updatet_blitz_docu.3.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.3.patch) by @jdemeyer created at 2011-01-28 13:47:51",
    "created_at": "2011-01-28T13:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95986",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_9791_updatet_blitz_docu.3.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.3.patch) by @jdemeyer created at 2011-01-28 13:47:51



---

archive/issue_comments_095987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-28T13:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-95987",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_024558.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-28T13:47:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9790#event-24558"
}
```
