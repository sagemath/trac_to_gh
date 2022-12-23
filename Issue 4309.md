# Issue 4309: Kerberos authentification for SAGE notebook

archive/issues_004309.json:
```json
{
    "body": "Assignee: was\n\nCC:  embray jdemeyer fbissey\n\nThis patch adds Kerberos authentification support for the SAGE notebook. It also adds the options krb_srv, krb_realm for the notebook() command.\n\nThis patch however depends on pykerberos which depends on kerberos which depends on a couple of other libraries all in all a little less size than SAGE itself and all not in SAGE :-). Nevertheless ... \n\nGreetings, \nKilian. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4309\n\n",
    "created_at": "2008-10-16T17:30:31Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "title": "Kerberos authentification for SAGE notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4309",
    "user": "kkilger"
}
```
Assignee: was

CC:  embray jdemeyer fbissey

This patch adds Kerberos authentification support for the SAGE notebook. It also adds the options krb_srv, krb_realm for the notebook() command.

This patch however depends on pykerberos which depends on kerberos which depends on a couple of other libraries all in all a little less size than SAGE itself and all not in SAGE :-). Nevertheless ... 

Greetings, 
Kilian. 

Issue created by migration from https://trac.sagemath.org/ticket/4309





---

archive/issue_comments_031541.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-16T17:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31541",
    "user": "kkilger"
}
```

Attachment



---

archive/issue_comments_031542.json:
```json
{
    "body": "This doesn't apply in sage-3.2.alpha1",
    "created_at": "2008-11-09T21:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31542",
    "user": "TimothyClemans"
}
```

This doesn't apply in sage-3.2.alpha1



---

archive/issue_comments_031543.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-09T23:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31543",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_031544.json:
```json
{
    "body": "Kerberos shouldn't be required to use the notebook. Make Kerberos authentication optional.",
    "created_at": "2008-11-09T23:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31544",
    "user": "TimothyClemans"
}
```

Kerberos shouldn't be required to use the notebook. Make Kerberos authentication optional.



---

archive/issue_comments_031545.json:
```json
{
    "body": "my.patch is replaced by sage-3950_1.patch and applies in sage-3.2.alpha1",
    "created_at": "2008-11-10T00:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31545",
    "user": "TimothyClemans"
}
```

my.patch is replaced by sage-3950_1.patch and applies in sage-3.2.alpha1



---

archive/issue_comments_031546.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-10T02:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31546",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_031547.json:
```json
{
    "body": "OK now Kerberos isn't required.",
    "created_at": "2008-11-10T02:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31547",
    "user": "TimothyClemans"
}
```

OK now Kerberos isn't required.



---

archive/issue_comments_031548.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-10T04:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31548",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_031549.json:
```json
{
    "body": "Changing component from user interface to notebook.",
    "created_at": "2008-11-10T04:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31549",
    "user": "TimothyClemans"
}
```

Changing component from user interface to notebook.



---

archive/issue_comments_031550.json:
```json
{
    "body": "Changing assignee from was to kkilger.",
    "created_at": "2008-11-10T04:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31550",
    "user": "TimothyClemans"
}
```

Changing assignee from was to kkilger.



---

archive/issue_comments_031551.json:
```json
{
    "body": "Hi,\n\nI like the design of this patch and how the kerberos stuff is optional.  \n\nUnfortunately, this is hard to referee if you don't explain to me how to install pykerberos.  Also, the patch itself should contain code that says \"hey, you need kerberos, and here's how to install it\" when the user turns on kerberos via an option to notebook, but \n\n```\nimport kerberos\n```\n\nfails.  That could be either a paragraph of text, an optional spkg to install, or a link to a wiki page that describes what to do.  \n\nOK?\n\nThanks!",
    "created_at": "2008-11-29T03:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31551",
    "user": "was"
}
```

Hi,

I like the design of this patch and how the kerberos stuff is optional.  

Unfortunately, this is hard to referee if you don't explain to me how to install pykerberos.  Also, the patch itself should contain code that says "hey, you need kerberos, and here's how to install it" when the user turns on kerberos via an option to notebook, but 

```
import kerberos
```

fails.  That could be either a paragraph of text, an optional spkg to install, or a link to a wiki page that describes what to do.  

OK?

Thanks!



---

archive/issue_comments_031552.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2019-06-16T18:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31552",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_031553.json:
```json
{
    "body": "notebook is deprecated, so this can probably be closed",
    "created_at": "2019-06-16T18:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31553",
    "user": "chapoton"
}
```

notebook is deprecated, so this can probably be closed



---

archive/issue_comments_031554.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-06-16T18:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31554",
    "user": "fbissey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031555.json:
```json
{
    "body": "Yes.",
    "created_at": "2019-06-16T18:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31555",
    "user": "fbissey"
}
```

Yes.



---

archive/issue_comments_031556.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2019-06-16T20:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31556",
    "user": "chapoton"
}
```

Resolution: wontfix
