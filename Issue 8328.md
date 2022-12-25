# Issue 8328: clisp rather than ecl mentioned on web page.

archive/issues_008328.json:
```json
{
    "body": "Assignee: mvngu\n\nhttp://www.sagemath.org/doc/tutorial/interfaces.html\nsays:\n\n\"Maxima is included with Sage, as is clisp (a version of the Lisp language).\"\n\nClearly this is wrong. \n\nIt would be worth going over the web site with a recursive grep, to see if there are any other mentions of clisp or Vmware, as I believe there are a few points where VMware is mentioned, despite the fact there is a shift to VirtualBox. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/8328\n\n",
    "created_at": "2010-02-22T19:20:49Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "clisp rather than ecl mentioned on web page.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8328",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: mvngu

http://www.sagemath.org/doc/tutorial/interfaces.html
says:

"Maxima is included with Sage, as is clisp (a version of the Lisp language)."

Clearly this is wrong. 

It would be worth going over the web site with a recursive grep, to see if there are any other mentions of clisp or Vmware, as I believe there are a few points where VMware is mentioned, despite the fact there is a shift to VirtualBox. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/8328





---

archive/issue_comments_074016.json:
```json
{
    "body": "Attachment [trac_8328-tutorial.patch](tarball://root/attachments/some-uuid/ticket8328/trac_8328-tutorial.patch) by mvngu created at 2010-02-26 02:13:32\n\nbased on Sage 4.3.3",
    "created_at": "2010-02-26T02:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8328#issuecomment-74016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8328-tutorial.patch](tarball://root/attachments/some-uuid/ticket8328/trac_8328-tutorial.patch) by mvngu created at 2010-02-26 02:13:32

based on Sage 4.3.3



---

archive/issue_comments_074017.json:
```json
{
    "body": "The patch [trac_8328-tutorial.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8328/trac_8328-tutorial.patch) only fixes that one issue reported in the ticket description. I did a recursive grep over all `.rst` files in the following documentation, looking for occurrences of \"clisp\" and \"VMware\", and other variations in spelling:\n\n* A Tour of Sage\n* Bordeaux 2008 lecture\n* Constructions Document\n* Developer's Guide\n* Installation Guide\n* Numerical Guide\n* Tutorial\n\nAnd I only found the occurrences as fixed in the patch.",
    "created_at": "2010-02-26T02:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8328#issuecomment-74017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch [trac_8328-tutorial.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8328/trac_8328-tutorial.patch) only fixes that one issue reported in the ticket description. I did a recursive grep over all `.rst` files in the following documentation, looking for occurrences of "clisp" and "VMware", and other variations in spelling:

* A Tour of Sage
* Bordeaux 2008 lecture
* Constructions Document
* Developer's Guide
* Installation Guide
* Numerical Guide
* Tutorial

And I only found the occurrences as fixed in the patch.



---

archive/issue_comments_074018.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-26T02:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8328#issuecomment-74018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074019.json:
```json
{
    "body": "I thought I'd seen VMware somewhere - it might have been on the Wiki. \n\nAnyway, that looks good to me.",
    "created_at": "2010-02-26T02:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8328#issuecomment-74019",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I thought I'd seen VMware somewhere - it might have been on the Wiki. 

Anyway, that looks good to me.



---

archive/issue_comments_074020.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T02:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8328#issuecomment-74020",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019944.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T22:06:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8328#event-19944"
}
```



---

archive/issue_comments_074021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8328#issuecomment-74021",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
