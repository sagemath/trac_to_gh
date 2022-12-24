# Issue 5178: [with patch; needs review] change LLL_gram to work with Gram matrices with not-necessarily integer entries

archive/issues_005178.json:
```json
{
    "body": "Assignee: was\n\nCC:  boothby craigcitro cremona kohel mabshoff malb ncalexan slelievre tornaria was\n\nThis patch changes LLL_gram to work with Gram matrices with not-necessarily integer entries.  Also it fixes several \"non-optimal\" coding issues both in the old implementation and the doctests.  For example, instead of computing U.det() to determine if the unimodular A has det -1 or 1, we just compute A.change_ring(GF(3)).det(), which is much faster. \n\nChanging LLL_gram to work for nonintegral gram matrices is critical for applications to computing class groups for the course I'm teaching right now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5178\n\n",
    "created_at": "2009-02-04T18:23:08Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.2",
    "title": "[with patch; needs review] change LLL_gram to work with Gram matrices with not-necessarily integer entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5178",
    "user": "was"
}
```
Assignee: was

CC:  boothby craigcitro cremona kohel mabshoff malb ncalexan slelievre tornaria was

This patch changes LLL_gram to work with Gram matrices with not-necessarily integer entries.  Also it fixes several "non-optimal" coding issues both in the old implementation and the doctests.  For example, instead of computing U.det() to determine if the unimodular A has det -1 or 1, we just compute A.change_ring(GF(3)).det(), which is much faster. 

Changing LLL_gram to work for nonintegral gram matrices is critical for applications to computing class groups for the course I'm teaching right now.

Issue created by migration from https://trac.sagemath.org/ticket/5178





---

archive/issue_comments_039688.json:
```json
{
    "body": "Attachment [trac_5178.patch](tarball://root/attachments/some-uuid/ticket5178/trac_5178.patch) by was created at 2009-02-04 18:23:40",
    "created_at": "2009-02-04T18:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39688",
    "user": "was"
}
```

Attachment [trac_5178.patch](tarball://root/attachments/some-uuid/ticket5178/trac_5178.patch) by was created at 2009-02-04 18:23:40



---

archive/issue_comments_039689.json:
```json
{
    "body": "Gonzalo Tornaria sent this review in email to me:\n\n```\nLooks good to me.\n\nHowever, it seems pari is hanging when using lllgram() on some\nmatrices with rational or integer entries; maybe indefinite or\nsemidefinite matrices are the issue.\nMoreover, sage hangs badly on this...\n\nE.g.\n\nsage: pari(\"[1,1;1,1/2]\").qflllgram()\n\n(it also hangs when running equivalent command from gp, Ctrl-C stops\ngp but not sage).\n[equivalent command = qflllgram([1,1,1,1/2])\n\nHowever, using 0.5 instead of 1/2 works ok.\n\nSeems a bug in pari, but it was not exposed in sage's LLL_gram() before.\n\nGonzalo\n```\n\n\nHe does point out that bad things can happen, but that the bugs are in PARI, not the new code attached to this patch.",
    "created_at": "2009-02-05T05:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39689",
    "user": "was"
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

archive/issue_comments_039690.json:
```json
{
    "body": "I reported the bug upstream.  Is Gonzalo's +1 good enough?  I'm not really comfortable with LLL enough to sign off on this.",
    "created_at": "2009-02-06T06:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39690",
    "user": "boothby"
}
```

I reported the bug upstream.  Is Gonzalo's +1 good enough?  I'm not really comfortable with LLL enough to sign off on this.



---

archive/issue_comments_039691.json:
```json
{
    "body": "Email from Bill Allombert in response to the bug:\n\n\n```\nHello,\nThis problem does not occurs with PARI 2.4.3.\nThis seems to be another instance of bug #505 which was fixed in\nPARI 2.4.1 as\n\n 1- qflll / qflllgram (t_MAT with t_FRAC entries) would not reduce to\n    the integer case (--> insufficient precision, SEGV) [#505]\n\nThe fix should probably be backported.\n\nThanks for your bug report,\nBill\n```\n",
    "created_at": "2009-02-06T17:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39691",
    "user": "boothby"
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

archive/issue_comments_039692.json:
```json
{
    "body": "So, it this a positive review then? \n\nNick did ping me last night about updating to pari 2.4.3svn sources and it seems that we don't really have a choice any more. But this issue should be raised on sage-nt I guess.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T20:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39692",
    "user": "mabshoff"
}
```

So, it this a positive review then? 

Nick did ping me last night about updating to pari 2.4.3svn sources and it seems that we don't really have a choice any more. But this issue should be raised on sage-nt I guess.

Cheers,

Michael



---

archive/issue_comments_039693.json:
```json
{
    "body": "Can we get some movement on this?  I don't think an updated pari is happening anytime soon but it would be nice to close this.",
    "created_at": "2009-06-04T21:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39693",
    "user": "ncalexan"
}
```

Can we get some movement on this?  I don't think an updated pari is happening anytime soon but it would be nice to close this.



---

archive/issue_comments_039694.json:
```json
{
    "body": "This looks good. The only objection I have is that the documentation isn't correctly formatted for sphinx -- in particular, the various sections of the docstring (like `EXAMPLES`) should have a double colon, and there should be more blank lines to get things to format correctly. Also, one or two more examples with noninteger entries in the docstring wouldn't hurt, if you're already there. Maybe something from a class group computation, even if it requires `# long`?",
    "created_at": "2009-06-20T08:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39694",
    "user": "craigcitro"
}
```

This looks good. The only objection I have is that the documentation isn't correctly formatted for sphinx -- in particular, the various sections of the docstring (like `EXAMPLES`) should have a double colon, and there should be more blank lines to get things to format correctly. Also, one or two more examples with noninteger entries in the docstring wouldn't hurt, if you're already there. Maybe something from a class group computation, even if it requires `# long`?



---

archive/issue_comments_039695.json:
```json
{
    "body": "Just got an email from Bill Allombert regarding this bug:\n\n\n```\nHello,\nPARI 2.5.0-stable was released with a fix for this problem,\nclosing this report.\n\nThanks for using our bug tracking system,\nCheers,\nBill.\n```\n",
    "created_at": "2011-06-23T23:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39695",
    "user": "boothby"
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

archive/issue_comments_039696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-23T23:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39696",
    "user": "boothby"
}
```

Resolution: fixed



---

archive/issue_comments_039697.json:
```json
{
    "body": "oops, didn't realize changing the \"upstream\" field would close the ticket",
    "created_at": "2011-06-24T03:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39697",
    "user": "boothby"
}
```

oops, didn't realize changing the "upstream" field would close the ticket



---

archive/issue_comments_039698.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-06-24T03:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39698",
    "user": "boothby"
}
```

Changing status from closed to new.



---

archive/issue_comments_039699.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-06-24T03:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39699",
    "user": "boothby"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039700.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-24T03:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39700",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039701.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-24T03:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39701",
    "user": "boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_039702.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-09-18T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39702",
    "user": "slelievre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039703.json:
```json
{
    "body": "Changing keywords from \"\" to \"LLL, Gram\".",
    "created_at": "2020-09-18T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39703",
    "user": "slelievre"
}
```

Changing keywords from "" to "LLL, Gram".



---

archive/issue_comments_039704.json:
```json
{
    "body": "Turned the 2009 patch into a branch based on Sage 9.2.beta12.\n\nPlease review.\n----\nNew commits:",
    "created_at": "2020-09-18T09:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39704",
    "user": "slelievre"
}
```

Turned the 2009 patch into a branch based on Sage 9.2.beta12.

Please review.
----
New commits:



---

archive/issue_comments_039705.json:
```json
{
    "body": "Looks good to me",
    "created_at": "2020-09-18T10:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39705",
    "user": "malb"
}
```

Looks good to me



---

archive/issue_comments_039706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-09-18T10:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39706",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039707.json:
```json
{
    "body": "Replying to [comment:6 craigcitro]:\n> This looks good. The only objection I have is that the documentation\n> isn't correctly formatted for sphinx -- in particular, the various\n> sections of the docstring (like `EXAMPLES`) should have a double colon,\n> and there should be more blank lines to get things to format correctly.\n\nAddressed in the branch.\n\n> Also, one or two more examples with noninteger entries in the\n> docstring wouldn't hurt, if you're already there. Maybe something\n> from a class group computation, even if it requires `# long`?\n\nI agree. William, would you have a few examples from your course?\n\nSince Martin already gave positive review (thanks!),\nadding examples could be done in a follow-up ticket.",
    "created_at": "2020-09-18T10:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39707",
    "user": "slelievre"
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

archive/issue_comments_039708.json:
```json
{
    "body": "Possible follow-up improvements:\n\n- Add optional parameter `force_orientation_preserving=True`.\n  Setting it to `False` when calling the method would skip\n  the last part (that checks whether the determinant is 1 or -1\n  and changes the sign of the last column in case it is -1)\n  and save some time.\n\n- Maybe PARI has an option to force returning a determinant 1\n  transformation matrix? If so, use it.\n\n- Add cross-references in the documentation to/from any similar\n  methods, e.g. provided by fplll.",
    "created_at": "2020-09-18T10:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39708",
    "user": "slelievre"
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

archive/issue_comments_039709.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-09-23T21:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39709",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_039710.json:
```json
{
    "body": "Follow-up at #30678.",
    "created_at": "2020-09-28T10:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5178#issuecomment-39710",
    "user": "slelievre"
}
```

Follow-up at #30678.
