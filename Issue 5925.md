# Issue 5925: [with patch, positive review] Improve speed of CombinatorialAlgebra.multiply()

archive/issues_005925.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n- Treat the case where _multiply_basis returns a monomial specially, to avoid creating lots of temporary dictionaries.  Speeds things up significantly.\n\n\n- Use z_elt.get(m,ABRzero) to provide a default value.  Faster.\n\n\n- Pull left_c * right_c out of inner loop.  Didn't time this, but it must be faster.\n\n\n- Replace first use of BR with ABR so that BR isn't used twice in the same function for different rings.\n\n\n- Add doctests so the four major cases are all tested locally.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5925\n\n",
    "closed_at": "2009-06-04T19:23:05Z",
    "created_at": "2009-04-29T01:04:40Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] Improve speed of CombinatorialAlgebra.multiply()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5925",
    "user": "https://github.com/jdchristensen"
}
```
Assignee: @mwhansen

CC:  sage-combinat

- Treat the case where _multiply_basis returns a monomial specially, to avoid creating lots of temporary dictionaries.  Speeds things up significantly.


- Use z_elt.get(m,ABRzero) to provide a default value.  Faster.


- Pull left_c * right_c out of inner loop.  Didn't time this, but it must be faster.


- Replace first use of BR with ABR so that BR isn't used twice in the same function for different rings.


- Add doctests so the four major cases are all tested locally.


Issue created by migration from https://trac.sagemath.org/ticket/5925





---

archive/issue_comments_046754.json:
```json
{
    "body": "Attachment [multiply.patch](tarball://root/attachments/some-uuid/ticket5925/multiply.patch) by @jdchristensen created at 2009-04-29 01:05:18\n\npatch against 3.4",
    "created_at": "2009-04-29T01:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46754",
    "user": "https://github.com/jdchristensen"
}
```

Attachment [multiply.patch](tarball://root/attachments/some-uuid/ticket5925/multiply.patch) by @jdchristensen created at 2009-04-29 01:05:18

patch against 3.4



---

archive/issue_comments_046755.json:
```json
{
    "body": "I'm happy to rebase if needed.\n\nTiming test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:\n\nY=[[1,2,3,4],[5,6]]\ntime eY=e(Y)\ntime eY2=eY*eY\n\nThe second time is the one I'm looking to improve.\n\nBefore patch:\n\nTime: CPU 0.56 s, Wall: 0.75 s\nTime: CPU 1.93 s, Wall: 1.93 s\n\nAfter patch:\n\nTime: CPU 0.56 s, Wall: 0.75 s\nTime: CPU 1.61 s, Wall: 1.61 s\n\nI tested each change separately, and each showed an improvement in the\nsecond time.",
    "created_at": "2009-04-29T01:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46755",
    "user": "https://github.com/jdchristensen"
}
```

I'm happy to rebase if needed.

Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:

Y=[[1,2,3,4],[5,6]]
time eY=e(Y)
time eY2=eY*eY

The second time is the one I'm looking to improve.

Before patch:

Time: CPU 0.56 s, Wall: 0.75 s
Time: CPU 1.93 s, Wall: 1.93 s

After patch:

Time: CPU 0.56 s, Wall: 0.75 s
Time: CPU 1.61 s, Wall: 1.61 s

I tested each change separately, and each showed an improvement in the
second time.



---

archive/issue_events_013890.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T07:11:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5925#event-13890"
}
```



---

archive/issue_comments_046756.json:
```json
{
    "body": "Hi Dan,\n\ntwo things:\n\n* make sure to assign a milestone to each ticket when you open it. In most cases it should be the next release.\n* please add yourself to the account listing at http://trac.sagemath.org/sage_trac/wiki\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T07:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46756",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Dan,

two things:

* make sure to assign a milestone to each ticket when you open it. In most cases it should be the next release.
* please add yourself to the account listing at http://trac.sagemath.org/sage_trac/wiki

Cheers,

Michael



---

archive/issue_events_013891.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T19:23:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5925#event-13891"
}
```



---

archive/issue_comments_046757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46757",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_046758.json:
```json
{
    "body": "Looks good.\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46758",
    "user": "https://github.com/mwhansen"
}
```

Looks good.

Merged in 4.0.1.rc1.



---

archive/issue_comments_046759.json:
```json
{
    "body": "Replying to [comment:1 jdc]:\n> Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:\n> \n> Y=[[1,2,3,4],[5,6]]\n> time eY=e(Y)\n> time eY2=eY*eY\n\n\n\nHi Dan. I'm showcasing the feature of this ticket in the release tour. The above code doesn't look sensible to me, since `time eY=e(Y)` results in a `ValueError` under Sage 4.0 and 4.0.1. Can you post sample code to illustrate the timing improvement introduced by the patch? The code should illustrate this both before and after applying the patch.",
    "created_at": "2009-06-07T06:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:1 jdc]:
> Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:
> 
> Y=[[1,2,3,4],[5,6]]
> time eY=e(Y)
> time eY2=eY*eY



Hi Dan. I'm showcasing the feature of this ticket in the release tour. The above code doesn't look sensible to me, since `time eY=e(Y)` results in a `ValueError` under Sage 4.0 and 4.0.1. Can you post sample code to illustrate the timing improvement introduced by the patch? The code should illustrate this both before and after applying the patch.



---

archive/issue_comments_046760.json:
```json
{
    "body": "Replying to [comment:7 mvngu]:\n> Replying to [comment:1 jdc]:\n> > Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:\n\n\n```\nY=[[1,2,3,4],[5,6]]\ntime eY=e(Y)\ntime eY2=eY*eY\n```\n\n> Hi Dan. I'm showcasing the feature of this ticket in the release tour. The above code doesn't look sensible to me, since `time eY=e(Y)` results in a `ValueError` under Sage 4.0 and 4.0.1. Can you post sample code to illustrate the timing improvement introduced by the patch? The code should illustrate this both before and after applying the patch.\n\n\nDid you try doing:\n\n```\nfrom sage.combinat.symmetric_group_algebra import e\n```\n\nbefore running the above code?  I don't have sage 4.0 or higher installed yet, and I'm about to be offline for about a month, so I'm not going to be able to look into this further for a while.",
    "created_at": "2009-06-08T15:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46760",
    "user": "https://github.com/jdchristensen"
}
```

Replying to [comment:7 mvngu]:
> Replying to [comment:1 jdc]:
> > Timing test on 2.2GHz Core2Duo running 32-bit Ubuntu 8.04:


```
Y=[[1,2,3,4],[5,6]]
time eY=e(Y)
time eY2=eY*eY
```

> Hi Dan. I'm showcasing the feature of this ticket in the release tour. The above code doesn't look sensible to me, since `time eY=e(Y)` results in a `ValueError` under Sage 4.0 and 4.0.1. Can you post sample code to illustrate the timing improvement introduced by the patch? The code should illustrate this both before and after applying the patch.


Did you try doing:

```
from sage.combinat.symmetric_group_algebra import e
```

before running the above code?  I don't have sage 4.0 or higher installed yet, and I'm about to be offline for about a month, so I'm not going to be able to look into this further for a while.



---

archive/issue_comments_046761.json:
```json
{
    "body": "Why the hell was sage-combinat not in CC to that one?\n\nThis change should have gone through the Sage-Combinat server to merge with the changes there.\nBesides CombinatorialAlgebra is deprecated.\n\nNow I get one more conflict to handle.\n\n(anyone complaining about our changes in Sage-Combinat not going into Sage quickly enough is welcome to give a hand\non the review process for #5891).",
    "created_at": "2009-06-09T22:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46761",
    "user": "https://github.com/nthiery"
}
```

Why the hell was sage-combinat not in CC to that one?

This change should have gone through the Sage-Combinat server to merge with the changes there.
Besides CombinatorialAlgebra is deprecated.

Now I get one more conflict to handle.

(anyone complaining about our changes in Sage-Combinat not going into Sage quickly enough is welcome to give a hand
on the review process for #5891).



---

archive/issue_comments_046762.json:
```json
{
    "body": "Hi Nicolas,\n\n> Why the hell was sage-combinat not in CC to that one?\n> \n> This change should have gone through the Sage-Combinat server to merge with the changes there.\n> Besides CombinatorialAlgebra is deprecated.\n> \n\n\nI think Dan (djc) is new to Sage, and I don't know that there's any information anywhere saying that all changes to combinatorics must pass through sage-combinat, or that this is even the policy. I agree it's frustrating, but I don't think Dan is at fault at all. This was probably an overly harsh reply ... so Dan, please don't take it personally, since I'm sure Nicolas didn't intend that. `:)`\n\nOn a related note, I agree that it would be nice if all combinatorics trac tickets got automatically cc'd to sage-combinat, or a separate sage-combinat-trac mailing list. This ticket was set to component: combinatorics; Mike seems to be the owner for that component, but would it be better if we set it to an account whose email address was a sage-combinat mailing list? Then the list would automatically receive notifications of any new tickets with component combinatorics (unless someone set the owner on creation). A better choice would be to set up an email account that was subscribed to sage-trac (which is *every* trac email) and forwarded along anything that had the word \"combinatorics\". This would be pretty trivial to do with a dedicated gmail account, though there's probably an even more lightweight solution out there ...",
    "created_at": "2009-06-09T23:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46762",
    "user": "https://github.com/craigcitro"
}
```

Hi Nicolas,

> Why the hell was sage-combinat not in CC to that one?
> 
> This change should have gone through the Sage-Combinat server to merge with the changes there.
> Besides CombinatorialAlgebra is deprecated.
> 


I think Dan (djc) is new to Sage, and I don't know that there's any information anywhere saying that all changes to combinatorics must pass through sage-combinat, or that this is even the policy. I agree it's frustrating, but I don't think Dan is at fault at all. This was probably an overly harsh reply ... so Dan, please don't take it personally, since I'm sure Nicolas didn't intend that. `:)`

On a related note, I agree that it would be nice if all combinatorics trac tickets got automatically cc'd to sage-combinat, or a separate sage-combinat-trac mailing list. This ticket was set to component: combinatorics; Mike seems to be the owner for that component, but would it be better if we set it to an account whose email address was a sage-combinat mailing list? Then the list would automatically receive notifications of any new tickets with component combinatorics (unless someone set the owner on creation). A better choice would be to set up an email account that was subscribed to sage-trac (which is *every* trac email) and forwarded along anything that had the word "combinatorics". This would be pretty trivial to do with a dedicated gmail account, though there's probably an even more lightweight solution out there ...



---

archive/issue_comments_046763.json:
```json
{
    "body": "Replying to [comment:10 craigcitro]:\n> Hi Nicolas,\n> I think Dan (djc) is new to Sage, and I don't know that there's any information anywhere saying that all changes to combinatorics must pass through sage-combinat, or that this is even the policy. I agree it's frustrating, but I don't think Dan is at fault at all. This was probably an overly harsh reply ... so Dan, please don't take it personally, since I'm sure Nicolas didn't intend that. `:)`\n\n\nYes, thanks Craig for pointing this out. \n\nSorry Dan: My comment was absolutely not targeting you. I definitely appreciate your contribution, and I very much hope to hear from you soon about other parts of the combinat code!\n\nOn the other hand, it's not like noone who handled this patch was aware of Sage-Combinat and CombinatorialAlgebra.\nWell, the point is not to find a culprit. But, with the current pile of patches, the Sage-Combinat server is getting really hard to maintain. So please all be careful (or step to up to maintain it). Thanks!\n\n> On a related note, I agree that it would be nice if all combinatorics trac tickets got automatically cc'd to sage-combinat, or a separate sage-combinat-trac mailing list. This ticket was set to component: combinatorics; Mike seems to be the owner for that component, but would it be better if we set it to an account whose email address was a sage-combinat mailing list? Then the list would automatically receive notifications of any new tickets with component combinatorics (unless someone set the owner on creation). A better choice would be to set up an email account that was subscribed to sage-trac (which is *every* trac email) and forwarded along anything that had the word \"combinatorics\". This would be pretty trivial to do with a dedicated gmail account, though there's probably an even more lightweight solution out there ...\n\n\nYup. There readily is a sage-combinat account, which is forwarded to sage-combinat-commits. Yes, it would be great if any change to the combinatorics component was forwarded there.\n\nCheers",
    "created_at": "2009-06-10T03:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5925#issuecomment-46763",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:10 craigcitro]:
> Hi Nicolas,
> I think Dan (djc) is new to Sage, and I don't know that there's any information anywhere saying that all changes to combinatorics must pass through sage-combinat, or that this is even the policy. I agree it's frustrating, but I don't think Dan is at fault at all. This was probably an overly harsh reply ... so Dan, please don't take it personally, since I'm sure Nicolas didn't intend that. `:)`


Yes, thanks Craig for pointing this out. 

Sorry Dan: My comment was absolutely not targeting you. I definitely appreciate your contribution, and I very much hope to hear from you soon about other parts of the combinat code!

On the other hand, it's not like noone who handled this patch was aware of Sage-Combinat and CombinatorialAlgebra.
Well, the point is not to find a culprit. But, with the current pile of patches, the Sage-Combinat server is getting really hard to maintain. So please all be careful (or step to up to maintain it). Thanks!

> On a related note, I agree that it would be nice if all combinatorics trac tickets got automatically cc'd to sage-combinat, or a separate sage-combinat-trac mailing list. This ticket was set to component: combinatorics; Mike seems to be the owner for that component, but would it be better if we set it to an account whose email address was a sage-combinat mailing list? Then the list would automatically receive notifications of any new tickets with component combinatorics (unless someone set the owner on creation). A better choice would be to set up an email account that was subscribed to sage-trac (which is *every* trac email) and forwarded along anything that had the word "combinatorics". This would be pretty trivial to do with a dedicated gmail account, though there's probably an even more lightweight solution out there ...


Yup. There readily is a sage-combinat account, which is forwarded to sage-combinat-commits. Yes, it would be great if any change to the combinatorics component was forwarded there.

Cheers
