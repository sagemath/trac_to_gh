# Issue 3152: notebook -- improve gap-mode help interface

archive/issues_003152.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nOn 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:\n> Some other minor issues about using GAP within the notebook, under\n> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at\n> the top.  The following things don't work correctly:\n> 0) If I type something that gives an error in GAP, the error\n> message is buried in a python exception/backtrace.\n> \n> 1) If I type \"?SymmetricGroup\" (which works within GAP), all I see\n> is\n> \n>    Help: Showing `Reference: SymmetricGroup'\n>    Page from 104\n> \n> It's similar with other \"?foo\" commands.\n> \n> 2) If I type \"SymmetricGroup?\" and hit tab, it shows me help about\n> sage's wrapped SymmetricGroup function.  I don't think this will\n> be helpful for functions not wrapped by sage.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3152\n\n",
    "created_at": "2008-05-10T21:28:29Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "notebook -- improve gap-mode help interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3152",
    "user": "was"
}
```
Assignee: boothby


```
On 7/26/07, Dan Christensen <jdc@uwo.ca> wrote:
> Some other minor issues about using GAP within the notebook, under
> 2.7.1.  I've put my entire worksheet in GAP mode using the menu at
> the top.  The following things don't work correctly:
> 0) If I type something that gives an error in GAP, the error
> message is buried in a python exception/backtrace.
> 
> 1) If I type "?SymmetricGroup" (which works within GAP), all I see
> is
> 
>    Help: Showing `Reference: SymmetricGroup'
>    Page from 104
> 
> It's similar with other "?foo" commands.
> 
> 2) If I type "SymmetricGroup?" and hit tab, it shows me help about
> sage's wrapped SymmetricGroup function.  I don't think this will
> be helpful for functions not wrapped by sage.
```


Issue created by migration from https://trac.sagemath.org/ticket/3152





---

archive/issue_comments_021857.json:
```json
{
    "body": "#5043 is conceivably related.",
    "created_at": "2012-06-29T02:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3152#issuecomment-21857",
    "user": "kcrisman"
}
```

#5043 is conceivably related.



---

archive/issue_comments_021858.json:
```json
{
    "body": "I just tried with and without the patch for #5043 and 0 and 1 are unchanged.  2 works correctly, but it's not due to the patch at #5043.",
    "created_at": "2012-06-29T07:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3152#issuecomment-21858",
    "user": "iandrus"
}
```

I just tried with and without the patch for #5043 and 0 and 1 are unchanged.  2 works correctly, but it's not due to the patch at #5043.



---

archive/issue_comments_021859.json:
```json
{
    "body": "https://github.com/sagemath/sagenb/issues/317",
    "created_at": "2014-12-19T04:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3152#issuecomment-21859",
    "user": "kcrisman"
}
```

https://github.com/sagemath/sagenb/issues/317



---

archive/issue_comments_021860.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2014-12-19T04:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3152#issuecomment-21860",
    "user": "kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_021861.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3152#issuecomment-21861",
    "user": "boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_021862.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3152#issuecomment-21862",
    "user": "boothby"
}
```

Resolution: invalid
