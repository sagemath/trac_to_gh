# Issue 4309: Kerberos authentification for SAGE notebook

archive/issues_004309.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @embray @jdemeyer @kiwifb\n\nThis patch adds Kerberos authentification support for the SAGE notebook. It also adds the options krb_srv, krb_realm for the notebook() command.\n\nThis patch however depends on pykerberos which depends on kerberos which depends on a couple of other libraries all in all a little less size than SAGE itself and all not in SAGE :-). Nevertheless ... \n\nGreetings, \nKilian. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4309\n\n",
    "created_at": "2008-10-16T17:30:31Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Kerberos authentification for SAGE notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4309",
    "user": "https://trac.sagemath.org/admin/accounts/users/kkilger"
}
```
Assignee: @williamstein

CC:  @embray @jdemeyer @kiwifb

This patch adds Kerberos authentification support for the SAGE notebook. It also adds the options krb_srv, krb_realm for the notebook() command.

This patch however depends on pykerberos which depends on kerberos which depends on a couple of other libraries all in all a little less size than SAGE itself and all not in SAGE :-). Nevertheless ... 

Greetings, 
Kilian. 

Issue created by migration from https://trac.sagemath.org/ticket/4309





---

archive/issue_comments_031479.json:
```json
{
    "body": "Attachment [my.patch](tarball://root/attachments/some-uuid/ticket4309/my.patch) by kkilger created at 2008-10-16 17:31:02",
    "created_at": "2008-10-16T17:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31479",
    "user": "https://trac.sagemath.org/admin/accounts/users/kkilger"
}
```

Attachment [my.patch](tarball://root/attachments/some-uuid/ticket4309/my.patch) by kkilger created at 2008-10-16 17:31:02



---

archive/issue_comments_031480.json:
```json
{
    "body": "This doesn't apply in sage-3.2.alpha1",
    "created_at": "2008-11-09T21:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31480",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

This doesn't apply in sage-3.2.alpha1



---

archive/issue_comments_031481.json:
```json
{
    "body": "Attachment [sage-4309_1.patch](tarball://root/attachments/some-uuid/ticket4309/sage-4309_1.patch) by TimothyClemans created at 2008-11-09 23:54:01",
    "created_at": "2008-11-09T23:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31481",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4309_1.patch](tarball://root/attachments/some-uuid/ticket4309/sage-4309_1.patch) by TimothyClemans created at 2008-11-09 23:54:01



---

archive/issue_comments_031482.json:
```json
{
    "body": "Kerberos shouldn't be required to use the notebook. Make Kerberos authentication optional.",
    "created_at": "2008-11-09T23:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31482",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Kerberos shouldn't be required to use the notebook. Make Kerberos authentication optional.



---

archive/issue_comments_031483.json:
```json
{
    "body": "my.patch is replaced by sage-3950_1.patch and applies in sage-3.2.alpha1",
    "created_at": "2008-11-10T00:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31483",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

my.patch is replaced by sage-3950_1.patch and applies in sage-3.2.alpha1



---

archive/issue_comments_031484.json:
```json
{
    "body": "Attachment [sage-4309_2.patch](tarball://root/attachments/some-uuid/ticket4309/sage-4309_2.patch) by TimothyClemans created at 2008-11-10 02:07:54",
    "created_at": "2008-11-10T02:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31484",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4309_2.patch](tarball://root/attachments/some-uuid/ticket4309/sage-4309_2.patch) by TimothyClemans created at 2008-11-10 02:07:54



---

archive/issue_comments_031485.json:
```json
{
    "body": "OK now Kerberos isn't required.",
    "created_at": "2008-11-10T02:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31485",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

OK now Kerberos isn't required.



---

archive/issue_comments_031486.json:
```json
{
    "body": "Attachment [sage-4309_3.patch](tarball://root/attachments/some-uuid/ticket4309/sage-4309_3.patch) by TimothyClemans created at 2008-11-10 04:02:41",
    "created_at": "2008-11-10T04:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31486",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4309_3.patch](tarball://root/attachments/some-uuid/ticket4309/sage-4309_3.patch) by TimothyClemans created at 2008-11-10 04:02:41



---

archive/issue_comments_031487.json:
```json
{
    "body": "Changing component from user interface to notebook.",
    "created_at": "2008-11-10T04:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31487",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing component from user interface to notebook.



---

archive/issue_comments_031488.json:
```json
{
    "body": "Changing assignee from @williamstein to kkilger.",
    "created_at": "2008-11-10T04:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31488",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from @williamstein to kkilger.



---

archive/issue_comments_031489.json:
```json
{
    "body": "Hi,\n\nI like the design of this patch and how the kerberos stuff is optional.  \n\nUnfortunately, this is hard to referee if you don't explain to me how to install pykerberos.  Also, the patch itself should contain code that says \"hey, you need kerberos, and here's how to install it\" when the user turns on kerberos via an option to notebook, but \n\n```\nimport kerberos\n```\n\nfails.  That could be either a paragraph of text, an optional spkg to install, or a link to a wiki page that describes what to do.  \n\nOK?\n\nThanks!",
    "created_at": "2008-11-29T03:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31489",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_031490.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2019-06-16T18:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31490",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_031491.json:
```json
{
    "body": "notebook is deprecated, so this can probably be closed",
    "created_at": "2019-06-16T18:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31491",
    "user": "https://github.com/fchapoton"
}
```

notebook is deprecated, so this can probably be closed



---

archive/issue_comments_031492.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-06-16T18:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31492",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031493.json:
```json
{
    "body": "Yes.",
    "created_at": "2019-06-16T18:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31493",
    "user": "https://github.com/kiwifb"
}
```

Yes.



---

archive/issue_comments_031494.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2019-06-16T20:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4309#issuecomment-31494",
    "user": "https://github.com/fchapoton"
}
```

Resolution: wontfix



---

archive/issue_events_004552.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-06-16T20:08:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4309",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4309#event-4552"
}
```
