# Issue 4874: [with patch; with positive review] performance issue for generic polynomial rings

archive/issues_004874.json:
```json
{
    "body": "Assignee: somebody\n\n```\nreplacing multiplications by shift in quo_rem found\npolynomial_element_generic.py gives great improvement on this tiny\nexample:\n\nsage: R.<x>=PolynomialRing(GF(4,'a'))\nsage: P=R.random_element(20)\nsage: Q=R.random_element(256)\nsage: time Q % P\n\nbefore:\nCPU time: 0.08 s,  Wall time: 0.08 s\n\nafter:\nCPU time: 0.74 s,  Wall time: 0.74 s\n\nshould be very easy to fix\nthe diff is:\n\n545,549c545,547\n<             aaa = (R.leading_coefficient()/B.leading_coefficient())\n<             bbb = X**(R.degree()-B.degree())\n<             S = aaa * bbb\n<             Q += S\n<             R -= S*B\n---\n>             aaa = P(R.leading_coefficient()/B.leading_coefficient())\n>             Q += aaa.shift(R.degree()-B.degree())\n>             R -= (aaa * B).shift(R.degree()-B.degree())\n\n```\n\nCredit should go to \"yannlaiglechapuy\".\n\nThis came up in sage-devel. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4874\n\n",
    "closed_at": "2009-01-19T03:45:46Z",
    "created_at": "2008-12-24T18:51:32Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; with positive review] performance issue for generic polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4874",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
replacing multiplications by shift in quo_rem found
polynomial_element_generic.py gives great improvement on this tiny
example:

sage: R.<x>=PolynomialRing(GF(4,'a'))
sage: P=R.random_element(20)
sage: Q=R.random_element(256)
sage: time Q % P

before:
CPU time: 0.08 s,  Wall time: 0.08 s

after:
CPU time: 0.74 s,  Wall time: 0.74 s

should be very easy to fix
the diff is:

545,549c545,547
<             aaa = (R.leading_coefficient()/B.leading_coefficient())
<             bbb = X**(R.degree()-B.degree())
<             S = aaa * bbb
<             Q += S
<             R -= S*B
---
>             aaa = P(R.leading_coefficient()/B.leading_coefficient())
>             Q += aaa.shift(R.degree()-B.degree())
>             R -= (aaa * B).shift(R.degree()-B.degree())

```

Credit should go to "yannlaiglechapuy".

This came up in sage-devel. 

Issue created by migration from https://trac.sagemath.org/ticket/4874





---

archive/issue_events_011223.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-24T21:54:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4874#event-11223"
}
```



---

archive/issue_comments_036828.json:
```json
{
    "body": "patch added",
    "created_at": "2009-01-06T19:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4874#issuecomment-36828",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

patch added



---

archive/issue_comments_036829.json:
```json
{
    "body": "Thanks for the patch.\n\nFor the credit situation: \"yannlaiglechapuy\" in real life is \"Yann Laigle-Chapuy\" :)\n\nAssigned to 3.3 since it would be nice to get this in due to its improved performance.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-06T19:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4874#issuecomment-36829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks for the patch.

For the credit situation: "yannlaiglechapuy" in real life is "Yann Laigle-Chapuy" :)

Assigned to 3.3 since it would be nice to get this in due to its improved performance.

Cheers,

Michael



---

archive/issue_events_011224.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-06T19:52:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4874#event-11224"
}
```



---

archive/issue_events_011225.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-06T19:52:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4874#event-11225"
}
```



---

archive/issue_events_011226.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-07T17:14:54Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4874#event-11226"
}
```



---

archive/issue_comments_036830.json:
```json
{
    "body": "Attachment [trac_4874.patch](tarball://root/attachments/some-uuid/ticket4874/trac_4874.patch) by ylchapuy created at 2009-01-18 12:44:38",
    "created_at": "2009-01-18T12:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4874#issuecomment-36830",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_4874.patch](tarball://root/attachments/some-uuid/ticket4874/trac_4874.patch) by ylchapuy created at 2009-01-18 12:44:38



---

archive/issue_comments_036831.json:
```json
{
    "body": "Review: Patch looks good, applies cleanly to 3.2.3, all tests in rings/polynomial pass.  Publish!",
    "created_at": "2009-01-18T17:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4874#issuecomment-36831",
    "user": "https://github.com/JohnCremona"
}
```

Review: Patch looks good, applies cleanly to 3.2.3, all tests in rings/polynomial pass.  Publish!



---

archive/issue_comments_036832.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T03:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4874#issuecomment-36832",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_036833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T03:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4874#issuecomment-36833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011227.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-19T03:45:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4874",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4874#event-11227"
}
```
