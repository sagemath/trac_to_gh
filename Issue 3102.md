# Issue 3102: debugging output in p-adics with print mode "digits"

archive/issues_003102.json:
```json
{
    "body": "Assignee: mabshoff\n\nSomeone apparently forgot to uncomment some debugging code:\n\n\n```\nsage: K = Qp(7, print_mode=\"digits\")\nsage: K(1/2)     # ok\n...33333333333333333334\nsage: K(1/42)    # hmmmmmmmm\n['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6']\n-1\n['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']\n['6']\n...5555555555555555555.6\nsage: \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3102\n\n",
    "created_at": "2008-05-04T21:54:08Z",
    "labels": [
        "component: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "debugging output in p-adics with print mode \"digits\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3102",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: mabshoff

Someone apparently forgot to uncomment some debugging code:


```
sage: K = Qp(7, print_mode="digits")
sage: K(1/2)     # ok
...33333333333333333334
sage: K(1/42)    # hmmmmmmmm
['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6']
-1
['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']
['6']
...5555555555555555555.6
sage: 
```



Issue created by migration from https://trac.sagemath.org/ticket/3102





---

archive/issue_comments_021377.json:
```json
{
    "body": "Changing assignee from mabshoff to somebody.",
    "created_at": "2008-05-04T21:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21377",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from mabshoff to somebody.



---

archive/issue_comments_021378.json:
```json
{
    "body": "Changing component from Cygwin to basic arithmetic.",
    "created_at": "2008-05-04T21:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21378",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing component from Cygwin to basic arithmetic.



---

archive/issue_comments_021379.json:
```json
{
    "body": "Attachment [trac_3102.patch](tarball://root/attachments/some-uuid/ticket3102/trac_3102.patch) by @garyfurnish created at 2008-09-07 22:04:16",
    "created_at": "2008-09-07T22:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21379",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3102.patch](tarball://root/attachments/some-uuid/ticket3102/trac_3102.patch) by @garyfurnish created at 2008-09-07 22:04:16



---

archive/issue_comments_021380.json:
```json
{
    "body": "Well, the patch applied fine and doctests pass.  BUT  when I manually type in\n\n```\n            sage: K = Qp(7, print_mode=\"digits\")\n            sage: repr(K(1/2))\n```\n\nI do NOT get what the doctest says I should:\n\n```\n            '...3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|4'\n```\n\nbut instead I get this:\n\n```\n'...33333333333333333334'\n```\n\n\nI don't know why the vertial lines a re missing, or whether they should be there;  but I do know that the doctester ignores what comes after three dots ... so any p-adics print mode which includes the dots is going to be rather hard to doctest.",
    "created_at": "2008-09-08T20:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21380",
    "user": "https://github.com/JohnCremona"
}
```

Well, the patch applied fine and doctests pass.  BUT  when I manually type in

```
            sage: K = Qp(7, print_mode="digits")
            sage: repr(K(1/2))
```

I do NOT get what the doctest says I should:

```
            '...3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|3|4'
```

but instead I get this:

```
'...33333333333333333334'
```


I don't know why the vertial lines a re missing, or whether they should be there;  but I do know that the doctester ignores what comes after three dots ... so any p-adics print mode which includes the dots is going to be rather hard to doctest.



---

archive/issue_comments_021381.json:
```json
{
    "body": "I think this is working as intended -- The other p-adic print statements also have the lines (see line 68).  It seems to be something specific to testing the printer so that it generates different output in doctests and runtime.  It looks like it may be enabling the bars global state early in the tests and never disabling it.",
    "created_at": "2008-09-09T00:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21381",
    "user": "https://github.com/garyfurnish"
}
```

I think this is working as intended -- The other p-adic print statements also have the lines (see line 68).  It seems to be something specific to testing the printer so that it generates different output in doctests and runtime.  It looks like it may be enabling the bars global state early in the tests and never disabling it.



---

archive/issue_comments_021382.json:
```json
{
    "body": "But in line 68 you have just set the print-mode to \"bars\", while here you have set the mode to \"digits\".\n\nI just don't understand the concept of output being different during doctests and runtime!\n\nRegarding your last sentence: each test should be independent of earlier ones surely, starting in a separate Sage session?  How can it be correct to explicitly set the print_mode to \"digits\" but have a doctest showing that apparantly \"bars\" is output?\n\nI still find this too confusing.",
    "created_at": "2008-09-09T08:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21382",
    "user": "https://github.com/JohnCremona"
}
```

But in line 68 you have just set the print-mode to "bars", while here you have set the mode to "digits".

I just don't understand the concept of output being different during doctests and runtime!

Regarding your last sentence: each test should be independent of earlier ones surely, starting in a separate Sage session?  How can it be correct to explicitly set the print_mode to "digits" but have a doctest showing that apparantly "bars" is output?

I still find this too confusing.



---

archive/issue_comments_021383.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> But in line 68 you have just set the print-mode to \"bars\", while here you have set the mode to \"digits\".\n> \n> I just don't understand the concept of output being different during doctests and runtime!\n> \n> Regarding your last sentence: each test should be independent of earlier ones surely, starting in a separate Sage session?  How can it be correct to explicitly set the print_mode to \"digits\" but have a doctest showing that apparantly \"bars\" is output?\n> \n> I still find this too confusing.\n\n\nJohn Cremona is definitely right here.",
    "created_at": "2008-09-24T17:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21383",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:6 cremona]:
> But in line 68 you have just set the print-mode to "bars", while here you have set the mode to "digits".
> 
> I just don't understand the concept of output being different during doctests and runtime!
> 
> Regarding your last sentence: each test should be independent of earlier ones surely, starting in a separate Sage session?  How can it be correct to explicitly set the print_mode to "digits" but have a doctest showing that apparantly "bars" is output?
> 
> I still find this too confusing.


John Cremona is definitely right here.



---

archive/issue_comments_021384.json:
```json
{
    "body": "Attachment [sage-3102.patch](tarball://root/attachments/some-uuid/ticket3102/sage-3102.patch) by @williamstein created at 2008-11-27 07:01:34\n\nfollowup -- apply the above patch *and* this one.",
    "created_at": "2008-11-27T07:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21384",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3102.patch](tarball://root/attachments/some-uuid/ticket3102/sage-3102.patch) by @williamstein created at 2008-11-27 07:01:34

followup -- apply the above patch *and* this one.



---

archive/issue_comments_021385.json:
```json
{
    "body": "I attached a tiny patch that addresses and clarifies some of the issues discussed above.  See #4637 for a ticket for the bug that the above exposes.",
    "created_at": "2008-11-27T07:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21385",
    "user": "https://github.com/williamstein"
}
```

I attached a tiny patch that addresses and clarifies some of the issues discussed above.  See #4637 for a ticket for the bug that the above exposes.



---

archive/issue_comments_021386.json:
```json
{
    "body": "Second patch looks good, too.",
    "created_at": "2008-11-27T07:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21386",
    "user": "https://github.com/craigcitro"
}
```

Second patch looks good, too.



---

archive/issue_events_003318.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T07:31:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3102#event-3318"
}
```



---

archive/issue_comments_021387.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T07:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.1.rc0



---

archive/issue_comments_021388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T07:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3102#issuecomment-21388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
