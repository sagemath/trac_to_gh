# Issue 5888: quadratic forms added a stupid/broken new function to sage for random integer.  Remove!

archive/issues_005888.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @JohnCremona\n\n\n```\n\n\nOn Thu, Apr 23, 2009 at 11:51 PM, Bill Hart <goodwillhart@googlemail.com> wrote:\n> Yeah, the random_int_upto function looks broken.\n> random_int_upto(2^100) is always divisible by 2^47. Not very random.\n\n\nI've never heard of that function, and expected it to be something you defined.\nI was surprised to find it is in Sage.\n\nThis was some weird crap that Jon Hanke just added to Sage in his big patch (bomb), evidently.\n\nFile:\t\t/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.py\nDefinition:\trandom_int_upto(n)\nSource:\ndef random_int_upto(n):\n    \"\"\"\n    Returns a random integer x satisfying 0 <= x < n.\n\n    EXAMPLES:\n        sage: x = random_int_upto(10) \n        sage: x >= 0\n        True\n        sage: x < 10\n        True\n    \"\"\"\n    return floor(n * random())\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5888\n\n",
    "created_at": "2009-04-24T06:53:32Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "quadratic forms added a stupid/broken new function to sage for random integer.  Remove!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5888",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

CC:  @JohnCremona


```


On Thu, Apr 23, 2009 at 11:51 PM, Bill Hart <goodwillhart@googlemail.com> wrote:
> Yeah, the random_int_upto function looks broken.
> random_int_upto(2^100) is always divisible by 2^47. Not very random.


I've never heard of that function, and expected it to be something you defined.
I was surprised to find it is in Sage.

This was some weird crap that Jon Hanke just added to Sage in his big patch (bomb), evidently.

File:		/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.py
Definition:	random_int_upto(n)
Source:
def random_int_upto(n):
    """
    Returns a random integer x satisfying 0 <= x < n.

    EXAMPLES:
        sage: x = random_int_upto(10) 
        sage: x >= 0
        True
        sage: x < 10
        True
    """
    return floor(n * random())
```


Issue created by migration from https://trac.sagemath.org/ticket/5888





---

archive/issue_comments_046466.json:
```json
{
    "body": "Well, random() returns a python float, so *boom* for anything large. That function should get a max size check, get deprecated and use generic infrastructure. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T07:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5888#issuecomment-46466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, random() returns a python float, so *boom* for anything large. That function should get a max size check, get deprecated and use generic infrastructure. 

Cheers,

Michael



---

archive/issue_comments_046467.json:
```json
{
    "body": "John Cremona fixes this at #5834.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T10:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5888#issuecomment-46467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John Cremona fixes this at #5834.

Cheers,

Michael



---

archive/issue_comments_046468.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-25T16:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5888#issuecomment-46468",
    "user": "https://github.com/jonhanke"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046469.json:
```json
{
    "body": "Changing assignee from somebody to @jonhanke.",
    "created_at": "2009-04-25T16:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5888#issuecomment-46469",
    "user": "https://github.com/jonhanke"
}
```

Changing assignee from somebody to @jonhanke.



---

archive/issue_comments_046470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T18:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5888#issuecomment-46470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046471.json:
```json
{
    "body": "This has been fixed in Sage 4.0.alpha0 via #5834.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T18:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5888#issuecomment-46471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed in Sage 4.0.alpha0 via #5834.

Cheers,

Michael
