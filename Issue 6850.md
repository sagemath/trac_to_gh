# Issue 6850: follow-up to #6531: really add ring.pyx to reference manual

archive/issues_006850.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @loefflerd @JohnCremona\n\nThe patch `trac_6531-restify_generic_ring-rebase.patch` at #6531 was intended to provide documentation and doctests for the module `sage/rings/ring.pyx`. It was also meant to add that module to the reference manual, but doesn't really make any changes to `doc/en/reference/rings.rst` to allow this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6850\n\n",
    "created_at": "2009-08-31T05:44:47Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "follow-up to #6531: really add ring.pyx to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  @loefflerd @JohnCremona

The patch `trac_6531-restify_generic_ring-rebase.patch` at #6531 was intended to provide documentation and doctests for the module `sage/rings/ring.pyx`. It was also meant to add that module to the reference manual, but doesn't really make any changes to `doc/en/reference/rings.rst` to allow this.

Issue created by migration from https://trac.sagemath.org/ticket/6850





---

archive/issue_comments_056386.json:
```json
{
    "body": "Attachment [trac_6850-add-ring.patch](tarball://root/attachments/some-uuid/ticket6850/trac_6850-add-ring.patch) by mvngu created at 2009-08-31 05:48:31\n\ndepends on #6531",
    "created_at": "2009-08-31T05:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6850#issuecomment-56386",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6850-add-ring.patch](tarball://root/attachments/some-uuid/ticket6850/trac_6850-add-ring.patch) by mvngu created at 2009-08-31 05:48:31

depends on #6531



---

archive/issue_comments_056387.json:
```json
{
    "body": "The patch `trac_6850-add-ring.patch` actually adds the module `sage/rings/ring.pyx` to the reference manual and fixes some typos found in that module. It depends on #6531.",
    "created_at": "2009-08-31T05:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6850#issuecomment-56387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_6850-add-ring.patch` actually adds the module `sage/rings/ring.pyx` to the reference manual and fixes some typos found in that module. It depends on #6531.



---

archive/issue_comments_056388.json:
```json
{
    "body": "Sorry, that was my fault -- David's original patch did make the necessary changes to the .rst file but somehow that was carried forward into the patch I made.\n\nThe patch applies and builds fine (on top of the new one at #6531).",
    "created_at": "2009-08-31T11:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6850#issuecomment-56388",
    "user": "https://github.com/JohnCremona"
}
```

Sorry, that was my fault -- David's original patch did make the necessary changes to the .rst file but somehow that was carried forward into the patch I made.

The patch applies and builds fine (on top of the new one at #6531).



---

archive/issue_comments_056389.json:
```json
{
    "body": "Changing keywords from \"\" to \"Rings documentation\".",
    "created_at": "2009-08-31T11:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6850#issuecomment-56389",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "Rings documentation".



---

archive/issue_comments_056390.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-31T11:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6850#issuecomment-56390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007083.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-08-31T11:41:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6850",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6850#event-7083"
}
```
