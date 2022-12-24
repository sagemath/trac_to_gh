# Issue 7833: r-2.9.2 - fix compilation on FreeBSD

archive/issues_007833.json:
```json
{
    "body": "Assignee: pjeremy\n\nCC:  jason was\n\nPass CFLAGS, CPPFLAGS and LDFLAGS from the environment into the build process.  This also corrects a typo in CPPFLAGS.\n\nNote that FreeBSD needs the path to libiconv to be explicitly specified.  In theory, --with-libiconv-prefix should work but configure script is broken and ignores that path when looking for libiconv.  Hard-wire /usr/local/include and /usr/local/lib via xxFLAGS.  Without this change, you get:\n\n```\nchecking iconv.h usability... no\nchecking iconv.h presence... no\nchecking for iconv.h... no\nchecking for iconv... no\nchecking for iconvlist... no\nconfigure: error: --with-iconv=yes (default) and a suitable iconv is not available\nError configuring R.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7833\n\n",
    "created_at": "2010-01-03T10:39:43Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "r-2.9.2 - fix compilation on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7833",
    "user": "pjeremy"
}
```
Assignee: pjeremy

CC:  jason was

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

archive/issue_comments_067856.json:
```json
{
    "body": "Attachment [7833.r.patch](tarball://root/attachments/some-uuid/ticket7833/7833.r.patch) by pjeremy created at 2010-01-03 10:40:27",
    "created_at": "2010-01-03T10:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67856",
    "user": "pjeremy"
}
```

Attachment [7833.r.patch](tarball://root/attachments/some-uuid/ticket7833/7833.r.patch) by pjeremy created at 2010-01-03 10:40:27



---

archive/issue_comments_067857.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T10:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67857",
    "user": "pjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067858.json:
```json
{
    "body": "Is #6532 relevant here?  Is it possible to update this patch for that spkg - it looks like it should be fairly trivial.  You could review that one first if that makes it easier; unfortunately, I don't have access to a FreeBSD machine to return the favor :(",
    "created_at": "2010-01-04T15:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67858",
    "user": "kcrisman"
}
```

Is #6532 relevant here?  Is it possible to update this patch for that spkg - it looks like it should be fairly trivial.  You could review that one first if that makes it easier; unfortunately, I don't have access to a FreeBSD machine to return the favor :(



---

archive/issue_comments_067859.json:
```json
{
    "body": "I don't have a FreeBSD machine, but this patch looks fine to me. The previous spkg-install was clearly written incorrectly. The issues at #6532 are something quite separate. So a positive review from me. \n\nDave",
    "created_at": "2010-01-13T22:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67859",
    "user": "drkirkby"
}
```

I don't have a FreeBSD machine, but this patch looks fine to me. The previous spkg-install was clearly written incorrectly. The issues at #6532 are something quite separate. So a positive review from me. 

Dave



---

archive/issue_comments_067860.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T22:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67860",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067861.json:
```json
{
    "body": "PS, \nDon't forget to report this upstream!",
    "created_at": "2010-01-13T23:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67861",
    "user": "drkirkby"
}
```

PS, 
Don't forget to report this upstream!



---

archive/issue_comments_067862.json:
```json
{
    "body": "This needs a link to an spkg to be reviewed.  However, I have incorporated it in the spkg at #6532, so hopefully that will be sufficient!",
    "created_at": "2010-01-15T19:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67862",
    "user": "kcrisman"
}
```

This needs a link to an spkg to be reviewed.  However, I have incorporated it in the spkg at #6532, so hopefully that will be sufficient!



---

archive/issue_comments_067863.json:
```json
{
    "body": "Can someone check that #6532 would resolve this?",
    "created_at": "2010-01-25T19:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67863",
    "user": "kcrisman"
}
```

Can someone check that #6532 would resolve this?



---

archive/issue_comments_067864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T23:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67864",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_067865.json:
```json
{
    "body": "Ticket #6532 incorporates the patch on this ticket, so no need to merge the patch here.",
    "created_at": "2010-01-25T23:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7833#issuecomment-67865",
    "user": "mvngu"
}
```

Ticket #6532 incorporates the patch on this ticket, so no need to merge the patch here.
