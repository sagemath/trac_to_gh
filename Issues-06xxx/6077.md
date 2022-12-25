# Issue 6077: [with patch, positive review] simplicial complex method for polytopes

archive/issues_006077.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @jhpalmieri\n\nKeywords: polytopes, simplicial\n\nThis just adds a simplicial complex method for the polytope class, which requires lrs to compute a triangulation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6077\n\n",
    "closed_at": "2009-05-21T01:41:00Z",
    "created_at": "2009-05-18T22:06:08Z",
    "labels": [
        "component: geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, positive review] simplicial complex method for polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

CC:  @jhpalmieri

Keywords: polytopes, simplicial

This just adds a simplicial complex method for the polytope class, which requires lrs to compute a triangulation.

Issue created by migration from https://trac.sagemath.org/ticket/6077





---

archive/issue_comments_048275.json:
```json
{
    "body": "Attachment [trac_6077_polysimpcomplex.patch](tarball://root/attachments/some-uuid/ticket6077/trac_6077_polysimpcomplex.patch) by mhampton created at 2009-05-18 22:07:20\n\nadds a simplicial_complex method to polytopes",
    "created_at": "2009-05-18T22:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6077_polysimpcomplex.patch](tarball://root/attachments/some-uuid/ticket6077/trac_6077_polysimpcomplex.patch) by mhampton created at 2009-05-18 22:07:20

adds a simplicial_complex method to polytopes



---

archive/issue_comments_048276.json:
```json
{
    "body": "Mostly good, but needs a few fixes.  I'm attaching a referee's patch which does the following:\n\n- removes the 'verbose' argument, since it's not used\n\n- inserts a warning about this possibly failing if the dimension is larger than 3\n\n- inserts '# optional' flags on the doctests so that they don't fail on machines without lrs installed\n\nmhampton's patch gets a positive review from me; only my patch needs to be reviewed.  With my patch, all tests pass on sage.math (without lrs installed).  With lrs installed, sage -t -optional passes on this file.  (But someone else should probably double-check this.)",
    "created_at": "2009-05-19T03:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48276",
    "user": "https://github.com/jhpalmieri"
}
```

Mostly good, but needs a few fixes.  I'm attaching a referee's patch which does the following:

- removes the 'verbose' argument, since it's not used

- inserts a warning about this possibly failing if the dimension is larger than 3

- inserts '# optional' flags on the doctests so that they don't fail on machines without lrs installed

mhampton's patch gets a positive review from me; only my patch needs to be reviewed.  With my patch, all tests pass on sage.math (without lrs installed).  With lrs installed, sage -t -optional passes on this file.  (But someone else should probably double-check this.)



---

archive/issue_comments_048277.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2009-05-19T03:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48277",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_048278.json:
```json
{
    "body": "Attachment [6077-referee.patch](tarball://root/attachments/some-uuid/ticket6077/6077-referee.patch) by mhampton created at 2009-05-19 18:50:18",
    "created_at": "2009-05-19T18:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48278",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [6077-referee.patch](tarball://root/attachments/some-uuid/ticket6077/6077-referee.patch) by mhampton created at 2009-05-19 18:50:18



---

archive/issue_comments_048279.json:
```json
{
    "body": "Attachment [6077_v2.patch](tarball://root/attachments/some-uuid/ticket6077/6077_v2.patch) by mhampton created at 2009-05-19 19:04:16\n\nThanks for looking at this.  Let me apologize for being somewhat confused about it - I have code in development for doing triangulations with lrs, but currently Sage doesn't use this.  So the warning about possibly not working in high dimensions is good, but I can also delete the check for lrs until I merge that code in.\n\nAnyway, I have added a new patch \"6077_v2.patch\" which does not depend on the others and should account for the above comments and corrections.",
    "created_at": "2009-05-19T19:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [6077_v2.patch](tarball://root/attachments/some-uuid/ticket6077/6077_v2.patch) by mhampton created at 2009-05-19 19:04:16

Thanks for looking at this.  Let me apologize for being somewhat confused about it - I have code in development for doing triangulations with lrs, but currently Sage doesn't use this.  So the warning about possibly not working in high dimensions is good, but I can also delete the check for lrs until I merge that code in.

Anyway, I have added a new patch "6077_v2.patch" which does not depend on the others and should account for the above comments and corrections.



---

archive/issue_comments_048280.json:
```json
{
    "body": "Looks good to me. Passes all tests (without lrs installed, which shouldn't be relevant anymore).",
    "created_at": "2009-05-19T21:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48280",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me. Passes all tests (without lrs installed, which shouldn't be relevant anymore).



---

archive/issue_comments_048281.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T01:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48281",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_014266.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T01:41:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6077#event-14266"
}
```



---

archive/issue_comments_048282.json:
```json
{
    "body": "Merged 6077_v2.patch only in Sage 4.0.rc0. In case that was not intended please let me know.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T01:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6077#issuecomment-48282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 6077_v2.patch only in Sage 4.0.rc0. In case that was not intended please let me know.

Cheers,

Michael



---

archive/issue_events_014267.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-21T01:41:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6077",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6077#event-14267"
}
```
