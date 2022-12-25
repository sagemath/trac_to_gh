# Issue 9373: some overhaul in organization of database of common graph generators

archive/issues_009373.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThe database of common graph generators maintains two separate lists of such generators. This entails a lot of work when updating that database as one would need to update two separate lists. Not only that, but having two lists that contain essentially the same information is information duplication. One could update a list and then forgot to update the other list. Better to have one list with links to corresponding generators.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9373\n\n",
    "created_at": "2010-06-29T15:48:05Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "some overhaul in organization of database of common graph generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9373",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: jason, ncohen, rlm

The database of common graph generators maintains two separate lists of such generators. This entails a lot of work when updating that database as one would need to update two separate lists. Not only that, but having two lists that contain essentially the same information is information duplication. One could update a list and then forgot to update the other list. Better to have one list with links to corresponding generators.

Issue created by migration from https://trac.sagemath.org/ticket/9373





---

archive/issue_comments_088932.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T17:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088933.json:
```json
{
    "body": "Attachment [trac_9373-graphdb.patch](tarball://root/attachments/some-uuid/ticket9373/trac_9373-graphdb.patch) by mvngu created at 2010-06-29 17:18:46",
    "created_at": "2010-06-29T17:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88933",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_9373-graphdb.patch](tarball://root/attachments/some-uuid/ticket9373/trac_9373-graphdb.patch) by mvngu created at 2010-06-29 17:18:46



---

archive/issue_comments_088934.json:
```json
{
    "body": "Hello Minh !! I applied this patch on 4.5.rc1, which has a lot of new Graph methods, and found this patch needed to be rebased. I just finished, and your patch is fine for me, thank you for your work ! Here is the rebased version.. Could you give it a final check before setting this to \"positive review\" ? :-)\n\nNathann",
    "created_at": "2010-07-16T02:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88934",
    "user": "https://github.com/nathanncohen"
}
```

Hello Minh !! I applied this patch on 4.5.rc1, which has a lot of new Graph methods, and found this patch needed to be rebased. I just finished, and your patch is fine for me, thank you for your work ! Here is the rebased version.. Could you give it a final check before setting this to "positive review" ? :-)

Nathann



---

archive/issue_comments_088935.json:
```json
{
    "body": "With a rebased patch, some people consider it rather rude to have the rebase author's name in the username field, instead of the original author's name. Your rebased patch clearly has your username. It's like a reviewer replacing the original author's name with their own name, thus claiming credit for authoring the original patch. Perhaps you overlooked this?",
    "created_at": "2010-07-16T03:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With a rebased patch, some people consider it rather rude to have the rebase author's name in the username field, instead of the original author's name. Your rebased patch clearly has your username. It's like a reviewer replacing the original author's name with their own name, thus claiming credit for authoring the original patch. Perhaps you overlooked this?



---

archive/issue_comments_088936.json:
```json
{
    "body": "?.....\n\nI'm terribly sorry....\n\nHow can I change this field ? Manually ? :-/\n\nNathann",
    "created_at": "2010-07-16T03:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88936",
    "user": "https://github.com/nathanncohen"
}
```

?.....

I'm terribly sorry....

How can I change this field ? Manually ? :-/

Nathann



---

archive/issue_comments_088937.json:
```json
{
    "body": "Attachment [trac_9373.patch](tarball://root/attachments/some-uuid/ticket9373/trac_9373.patch) by @nathanncohen created at 2010-07-16 03:15:20\n\nOk, I just edited the corresponding line and replaced it with what was written in your patch.\n\nI really hadn't thought of it... I'm very very sorry for that :-/\n\nNathann",
    "created_at": "2010-07-16T03:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88937",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9373.patch](tarball://root/attachments/some-uuid/ticket9373/trac_9373.patch) by @nathanncohen created at 2010-07-16 03:15:20

Ok, I just edited the corresponding line and replaced it with what was written in your patch.

I really hadn't thought of it... I'm very very sorry for that :-/

Nathann



---

archive/issue_comments_088938.json:
```json
{
    "body": "Thanks, Nathann. Positive review to your rebased patch.",
    "created_at": "2010-07-16T05:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88938",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Thanks, Nathann. Positive review to your rebased patch.



---

archive/issue_comments_088939.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T05:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88939",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-88940",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
