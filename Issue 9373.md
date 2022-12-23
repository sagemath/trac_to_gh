# Issue 9373: some overhaul in organization of database of common graph generators

archive/issues_009373.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThe database of common graph generators maintains two separate lists of such generators. This entails a lot of work when updating that database as one would need to update two separate lists. Not only that, but having two lists that contain essentially the same information is information duplication. One could update a list and then forgot to update the other list. Better to have one list with links to corresponding generators.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9373\n\n",
    "created_at": "2010-06-29T15:48:05Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "some overhaul in organization of database of common graph generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9373",
    "user": "mvngu"
}
```
Assignee: jason, ncohen, rlm

The database of common graph generators maintains two separate lists of such generators. This entails a lot of work when updating that database as one would need to update two separate lists. Not only that, but having two lists that contain essentially the same information is information duplication. One could update a list and then forgot to update the other list. Better to have one list with links to corresponding generators.

Issue created by migration from https://trac.sagemath.org/ticket/9373





---

archive/issue_comments_089072.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T17:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89072",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089073.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-29T17:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89073",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_089074.json:
```json
{
    "body": "Hello Minh !! I applied this patch on 4.5.rc1, which has a lot of new Graph methods, and found this patch needed to be rebased. I just finished, and your patch is fine for me, thank you for your work ! Here is the rebased version.. Could you give it a final check before setting this to \"positive review\" ? :-)\n\nNathann",
    "created_at": "2010-07-16T02:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89074",
    "user": "ncohen"
}
```

Hello Minh !! I applied this patch on 4.5.rc1, which has a lot of new Graph methods, and found this patch needed to be rebased. I just finished, and your patch is fine for me, thank you for your work ! Here is the rebased version.. Could you give it a final check before setting this to "positive review" ? :-)

Nathann



---

archive/issue_comments_089075.json:
```json
{
    "body": "With a rebased patch, some people consider it rather rude to have the rebase author's name in the username field, instead of the original author's name. Your rebased patch clearly has your username. It's like a reviewer replacing the original author's name with their own name, thus claiming credit for authoring the original patch. Perhaps you overlooked this?",
    "created_at": "2010-07-16T03:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89075",
    "user": "mvngu"
}
```

With a rebased patch, some people consider it rather rude to have the rebase author's name in the username field, instead of the original author's name. Your rebased patch clearly has your username. It's like a reviewer replacing the original author's name with their own name, thus claiming credit for authoring the original patch. Perhaps you overlooked this?



---

archive/issue_comments_089076.json:
```json
{
    "body": "?.....\n\nI'm terribly sorry....\n\nHow can I change this field ? Manually ? :-/\n\nNathann",
    "created_at": "2010-07-16T03:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89076",
    "user": "ncohen"
}
```

?.....

I'm terribly sorry....

How can I change this field ? Manually ? :-/

Nathann



---

archive/issue_comments_089077.json:
```json
{
    "body": "Attachment\n\nOk, I just edited the corresponding line and replaced it with what was written in your patch.\n\nI really hadn't thought of it... I'm very very sorry for that :-/\n\nNathann",
    "created_at": "2010-07-16T03:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89077",
    "user": "ncohen"
}
```

Attachment

Ok, I just edited the corresponding line and replaced it with what was written in your patch.

I really hadn't thought of it... I'm very very sorry for that :-/

Nathann



---

archive/issue_comments_089078.json:
```json
{
    "body": "Thanks, Nathann. Positive review to your rebased patch.",
    "created_at": "2010-07-16T05:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89078",
    "user": "mvngu"
}
```

Thanks, Nathann. Positive review to your rebased patch.



---

archive/issue_comments_089079.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T05:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89079",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9373#issuecomment-89080",
    "user": "mpatel"
}
```

Resolution: fixed
