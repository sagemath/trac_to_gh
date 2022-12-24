# Issue 9454: Add support for account tokens

archive/issues_009454.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  chapoton\n\nThe attached patch adds support for a new token-based challenge mechanism for account creation in the sage notebook.\n\nWorkflow:\n\nThe admin enables challenges, and sets challenge_type to token.\n\nThe admin generates 50 tokens (through the user management interface) and distributes these to 50 people. (Students taking some class, for example.)\n\nEach person that receives a token can use that token (once) to create an account.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9454\n\n",
    "created_at": "2010-07-08T14:57:46Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "Add support for account tokens",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9454",
    "user": "wjp"
}
```
Assignee: jason, was

CC:  chapoton

The attached patch adds support for a new token-based challenge mechanism for account creation in the sage notebook.

Workflow:

The admin enables challenges, and sets challenge_type to token.

The admin generates 50 tokens (through the user management interface) and distributes these to 50 people. (Students taking some class, for example.)

Each person that receives a token can use that token (once) to create an account.


Issue created by migration from https://trac.sagemath.org/ticket/9454





---

archive/issue_comments_090591.json:
```json
{
    "body": "Attachment [sagenb_account_tokens.patch](tarball://root/attachments/some-uuid/ticket9454/sagenb_account_tokens.patch) by wjp created at 2010-07-08 14:58:26",
    "created_at": "2010-07-08T14:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90591",
    "user": "wjp"
}
```

Attachment [sagenb_account_tokens.patch](tarball://root/attachments/some-uuid/ticket9454/sagenb_account_tokens.patch) by wjp created at 2010-07-08 14:58:26



---

archive/issue_comments_090592.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-08T14:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90592",
    "user": "wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090593.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90593",
    "user": "jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_090594.json:
```json
{
    "body": "This looks really cool, and some stuff could still be used directly [upstream](https://github.com/sagemath/sagenb/blob/master/sagenb/notebook/challenge.py), but it does need some rebasing or an upstream request or something.",
    "created_at": "2013-06-18T20:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90594",
    "user": "kcrisman"
}
```

This looks really cool, and some stuff could still be used directly [upstream](https://github.com/sagemath/sagenb/blob/master/sagenb/notebook/challenge.py), but it does need some rebasing or an upstream request or something.



---

archive/issue_comments_090595.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-18T20:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90595",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090596.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90596",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090597.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90597",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_090598.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-09T09:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9454#issuecomment-90598",
    "user": "chapoton"
}
```

Resolution: invalid
