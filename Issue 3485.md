# Issue 3485: [with patch, request comments, not ready for review] new sage_input function gives a sequence of commands to reproduce sage values

archive/issues_003485.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  ncalexan wstein\n\nThis patch creates a new sage_input function, that does things like this:\n\n```\nsage: sage_input((polygen(GF(3))+1)^4)\n\nR.<x> = GF(3)[]\nx^4 + x^3 + x + 1\n```\n\n\nI am not done writing docstrings and doctests, so the patch is not ready for review; but any comments on the general approach would be appreciated.  (Also, sage_input is implemented for only a few types; but I picked \"complicated\" types, so I think the underlying framework is ready to go.)\n\nThis patch depends on #3484.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3485\n\n",
    "created_at": "2008-06-20T08:18:11Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, request comments, not ready for review] new sage_input function gives a sequence of commands to reproduce sage values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3485",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  ncalexan wstein

This patch creates a new sage_input function, that does things like this:

```
sage: sage_input((polygen(GF(3))+1)^4)

R.<x> = GF(3)[]
x^4 + x^3 + x + 1
```


I am not done writing docstrings and doctests, so the patch is not ready for review; but any comments on the general approach would be appreciated.  (Also, sage_input is implemented for only a few types; but I picked "complicated" types, so I think the underlying framework is ready to go.)

This patch depends on #3484.

Issue created by migration from https://trac.sagemath.org/ticket/3485





---

archive/issue_comments_024561.json:
```json
{
    "body": "Attachment [trac3485-sage_input.patch](tarball://root/attachments/some-uuid/ticket3485/trac3485-sage_input.patch) by cwitty created at 2008-06-27 02:55:39",
    "created_at": "2008-06-27T02:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24561",
    "user": "cwitty"
}
```

Attachment [trac3485-sage_input.patch](tarball://root/attachments/some-uuid/ticket3485/trac3485-sage_input.patch) by cwitty created at 2008-06-27 02:55:39



---

archive/issue_comments_024562.json:
```json
{
    "body": "Attachment [trac3485-sage_input-v2.patch](tarball://root/attachments/some-uuid/ticket3485/trac3485-sage_input-v2.patch) by cwitty created at 2008-06-27 02:58:15",
    "created_at": "2008-06-27T02:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24562",
    "user": "cwitty"
}
```

Attachment [trac3485-sage_input-v2.patch](tarball://root/attachments/some-uuid/ticket3485/trac3485-sage_input-v2.patch) by cwitty created at 2008-06-27 02:58:15



---

archive/issue_comments_024563.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-06T10:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24563",
    "user": "mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024564.json:
```json
{
    "body": "I will ping somebody to review this patch and #3484 soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T10:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24564",
    "user": "mabshoff"
}
```

I will ping somebody to review this patch and #3484 soon.

Cheers,

Michael



---

archive/issue_comments_024565.json:
```json
{
    "body": "REFEREE REPORT:\n\n* My god, this is some of the most beautiful and well documented systematic code I've ever soon.  I have no problems with any of it.  Damn.  Positive review.",
    "created_at": "2008-08-13T09:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24565",
    "user": "was"
}
```

REFEREE REPORT:

* My god, this is some of the most beautiful and well documented systematic code I've ever soon.  I have no problems with any of it.  Damn.  Positive review.



---

archive/issue_comments_024566.json:
```json
{
    "body": "There is some slight problem applying this:\n\n```\nsage-3.1.alpha2/devel/sage$ patch -p1 --dry-run < trac_3485-sage_input-v2.patch \npatching file sage/misc/all.py\nHunk #1 succeeded at 65 (offset 2 lines).\npatching file sage/misc/sage_input.py\npatching file sage/rings/integer.pyx\nHunk #1 succeeded at 2943 (offset 16 lines).\npatching file sage/rings/integer_mod.pyx\npatching file sage/rings/integer_ring.pyx\nHunk #1 succeeded at 823 with fuzz 2 (offset 8 lines).\npatching file sage/rings/polynomial/polynomial_element.pyx\npatching file sage/rings/polynomial/polynomial_ring.py\nHunk #1 succeeded at 392 with fuzz 2 (offset 17 lines).\npatching file sage/rings/real_mpfr.pyx\nHunk #1 succeeded at 280 (offset 12 lines).\nHunk #2 succeeded at 966 (offset 16 lines).\npatching file sage/rings/ring.pyx\nHunk #1 FAILED at 1505.\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/ring.pyx.rej\n```\n\nIt also seems that only trac3485-sage_input-v2.patch should be applied.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T17:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24566",
    "user": "mabshoff"
}
```

There is some slight problem applying this:

```
sage-3.1.alpha2/devel/sage$ patch -p1 --dry-run < trac_3485-sage_input-v2.patch 
patching file sage/misc/all.py
Hunk #1 succeeded at 65 (offset 2 lines).
patching file sage/misc/sage_input.py
patching file sage/rings/integer.pyx
Hunk #1 succeeded at 2943 (offset 16 lines).
patching file sage/rings/integer_mod.pyx
patching file sage/rings/integer_ring.pyx
Hunk #1 succeeded at 823 with fuzz 2 (offset 8 lines).
patching file sage/rings/polynomial/polynomial_element.pyx
patching file sage/rings/polynomial/polynomial_ring.py
Hunk #1 succeeded at 392 with fuzz 2 (offset 17 lines).
patching file sage/rings/real_mpfr.pyx
Hunk #1 succeeded at 280 (offset 12 lines).
Hunk #2 succeeded at 966 (offset 16 lines).
patching file sage/rings/ring.pyx
Hunk #1 FAILED at 1505.
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/ring.pyx.rej
```

It also seems that only trac3485-sage_input-v2.patch should be applied.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_024567.json:
```json
{
    "body": "Yes, only apply -v2.patch.\n\nThe patch to ring.pyx only adds a new method, so it should be easy to apply by hand.  But if you don't want to do that, I can rebase the patch against alpha1 tonight.",
    "created_at": "2008-08-13T18:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24567",
    "user": "cwitty"
}
```

Yes, only apply -v2.patch.

The patch to ring.pyx only adds a new method, so it should be easy to apply by hand.  But if you don't want to do that, I can rebase the patch against alpha1 tonight.



---

archive/issue_comments_024568.json:
```json
{
    "body": "Attachment [trac3485-sage_input-review-response.patch](tarball://root/attachments/some-uuid/ticket3485/trac3485-sage_input-review-response.patch) by cwitty created at 2008-08-13 18:19:32",
    "created_at": "2008-08-13T18:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24568",
    "user": "cwitty"
}
```

Attachment [trac3485-sage_input-review-response.patch](tarball://root/attachments/some-uuid/ticket3485/trac3485-sage_input-review-response.patch) by cwitty created at 2008-08-13 18:19:32



---

archive/issue_comments_024569.json:
```json
{
    "body": "Merged trac3485-sage_input-v2.patch and trac3485-sage_input-review-response.patch in Sage 3.1.alpha2",
    "created_at": "2008-08-13T18:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24569",
    "user": "mabshoff"
}
```

Merged trac3485-sage_input-v2.patch and trac3485-sage_input-review-response.patch in Sage 3.1.alpha2



---

archive/issue_comments_024570.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T18:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3485#issuecomment-24570",
    "user": "mabshoff"
}
```

Resolution: fixed
