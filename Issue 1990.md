# Issue 1990: ZZ.random_element() -- never returns 0 and typos/nonsense in docstrings

archive/issues_001990.json:
```json
{
    "body": "Assignee: somebody\n\n1. ZZ.random_element() never returns 0. This is a bug.\n\n2. \"ZZ.random_element() -- return an integer over the natrual distribution $Pr(n) = 1/2|n|(|n|+1)$.\"  This contains a typo \"natrual\".  Also the formula doesn't make any sense.  What's in the numerator / denominator?  What does it mean at 0?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1990\n\n",
    "created_at": "2008-01-31T03:45:39Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "ZZ.random_element() -- never returns 0 and typos/nonsense in docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1990",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

1. ZZ.random_element() never returns 0. This is a bug.

2. "ZZ.random_element() -- return an integer over the natrual distribution $Pr(n) = 1/2|n|(|n|+1)$."  This contains a typo "natrual".  Also the formula doesn't make any sense.  What's in the numerator / denominator?  What does it mean at 0?

Issue created by migration from https://trac.sagemath.org/ticket/1990





---

archive/issue_comments_012855.json:
```json
{
    "body": "\n```\n[10:40pm] william_stein: the doc for ZZ.random_element is:\"ZZ.random_element() -- return an integer over the natrual distribution $Pr(n) = 1/2|n|(|n|+1)$.\"\n[10:40pm] kedlaya: if you really picked a random element of Z, would it ever be 0?\n[10:40pm] william_stein: kedlaya -- there is a documented distribution.\n[10:40pm] kedlaya: oh, ok.\n[10:41pm] william_stein: I don't even know what \"$Pr(n) = 1/2|n|(|n|+1)$.\" means.\n[10:46pm] kedlaya: you mean because of bad parentheses?\n[10:46pm] william_stein: yes\n[10:47pm] kedlaya: and the fact that it doesn't make sense at n=0\n[10:47pm] william_stein: yep\n[10:47pm] kedlaya: i guess it means 0 for n = 0, and otherwise 1/(2 |n| (|n| + 1))\n[10:47pm] kedlaya: since that distro does have total measure 1\n[10:48pm] william_stein: that's most likely.\n[10:48pm] kedlaya: but who picked that anyway?\n[10:48pm] william_stein: But it is not a good choice.\n[10:48pm] william_stein: I think either Robert Bradshaw or jkantor?\n[10:48pm] kedlaya: i'm not sure what constitutes a good choice.\n[10:48pm] jkantor: not me\n[10:48pm] jkantor: poisson distribution would be good\n[10:48pm] william_stein: jkantor -- I've made this trac #1990...\n[10:49pm] kedlaya: doesn't that still leave a parameter choice? And poisson is only a distro on nonnegative integers.\n[10:49pm] jkantor: your right\n[10:50pm] kedlaya: but other than that, I agree with you. \n[10:50pm] jkantor: about the non-negative, sorry\n[10:50pm] kedlaya: i'd say pick the sign at random, but then I'm not sure what to do with 0\n```\n",
    "created_at": "2008-01-31T04:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12855",
    "user": "https://github.com/williamstein"
}
```


```
[10:40pm] william_stein: the doc for ZZ.random_element is:"ZZ.random_element() -- return an integer over the natrual distribution $Pr(n) = 1/2|n|(|n|+1)$."
[10:40pm] kedlaya: if you really picked a random element of Z, would it ever be 0?
[10:40pm] william_stein: kedlaya -- there is a documented distribution.
[10:40pm] kedlaya: oh, ok.
[10:41pm] william_stein: I don't even know what "$Pr(n) = 1/2|n|(|n|+1)$." means.
[10:46pm] kedlaya: you mean because of bad parentheses?
[10:46pm] william_stein: yes
[10:47pm] kedlaya: and the fact that it doesn't make sense at n=0
[10:47pm] william_stein: yep
[10:47pm] kedlaya: i guess it means 0 for n = 0, and otherwise 1/(2 |n| (|n| + 1))
[10:47pm] kedlaya: since that distro does have total measure 1
[10:48pm] william_stein: that's most likely.
[10:48pm] kedlaya: but who picked that anyway?
[10:48pm] william_stein: But it is not a good choice.
[10:48pm] william_stein: I think either Robert Bradshaw or jkantor?
[10:48pm] kedlaya: i'm not sure what constitutes a good choice.
[10:48pm] jkantor: not me
[10:48pm] jkantor: poisson distribution would be good
[10:48pm] william_stein: jkantor -- I've made this trac #1990...
[10:49pm] kedlaya: doesn't that still leave a parameter choice? And poisson is only a distro on nonnegative integers.
[10:49pm] jkantor: your right
[10:50pm] kedlaya: but other than that, I agree with you. 
[10:50pm] jkantor: about the non-negative, sorry
[10:50pm] kedlaya: i'd say pick the sign at random, but then I'm not sure what to do with 0
```




---

archive/issue_comments_012856.json:
```json
{
    "body": "I was the one that picked this distribution--after soliciting feedback from (a much smaller) sage-devel. A better way to think of this is floor(1/X) where X is a real number uniformly chosen from [-1,1]. \n\nI was looking for a distribution that was:\n\n* Parameterless\n* Reasonably small mean absolute value, with non-negligible probability for large values\n* Unbounded\n* Fast\n\nI'm willing to forgo the first criterion. I figured it was better than a uniform choice out of [-2,-1,0,1,2], though the fact that it never chose 0 did bother me a bit. \n\nThe poisson distribution, multiplied by a random sign, might work, but what choice for a parameter? It is also strange because it would have two \"peaks\" (unless the mean is really small, in which case no large integers would ever be produced in practice).",
    "created_at": "2008-01-31T07:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12856",
    "user": "https://github.com/robertwb"
}
```

I was the one that picked this distribution--after soliciting feedback from (a much smaller) sage-devel. A better way to think of this is floor(1/X) where X is a real number uniformly chosen from [-1,1]. 

I was looking for a distribution that was:

* Parameterless
* Reasonably small mean absolute value, with non-negligible probability for large values
* Unbounded
* Fast

I'm willing to forgo the first criterion. I figured it was better than a uniform choice out of [-2,-1,0,1,2], though the fact that it never chose 0 did bother me a bit. 

The poisson distribution, multiplied by a random sign, might work, but what choice for a parameter? It is also strange because it would have two "peaks" (unless the mean is really small, in which case no large integers would ever be produced in practice).



---

archive/issue_comments_012857.json:
```json
{
    "body": "Absent further discussion on this ticket, I will modify this function so it returns 0 some of the time and improve/correct the docstring.",
    "created_at": "2008-02-14T06:26:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12857",
    "user": "https://github.com/robertwb"
}
```

Absent further discussion on this ticket, I will modify this function so it returns 0 some of the time and improve/correct the docstring.



---

archive/issue_comments_012858.json:
```json
{
    "body": "Attachment [trac1990-zz-random-element.patch](tarball://root/attachments/some-uuid/ticket1990/trac1990-zz-random-element.patch) by cwitty created at 2008-03-29 18:35:19",
    "created_at": "2008-03-29T18:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12858",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac1990-zz-random-element.patch](tarball://root/attachments/some-uuid/ticket1990/trac1990-zz-random-element.patch) by cwitty created at 2008-03-29 18:35:19



---

archive/issue_comments_012859.json:
```json
{
    "body": "Works great and looks good to me. Resolves the problems too (now 0 is returned 20% of the type by default, and it has a much better docstring).",
    "created_at": "2008-03-29T18:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12859",
    "user": "https://github.com/robertwb"
}
```

Works great and looks good to me. Resolves the problems too (now 0 is returned 20% of the type by default, and it has a much better docstring).



---

archive/issue_comments_012860.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T19:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12860",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_012861.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T19:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1990#issuecomment-12861",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
