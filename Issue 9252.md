# Issue 9252: documentation errors in tutorial

archive/issues_009252.json:
```json
{
    "body": "Assignee: wjlaffin\n\nCC:  @kcrisman @embray @tscrim\n\n$'s are not escaped, multilines appear wrong, etc.\n\npatch to appear shortly\n\nIssue created by migration from https://trac.sagemath.org/ticket/9252\n\n",
    "created_at": "2010-06-17T08:03:23Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "documentation errors in tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9252",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```
Assignee: wjlaffin

CC:  @kcrisman @embray @tscrim

$'s are not escaped, multilines appear wrong, etc.

patch to appear shortly

Issue created by migration from https://trac.sagemath.org/ticket/9252





---

archive/issue_comments_086931.json:
```json
{
    "body": "Attachment [trac9252.patch](tarball://root/attachments/some-uuid/ticket9252/trac9252.patch) by wjlaffin created at 2010-06-17 23:03:56",
    "created_at": "2010-06-17T23:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86931",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Attachment [trac9252.patch](tarball://root/attachments/some-uuid/ticket9252/trac9252.patch) by wjlaffin created at 2010-06-17 23:03:56



---

archive/issue_comments_086932.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-17T23:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86932",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_086933.json:
```json
{
    "body": "Whops. Forgot to test that. Disregard the first one.",
    "created_at": "2010-06-17T23:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86933",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Whops. Forgot to test that. Disregard the first one.



---

archive/issue_comments_086934.json:
```json
{
    "body": "Attachment [trac9252.1.patch](tarball://root/attachments/some-uuid/ticket9252/trac9252.1.patch) by wjlaffin created at 2010-06-17 23:22:01",
    "created_at": "2010-06-17T23:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86934",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Attachment [trac9252.1.patch](tarball://root/attachments/some-uuid/ticket9252/trac9252.1.patch) by wjlaffin created at 2010-06-17 23:22:01



---

archive/issue_comments_086935.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-17T23:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86935",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086936.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-18T00:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86936",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_086937.json:
```json
{
    "body": "I don't think this works with the static documentation; the backslashes that you've inserted are visible there.",
    "created_at": "2010-06-18T00:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86937",
    "user": "https://github.com/jhpalmieri"
}
```

I don't think this works with the static documentation; the backslashes that you've inserted are visible there.



---

archive/issue_comments_086938.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> I don't think this works with the static documentation; the backslashes that you've inserted are visible there.\n\nWhen you(or really anyone) says \"static version\" do they mean the pdf's? Would I be able to see them with \n\n```\nsage -docbuild tutorial pdf\n```\n\n?\n\nOn that note, where is the code that adds the $$=latex hack to the documentation? Maybe I can just patch that a little instead.\n\nWhat about the literal blocks that are meant for the interactive shell? 'sage:' always gets turned into a cell, so I needed to add some kind of header in the literal block (a bad hack) to get it to print correctly in the live-help.\n\nThanks for looking at my patch!",
    "created_at": "2010-06-18T04:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86938",
    "user": "https://trac.sagemath.org/admin/accounts/users/wjlaffin"
}
```

Replying to [comment:3 jhpalmieri]:
> I don't think this works with the static documentation; the backslashes that you've inserted are visible there.

When you(or really anyone) says "static version" do they mean the pdf's? Would I be able to see them with 

```
sage -docbuild tutorial pdf
```

?

On that note, where is the code that adds the $$=latex hack to the documentation? Maybe I can just patch that a little instead.

What about the literal blocks that are meant for the interactive shell? 'sage:' always gets turned into a cell, so I needed to add some kind of header in the literal block (a bad hack) to get it to print correctly in the live-help.

Thanks for looking at my patch!



---

archive/issue_comments_086939.json:
```json
{
    "body": "Replying to [comment:4 wjlaffin]:\n> When you(or really anyone) says \"static version\" do they mean the pdf's? \n\nNo, the html version.  From the command line, execute \"tutorial()\", or from the notebook click the \"Help\" button and then the button for \"Fast Static Versions of the Documentation\".  Then click on the word \"Tutorial\".  Or open the file SAGE_ROOT/devel/sage/doc/output/html/en/tutorial/index.html in your web browser.\n\n> On that note, where is the code that adds the $$=latex hack to the documentation? Maybe I can just patch that a little instead.\n> \n> What about the literal blocks that are meant for the interactive shell? 'sage:' always gets turned into a cell, so I needed to add some kind of header in the literal block (a bad hack) to get it to print correctly in the live-help.\n\nSome of this is in sage/sage/misc/sagedoc.py (e.g., `process_dollars`).  See also SAGE_ROOT/devel/sage/doc/common/conf.py.\n\nIt looks like the conversion from the html file to the \"live\" version of the docs is in the notebook code: SAGE_ROOT/local/lib/python/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/docHTMLProcessor.py, it looks like.  Since you're dealing with differences between the static and the live versions, you may need to look there.",
    "created_at": "2010-06-18T05:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86939",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:4 wjlaffin]:
> When you(or really anyone) says "static version" do they mean the pdf's? 

No, the html version.  From the command line, execute "tutorial()", or from the notebook click the "Help" button and then the button for "Fast Static Versions of the Documentation".  Then click on the word "Tutorial".  Or open the file SAGE_ROOT/devel/sage/doc/output/html/en/tutorial/index.html in your web browser.

> On that note, where is the code that adds the $$=latex hack to the documentation? Maybe I can just patch that a little instead.
> 
> What about the literal blocks that are meant for the interactive shell? 'sage:' always gets turned into a cell, so I needed to add some kind of header in the literal block (a bad hack) to get it to print correctly in the live-help.

Some of this is in sage/sage/misc/sagedoc.py (e.g., `process_dollars`).  See also SAGE_ROOT/devel/sage/doc/common/conf.py.

It looks like the conversion from the html file to the "live" version of the docs is in the notebook code: SAGE_ROOT/local/lib/python/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/docHTMLProcessor.py, it looks like.  Since you're dealing with differences between the static and the live versions, you may need to look there.



---

archive/issue_comments_086940.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2019-05-10T18:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86940",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_086941.json:
```json
{
    "body": "obsolete, probably ?",
    "created_at": "2019-05-10T18:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86941",
    "user": "https://github.com/fchapoton"
}
```

obsolete, probably ?



---

archive/issue_comments_086942.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2019-05-17T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86942",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_086943.json:
```json
{
    "body": "Yes, I think so. Let's close it.",
    "created_at": "2019-05-17T17:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86943",
    "user": "https://github.com/jhpalmieri"
}
```

Yes, I think so. Let's close it.



---

archive/issue_comments_086944.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-05-22T19:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9252#issuecomment-86944",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_009413.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2019-05-22T19:51:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9252",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9252#event-9413"
}
```
