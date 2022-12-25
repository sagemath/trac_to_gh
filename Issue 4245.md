# Issue 4245: notebook -- error clicking editing when there is a < in the html.

archive/issues_004245.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\nOn Sun, Oct 5, 2008 at 3:56 AM, Jo\u00ebl Duet <joel.duet@gmail.com> wrote:\n> Hi,\n> Here is my problem :\n> I want to write \"a<b\" in the HTML part of my worksheet (notebook() style).\n>\n> 1) I click \"Edit\"\n> 2) After a }}} and before a {{{, I type (without quotes) : \" <p> Let\n> <i>a&lt;b</i>.</p>\"\n> 3) I click \"Save Changes\"\n>\n> And it's done but if I click again at \"Edit\", I get (without quotes) : \"<p>\n> Let <i>a<b</i>.</p>\" and it's bad.\n>\n> What can I do if I want to Edit several times ?\n>\n\nThis is definitely a bug, which could be fixed.  In the meantime, as a workround \nyou might just do\n\n\"<p>Let  $a < b$.</p>\"\n\nsince that will look better anyways. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4245\n\n",
    "created_at": "2008-10-05T18:46:04Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "notebook -- error clicking editing when there is a < in the html.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4245",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```

On Sun, Oct 5, 2008 at 3:56 AM, Joël Duet <joel.duet@gmail.com> wrote:
> Hi,
> Here is my problem :
> I want to write "a<b" in the HTML part of my worksheet (notebook() style).
>
> 1) I click "Edit"
> 2) After a }}} and before a {{{, I type (without quotes) : " <p> Let
> <i>a&lt;b</i>.</p>"
> 3) I click "Save Changes"
>
> And it's done but if I click again at "Edit", I get (without quotes) : "<p>
> Let <i>a<b</i>.</p>" and it's bad.
>
> What can I do if I want to Edit several times ?
>

This is definitely a bug, which could be fixed.  In the meantime, as a workround 
you might just do

"<p>Let  $a < b$.</p>"

since that will look better anyways. 
```


Issue created by migration from https://trac.sagemath.org/ticket/4245





---

archive/issue_comments_030791.json:
```json
{
    "body": "I can't tell if I'm seeing the same problem or not, so I have a new ticket which might be related: #4316.",
    "created_at": "2008-10-17T23:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30791",
    "user": "https://github.com/jhpalmieri"
}
```

I can't tell if I'm seeing the same problem or not, so I have a new ticket which might be related: #4316.



---

archive/issue_comments_030792.json:
```json
{
    "body": "Attachment [trac_4245.patch](tarball://root/attachments/some-uuid/ticket4245/trac_4245.patch) by @mwhansen created at 2009-01-24 07:33:57",
    "created_at": "2009-01-24T07:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30792",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4245.patch](tarball://root/attachments/some-uuid/ticket4245/trac_4245.patch) by @mwhansen created at 2009-01-24 07:33:57



---

archive/issue_comments_030793.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T07:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30793",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030794.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-24T07:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30794",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_030795.json:
```json
{
    "body": "When testing the problem in #4316:\n\n```\n%html \nsome math: $x<y$.\n```\n\nI get the message \n\n```\nNameError: global name 'cgi' is not defined\n```\n\nMore importantly, when testing the problem reported here, I don't see a change in behavior: after editing the worksheet and typing \n\n```\n<p> Let <i>a&lt;b</i>.</p>\n```\n\nin between cells and saving, it looks fine, but when I click \"Edit\" again, the `&lt;` has turned into `<`, and it is printed wrong.",
    "created_at": "2009-01-24T16:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30795",
    "user": "https://github.com/jhpalmieri"
}
```

When testing the problem in #4316:

```
%html 
some math: $x<y$.
```

I get the message 

```
NameError: global name 'cgi' is not defined
```

More importantly, when testing the problem reported here, I don't see a change in behavior: after editing the worksheet and typing 

```
<p> Let <i>a&lt;b</i>.</p>
```

in between cells and saving, it looks fine, but when I click "Edit" again, the `&lt;` has turned into `<`, and it is printed wrong.



---

archive/issue_comments_030796.json:
```json
{
    "body": "Mike's patch above breaks %html mode since it assumes you literally want \"<\" every time you write it.  That means you can't type `<b>hello</b>`.  I like it better the other way (before), that demanded that you type &lt; instead of <.\n\nThis is somewhat of a moot point now that TinyMCE is in.",
    "created_at": "2009-02-06T08:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30796",
    "user": "https://github.com/jasongrout"
}
```

Mike's patch above breaks %html mode since it assumes you literally want "<" every time you write it.  That means you can't type `<b>hello</b>`.  I like it better the other way (before), that demanded that you type &lt; instead of <.

This is somewhat of a moot point now that TinyMCE is in.



---

archive/issue_comments_030797.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2009-02-06T08:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30797",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_030798.json:
```json
{
    "body": "I've attached a patch which fixes the quoting issue for the Edit button.  Basically, we need to escape ampersands as well as less thans.",
    "created_at": "2009-02-06T08:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30798",
    "user": "https://github.com/jasongrout"
}
```

I've attached a patch which fixes the quoting issue for the Edit button.  Basically, we need to escape ampersands as well as less thans.



---

archive/issue_comments_030799.json:
```json
{
    "body": "Attachment [trac_4245-html-escape.patch](tarball://root/attachments/some-uuid/ticket4245/trac_4245-html-escape.patch) by @jasongrout created at 2009-02-06 08:58:23",
    "created_at": "2009-02-06T08:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30799",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4245-html-escape.patch](tarball://root/attachments/some-uuid/ticket4245/trac_4245-html-escape.patch) by @jasongrout created at 2009-02-06 08:58:23



---

archive/issue_comments_030800.json:
```json
{
    "body": "Apply only trac_4245-html-escape.patch",
    "created_at": "2009-02-06T08:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30800",
    "user": "https://github.com/jasongrout"
}
```

Apply only trac_4245-html-escape.patch



---

archive/issue_comments_030801.json:
```json
{
    "body": "Changing assignee from @mwhansen to @jasongrout.",
    "created_at": "2009-02-06T08:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30801",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @mwhansen to @jasongrout.



---

archive/issue_comments_030802.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-02-06T08:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30802",
    "user": "https://github.com/jasongrout"
}
```

Changing status from assigned to new.



---

archive/issue_comments_030803.json:
```json
{
    "body": "Positive review, fixes the problem for me.  Explanation makes sense too, although interestingly I never saw e.g. &lt anywhere, whether in TinyMCE or in the Edit button, or even in \"View Source\", when this problem occurred.",
    "created_at": "2009-02-06T14:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30803",
    "user": "https://github.com/kcrisman"
}
```

Positive review, fixes the problem for me.  Explanation makes sense too, although interestingly I never saw e.g. &lt anywhere, whether in TinyMCE or in the Edit button, or even in "View Source", when this problem occurred.



---

archive/issue_comments_030804.json:
```json
{
    "body": "Looks good to me, too.",
    "created_at": "2009-02-06T15:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30804",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me, too.



---

archive/issue_comments_030805.json:
```json
{
    "body": "kcrisman: that was the problem.  There should have &lt; things in the Edit view.",
    "created_at": "2009-02-06T16:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30805",
    "user": "https://github.com/jasongrout"
}
```

kcrisman: that was the problem.  There should have &lt; things in the Edit view.



---

archive/issue_comments_030806.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T21:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004484.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T21:53:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4245#event-4484"
}
```



---

archive/issue_comments_030807.json:
```json
{
    "body": "Merged trac_4245-html-escape.patch only in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T21:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4245#issuecomment-30807",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_4245-html-escape.patch only in Sage 3.3.alpha6.

Cheers,

Michael
