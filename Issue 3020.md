# Issue 3020: Finite Fields of characteristic 2 slow to construct

archive/issues_003020.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb cwitty\n\nKeywords: finite fields\n\nConstruction of GF(2^n) is very slow for n>=16 (out of the givaro range), owing to slow search for suitable defining irreducible polynomials over GF(2).  Also the polynomials produced are dense.\n\nA new function GF2X_sparse_irreducible() has been added, using a precomputed lookup table for degrees up to 2048 (taken from NTL's source code) and otherwise looking for tri- and pentanomials first.\n\nPatch attached, based on 3.0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3020\n\n",
    "created_at": "2008-04-24T21:40:17Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Finite Fields of characteristic 2 slow to construct",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3020",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

CC:  @malb cwitty

Keywords: finite fields

Construction of GF(2^n) is very slow for n>=16 (out of the givaro range), owing to slow search for suitable defining irreducible polynomials over GF(2).  Also the polynomials produced are dense.

A new function GF2X_sparse_irreducible() has been added, using a precomputed lookup table for degrees up to 2048 (taken from NTL's source code) and otherwise looking for tri- and pentanomials first.

Patch attached, based on 3.0.

Issue created by migration from https://trac.sagemath.org/ticket/3020





---

archive/issue_comments_020703.json:
```json
{
    "body": "Attachment [9606.patch](tarball://root/attachments/some-uuid/ticket3020/9606.patch) by @JohnCremona created at 2008-04-24 21:40:33",
    "created_at": "2008-04-24T21:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20703",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [9606.patch](tarball://root/attachments/some-uuid/ticket3020/9606.patch) by @JohnCremona created at 2008-04-24 21:40:33



---

archive/issue_comments_020704.json:
```json
{
    "body": "The patch looks good, some comments though:\n* I'd prefer to have the table in a different file rather than `finite_field.py`, say `gf2x_irred_table.py`?\n* This is table from NTL? Can't we just read in the NTL table automatically?\n* Did you check if each entry is irreducible? I assume so, I just want to make it formally sure.",
    "created_at": "2008-04-24T23:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20704",
    "user": "https://github.com/malb"
}
```

The patch looks good, some comments though:
* I'd prefer to have the table in a different file rather than `finite_field.py`, say `gf2x_irred_table.py`?
* This is table from NTL? Can't we just read in the NTL table automatically?
* Did you check if each entry is irreducible? I assume so, I just want to make it formally sure.



---

archive/issue_comments_020705.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-04-24T23:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20705",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020706.json:
```json
{
    "body": "Changing assignee from tbd to @JohnCremona.",
    "created_at": "2008-04-25T06:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from tbd to @JohnCremona.



---

archive/issue_comments_020707.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> The patch looks good, some comments though:\n>  * I'd prefer to have the table in a different file rather than `finite_field.py`, say `gf2x_irred_table.py`?\n\nOk, I can do that.  If I then put\n\n```\n   import gf2x_irred_table\n```\n\nat the appropriate point in finite_field.py, it would only read it in if the function is called, right?\n\n>  * This is table from NTL? Can't we just read in the NTL table automatically?\n\nThis was intended to be a quick fix.  A better fix (as I originally posted) is to change the NTL wrapping code to use NTL's own function, when creating the field.  At the same time we could just wrap NTL's BuildSparseIrred() function.\n\n>  * Did you check if each entry is irreducible? I assume so, I just want to make it formally sure.\n\nI checked for k<1000 and was intending to do the rest (as you say, to be formally sure), but it takes quite a long time.",
    "created_at": "2008-04-25T08:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20707",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 malb]:
> The patch looks good, some comments though:
>  * I'd prefer to have the table in a different file rather than `finite_field.py`, say `gf2x_irred_table.py`?

Ok, I can do that.  If I then put

```
   import gf2x_irred_table
```

at the appropriate point in finite_field.py, it would only read it in if the function is called, right?

>  * This is table from NTL? Can't we just read in the NTL table automatically?

This was intended to be a quick fix.  A better fix (as I originally posted) is to change the NTL wrapping code to use NTL's own function, when creating the field.  At the same time we could just wrap NTL's BuildSparseIrred() function.

>  * Did you check if each entry is irreducible? I assume so, I just want to make it formally sure.

I checked for k<1000 and was intending to do the rest (as you say, to be formally sure), but it takes quite a long time.



---

archive/issue_comments_020708.json:
```json
{
    "body": "Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3020/9607.patch) by @JohnCremona created at 2008-04-25 08:22:13",
    "created_at": "2008-04-25T08:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20708",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3020/9607.patch) by @JohnCremona created at 2008-04-25 08:22:13



---

archive/issue_comments_020709.json:
```json
{
    "body": "The second patch moves the table to a separate file as recommended.  Apply *both* patches!",
    "created_at": "2008-04-25T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20709",
    "user": "https://github.com/JohnCremona"
}
```

The second patch moves the table to a separate file as recommended.  Apply *both* patches!



---

archive/issue_comments_020710.json:
```json
{
    "body": "I have now checked that all 2048 polynomials in the table are irreducible, using Sage's .is_irreducible() function.  This took a _very_ long time (more than 36 hours to do the last thousand) indicating that some improvement might be possible.  But it's done.",
    "created_at": "2008-04-27T10:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20710",
    "user": "https://github.com/JohnCremona"
}
```

I have now checked that all 2048 polynomials in the table are irreducible, using Sage's .is_irreducible() function.  This took a _very_ long time (more than 36 hours to do the last thousand) indicating that some improvement might be possible.  But it's done.



---

archive/issue_comments_020711.json:
```json
{
    "body": "apply after both the preceding patches",
    "created_at": "2008-04-27T16:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20711",
    "user": "https://github.com/JohnCremona"
}
```

apply after both the preceding patches



---

archive/issue_comments_020712.json:
```json
{
    "body": "Attachment [9608.patch](tarball://root/attachments/some-uuid/ticket3020/9608.patch) by @JohnCremona created at 2008-04-27 16:11:35\n\nTrivial fix to previous, correcting a very stupid Python indentation howler -- which meant that for all n for which the tabulated irreducib;e was a trinomial, it did not return the table poly but searched for one.",
    "created_at": "2008-04-27T16:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20712",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [9608.patch](tarball://root/attachments/some-uuid/ticket3020/9608.patch) by @JohnCremona created at 2008-04-27 16:11:35

Trivial fix to previous, correcting a very stupid Python indentation howler -- which meant that for all n for which the tabulated irreducib;e was a trinomial, it did not return the table poly but searched for one.



---

archive/issue_comments_020713.json:
```json
{
    "body": "I've attached an alternative implementation which uses NTL directly rather than re-implementing its behaviour in Sage. \n\n`@`John: I hope you don't mind, i.e. I don't step on your toes with that, but since you stated that your patch was a quick fix and we should switch to use NTL eventually, I figured it would be a good idea to do it know. Could you review the patch, i.e. check if it does what you want?\n\n`@`Carl: Somehow the NTL random polynomial generation doesn't obey your randgen framework, any idea why?",
    "created_at": "2008-05-05T21:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20713",
    "user": "https://github.com/malb"
}
```

I've attached an alternative implementation which uses NTL directly rather than re-implementing its behaviour in Sage. 

`@`John: I hope you don't mind, i.e. I don't step on your toes with that, but since you stated that your patch was a quick fix and we should switch to use NTL eventually, I figured it would be a good idea to do it know. Could you review the patch, i.e. check if it does what you want?

`@`Carl: Somehow the NTL random polynomial generation doesn't obey your randgen framework, any idea why?



---

archive/issue_comments_020714.json:
```json
{
    "body": "No problem, I am delighted that someone has done this properly, and only wish that it had been me to do that.  I am off to look at what you have done and test it now...\n\nComments: \n    #  typo in line 147 (spare -> sparse)\n\n    #  l.203-4: I wondered why you call BuildSparseIrred first.  But  I see that NTL's BuildRandomIrred takes a monic irreducible as input and returns another of the same degree, which is rather bizarre, so I guess you had no choice.  \n\nI checked the logic of the new code and am happy with it.\nThe patch applies cleanly to 3.0.1, and all doctests in sage/rings pass.\n\nVerdict: positive review! apart from the typo this patch (just the last one from malb) is good to go.",
    "created_at": "2008-05-06T08:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20714",
    "user": "https://github.com/JohnCremona"
}
```

No problem, I am delighted that someone has done this properly, and only wish that it had been me to do that.  I am off to look at what you have done and test it now...

Comments: 
    #  typo in line 147 (spare -> sparse)

    #  l.203-4: I wondered why you call BuildSparseIrred first.  But  I see that NTL's BuildRandomIrred takes a monic irreducible as input and returns another of the same degree, which is rather bizarre, so I guess you had no choice.  

I checked the logic of the new code and am happy with it.
The patch applies cleanly to 3.0.1, and all doctests in sage/rings pass.

Verdict: positive review! apart from the typo this patch (just the last one from malb) is good to go.



---

archive/issue_comments_020715.json:
```json
{
    "body": "Sorry forgot to change the summary",
    "created_at": "2008-05-06T08:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20715",
    "user": "https://github.com/JohnCremona"
}
```

Sorry forgot to change the summary



---

archive/issue_comments_020716.json:
```json
{
    "body": "Attachment [GF2X_sparse_poly.patch](tarball://root/attachments/some-uuid/ticket3020/GF2X_sparse_poly.patch) by @malb created at 2008-05-06 10:16:34\n\nupdated patch which fixes the typo",
    "created_at": "2008-05-06T10:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20716",
    "user": "https://github.com/malb"
}
```

Attachment [GF2X_sparse_poly.patch](tarball://root/attachments/some-uuid/ticket3020/GF2X_sparse_poly.patch) by @malb created at 2008-05-06 10:16:34

updated patch which fixes the typo



---

archive/issue_comments_020717.json:
```json
{
    "body": "> # typo in line 147 (spare -> sparse) \n\nFixed in updated patch (same patch, overwritten) \n\n> # l.203-4: I wondered why you call BuildSparseIrred first. But\n> I see that NTL's BuildRandomIrred takes a monic irreducible as\n> input and returns another of the same degree, which is rather\n> bizarre, so I guess you had no choice.\n\nexactly, but I'm not an NTL expert.",
    "created_at": "2008-05-06T10:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20717",
    "user": "https://github.com/malb"
}
```

> # typo in line 147 (spare -> sparse) 

Fixed in updated patch (same patch, overwritten) 

> # l.203-4: I wondered why you call BuildSparseIrred first. But
> I see that NTL's BuildRandomIrred takes a monic irreducible as
> input and returns another of the same degree, which is rather
> bizarre, so I guess you had no choice.

exactly, but I'm not an NTL expert.



---

archive/issue_comments_020718.json:
```json
{
    "body": "Hi,\n\nit is my understand now to only apply GF2X_sparse_poly.patch. What is the status of the concern regarding the random state? Was that just a general observation since Carl only covered so many randomness sources by his framework?\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T11:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi,

it is my understand now to only apply GF2X_sparse_poly.patch. What is the status of the concern regarding the random state? Was that just a general observation since Carl only covered so many randomness sources by his framework?

Cheers,

Michael



---

archive/issue_comments_020719.json:
```json
{
    "body": "Replying to [comment:13 mabshoff]:\n> it is my understand now to only apply GF2X_sparse_poly.patch. \n\ncorrect.\n\n> What is the status of the concern regarding the random state? Was that just a \n> general observation since Carl only covered so many randomness sources by his\n> framework?\n\nMy guess is that he covers NTL, but we can always open another ticket and address the issue there.",
    "created_at": "2008-05-06T11:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20719",
    "user": "https://github.com/malb"
}
```

Replying to [comment:13 mabshoff]:
> it is my understand now to only apply GF2X_sparse_poly.patch. 

correct.

> What is the status of the concern regarding the random state? Was that just a 
> general observation since Carl only covered so many randomness sources by his
> framework?

My guess is that he covers NTL, but we can always open another ticket and address the issue there.



---

archive/issue_events_003225.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-06T19:28:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3020#event-3225"
}
```



---

archive/issue_comments_020720.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-06T19:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020721.json:
```json
{
    "body": "Merged GF2X_sparse_poly.patch in Sage 3.0.2.alpha0",
    "created_at": "2008-05-06T19:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3020#issuecomment-20721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged GF2X_sparse_poly.patch in Sage 3.0.2.alpha0
