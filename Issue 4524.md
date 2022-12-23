# Issue 4524: interact : incomplete default string in the input box

archive/issues_004524.json:
```json
{
    "body": "Assignee: itolkov\n\nKeywords: input_box\n\nUsing interact in sage 3.1.4, the default string doesn't print completly in the input box. It looks like it prints up to the first character ' found.\nThe folowing example works well \n\n\n```\n@interact\ndef _(a=input_box(default='interact is \"cool\"',type=str,label='Name:')):\n    print a\n```\n\n\nand it puts *interact is \"cool\"* in the input box. But in the next one, \n\n\n```\n@interact\ndef _(a=input_box(default=\"interact is 'cool'\",type=str,label='Name:')):\n    print a\n```\n\n\nthe default string in the input box is incomplete, it puts only *interact is *. So, we don't know if interact is cool or not !\n\nIssue created by migration from https://trac.sagemath.org/ticket/4524\n\n",
    "created_at": "2008-11-14T17:04:23Z",
    "labels": [
        "interact",
        "major",
        "bug"
    ],
    "title": "interact : incomplete default string in the input box",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4524",
    "user": "slabbe"
}
```
Assignee: itolkov

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

archive/issue_comments_033574.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T08:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33574",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_033575.json:
```json
{
    "body": "Changing assignee from itolkov to mhansen.",
    "created_at": "2009-01-23T08:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33575",
    "user": "mhansen"
}
```

Changing assignee from itolkov to mhansen.



---

archive/issue_comments_033576.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T08:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33576",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033577.json:
```json
{
    "body": "First, that is the first time I review a patch. So if you have comment on the way I review, tell me. I also have some questions that I write below as I have them. Moreover, I am not familiar with notebook code at all....so should I let the job to somebody else?\n\nHowever, I applied the patch and I can at least say that the problem I submitted is now fixed which is cool!\n\nThere is a small issue here (double that) :\n\n\n```\nNote that any HTML that that uses quotes around this should use double quotes and not single quotes. \n```\n\n\nAlso, I don't know if you agreee, but I suggest to add the second example below :\n\n\n```\nEXAMPLES: \n    sage: from sage.server.notebook.interact import InteractControl \n    sage: InteractControl('x', '\"cool\"').html_escaped_default_value() \n    '&quot;cool&quot;' \n    sage: InteractControl('x',\"'cool'\").html_escaped_default_value()\n    \"'cool'\"\n```\n\n\nMy last question is : I could have posted a patch for both issues (double that, and the 2nd example). What is commonly done? Do we leave the changes to the patcher?\n\nMy statement is Positive review pending fixes on at least the first of my two doc-suggestions.\n\nThanks for the fix,",
    "created_at": "2009-01-23T18:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33577",
    "user": "slabbe"
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

archive/issue_comments_033578.json:
```json
{
    "body": "I've posted a patch which addresses the issues.\n\nYou could have posted a patch and then asked me to review your portion of the patch.",
    "created_at": "2009-01-24T15:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33578",
    "user": "mhansen"
}
```

I've posted a patch which addresses the issues.

You could have posted a patch and then asked me to review your portion of the patch.



---

archive/issue_comments_033579.json:
```json
{
    "body": "Attachment\n\nPositive review.",
    "created_at": "2009-01-24T16:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33579",
    "user": "slabbe"
}
```

Attachment

Positive review.



---

archive/issue_comments_033580.json:
```json
{
    "body": "I think it can be merged in sage 3.3.",
    "created_at": "2009-01-24T16:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33580",
    "user": "slabbe"
}
```

I think it can be merged in sage 3.3.



---

archive/issue_comments_033581.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T18:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33581",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_033582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4524#issuecomment-33582",
    "user": "mabshoff"
}
```

Resolution: fixed
