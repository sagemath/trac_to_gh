# Issue 8802: sqrt() for QQbar and AA should have a parameter "all"

archive/issues_008802.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @robertwb @loefflerd @JohnCremona\n\nThis is inconsistent with other versions of sqrt():\n\n```\nsage: QQbar(2).sqrt()\n1.414213562373095?\nsage: QQbar(2).sqrt(all=True)\n```\n\n\nIn addition, there should be a parameter \"extend\" to handle this:\n\n```\nsage: AA(2).sqrt()\n1.414213562373095?\nsage: AA(-2).sqrt()\n1.414213562373095?*I\n```\n\nIn the second example, we should not return a root in QQbar unless extend=True.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8802\n\n",
    "created_at": "2010-04-28T14:41:11Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "sqrt() for QQbar and AA should have a parameter \"all\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8802",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @aghitza

CC:  @robertwb @loefflerd @JohnCremona

This is inconsistent with other versions of sqrt():

```
sage: QQbar(2).sqrt()
1.414213562373095?
sage: QQbar(2).sqrt(all=True)
```


In addition, there should be a parameter "extend" to handle this:

```
sage: AA(2).sqrt()
1.414213562373095?
sage: AA(-2).sqrt()
1.414213562373095?*I
```

In the second example, we should not return a root in QQbar unless extend=True.

Issue created by migration from https://trac.sagemath.org/ticket/8802





---

archive/issue_comments_080617.json:
```json
{
    "body": "Attachment [trac_8802-sqrt-qqbar.patch](tarball://root/attachments/some-uuid/ticket8802/trac_8802-sqrt-qqbar.patch) by barinder created at 2010-06-07 15:17:16\n\nAdd all and extend parameters to sqrt for QQbar and AA",
    "created_at": "2010-06-07T15:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80617",
    "user": "https://trac.sagemath.org/admin/accounts/users/barinder"
}
```

Attachment [trac_8802-sqrt-qqbar.patch](tarball://root/attachments/some-uuid/ticket8802/trac_8802-sqrt-qqbar.patch) by barinder created at 2010-06-07 15:17:16

Add all and extend parameters to sqrt for QQbar and AA



---

archive/issue_comments_080618.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-07T15:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80618",
    "user": "https://trac.sagemath.org/admin/accounts/users/barinder"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080619.json:
```json
{
    "body": "Patch based on 4.4.2 and works fine on 4.4.3. The two problems identified by cremona have been resolved:\n\n\n```\nsage: QQbar(2).sqrt()\n1.414213562373095?\nsage: QQbar(2).sqrt(all=True)\n[1.414213562373095?, -1.414213562373095?]\n```\n\n\nThe following command \n\n\n```\nsage: AA(-2).sqrt(extend=False)\n```\n \n\nreturns an error, like it should.",
    "created_at": "2010-06-07T15:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80619",
    "user": "https://trac.sagemath.org/admin/accounts/users/barinder"
}
```

Patch based on 4.4.2 and works fine on 4.4.3. The two problems identified by cremona have been resolved:


```
sage: QQbar(2).sqrt()
1.414213562373095?
sage: QQbar(2).sqrt(all=True)
[1.414213562373095?, -1.414213562373095?]
```


The following command 


```
sage: AA(-2).sqrt(extend=False)
```
 

returns an error, like it should.



---

archive/issue_comments_080620.json:
```json
{
    "body": "Mostly looks good. Some minor comments: \n\n* There's a lot of redundancy between the AA and QQbar cases, perhaps it could be consolidated (this isn't that big of a deal though)\n* You normalize the root order in the all=True case, which I think is good, but the same normalization would probably be worth doing for the all=False case too (I'd be happy if it might negate twice to simplify the logic, as that will be relatively cheap).",
    "created_at": "2010-06-07T16:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80620",
    "user": "https://github.com/robertwb"
}
```

Mostly looks good. Some minor comments: 

* There's a lot of redundancy between the AA and QQbar cases, perhaps it could be consolidated (this isn't that big of a deal though)
* You normalize the root order in the all=True case, which I think is good, but the same normalization would probably be worth doing for the all=False case too (I'd be happy if it might negate twice to simplify the logic, as that will be relatively cheap).



---

archive/issue_comments_080621.json:
```json
{
    "body": "Attachment [trac_8802-sqrt-qqbar-v2.patch](tarball://root/attachments/some-uuid/ticket8802/trac_8802-sqrt-qqbar-v2.patch) by barinder created at 2010-06-07 17:33:01\n\nAs before, but addresses the ordering issue raised by robertwb",
    "created_at": "2010-06-07T17:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80621",
    "user": "https://trac.sagemath.org/admin/accounts/users/barinder"
}
```

Attachment [trac_8802-sqrt-qqbar-v2.patch](tarball://root/attachments/some-uuid/ticket8802/trac_8802-sqrt-qqbar-v2.patch) by barinder created at 2010-06-07 17:33:01

As before, but addresses the ordering issue raised by robertwb



---

archive/issue_comments_080622.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-09T13:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80622",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080623.json:
```json
{
    "body": "Attachment [trac_8802-sqrt-qqbar-v3.patch](tarball://root/attachments/some-uuid/ticket8802/trac_8802-sqrt-qqbar-v3.patch) by @JohnCremona created at 2010-06-09 14:50:51\n\nFixed docstring format issues and simplified: applies to 4.4.4.alpha0",
    "created_at": "2010-06-09T14:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80623",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8802-sqrt-qqbar-v3.patch](tarball://root/attachments/some-uuid/ticket8802/trac_8802-sqrt-qqbar-v3.patch) by @JohnCremona created at 2010-06-09 14:50:51

Fixed docstring format issues and simplified: applies to 4.4.4.alpha0



---

archive/issue_comments_080624.json:
```json
{
    "body": "Version 3 of the patch (jointly written by Barinder and John) simplifies the code more and fixes docstring issues.  We removed the sign normalisation code, since the pow function already delivers a normalised result.",
    "created_at": "2010-06-09T14:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80624",
    "user": "https://github.com/JohnCremona"
}
```

Version 3 of the patch (jointly written by Barinder and John) simplifies the code more and fixes docstring issues.  We removed the sign normalisation code, since the pow function already delivers a normalised result.



---

archive/issue_comments_080625.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-09T14:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80625",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080626.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T10:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80626",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080627.json:
```json
{
    "body": "Looks good to me too.",
    "created_at": "2010-06-10T15:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80627",
    "user": "https://github.com/robertwb"
}
```

Looks good to me too.



---

archive/issue_comments_080628.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-11T19:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8802#issuecomment-80628",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021473.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-11T19:16:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8802",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8802#event-21473"
}
```
