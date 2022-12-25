# Issue 4433: [with patch, positive review] Replace factorial with a symbolic version

archive/issues_004433.json:
```json
{
    "body": "Assignee: whuss\n\nThis patch depends on #4432. It replaces the factorial in sage.rings.arith with the symbolic\nversion of #4432 in sage.calculus.calculus.\n\nFor now sage.rings.arith.factorial is just renamed to factorial_numeric, otherwise I got\ncircular imports at Sage startup.\n\nThe patch is against sage-3.2alpha1.\n\nAfter applying this patch plus the patches at #4432 all doctests passed.\n\nA sample session:\n\n```\nsage: gamma(x/2)(x=5)\n3*sqrt(pi)/4\n\nsage: f = factorial(x + factorial(y))\nsage: maxima(f).sage()\nfactorial(factorial(y) + x)\n\nsage: f(y=x)(x=3)\n362880\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4433\n\n",
    "closed_at": "2008-11-28T07:28:57Z",
    "created_at": "2008-11-03T20:07:01Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, positive review] Replace factorial with a symbolic version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4433",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: whuss

This patch depends on #4432. It replaces the factorial in sage.rings.arith with the symbolic
version of #4432 in sage.calculus.calculus.

For now sage.rings.arith.factorial is just renamed to factorial_numeric, otherwise I got
circular imports at Sage startup.

The patch is against sage-3.2alpha1.

After applying this patch plus the patches at #4432 all doctests passed.

A sample session:

```
sage: gamma(x/2)(x=5)
3*sqrt(pi)/4

sage: f = factorial(x + factorial(y))
sage: maxima(f).sage()
factorial(factorial(y) + x)

sage: f(y=x)(x=3)
362880
```



Issue created by migration from https://trac.sagemath.org/ticket/4433





---

archive/issue_comments_032517.json:
```json
{
    "body": "Attachment [factorial.patch](tarball://root/attachments/some-uuid/ticket4433/factorial.patch) by whuss created at 2008-11-03 20:07:42",
    "created_at": "2008-11-03T20:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32517",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [factorial.patch](tarball://root/attachments/some-uuid/ticket4433/factorial.patch) by whuss created at 2008-11-03 20:07:42



---

archive/issue_comments_032518.json:
```json
{
    "body": "Changing assignee from @burcin to whuss.",
    "created_at": "2008-11-03T20:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32518",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing assignee from @burcin to whuss.



---

archive/issue_comments_032519.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-11-04T07:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32519",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_032520.json:
```json
{
    "body": "I don't understand the purpose of converting everything to use the new factorial function defined in calculus.all since none of the existing code needed any of the functionality it provides.",
    "created_at": "2008-11-04T21:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32520",
    "user": "https://github.com/mwhansen"
}
```

I don't understand the purpose of converting everything to use the new factorial function defined in calculus.all since none of the existing code needed any of the functionality it provides.



---

archive/issue_comments_032521.json:
```json
{
    "body": "Attachment [factorial2.patch](tarball://root/attachments/some-uuid/ticket4433/factorial2.patch) by whuss created at 2008-11-05 16:31:22",
    "created_at": "2008-11-05T16:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32521",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [factorial2.patch](tarball://root/attachments/some-uuid/ticket4433/factorial2.patch) by whuss created at 2008-11-05 16:31:22



---

archive/issue_comments_032522.json:
```json
{
    "body": "I wanted to remove the factorial in rings.arith completely, because I think it is confusing\nto have to different factorial functions at the toplevel. Also Sage doesn't do this for the\nother symbolic functions like sin().\n\nIn the previous version rings.arith.factorial_numeric() was just there because I had not yet\nsolved the problem of circular imports at Sage startup.\n\nNow second patch that I just uploaded fixes this problem. Now there is only the factorial\nin calculus.all.\n\nWith both patches applied to sage-3.2alpha1 all doctests pass for me.",
    "created_at": "2008-11-05T16:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32522",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

I wanted to remove the factorial in rings.arith completely, because I think it is confusing
to have to different factorial functions at the toplevel. Also Sage doesn't do this for the
other symbolic functions like sin().

In the previous version rings.arith.factorial_numeric() was just there because I had not yet
solved the problem of circular imports at Sage startup.

Now second patch that I just uploaded fixes this problem. Now there is only the factorial
in calculus.all.

With both patches applied to sage-3.2alpha1 all doctests pass for me.



---

archive/issue_comments_032523.json:
```json
{
    "body": "A couple remarks:\n\n* the first patch removes \"!\" from the list of tokens which we used to ignore up to now. Now it changes meaning to be factorial, but I am not so sure it is a good idea since we use to explicitly forbid it. I don't know the reason why we did that, so see my comment below.\n* the second patch removes fact() [nee factorial_numeric()] from arith.py, but policy is to deprecate removed functions, especially something as simple and long existing like fact() in that file cannot be just removed. See \"def dynkin_diagram(t)\" in combinat/root_system/dynkin_diagram.py for an good example on how to use deprecation in Sage. \n\nEspecially the \"!\" change should be discussed on [sage-devel] since that is a rather fundamental change. I also cannot find a single occurrence of \"!\" in the docstring or tests, but maybe I  overlooked something. *If* the patch is merged with the \"!\" change it needs to be doctests.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T17:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32523",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A couple remarks:

* the first patch removes "!" from the list of tokens which we used to ignore up to now. Now it changes meaning to be factorial, but I am not so sure it is a good idea since we use to explicitly forbid it. I don't know the reason why we did that, so see my comment below.
* the second patch removes fact() [nee factorial_numeric()] from arith.py, but policy is to deprecate removed functions, especially something as simple and long existing like fact() in that file cannot be just removed. See "def dynkin_diagram(t)" in combinat/root_system/dynkin_diagram.py for an good example on how to use deprecation in Sage. 

Especially the "!" change should be discussed on [sage-devel] since that is a rather fundamental change. I also cannot find a single occurrence of "!" in the docstring or tests, but maybe I  overlooked something. *If* the patch is merged with the "!" change it needs to be doctests.

Cheers,

Michael



---

archive/issue_comments_032524.json:
```json
{
    "body": "And a final comment about calculus.py: That file is rather large and messy, so there are various people who think that the file should be split up in the future. \"New symbolics\" might be just what is required there in the long term.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T17:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32524",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And a final comment about calculus.py: That file is rather large and messy, so there are various people who think that the file should be split up in the future. "New symbolics" might be just what is required there in the long term.

Cheers,

Michael



---

archive/issue_comments_032525.json:
```json
{
    "body": "We also shouldn't get rid of the documentation and algorithm keyword in sage.rings.arith.factorial just because.  Overall, I'd recommend just leaving it as is and not importing it to the top level.",
    "created_at": "2008-11-05T17:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32525",
    "user": "https://github.com/mwhansen"
}
```

We also shouldn't get rid of the documentation and algorithm keyword in sage.rings.arith.factorial just because.  Overall, I'd recommend just leaving it as is and not importing it to the top level.



---

archive/issue_comments_032526.json:
```json
{
    "body": "Mike Hansen just pointed out to me in IRC that the \"!\" is used on the Maxima side, so I was wrong and you can disregard my comment about that.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T21:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike Hansen just pointed out to me in IRC that the "!" is used on the Maxima side, so I was wrong and you can disregard my comment about that.

Cheers,

Michael



---

archive/issue_comments_032527.json:
```json
{
    "body": "Attachment [factorial3.patch](tarball://root/attachments/some-uuid/ticket4433/factorial3.patch) by whuss created at 2008-11-06 12:47:37\n\nsupersedes the previous two patches",
    "created_at": "2008-11-06T12:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32527",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [factorial3.patch](tarball://root/attachments/some-uuid/ticket4433/factorial3.patch) by whuss created at 2008-11-06 12:47:37

supersedes the previous two patches



---

archive/issue_comments_032528.json:
```json
{
    "body": "In the new patch sage.rings.arith.factorial is kept but deprecated.",
    "created_at": "2008-11-06T12:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32528",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

In the new patch sage.rings.arith.factorial is kept but deprecated.



---

archive/issue_comments_032529.json:
```json
{
    "body": "The other issues should by fixed by the latest patch for #4432.",
    "created_at": "2008-11-06T13:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32529",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

The other issues should by fixed by the latest patch for #4432.



---

archive/issue_comments_032530.json:
```json
{
    "body": "Since there is a new patch up here this one needs review again.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T09:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since there is a new patch up here this one needs review again.

Cheers,

Michael



---

archive/issue_events_010021.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T07:28:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4433#event-10021"
}
```



---

archive/issue_comments_032531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T07:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032532.json:
```json
{
    "body": "Fixed by #4432 in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T07:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by #4432 in Sage 3.2.1.rc0



---

archive/issue_comments_032533.json:
```json
{
    "body": "The positive review stems from the review of the cumulative patch at #4432.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T07:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4433",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4433#issuecomment-32533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The positive review stems from the review of the cumulative patch at #4432.

Cheers,

Michael
