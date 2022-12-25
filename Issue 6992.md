# Issue 6992: rename lngamma to log gamma

archive/issues_006992.json:
```json
{
    "body": "Assignee: @burcin\n\nThe Sage convention is to use `log` for the natural logarithm. See #6902 for more discussion.\n\nAttached patch renames the `lngamma` functions in the library, and adds deprecation notices where appropriate.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6992\n\n",
    "created_at": "2009-09-22T19:10:47Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "rename lngamma to log gamma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6992",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

The Sage convention is to use `log` for the natural logarithm. See #6902 for more discussion.

Attached patch renames the `lngamma` functions in the library, and adds deprecation notices where appropriate.


Issue created by migration from https://trac.sagemath.org/ticket/6992





---

archive/issue_comments_057722.json:
```json
{
    "body": "Attachment [trac_6992-rename_lgamma.patch](tarball://root/attachments/some-uuid/ticket6992/trac_6992-rename_lgamma.patch) by @burcin created at 2009-09-22 19:13:45",
    "created_at": "2009-09-22T19:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57722",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6992-rename_lgamma.patch](tarball://root/attachments/some-uuid/ticket6992/trac_6992-rename_lgamma.patch) by @burcin created at 2009-09-22 19:13:45



---

archive/issue_comments_057723.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-22T19:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57723",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057724.json:
```json
{
    "body": "New pynac package available at #6993.",
    "created_at": "2009-09-22T19:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57724",
    "user": "https://github.com/burcin"
}
```

New pynac package available at #6993.



---

archive/issue_comments_057725.json:
```json
{
    "body": "In sage/symbolic/expression.pyx, there is a plot of the log_gamma function in line 4918, which nonetheless raises the DeprecationWarning when I test it via sage -t, though not when I cut and paste that command.  It happens also upon a retest.  Do you get this?  I find it very strange, so I wonder if I did something wrong.",
    "created_at": "2009-09-23T02:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57725",
    "user": "https://github.com/kcrisman"
}
```

In sage/symbolic/expression.pyx, there is a plot of the log_gamma function in line 4918, which nonetheless raises the DeprecationWarning when I test it via sage -t, though not when I cut and paste that command.  It happens also upon a retest.  Do you get this?  I find it very strange, so I wonder if I did something wrong.



---

archive/issue_comments_057726.json:
```json
{
    "body": "Upon applying all the patches involved, this disappears, quite mysteriously.",
    "created_at": "2009-09-23T20:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57726",
    "user": "https://github.com/kcrisman"
}
```

Upon applying all the patches involved, this disappears, quite mysteriously.



---

archive/issue_comments_057727.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T22:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057728.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.



---

archive/issue_comments_057729.json:
```json
{
    "body": "#12521 gets rid of the deprecated functions.",
    "created_at": "2013-06-25T09:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6992#issuecomment-57729",
    "user": "https://github.com/eviatarbach"
}
```

#12521 gets rid of the deprecated functions.
