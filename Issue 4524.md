# Issue 4524: interact : incomplete default string in the input box

archive/issues_004524.json:
```json
{
    "body": "Assignee: @itolkov\n\nKeywords: input_box\n\nUsing interact in sage 3.1.4, the default string doesn't print completly in the input box. It looks like it prints up to the first character ' found.\nThe folowing example works well \n\n\n```\n@interact\ndef _(a=input_box(default='interact is \"cool\"',type=str,label='Name:')):\n    print a\n```\n\n\nand it puts *interact is \"cool\"* in the input box. But in the next one, \n\n\n```\n@interact\ndef _(a=input_box(default=\"interact is 'cool'\",type=str,label='Name:')):\n    print a\n```\n\n\nthe default string in the input box is incomplete, it puts only *interact is *. So, we don't know if interact is cool or not !\n\nIssue created by migration from https://trac.sagemath.org/ticket/4524\n\n",
    "created_at": "2008-11-14T17:04:23Z",
    "labels": [
        "component: interact",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "interact : incomplete default string in the input box",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4524",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @itolkov

Keywords: input_box

Using interact in sage 3.1.4, the default string doesn't print completly in the input box. It looks like it prints up to the first character ' found.
The folowing example works well 


```
@interact
def _(a=input_box(default='interact is "cool"',type=str,label='Name:')):
    print a
```


and it puts *interact is "cool"* in the input box. But in the next one, 


```
@interact
def _(a=input_box(default="interact is 'cool'",type=str,label='Name:')):
    print a
```


the default string in the input box is incomplete, it puts only *interact is *. So, we don't know if interact is cool or not !

Issue created by migration from https://trac.sagemath.org/ticket/4524





---

archive/issue_comments_033508.json:
```json
{
    "body": "Attachment [trac_4524.patch](tarball://root/attachments/some-uuid/ticket4524/trac_4524.patch) by @mwhansen created at 2009-01-23 08:10:46",
    "created_at": "2009-01-23T08:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33508",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4524.patch](tarball://root/attachments/some-uuid/ticket4524/trac_4524.patch) by @mwhansen created at 2009-01-23 08:10:46



---

archive/issue_comments_033509.json:
```json
{
    "body": "Changing assignee from @itolkov to @mwhansen.",
    "created_at": "2009-01-23T08:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33509",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @itolkov to @mwhansen.



---

archive/issue_comments_033510.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T08:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33510",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033511.json:
```json
{
    "body": "First, that is the first time I review a patch. So if you have comment on the way I review, tell me. I also have some questions that I write below as I have them. Moreover, I am not familiar with notebook code at all....so should I let the job to somebody else?\n\nHowever, I applied the patch and I can at least say that the problem I submitted is now fixed which is cool!\n\nThere is a small issue here (double that) :\n\n\n```\nNote that any HTML that that uses quotes around this should use double quotes and not single quotes. \n```\n\n\nAlso, I don't know if you agreee, but I suggest to add the second example below :\n\n\n```\nEXAMPLES: \n    sage: from sage.server.notebook.interact import InteractControl \n    sage: InteractControl('x', '\"cool\"').html_escaped_default_value() \n    '&quot;cool&quot;' \n    sage: InteractControl('x',\"'cool'\").html_escaped_default_value()\n    \"'cool'\"\n```\n\n\nMy last question is : I could have posted a patch for both issues (double that, and the 2nd example). What is commonly done? Do we leave the changes to the patcher?\n\nMy statement is Positive review pending fixes on at least the first of my two doc-suggestions.\n\nThanks for the fix,",
    "created_at": "2009-01-23T18:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33511",
    "user": "https://github.com/seblabbe"
}
```

First, that is the first time I review a patch. So if you have comment on the way I review, tell me. I also have some questions that I write below as I have them. Moreover, I am not familiar with notebook code at all....so should I let the job to somebody else?

However, I applied the patch and I can at least say that the problem I submitted is now fixed which is cool!

There is a small issue here (double that) :


```
Note that any HTML that that uses quotes around this should use double quotes and not single quotes. 
```


Also, I don't know if you agreee, but I suggest to add the second example below :


```
EXAMPLES: 
    sage: from sage.server.notebook.interact import InteractControl 
    sage: InteractControl('x', '"cool"').html_escaped_default_value() 
    '&quot;cool&quot;' 
    sage: InteractControl('x',"'cool'").html_escaped_default_value()
    "'cool'"
```


My last question is : I could have posted a patch for both issues (double that, and the 2nd example). What is commonly done? Do we leave the changes to the patcher?

My statement is Positive review pending fixes on at least the first of my two doc-suggestions.

Thanks for the fix,



---

archive/issue_comments_033512.json:
```json
{
    "body": "I've posted a patch which addresses the issues.\n\nYou could have posted a patch and then asked me to review your portion of the patch.",
    "created_at": "2009-01-24T15:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33512",
    "user": "https://github.com/mwhansen"
}
```

I've posted a patch which addresses the issues.

You could have posted a patch and then asked me to review your portion of the patch.



---

archive/issue_comments_033513.json:
```json
{
    "body": "Attachment [trac_4524-2.patch](tarball://root/attachments/some-uuid/ticket4524/trac_4524-2.patch) by @seblabbe created at 2009-01-24 16:58:35\n\nPositive review.",
    "created_at": "2009-01-24T16:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33513",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_4524-2.patch](tarball://root/attachments/some-uuid/ticket4524/trac_4524-2.patch) by @seblabbe created at 2009-01-24 16:58:35

Positive review.



---

archive/issue_comments_033514.json:
```json
{
    "body": "I think it can be merged in sage 3.3.",
    "created_at": "2009-01-24T16:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33514",
    "user": "https://github.com/seblabbe"
}
```

I think it can be merged in sage 3.3.



---

archive/issue_events_004768.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-24T18:42:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4524#event-4768"
}
```



---

archive/issue_comments_033515.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T18:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_033516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
