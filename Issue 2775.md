# Issue 2775: multivariate factoring over some rings gives incorrect results

archive/issues_002775.json:
```json
{
    "body": "Assignee: somebody\n\nThis example is from Genya Zaytman:\n\n\n```\nsage: version()\n'SAGE Version sage-2.11, Release Date: 2008-03-30'\nsage: q = 1073741789\nsage: T.<aa, bb> = PolynomialRing(GF(q))\nsage: f = aa^2 + 12124343*bb*aa + 32434598*bb^2; f\naa^2 + 12124343*aa*bb + 32434598*bb^2\nsage: f.factor()\n(32434598) * (16373350*aa^2 + 437239695*aa*bb + bb^2)\nsage: g = (32434598) * (16373350*aa^2 + 437239695*aa*bb + bb^2); g\naa^2 - 49344938*aa*bb + 32434598*bb^2\nsage: f == g\nFalse\n```\n\n\nMichael Abshoff reports that this is a bug in Singular itself.\n\nSee also\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bb040b4580b44184\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2775\n\n",
    "created_at": "2008-04-02T16:16:26Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "multivariate factoring over some rings gives incorrect results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2775",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

This example is from Genya Zaytman:


```
sage: version()
'SAGE Version sage-2.11, Release Date: 2008-03-30'
sage: q = 1073741789
sage: T.<aa, bb> = PolynomialRing(GF(q))
sage: f = aa^2 + 12124343*bb*aa + 32434598*bb^2; f
aa^2 + 12124343*aa*bb + 32434598*bb^2
sage: f.factor()
(32434598) * (16373350*aa^2 + 437239695*aa*bb + bb^2)
sage: g = (32434598) * (16373350*aa^2 + 437239695*aa*bb + bb^2); g
aa^2 - 49344938*aa*bb + 32434598*bb^2
sage: f == g
False
```


Michael Abshoff reports that this is a bug in Singular itself.

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/bb040b4580b44184


Issue created by migration from https://trac.sagemath.org/ticket/2775





---

archive/issue_comments_019022.json:
```json
{
    "body": "Changing assignee from somebody to tbd.",
    "created_at": "2008-04-03T11:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19022",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to tbd.



---

archive/issue_comments_019023.json:
```json
{
    "body": "Changing component from basic arithmetic to factorization.",
    "created_at": "2008-04-03T11:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from basic arithmetic to factorization.



---

archive/issue_comments_019024.json:
```json
{
    "body": "We got word from the Singular team: My rough translation follows: \n\nOur analysis revealed that the cause is that the characteristic is too big: despite the fact that the Singular kernel can compute with characteristics up to 2<sup>31</sup> since 3-0-0, Factory has a limit of p <2<sup>29</sup> (31 bit for signed int, 2 bit as \"Type indicator\").\nUnfortunately this wasn't tested, since the former limit for Singular was much lower (2<sup>15</sup>).",
    "created_at": "2008-04-04T08:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19024",
    "user": "https://github.com/malb"
}
```

We got word from the Singular team: My rough translation follows: 

Our analysis revealed that the cause is that the characteristic is too big: despite the fact that the Singular kernel can compute with characteristics up to 2<sup>31</sup> since 3-0-0, Factory has a limit of p <2<sup>29</sup> (31 bit for signed int, 2 bit as "Type indicator").
Unfortunately this wasn't tested, since the former limit for Singular was much lower (2<sup>15</sup>).



---

archive/issue_comments_019025.json:
```json
{
    "body": "Replying to [comment:3 malb]:\n> We got word from the Singular team: My rough translation follows: \n> \n> Our analysis revealed that the cause is that the characteristic is too big: despite the fact that the Singular kernel can compute with characteristics up to 2<sup>31</sup> since 3-0-0, Factory has a limit of p <2<sup>29</sup> (31 bit for signed int, 2 bit as \"Type indicator\").\n> Unfortunately this wasn't tested, since the former limit for Singular was much lower (2<sup>15</sup>).\n\nClarification: is \"Factory\" something in Sage, or something in Singular? i.e. is this still a bug (or possibly documentation bug) at their end, or do we just need to stop using Singular when the characteristic gets this big?\n\nAnother question: is it really always 29 bits, or is it going to be 61 bits on a 64-bit machine?",
    "created_at": "2008-04-04T13:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19025",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Replying to [comment:3 malb]:
> We got word from the Singular team: My rough translation follows: 
> 
> Our analysis revealed that the cause is that the characteristic is too big: despite the fact that the Singular kernel can compute with characteristics up to 2<sup>31</sup> since 3-0-0, Factory has a limit of p <2<sup>29</sup> (31 bit for signed int, 2 bit as "Type indicator").
> Unfortunately this wasn't tested, since the former limit for Singular was much lower (2<sup>15</sup>).

Clarification: is "Factory" something in Sage, or something in Singular? i.e. is this still a bug (or possibly documentation bug) at their end, or do we just need to stop using Singular when the characteristic gets this big?

Another question: is it really always 29 bits, or is it going to be 61 bits on a 64-bit machine?



---

archive/issue_comments_019026.json:
```json
{
    "body": "Replying to [comment:4 dmharvey]:\n\n> Clarification: is \"Factory\" something in Sage, or something in Singular? i.e. is this still a bug (or possibly documentation bug) at their end, or do we just need to stop using Singular when the characteristic gets this big?\n\nFactory is a library that is part of Singular and used to do factorization. Other projects like M2 also use it. As you write we need to check the characteristic before passing the polynomial to factory nee Singular and otherwise throw an exception. \n \n> Another question: is it really always 29 bits, or is it going to be 61 bits on a 64-bit machine?\n\nIt seems to be always 29 bits. I tested on sage.math with a 64 bit Singular.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T13:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19026",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 dmharvey]:

> Clarification: is "Factory" something in Sage, or something in Singular? i.e. is this still a bug (or possibly documentation bug) at their end, or do we just need to stop using Singular when the characteristic gets this big?

Factory is a library that is part of Singular and used to do factorization. Other projects like M2 also use it. As you write we need to check the characteristic before passing the polynomial to factory nee Singular and otherwise throw an exception. 
 
> Another question: is it really always 29 bits, or is it going to be 61 bits on a 64-bit machine?

It seems to be always 29 bits. I tested on sage.math with a 64 bit Singular.

Cheers,

Michael



---

archive/issue_comments_019027.json:
```json
{
    "body": "> Clarification: is \"Factory\" something in Sage, or something in Singular? i.e. is\n> this still a bug (or possibly documentation bug) at their end, or do we just need\n> to stop using Singular when the characteristic gets this big?\n\n\"Factory\" is a Singular thing and we need to raise an `Exception` if the user attempts to factor of fields that large. I'll provide a patch later.\n\n> Another question: is it really always 29 bits, or is it going to be 61 bits on a\n> 64-bit machine?\n\nThe word is 29 bits, but I'll check later, too.",
    "created_at": "2008-04-04T13:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19027",
    "user": "https://github.com/malb"
}
```

> Clarification: is "Factory" something in Sage, or something in Singular? i.e. is
> this still a bug (or possibly documentation bug) at their end, or do we just need
> to stop using Singular when the characteristic gets this big?

"Factory" is a Singular thing and we need to raise an `Exception` if the user attempts to factor of fields that large. I'll provide a patch later.

> Another question: is it really always 29 bits, or is it going to be 61 bits on a
> 64-bit machine?

The word is 29 bits, but I'll check later, too.



---

archive/issue_comments_019028.json:
```json
{
    "body": "Replying to [comment:6 malb]:\n> \"Factory\" is a Singular thing and we need to raise an `Exception` if the user attempts to factor of fields that large. I'll provide a patch later.\n\nUmmm.... do we have any other way to provide the factorisation? For example, Genya (who reported this bug) actually wanted to factor the polynomial :-) I agree that an exception is better than an incorrect result, but it would be nice if.....",
    "created_at": "2008-04-04T13:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19028",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Replying to [comment:6 malb]:
> "Factory" is a Singular thing and we need to raise an `Exception` if the user attempts to factor of fields that large. I'll provide a patch later.

Ummm.... do we have any other way to provide the factorisation? For example, Genya (who reported this bug) actually wanted to factor the polynomial :-) I agree that an exception is better than an incorrect result, but it would be nice if.....



---

archive/issue_comments_019029.json:
```json
{
    "body": "Attachment [trac_2775.patch](tarball://root/attachments/some-uuid/ticket2775/trac_2775.patch) by @malb created at 2008-04-05 21:35:03",
    "created_at": "2008-04-05T21:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19029",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2775.patch](tarball://root/attachments/some-uuid/ticket2775/trac_2775.patch) by @malb created at 2008-04-05 21:35:03



---

archive/issue_comments_019030.json:
```json
{
    "body": "The attached patch raises a `NotImplementedError` if a factorisation with characteristic > 2<sup>29</sup> is attempted.",
    "created_at": "2008-04-05T21:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19030",
    "user": "https://github.com/malb"
}
```

The attached patch raises a `NotImplementedError` if a factorisation with characteristic > 2<sup>29</sup> is attempted.



---

archive/issue_comments_019031.json:
```json
{
    "body": "Patch looks good to me. It adds the original bug report as a doctest. Positive review. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T03:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. It adds the original bug report as a doctest. Positive review. 

Cheers,

Michael



---

archive/issue_events_002963.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-06T03:09:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2775#event-2963"
}
```



---

archive/issue_comments_019032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019033.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2775#issuecomment-19033",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2
