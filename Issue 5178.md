# Issue 5178: [with patch; needs review] change LLL_gram to work with Gram matrices with not-necessarily integer entries

archive/issues_005178.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  boothby @craigcitro @JohnCremona kohel mabshoff @malb @ncalexan @slel @tornaria @williamstein\n\nThis patch changes LLL_gram to work with Gram matrices with not-necessarily integer entries.  Also it fixes several \"non-optimal\" coding issues both in the old implementation and the doctests.  For example, instead of computing U.det() to determine if the unimodular A has det -1 or 1, we just compute A.change_ring(GF(3)).det(), which is much faster. \n\nChanging LLL_gram to work for nonintegral gram matrices is critical for applications to computing class groups for the course I'm teaching right now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5178\n\n",
    "created_at": "2009-02-04T18:23:08Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.2",
    "title": "[with patch; needs review] change LLL_gram to work with Gram matrices with not-necessarily integer entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5178",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  boothby @craigcitro @JohnCremona kohel mabshoff @malb @ncalexan @slel @tornaria @williamstein

This patch changes LLL_gram to work with Gram matrices with not-necessarily integer entries.  Also it fixes several "non-optimal" coding issues both in the old implementation and the doctests.  For example, instead of computing U.det() to determine if the unimodular A has det -1 or 1, we just compute A.change_ring(GF(3)).det(), which is much faster. 

Changing LLL_gram to work for nonintegral gram matrices is critical for applications to computing class groups for the course I'm teaching right now.

Issue created by migration from https://trac.sagemath.org/ticket/5178





---

archive/issue_comments_039612.json:
```json
{
    "body": "Attachment [trac_5178.patch](tarball://root/attachments/some-uuid/ticket5178/trac_5178.patch) by @williamstein created at 2009-02-04 18:23:40",
    "created_at": "2009-02-04T18:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39612",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5178.patch](tarball://root/attachments/some-uuid/ticket5178/trac_5178.patch) by @williamstein created at 2009-02-04 18:23:40



---

archive/issue_comments_039613.json:
```json
{
    "body": "Gonzalo Tornaria sent this review in email to me:\n\n```\nLooks good to me.\n\nHowever, it seems pari is hanging when using lllgram() on some\nmatrices with rational or integer entries; maybe indefinite or\nsemidefinite matrices are the issue.\nMoreover, sage hangs badly on this...\n\nE.g.\n\nsage: pari(\"[1,1;1,1/2]\").qflllgram()\n\n(it also hangs when running equivalent command from gp, Ctrl-C stops\ngp but not sage).\n[equivalent command = qflllgram([1,1,1,1/2])\n\nHowever, using 0.5 instead of 1/2 works ok.\n\nSeems a bug in pari, but it was not exposed in sage's LLL_gram() before.\n\nGonzalo\n```\n\n\nHe does point out that bad things can happen, but that the bugs are in PARI, not the new code attached to this patch.",
    "created_at": "2009-02-05T05:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39613",
    "user": "https://github.com/williamstein"
}
```

Gonzalo Tornaria sent this review in email to me:

```
Looks good to me.

However, it seems pari is hanging when using lllgram() on some
matrices with rational or integer entries; maybe indefinite or
semidefinite matrices are the issue.
Moreover, sage hangs badly on this...

E.g.

sage: pari("[1,1;1,1/2]").qflllgram()

(it also hangs when running equivalent command from gp, Ctrl-C stops
gp but not sage).
[equivalent command = qflllgram([1,1,1,1/2])

However, using 0.5 instead of 1/2 works ok.

Seems a bug in pari, but it was not exposed in sage's LLL_gram() before.

Gonzalo
```


He does point out that bad things can happen, but that the bugs are in PARI, not the new code attached to this patch.



---

archive/issue_comments_039614.json:
```json
{
    "body": "I reported the bug upstream.  Is Gonzalo's +1 good enough?  I'm not really comfortable with LLL enough to sign off on this.",
    "created_at": "2009-02-06T06:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39614",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I reported the bug upstream.  Is Gonzalo's +1 good enough?  I'm not really comfortable with LLL enough to sign off on this.



---

archive/issue_comments_039615.json:
```json
{
    "body": "Email from Bill Allombert in response to the bug:\n\n\n```\nHello,\nThis problem does not occurs with PARI 2.4.3.\nThis seems to be another instance of bug #505 which was fixed in\nPARI 2.4.1 as\n\n 1- qflll / qflllgram (t_MAT with t_FRAC entries) would not reduce to\n    the integer case (--> insufficient precision, SEGV) [#505]\n\nThe fix should probably be backported.\n\nThanks for your bug report,\nBill\n```\n",
    "created_at": "2009-02-06T17:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39615",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Email from Bill Allombert in response to the bug:


```
Hello,
This problem does not occurs with PARI 2.4.3.
This seems to be another instance of bug #505 which was fixed in
PARI 2.4.1 as

 1- qflll / qflllgram (t_MAT with t_FRAC entries) would not reduce to
    the integer case (--> insufficient precision, SEGV) [#505]

The fix should probably be backported.

Thanks for your bug report,
Bill
```




---

archive/issue_comments_039616.json:
```json
{
    "body": "So, it this a positive review then? \n\nNick did ping me last night about updating to pari 2.4.3svn sources and it seems that we don't really have a choice any more. But this issue should be raised on sage-nt I guess.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T20:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

So, it this a positive review then? 

Nick did ping me last night about updating to pari 2.4.3svn sources and it seems that we don't really have a choice any more. But this issue should be raised on sage-nt I guess.

Cheers,

Michael



---

archive/issue_comments_039617.json:
```json
{
    "body": "Can we get some movement on this?  I don't think an updated pari is happening anytime soon but it would be nice to close this.",
    "created_at": "2009-06-04T21:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39617",
    "user": "https://github.com/ncalexan"
}
```

Can we get some movement on this?  I don't think an updated pari is happening anytime soon but it would be nice to close this.



---

archive/issue_comments_039618.json:
```json
{
    "body": "This looks good. The only objection I have is that the documentation isn't correctly formatted for sphinx -- in particular, the various sections of the docstring (like `EXAMPLES`) should have a double colon, and there should be more blank lines to get things to format correctly. Also, one or two more examples with noninteger entries in the docstring wouldn't hurt, if you're already there. Maybe something from a class group computation, even if it requires `# long`?",
    "created_at": "2009-06-20T08:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39618",
    "user": "https://github.com/craigcitro"
}
```

This looks good. The only objection I have is that the documentation isn't correctly formatted for sphinx -- in particular, the various sections of the docstring (like `EXAMPLES`) should have a double colon, and there should be more blank lines to get things to format correctly. Also, one or two more examples with noninteger entries in the docstring wouldn't hurt, if you're already there. Maybe something from a class group computation, even if it requires `# long`?



---

archive/issue_comments_039619.json:
```json
{
    "body": "Just got an email from Bill Allombert regarding this bug:\n\n\n```\nHello,\nPARI 2.5.0-stable was released with a fix for this problem,\nclosing this report.\n\nThanks for using our bug tracking system,\nCheers,\nBill.\n```\n",
    "created_at": "2011-06-23T23:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39619",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Just got an email from Bill Allombert regarding this bug:


```
Hello,
PARI 2.5.0-stable was released with a fix for this problem,
closing this report.

Thanks for using our bug tracking system,
Cheers,
Bill.
```




---

archive/issue_comments_039620.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-23T23:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39620",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed



---

archive/issue_events_005430.json:
```json
{
    "actor": "boothby",
    "created_at": "2011-06-23T23:48:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5178#event-5430"
}
```



---

archive/issue_comments_039621.json:
```json
{
    "body": "oops, didn't realize changing the \"upstream\" field would close the ticket",
    "created_at": "2011-06-24T03:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39621",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

oops, didn't realize changing the "upstream" field would close the ticket



---

archive/issue_comments_039622.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-06-24T03:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39622",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from closed to new.



---

archive/issue_events_005431.json:
```json
{
    "actor": "boothby",
    "created_at": "2011-06-24T03:40:27Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5178#event-5431"
}
```



---

archive/issue_comments_039623.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-06-24T03:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39623",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039624.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-24T03:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39624",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039625.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-24T03:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39625",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_039626.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-09-18T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39626",
    "user": "https://github.com/slel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039627.json:
```json
{
    "body": "Changing keywords from \"\" to \"LLL, Gram\".",
    "created_at": "2020-09-18T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39627",
    "user": "https://github.com/slel"
}
```

Changing keywords from "" to "LLL, Gram".



---

archive/issue_comments_039628.json:
```json
{
    "body": "Turned the 2009 patch into a branch based on Sage 9.2.beta12.\n\nPlease review.\n----\nNew commits:",
    "created_at": "2020-09-18T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39628",
    "user": "https://github.com/slel"
}
```

Turned the 2009 patch into a branch based on Sage 9.2.beta12.

Please review.
----
New commits:



---

archive/issue_comments_039629.json:
```json
{
    "body": "Looks good to me",
    "created_at": "2020-09-18T10:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39629",
    "user": "https://github.com/malb"
}
```

Looks good to me



---

archive/issue_comments_039630.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-09-18T10:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39630",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039631.json:
```json
{
    "body": "Replying to [comment:6 craigcitro]:\n> This looks good. The only objection I have is that the documentation\n> isn't correctly formatted for sphinx -- in particular, the various\n> sections of the docstring (like `EXAMPLES`) should have a double colon,\n> and there should be more blank lines to get things to format correctly.\n\nAddressed in the branch.\n\n> Also, one or two more examples with noninteger entries in the\n> docstring wouldn't hurt, if you're already there. Maybe something\n> from a class group computation, even if it requires `# long`?\n\nI agree. William, would you have a few examples from your course?\n\nSince Martin already gave positive review (thanks!),\nadding examples could be done in a follow-up ticket.",
    "created_at": "2020-09-18T10:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39631",
    "user": "https://github.com/slel"
}
```

Replying to [comment:6 craigcitro]:
> This looks good. The only objection I have is that the documentation
> isn't correctly formatted for sphinx -- in particular, the various
> sections of the docstring (like `EXAMPLES`) should have a double colon,
> and there should be more blank lines to get things to format correctly.

Addressed in the branch.

> Also, one or two more examples with noninteger entries in the
> docstring wouldn't hurt, if you're already there. Maybe something
> from a class group computation, even if it requires `# long`?

I agree. William, would you have a few examples from your course?

Since Martin already gave positive review (thanks!),
adding examples could be done in a follow-up ticket.



---

archive/issue_comments_039632.json:
```json
{
    "body": "Possible follow-up improvements:\n\n- Add optional parameter `force_orientation_preserving=True`.\n  Setting it to `False` when calling the method would skip\n  the last part (that checks whether the determinant is 1 or -1\n  and changes the sign of the last column in case it is -1)\n  and save some time.\n\n- Maybe PARI has an option to force returning a determinant 1\n  transformation matrix? If so, use it.\n\n- Add cross-references in the documentation to/from any similar\n  methods, e.g. provided by fplll.",
    "created_at": "2020-09-18T10:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39632",
    "user": "https://github.com/slel"
}
```

Possible follow-up improvements:

- Add optional parameter `force_orientation_preserving=True`.
  Setting it to `False` when calling the method would skip
  the last part (that checks whether the determinant is 1 or -1
  and changes the sign of the last column in case it is -1)
  and save some time.

- Maybe PARI has an option to force returning a determinant 1
  transformation matrix? If so, use it.

- Add cross-references in the documentation to/from any similar
  methods, e.g. provided by fplll.



---

archive/issue_events_005432.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2020-09-23T21:27:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5178#event-5432"
}
```



---

archive/issue_comments_039633.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-09-23T21:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39633",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_039634.json:
```json
{
    "body": "Follow-up at #30678.",
    "created_at": "2020-09-28T10:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39634",
    "user": "https://github.com/slel"
}
```

Follow-up at #30678.
