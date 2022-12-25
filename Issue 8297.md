# Issue 8297: extra parenthesis when typesetting QQ arguments to symbolic functions

archive/issues_008297.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nFrom sage-devel:\n\n\n```\nOn Wed, 17 Feb 2010 23:16:13 -0800 (PST)\nH\u00e5kan Granath <hakan.granath@googlemail.com> wrote:\n\n> A minor inconvenience is the extra set of parentheses that appear\n> when typesetting QQ elements as arguments of functions, e.g.\n> \n> ----------------------------------------------------------------------\n> | Sage Version 4.3.2, Release Date: 2010-02-06                       |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> sage: latex(gamma(1/4))\n> \\Gamma\\left(\\left(\\frac{1}{4}\\right)\\right)\n> \n> \n> Unfortunately I can not create a patch myself to fix this since\n> I could not figure out where the problem comes from.\n> \n> /H\u00e5kan\n```\n\n\nHere is the thread:\n\nhttp://groups.google.com/group/sage-devel/t/d068d2fd544eadde\n\nIssue created by migration from https://trac.sagemath.org/ticket/8297\n\n",
    "created_at": "2010-02-18T09:30:19Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "extra parenthesis when typesetting QQ arguments to symbolic functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8297",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

From sage-devel:


```
On Wed, 17 Feb 2010 23:16:13 -0800 (PST)
Håkan Granath <hakan.granath@googlemail.com> wrote:

> A minor inconvenience is the extra set of parentheses that appear
> when typesetting QQ elements as arguments of functions, e.g.
> 
> ----------------------------------------------------------------------
> | Sage Version 4.3.2, Release Date: 2010-02-06                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: latex(gamma(1/4))
> \Gamma\left(\left(\frac{1}{4}\right)\right)
> 
> 
> Unfortunately I can not create a patch myself to fix this since
> I could not figure out where the problem comes from.
> 
> /Håkan
```


Here is the thread:

http://groups.google.com/group/sage-devel/t/d068d2fd544eadde

Issue created by migration from https://trac.sagemath.org/ticket/8297





---

archive/issue_comments_073377.json:
```json
{
    "body": "Attachment [trac_8297-sfunction_extra_paranthesis.patch](tarball://root/attachments/some-uuid/ticket8297/trac_8297-sfunction_extra_paranthesis.patch) by @burcin created at 2010-04-02 16:10:11",
    "created_at": "2010-04-02T16:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73377",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8297-sfunction_extra_paranthesis.patch](tarball://root/attachments/some-uuid/ticket8297/trac_8297-sfunction_extra_paranthesis.patch) by @burcin created at 2010-04-02 16:10:11



---

archive/issue_comments_073378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T16:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73378",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073379.json:
```json
{
    "body": "Changing keywords from \"pynac\" to \"\".",
    "created_at": "2010-04-02T16:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73379",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "pynac" to "".



---

archive/issue_comments_073380.json:
```json
{
    "body": "The fix for this was much easier than I expected. It didn't require any changes in pynac. :)",
    "created_at": "2010-04-02T16:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73380",
    "user": "https://github.com/burcin"
}
```

The fix for this was much easier than I expected. It didn't require any changes in pynac. :)



---

archive/issue_comments_073381.json:
```json
{
    "body": "The patch works, I have checked that it passes all tests, and html and\npdf manual builds. This is my first attempt to review a ticket\nhowever, and I stumbled upon 2 problems:\n\nIs the documentation for these functions actually in the reference\nmanual? I wanted to check that the newly generated files looked good,\nbut could not find the place. Maybe I am just blind...\n\nTyping sage.functions.log.Function_log? + TAB in the notebook (Linux\nbox with Firefox 3.6.3) the TESTS section (where some of the\ndocumentation of the patch appear) is messed up. This also happens for\nme without this patch, though.",
    "created_at": "2010-04-11T12:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73381",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

The patch works, I have checked that it passes all tests, and html and
pdf manual builds. This is my first attempt to review a ticket
however, and I stumbled upon 2 problems:

Is the documentation for these functions actually in the reference
manual? I wanted to check that the newly generated files looked good,
but could not find the place. Maybe I am just blind...

Typing sage.functions.log.Function_log? + TAB in the notebook (Linux
box with Firefox 3.6.3) the TESTS section (where some of the
documentation of the patch appear) is messed up. This also happens for
me without this patch, though.



---

archive/issue_comments_073382.json:
```json
{
    "body": "Attachment [trac_8297-sfunction_extra_paranthesis.take2.patch](tarball://root/attachments/some-uuid/ticket8297/trac_8297-sfunction_extra_paranthesis.take2.patch) by @burcin created at 2010-04-11 12:38:50\n\napply only this patch",
    "created_at": "2010-04-11T12:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73382",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8297-sfunction_extra_paranthesis.take2.patch](tarball://root/attachments/some-uuid/ticket8297/trac_8297-sfunction_extra_paranthesis.take2.patch) by @burcin created at 2010-04-11 12:38:50

apply only this patch



---

archive/issue_comments_073383.json:
```json
{
    "body": "The docstring was messed up because of the missing `r` before starting the string. attachment:trac_8297-sfunction_extra_paranthesis.take2.patch fixes this.\n\nI don't know why the documentation for these functions don't show up in the reference manual. I suggest opening a new ticket for that.",
    "created_at": "2010-04-11T12:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73383",
    "user": "https://github.com/burcin"
}
```

The docstring was messed up because of the missing `r` before starting the string. attachment:trac_8297-sfunction_extra_paranthesis.take2.patch fixes this.

I don't know why the documentation for these functions don't show up in the reference manual. I suggest opening a new ticket for that.



---

archive/issue_comments_073384.json:
```json
{
    "body": "Great, now sage.functions.log.Function_log? + TAB works well.",
    "created_at": "2010-04-11T13:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73384",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Great, now sage.functions.log.Function_log? + TAB works well.



---

archive/issue_comments_073385.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-11T13:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73385",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073386.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73386",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_073387.json:
```json
{
    "body": "Merged \"trac_8297-sfunction_extra_paranthesis.take2.patch\" into 4.4.alpha0",
    "created_at": "2010-04-15T23:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8297#issuecomment-73387",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8297-sfunction_extra_paranthesis.take2.patch" into 4.4.alpha0
