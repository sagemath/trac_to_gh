# Issue 9790: Fix documentation for weave in the "numerical_sage" document

archive/issues_009790.json:
```json
{
    "body": "Assignee: mvngu\n\n\n```\nimport weave\nfrom weave import converters\n```\n\n\nshould be\n\n\n```\nfrom scipy.weave import converters\n```\n\n\nSee http://ask.sagemath.org/question/56/error-while-trying-to-import-weave#comment-213\n\nIssue created by migration from https://trac.sagemath.org/ticket/9791\n\n",
    "created_at": "2010-08-24T01:38:43Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Fix documentation for weave in the \"numerical_sage\" document",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9790",
    "user": "mhansen"
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

archive/issue_comments_096121.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-25T15:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96121",
    "user": "maldun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096122.json:
```json
{
    "body": "Standard indentation in Sage is 4 spaces, so I think there is no reason to change that.",
    "created_at": "2011-01-25T17:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96122",
    "user": "jdemeyer"
}
```

Standard indentation in Sage is 4 spaces, so I think there is no reason to change that.



---

archive/issue_comments_096123.json:
```json
{
    "body": "I have a new patch, keeping indentation and adding a `sage:` prompt so at least the `import` statements are tested.",
    "created_at": "2011-01-25T17:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96123",
    "user": "jdemeyer"
}
```

I have a new patch, keeping indentation and adding a `sage:` prompt so at least the `import` statements are tested.



---

archive/issue_comments_096124.json:
```json
{
    "body": "Could you also correct\n\n```\n\t\"\"\"\n\n       code=\"\"\"\n```\n\nIt should probably be something like\n\n```\n       code=\"\"\" \"\"\"\n```\n\n\nThe link to the weave tutorial (at the end) doesn't work. Maybe you can fix this, too.",
    "created_at": "2011-01-25T17:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96124",
    "user": "aapitzsch"
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

archive/issue_comments_096125.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-25T17:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96125",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096126.json:
```json
{
    "body": "Apologies, there is an indentation problem, it's just that you fixed it the wrong way.",
    "created_at": "2011-01-25T17:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96126",
    "user": "jdemeyer"
}
```

Apologies, there is an indentation problem, it's just that you fixed it the wrong way.



---

archive/issue_comments_096127.json:
```json
{
    "body": "This file is a mess, there is more clean-up to do.",
    "created_at": "2011-01-25T17:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96127",
    "user": "jdemeyer"
}
```

This file is a mess, there is more clean-up to do.



---

archive/issue_comments_096128.json:
```json
{
    "body": "Attachment [9791.patch](tarball://root/attachments/some-uuid/ticket9791/9791.patch) by jdemeyer created at 2011-01-25 17:52:04\n\nReplaces previous patch",
    "created_at": "2011-01-25T17:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96128",
    "user": "jdemeyer"
}
```

Attachment [9791.patch](tarball://root/attachments/some-uuid/ticket9791/9791.patch) by jdemeyer created at 2011-01-25 17:52:04

Replaces previous patch



---

archive/issue_comments_096129.json:
```json
{
    "body": "I can't find an updated weave tutorial, so I just removed the link for now.",
    "created_at": "2011-01-25T17:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96129",
    "user": "jdemeyer"
}
```

I can't find an updated weave tutorial, so I just removed the link for now.



---

archive/issue_comments_096130.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-01-25T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96130",
    "user": "maldun"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_096131.json:
```json
{
    "body": "Replying to [comment:6 jdemeyer]:\n> This file is a mess, there is more clean-up to do.\n\nReplying to [comment:5 jdemeyer]:\n> Apologies, there is an indentation problem, it's just that you fixed it the wrong way. \n\nI wanted just to post that ^^\n\nThe thing with the \n\n\n\n```\n\"\"\"\n\ncode=\"\"\"\n```\n\n\nis correct since it belongs to the support_code\n\nI add a new patch with that thing corrected + a new updated link.\nI added some blank lines into the 3rd code snippet for a little optical clan up.\n\n\nAt least all examples should work now.",
    "created_at": "2011-01-25T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96131",
    "user": "maldun"
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

archive/issue_comments_096132.json:
```json
{
    "body": "Corrected version",
    "created_at": "2011-01-25T17:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96132",
    "user": "maldun"
}
```

Corrected version



---

archive/issue_comments_096133.json:
```json
{
    "body": "Attachment [trac_9791_updatet_blitz_docu.2.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.2.patch) by maldun created at 2011-01-25 18:13:05\n\nCorrected a small error\n\nSo I think we need review again ^^",
    "created_at": "2011-01-25T18:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96133",
    "user": "maldun"
}
```

Attachment [trac_9791_updatet_blitz_docu.2.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.2.patch) by maldun created at 2011-01-25 18:13:05

Corrected a small error

So I think we need review again ^^



---

archive/issue_comments_096134.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-25T18:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96134",
    "user": "maldun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_096135.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-26T09:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96135",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096136.json:
```json
{
    "body": "Sorry, I hadn't seen `\"\"\"` after `support_code`.\n\nThanks, everything looks good now.",
    "created_at": "2011-01-26T09:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96136",
    "user": "aapitzsch"
}
```

Sorry, I hadn't seen `"""` after `support_code`.

Thanks, everything looks good now.



---

archive/issue_comments_096137.json:
```json
{
    "body": "Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to \"combine\" both our patches?",
    "created_at": "2011-01-26T22:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96137",
    "user": "jdemeyer"
}
```

Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?



---

archive/issue_comments_096138.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-26T22:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96138",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_096139.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to \"combine\" both our patches?\n\nOk I double checked, and have to admit that I oversaw the optical clean up you did. I think a merge will be the best then =)",
    "created_at": "2011-01-27T00:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96139",
    "user": "maldun"
}
```

Replying to [comment:11 jdemeyer]:
> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?

Ok I double checked, and have to admit that I oversaw the optical clean up you did. I think a merge will be the best then =)



---

archive/issue_comments_096140.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-27T11:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96140",
    "user": "maldun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096141.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to \"combine\" both our patches?\n\nOk found some time to do the merge myself. I simply applied your patch and added my changes + a small change =)",
    "created_at": "2011-01-27T11:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96141",
    "user": "maldun"
}
```

Replying to [comment:11 jdemeyer]:
> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?

Ok found some time to do the merge myself. I simply applied your patch and added my changes + a small change =)



---

archive/issue_comments_096142.json:
```json
{
    "body": "Attachment [trac_9791_updatet_blitz_docu.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.patch) by maldun created at 2011-01-27 11:46:39\n\nLatest version that merges all changes together",
    "created_at": "2011-01-27T11:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96142",
    "user": "maldun"
}
```

Attachment [trac_9791_updatet_blitz_docu.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.patch) by maldun created at 2011-01-27 11:46:39

Latest version that merges all changes together



---

archive/issue_comments_096143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-27T12:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96143",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096144.json:
```json
{
    "body": "Fixed commit message, apply only this",
    "created_at": "2011-01-28T09:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96144",
    "user": "jdemeyer"
}
```

Fixed commit message, apply only this



---

archive/issue_comments_096145.json:
```json
{
    "body": "Attachment [trac_9791_updatet_blitz_docu.3.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.3.patch) by jdemeyer created at 2011-01-28 13:47:51",
    "created_at": "2011-01-28T13:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96145",
    "user": "jdemeyer"
}
```

Attachment [trac_9791_updatet_blitz_docu.3.patch](tarball://root/attachments/some-uuid/ticket9791/trac_9791_updatet_blitz_docu.3.patch) by jdemeyer created at 2011-01-28 13:47:51



---

archive/issue_comments_096146.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-28T13:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9790#issuecomment-96146",
    "user": "jdemeyer"
}
```

Resolution: fixed
