# Issue 1032: [with patch] Latex'ing variable names is more robust and consistent.

archive/issues_001032.json:
```json
{
    "body": "Assignee: @williamstein\n\nI've refined the latex_variable_name function and called it a few more places to make latex'ing much much better.\n\nPatch attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1032\n\n",
    "created_at": "2007-10-29T20:47:42Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "[with patch] Latex'ing variable names is more robust and consistent.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1032",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

I've refined the latex_variable_name function and called it a few more places to make latex'ing much much better.

Patch attached.

Issue created by migration from https://trac.sagemath.org/ticket/1032





---

archive/issue_comments_006281.json:
```json
{
    "body": "Attachment [latex_names.hg](tarball://root/attachments/some-uuid/ticket1032/latex_names.hg) by jbmohler created at 2007-10-29 20:48:16\n\nthe patch",
    "created_at": "2007-10-29T20:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6281",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [latex_names.hg](tarball://root/attachments/some-uuid/ticket1032/latex_names.hg) by jbmohler created at 2007-10-29 20:48:16

the patch



---

archive/issue_comments_006282.json:
```json
{
    "body": "Please not my worry on sage-devel about maybe this causing problems with singular...",
    "created_at": "2007-10-29T21:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6282",
    "user": "https://github.com/williamstein"
}
```

Please not my worry on sage-devel about maybe this causing problems with singular...



---

archive/issue_comments_006283.json:
```json
{
    "body": "See http://groups.google.com/group/sage-devel/t/89472eb36248053a to be exact.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-29T22:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6283",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See http://groups.google.com/group/sage-devel/t/89472eb36248053a to be exact.

Cheers,

Michael



---

archive/issue_comments_006284.json:
```json
{
    "body": "Towards the bottom of the thread linked by mabshoff, I believe we have William's approval for this patch.\n\nI've personally tested that singular, gp, maxima, and gap all appear to support '_'s in identifiers in their own interpreted languages.  I wanted to do some more extensive tests, but it wasn't quite as easy as I first thought it might be and now that I've tested each of their interpreted languages, I think such further testing does not hold much value.\n\nHence, I think this patch is good to be included (of course, I expect you to be suspicious of that statement -- since I'm the author of the patch!)",
    "created_at": "2007-10-31T15:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6284",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Towards the bottom of the thread linked by mabshoff, I believe we have William's approval for this patch.

I've personally tested that singular, gp, maxima, and gap all appear to support '_'s in identifiers in their own interpreted languages.  I wanted to do some more extensive tests, but it wasn't quite as easy as I first thought it might be and now that I've tested each of their interpreted languages, I think such further testing does not hold much value.

Hence, I think this patch is good to be included (of course, I expect you to be suspicious of that statement -- since I'm the author of the patch!)



---

archive/issue_comments_006285.json:
```json
{
    "body": "I think this is fine to go in.",
    "created_at": "2007-11-01T19:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6285",
    "user": "https://github.com/williamstein"
}
```

I think this is fine to go in.



---

archive/issue_comments_006286.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T23:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6286",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T23:26:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1032#event-2820"
}
```



---

archive/issue_comments_006287.json:
```json
{
    "body": "applied to 2.8.11.rc1 - I might have misunderstood some of the discussion, sorry.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-01T23:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.rc1 - I might have misunderstood some of the discussion, sorry.

Cheers,

Michael



---

archive/issue_comments_006288.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-11-02T00:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6288",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006289.json:
```json
{
    "body": "This breaks a treasured old behavior:\n\n```\n17:48 < mabshoff> Stuff like\n17:48 < mabshoff> File \"polynomial_ring.py\", line 383:\n17:48 < mabshoff>     sage: latex(S)\n17:48 < mabshoff> Expected:\n17:48 < mabshoff>     \\mathbf{Z}[\\alpha_{12}]\n17:48 < mabshoff> Got:\n17:48 < mabshoff>     \\mathbf{Z}[\\text{alpha12}]\n17:48 < mabshoff> Should I just fix those?\n17:48 < wstein> Hey, \\mathbf{Z}[\\text{alpha12}] is pretty damned LAME imho.\n17:48 < mabshoff> Nope, they actually look wrong.\n17:48 < wstein> So joel got rid of the nice behavior that used to be there?\n17:49 < wstein> That's stupid.\n17:49 < wstein> Reject it.\n17:49 < mabshoff> back it out?\n17:49 < wstein> I'm ok with allowing alpha_12, but I don't agree with *forcing* the use \n                of underscores for subscripts.\n17:49 < wstein> The latex form of alpha12 can't have any meaning except $\\alpha_{12}$.\n17:49 < wstein> Yes, I would back it out.\n17:49 < wstein> That's annoying.\n\n```",
    "created_at": "2007-11-02T00:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6289",
    "user": "https://github.com/williamstein"
}
```

This breaks a treasured old behavior:

```
17:48 < mabshoff> Stuff like
17:48 < mabshoff> File "polynomial_ring.py", line 383:
17:48 < mabshoff>     sage: latex(S)
17:48 < mabshoff> Expected:
17:48 < mabshoff>     \mathbf{Z}[\alpha_{12}]
17:48 < mabshoff> Got:
17:48 < mabshoff>     \mathbf{Z}[\text{alpha12}]
17:48 < mabshoff> Should I just fix those?
17:48 < wstein> Hey, \mathbf{Z}[\text{alpha12}] is pretty damned LAME imho.
17:48 < mabshoff> Nope, they actually look wrong.
17:48 < wstein> So joel got rid of the nice behavior that used to be there?
17:49 < wstein> That's stupid.
17:49 < wstein> Reject it.
17:49 < mabshoff> back it out?
17:49 < wstein> I'm ok with allowing alpha_12, but I don't agree with *forcing* the use 
                of underscores for subscripts.
17:49 < wstein> The latex form of alpha12 can't have any meaning except $\alpha_{12}$.
17:49 < wstein> Yes, I would back it out.
17:49 < wstein> That's annoying.

```



---

archive/issue_comments_006290.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-02T00:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6290",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002821.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-02T00:50:31Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1032#event-2821"
}
```



---

archive/issue_comments_006291.json:
```json
{
    "body": "I disagree with the doc-tests above\n\nExhibit A (vanilla 2.8.10):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.10, Release Date: 2007-10-28                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: P.<alpha12>=ZZ[]\nsage: latex(P)\n\\mathbf{Z}[\\text{alpha12}]\n```\n\nExhibit B (my patched version):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: latex\nsage: P.<alpha12>=ZZ[]\nsage: latex(P)\n\\mathbf{Z}[\\alpha_{12}]\n```",
    "created_at": "2007-11-02T11:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6291",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I disagree with the doc-tests above

Exhibit A (vanilla 2.8.10):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10, Release Date: 2007-10-28                      |
| Type notebook() for the GUI, and license() for information.        |
sage: P.<alpha12>=ZZ[]
sage: latex(P)
\mathbf{Z}[\text{alpha12}]
```

Exhibit B (my patched version):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: latex
sage: P.<alpha12>=ZZ[]
sage: latex(P)
\mathbf{Z}[\alpha_{12}]
```



---

archive/issue_comments_006292.json:
```json
{
    "body": "Attachment [latex_names_try2.hg](tarball://root/attachments/some-uuid/ticket1032/latex_names_try2.hg) by jbmohler created at 2007-11-02 18:38:57\n\nthe second patch (needed since hg already says the first patch is in)",
    "created_at": "2007-11-02T18:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6292",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [latex_names_try2.hg](tarball://root/attachments/some-uuid/ticket1032/latex_names_try2.hg) by jbmohler created at 2007-11-02 18:38:57

the second patch (needed since hg already says the first patch is in)



---

archive/issue_comments_006293.json:
```json
{
    "body": "The second patch is just the first patch rehashed because the first patch is already in the tree and hg won't reimport.  There are no other differences.\n\nIt unbundles and passes all doc-tests against 2.8.11.rc1",
    "created_at": "2007-11-02T18:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6293",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

The second patch is just the first patch rehashed because the first patch is already in the tree and hg won't reimport.  There are no other differences.

It unbundles and passes all doc-tests against 2.8.11.rc1



---

archive/issue_events_002822.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-02T19:37:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1032#event-2822"
}
```



---

archive/issue_comments_006294.json:
```json
{
    "body": "applied to 2.8.11.rc2.",
    "created_at": "2007-11-02T19:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.rc2.



---

archive/issue_comments_006295.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T19:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1032#issuecomment-6295",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
