# Issue 7833: r-2.9.2 - fix compilation on FreeBSD

archive/issues_007833.json:
```json
{
    "body": "Assignee: @peterjeremy\n\nCC:  @jasongrout @williamstein\n\nPass CFLAGS, CPPFLAGS and LDFLAGS from the environment into the build process.  This also corrects a typo in CPPFLAGS.\n\nNote that FreeBSD needs the path to libiconv to be explicitly specified.  In theory, --with-libiconv-prefix should work but configure script is broken and ignores that path when looking for libiconv.  Hard-wire /usr/local/include and /usr/local/lib via xxFLAGS.  Without this change, you get:\n\n```\nchecking iconv.h usability... no\nchecking iconv.h presence... no\nchecking for iconv.h... no\nchecking for iconv... no\nchecking for iconvlist... no\nconfigure: error: --with-iconv=yes (default) and a suitable iconv is not available\nError configuring R.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7833\n\n",
    "created_at": "2010-01-03T10:39:43Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "r-2.9.2 - fix compilation on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7833",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: @peterjeremy

CC:  @jasongrout @williamstein

Pass CFLAGS, CPPFLAGS and LDFLAGS from the environment into the build process.  This also corrects a typo in CPPFLAGS.

Note that FreeBSD needs the path to libiconv to be explicitly specified.  In theory, --with-libiconv-prefix should work but configure script is broken and ignores that path when looking for libiconv.  Hard-wire /usr/local/include and /usr/local/lib via xxFLAGS.  Without this change, you get:

```
checking iconv.h usability... no
checking iconv.h presence... no
checking for iconv.h... no
checking for iconv... no
checking for iconvlist... no
configure: error: --with-iconv=yes (default) and a suitable iconv is not available
Error configuring R.
```



Issue created by migration from https://trac.sagemath.org/ticket/7833





---

archive/issue_comments_067739.json:
```json
{
    "body": "Attachment [7833.r.patch](tarball://root/attachments/some-uuid/ticket7833/7833.r.patch) by @peterjeremy created at 2010-01-03 10:40:27",
    "created_at": "2010-01-03T10:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67739",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [7833.r.patch](tarball://root/attachments/some-uuid/ticket7833/7833.r.patch) by @peterjeremy created at 2010-01-03 10:40:27



---

archive/issue_comments_067740.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T10:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67740",
    "user": "https://github.com/peterjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067741.json:
```json
{
    "body": "Is #6532 relevant here?  Is it possible to update this patch for that spkg - it looks like it should be fairly trivial.  You could review that one first if that makes it easier; unfortunately, I don't have access to a FreeBSD machine to return the favor :(",
    "created_at": "2010-01-04T15:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67741",
    "user": "https://github.com/kcrisman"
}
```

Is #6532 relevant here?  Is it possible to update this patch for that spkg - it looks like it should be fairly trivial.  You could review that one first if that makes it easier; unfortunately, I don't have access to a FreeBSD machine to return the favor :(



---

archive/issue_comments_067742.json:
```json
{
    "body": "I don't have a FreeBSD machine, but this patch looks fine to me. The previous spkg-install was clearly written incorrectly. The issues at #6532 are something quite separate. So a positive review from me. \n\nDave",
    "created_at": "2010-01-13T22:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67742",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I don't have a FreeBSD machine, but this patch looks fine to me. The previous spkg-install was clearly written incorrectly. The issues at #6532 are something quite separate. So a positive review from me. 

Dave



---

archive/issue_comments_067743.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T22:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67743",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067744.json:
```json
{
    "body": "PS, \nDon't forget to report this upstream!",
    "created_at": "2010-01-13T23:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67744",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

PS, 
Don't forget to report this upstream!



---

archive/issue_comments_067745.json:
```json
{
    "body": "This needs a link to an spkg to be reviewed.  However, I have incorporated it in the spkg at #6532, so hopefully that will be sufficient!",
    "created_at": "2010-01-15T19:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67745",
    "user": "https://github.com/kcrisman"
}
```

This needs a link to an spkg to be reviewed.  However, I have incorporated it in the spkg at #6532, so hopefully that will be sufficient!



---

archive/issue_comments_067746.json:
```json
{
    "body": "Can someone check that #6532 would resolve this?",
    "created_at": "2010-01-25T19:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67746",
    "user": "https://github.com/kcrisman"
}
```

Can someone check that #6532 would resolve this?



---

archive/issue_comments_067747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T23:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67747",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_067748.json:
```json
{
    "body": "Ticket #6532 incorporates the patch on this ticket, so no need to merge the patch here.",
    "created_at": "2010-01-25T23:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67748",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #6532 incorporates the patch on this ticket, so no need to merge the patch here.



---

archive/issue_events_018734.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-25T23:30:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7833#event-18734"
}
```
