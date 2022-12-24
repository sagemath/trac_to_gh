# Issue 7629: Make it possible to restrict the domains of email addresses

archive/issues_007629.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @dandrake @fchapoton\n\nI'm setting up a campus server, and it would extremely useful if I could require valid email addresses and restrict email addresses to campus addresses.  This would allow anyone with a valid campus email address to create an account.\n\nNote that for this to work, we also need to make it required to confirm email addresses before accounts are activated.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7629\n\n",
    "created_at": "2009-12-08T19:58:17Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make it possible to restrict the domains of email addresses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7629",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  @dandrake @fchapoton

I'm setting up a campus server, and it would extremely useful if I could require valid email addresses and restrict email addresses to campus addresses.  This would allow anyone with a valid campus email address to create an account.

Note that for this to work, we also need to make it required to confirm email addresses before accounts are activated.

Issue created by migration from https://trac.sagemath.org/ticket/7629





---

archive/issue_comments_065179.json:
```json
{
    "body": "See #7630",
    "created_at": "2009-12-08T20:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65179",
    "user": "@jasongrout"
}
```

See #7630



---

archive/issue_comments_065180.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-19T09:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65180",
    "user": "@TimDumol"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_065181.json:
```json
{
    "body": "Validate with extra regexp from notebook settings.  Depends on #8038.  sagenb repo.",
    "created_at": "2010-01-28T06:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65181",
    "user": "@qed777"
}
```

Validate with extra regexp from notebook settings.  Depends on #8038.  sagenb repo.



---

archive/issue_comments_065182.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T06:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65182",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065183.json:
```json
{
    "body": "Attachment [trac_7629-validate_email_custom.patch](tarball://root/attachments/some-uuid/ticket7629/trac_7629-validate_email_custom.patch) by @qed777 created at 2010-01-28 06:28:57\n\nThe patch is from #8038's V3.",
    "created_at": "2010-01-28T06:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65183",
    "user": "@qed777"
}
```

Attachment [trac_7629-validate_email_custom.patch](tarball://root/attachments/some-uuid/ticket7629/trac_7629-validate_email_custom.patch) by @qed777 created at 2010-01-28 06:28:57

The patch is from #8038's V3.



---

archive/issue_comments_065184.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-08T13:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65184",
    "user": "@dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065185.json:
```json
{
    "body": "This needs a bit of work. \n\nFirst, is it possible to doctest this? Ultimately, the function is just doing a regex match, so we should be able to doctest it...but I don't exactly know how.\n\nSecond, I think `re.search` would be better than `re.match`; search finds the regex anywhere in the string, but match by default only looks at the beginning of the string (http://docs.python.org/library/re.html). We can use `re.search` and anyone who needs the regex to match at the beginning of the string can use `^`. I thought the patch was broken until I looked this up in the Python documentation, so others will definitely run into this.\n\nFinally, it would be nice to distinguish between invalid email addresses and disallowed addresses. Invalid is something like \"two..dots`@`foo.com\"; disallowed is something that the server admin doesn't allow. I say this because I'm anticipating emails from people outside of campus saying \"the server says my email isn't valid, but it is, really!\" and then I'd have to explain. Ideally, I'd like something like \"The server administrator has restricted the email addresses that can be used here, and yours is not allowed.\"\n\nWith doctests and `re.search`, I'll give this a positive review.",
    "created_at": "2010-02-08T13:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65185",
    "user": "@dandrake"
}
```

This needs a bit of work. 

First, is it possible to doctest this? Ultimately, the function is just doing a regex match, so we should be able to doctest it...but I don't exactly know how.

Second, I think `re.search` would be better than `re.match`; search finds the regex anywhere in the string, but match by default only looks at the beginning of the string (http://docs.python.org/library/re.html). We can use `re.search` and anyone who needs the regex to match at the beginning of the string can use `^`. I thought the patch was broken until I looked this up in the Python documentation, so others will definitely run into this.

Finally, it would be nice to distinguish between invalid email addresses and disallowed addresses. Invalid is something like "two..dots`@`foo.com"; disallowed is something that the server admin doesn't allow. I say this because I'm anticipating emails from people outside of campus saying "the server says my email isn't valid, but it is, really!" and then I'd have to explain. Ideally, I'd like something like "The server administrator has restricted the email addresses that can be used here, and yours is not allowed."

With doctests and `re.search`, I'll give this a positive review.



---

archive/issue_comments_065186.json:
```json
{
    "body": "https://github.com/sagemath/sagenb/issues/298",
    "created_at": "2014-12-10T20:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65186",
    "user": "@kcrisman"
}
```

https://github.com/sagemath/sagenb/issues/298



---

archive/issue_comments_065187.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65187",
    "user": "@mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_065188.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65188",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065189.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65189",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065190.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-31T08:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7629#issuecomment-65190",
    "user": "@fchapoton"
}
```

Resolution: invalid
