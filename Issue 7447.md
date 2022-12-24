# Issue 7447: SageNB version and install date / time

archive/issues_007447.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was timdumol\n\nOn occasion, it's useful to get the installed SageNB version from inside a Sage process.  Here's a possible API:\n\n```python\nsage: import sagenb.version\nsage: sagenb.version.version\n0.4.3\nsage: sagenb.version.date\n'2009-11-12 11:56:53'\n```\n\nThis is similar to `sage.version`, except this `date` also has the install / package build time.  This could be useful to developers.\n\nReminder: If this merges, update #7390's test report generator, which has a notebook version field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7447\n\n",
    "created_at": "2009-11-12T20:19:39Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "SageNB version and install date / time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7447",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  was timdumol

On occasion, it's useful to get the installed SageNB version from inside a Sage process.  Here's a possible API:

```python
sage: import sagenb.version
sage: sagenb.version.version
0.4.3
sage: sagenb.version.date
'2009-11-12 11:56:53'
```

This is similar to `sage.version`, except this `date` also has the install / package build time.  This could be useful to developers.

Reminder: If this merges, update #7390's test report generator, which has a notebook version field.

Issue created by migration from https://trac.sagemath.org/ticket/7447





---

archive/issue_comments_062686.json:
```json
{
    "body": "Attachment [trac_7447-sagenb_version.patch](tarball://root/attachments/some-uuid/ticket7447/trac_7447-sagenb_version.patch) by mpatel created at 2009-11-13 21:34:02\n\nAdd version and date to new sagenb source distributions.",
    "created_at": "2009-11-13T21:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62686",
    "user": "mpatel"
}
```

Attachment [trac_7447-sagenb_version.patch](tarball://root/attachments/some-uuid/ticket7447/trac_7447-sagenb_version.patch) by mpatel created at 2009-11-13 21:34:02

Add version and date to new sagenb source distributions.



---

archive/issue_comments_062687.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-13T21:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62687",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062688.json:
```json
{
    "body": "Can `distutils` or `setuptools` can do this more simply?",
    "created_at": "2009-11-13T21:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62688",
    "user": "mpatel"
}
```

Can `distutils` or `setuptools` can do this more simply?



---

archive/issue_comments_062689.json:
```json
{
    "body": "See #7467 for a `setuptools` alternative.",
    "created_at": "2009-11-15T08:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62689",
    "user": "mpatel"
}
```

See #7467 for a `setuptools` alternative.



---

archive/issue_comments_062690.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-11-24T08:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62690",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_062691.json:
```json
{
    "body": "Cleaner `setuptools` version.  Depends on #7467.  This patch only.  sagenb repo.",
    "created_at": "2009-12-06T00:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62691",
    "user": "mpatel"
}
```

Cleaner `setuptools` version.  Depends on #7467.  This patch only.  sagenb repo.



---

archive/issue_comments_062692.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-06T00:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62692",
    "user": "mpatel"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_062693.json:
```json
{
    "body": "Attachment [trac_7447-sagenb_version_v2.patch](tarball://root/attachments/some-uuid/ticket7447/trac_7447-sagenb_version_v2.patch) by mpatel created at 2009-12-06 00:21:49\n\nV2 follows (and depends on) the simpler, `setuptools`-based approach of #7467.  The [attachment:trac_7447-sagenb_version_v2.patch new patch] also adds the Sage Notebook version to HTML test reports.\n\nFor what it's worth, the local queue is\n\n```\ntrac_7390-sagenb_test_report_A.patch\ntrac_7390-sagenb_test_report_B_v2.patch\ntrac_7390-sagenb_test_report_referee.patch\ntrac_7402-pkg_resources.patch\ntrac_7428-publish_last_edited_v2.patch\ntrac_7444-search_after_publish.patch\ntrac_7376-search_by_username_v2.patch\ntrac_1321-sagenb_graphed.patch\nsagenb_7483.patch\nsagenb_7482.patch\nsagenb-7495.patch\nsagenb_3849.patch\ntrac_7467-setuptools.2.patch\ntrac_7447-sagenb_version_v2.patch\ntrac_4714-sagenb_jsmath_init.patch\ntrac_6855-published_interacts.patch\n```\n\nBut please let me know if I should rebase any patch(es).",
    "created_at": "2009-12-06T00:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62693",
    "user": "mpatel"
}
```

Attachment [trac_7447-sagenb_version_v2.patch](tarball://root/attachments/some-uuid/ticket7447/trac_7447-sagenb_version_v2.patch) by mpatel created at 2009-12-06 00:21:49

V2 follows (and depends on) the simpler, `setuptools`-based approach of #7467.  The [attachment:trac_7447-sagenb_version_v2.patch new patch] also adds the Sage Notebook version to HTML test reports.

For what it's worth, the local queue is

```
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B_v2.patch
trac_7390-sagenb_test_report_referee.patch
trac_7402-pkg_resources.patch
trac_7428-publish_last_edited_v2.patch
trac_7444-search_after_publish.patch
trac_7376-search_by_username_v2.patch
trac_1321-sagenb_graphed.patch
sagenb_7483.patch
sagenb_7482.patch
sagenb-7495.patch
sagenb_3849.patch
trac_7467-setuptools.2.patch
trac_7447-sagenb_version_v2.patch
trac_4714-sagenb_jsmath_init.patch
trac_6855-published_interacts.patch
```

But please let me know if I should rebase any patch(es).



---

archive/issue_comments_062694.json:
```json
{
    "body": "Attachment [sagenb_7447-rebase.patch](tarball://root/attachments/some-uuid/ticket7447/sagenb_7447-rebase.patch) by was created at 2009-12-09 00:11:44",
    "created_at": "2009-12-09T00:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62694",
    "user": "was"
}
```

Attachment [sagenb_7447-rebase.patch](tarball://root/attachments/some-uuid/ticket7447/sagenb_7447-rebase.patch) by was created at 2009-12-09 00:11:44



---

archive/issue_comments_062695.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T00:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62695",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062696.json:
```json
{
    "body": "Nice.  I had to rebase it, but that's fine.",
    "created_at": "2009-12-09T00:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62696",
    "user": "was"
}
```

Nice.  I had to rebase it, but that's fine.



---

archive/issue_comments_062697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T01:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62697",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_062698.json:
```json
{
    "body": "I merged this patch into sagenb-0.4.6.",
    "created_at": "2009-12-09T01:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7447#issuecomment-62698",
    "user": "was"
}
```

I merged this patch into sagenb-0.4.6.
