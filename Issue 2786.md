# Issue 2786: [with spkg] update zn_poly to 0.8

archive/issues_002786.json:
```json
{
    "body": "Assignee: mabshoff\n\nI have made an spkg for `zn_poly` 0.8, please see attached.\n\nCurrently spkg-install runs a test suite (about 10 minutes). This should be disabled in the deployed version. I wasn't quite sure of the right way to do that.\n\nIt may or may not be necessary to touch files in the sage library that depend on `zn_poly` and rebuild:\n\n```\ntouch devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx\ntouch devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob/*.cpp\n```\n\nSo far I have positive build/tune/test reports from mhansen (Ubuntu Gutsy, 64-bit), wstein (osx 10.5.2), ddrake (Ubuntu Hardy, 32 bit), and myself (intel 64 mac OSX 10.4.11, ppc 64 mac OSX 10.4.11, AMD64 linux).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2786\n\n",
    "created_at": "2008-04-03T02:29:11Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with spkg] update zn_poly to 0.8",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2786",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: mabshoff

I have made an spkg for `zn_poly` 0.8, please see attached.

Currently spkg-install runs a test suite (about 10 minutes). This should be disabled in the deployed version. I wasn't quite sure of the right way to do that.

It may or may not be necessary to touch files in the sage library that depend on `zn_poly` and rebuild:

```
touch devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx
touch devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob/*.cpp
```

So far I have positive build/tune/test reports from mhansen (Ubuntu Gutsy, 64-bit), wstein (osx 10.5.2), ddrake (Ubuntu Hardy, 32 bit), and myself (intel 64 mac OSX 10.4.11, ppc 64 mac OSX 10.4.11, AMD64 linux).


Issue created by migration from https://trac.sagemath.org/ticket/2786





---

archive/issue_comments_019098.json:
```json
{
    "body": "Attachment [zn_poly-0.8.spkg](tarball://root/attachments/some-uuid/ticket2786/zn_poly-0.8.spkg) by dmharvey created at 2008-04-03 02:29:41",
    "created_at": "2008-04-03T02:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2786#issuecomment-19098",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [zn_poly-0.8.spkg](tarball://root/attachments/some-uuid/ticket2786/zn_poly-0.8.spkg) by dmharvey created at 2008-04-03 02:29:41



---

archive/issue_comments_019099.json:
```json
{
    "body": "David,\n\nthe spkg looks food and builds fine. Numerous other people in IRC have confirmed that it builds for them, too. But: While the tuning phase is quick it seems that the spkg linked above runs integrity tests which took an extra eleven minutes of cputime on sage.math. While I think this is a good idea for 3.0.alphaX I would recommend that you turn that off before the final release of 3.0. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T15:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2786#issuecomment-19099",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David,

the spkg looks food and builds fine. Numerous other people in IRC have confirmed that it builds for them, too. But: While the tuning phase is quick it seems that the spkg linked above runs integrity tests which took an extra eleven minutes of cputime on sage.math. While I think this is a good idea for 3.0.alphaX I would recommend that you turn that off before the final release of 3.0. Positive review.

Cheers,

Michael



---

archive/issue_comments_019100.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-03T15:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2786#issuecomment-19100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_events_006431.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-03T15:55:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2786#event-6431"
}
```



---

archive/issue_comments_019101.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T15:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2786#issuecomment-19101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019102.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> But: While the tuning phase is quick it seems that the spkg linked above runs integrity tests which took an extra eleven minutes of cputime on sage.math. While I think this is a good idea for 3.0.alphaX I would recommend that you turn that off before the final release of 3.0. Positive review.\n\n\nOf course... I believe I already mentioned this above :-)\n\nQuestion: is there any standardised way to put in test suites like that which run only in alpha releases?",
    "created_at": "2008-04-03T16:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2786#issuecomment-19102",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Replying to [comment:1 mabshoff]:
> But: While the tuning phase is quick it seems that the spkg linked above runs integrity tests which took an extra eleven minutes of cputime on sage.math. While I think this is a good idea for 3.0.alphaX I would recommend that you turn that off before the final release of 3.0. Positive review.


Of course... I believe I already mentioned this above :-)

Question: is there any standardised way to put in test suites like that which run only in alpha releases?



---

archive/issue_comments_019103.json:
```json
{
    "body": "Replying to [comment:3 dmharvey]:\n\n> Of course... I believe I already mentioned this above :-)\n\n\nOops, I didn't read the ticket in detail, I just remembered you asking in IRC about a one minute tuning phase.\n \n> Question: is there any standardised way to put in test suites like that which run only in alpha releases?\n\n\nNope. Maybe we should add spkg-check-alpha, but that would increase build times across the board. Another possibility would be to run spkg-check depending on version number. We should take that over to sage-devel.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T16:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2786#issuecomment-19103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 dmharvey]:

> Of course... I believe I already mentioned this above :-)


Oops, I didn't read the ticket in detail, I just remembered you asking in IRC about a one minute tuning phase.
 
> Question: is there any standardised way to put in test suites like that which run only in alpha releases?


Nope. Maybe we should add spkg-check-alpha, but that would increase build times across the board. Another possibility would be to run spkg-check depending on version number. We should take that over to sage-devel.

Cheers,

Michael
