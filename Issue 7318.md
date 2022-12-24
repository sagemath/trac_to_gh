# Issue 7318: SageNB: Sphinxify erases doc/en/introspect

archive/issues_007318.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @TimDumol @williamstein\n\nIn Sage, `sagenb.misc.sphinxify.sphinxify` does\n\n```python\n    shutil.rmtree(confdir, ignore_errors=True)\n```\n\nafter running Sphinx, but this should happen only if `confdir` is a temporary directory.  Otherwise,\n\n```sh\nprompt$> cd $SAGE_ROOT/devel/sage/\nprompt$> hg stat\n! doc/en/introspect/__init__.py\n! doc/en/introspect/conf.py\n! doc/en/introspect/static/empty\n! doc/en/introspect/templates/layout.html\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7318\n\n",
    "created_at": "2009-10-27T03:17:20Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "SageNB: Sphinxify erases doc/en/introspect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7318",
    "user": "@qed777"
}
```
Assignee: boothby

CC:  @TimDumol @williamstein

In Sage, `sagenb.misc.sphinxify.sphinxify` does

```python
    shutil.rmtree(confdir, ignore_errors=True)
```

after running Sphinx, but this should happen only if `confdir` is a temporary directory.  Otherwise,

```sh
prompt$> cd $SAGE_ROOT/devel/sage/
prompt$> hg stat
! doc/en/introspect/__init__.py
! doc/en/introspect/conf.py
! doc/en/introspect/static/empty
! doc/en/introspect/templates/layout.html
```



Issue created by migration from https://trac.sagemath.org/ticket/7318





---

archive/issue_comments_061143.json:
```json
{
    "body": "Attachment [trac_7318-sphinxify_confdir.patch](tarball://root/attachments/some-uuid/ticket7318/trac_7318-sphinxify_confdir.patch) by @qed777 created at 2009-10-27 03:22:14\n\nPreserve doc/en/introspect in sphinxify.  Apply to sagenb repository.",
    "created_at": "2009-10-27T03:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7318#issuecomment-61143",
    "user": "@qed777"
}
```

Attachment [trac_7318-sphinxify_confdir.patch](tarball://root/attachments/some-uuid/ticket7318/trac_7318-sphinxify_confdir.patch) by @qed777 created at 2009-10-27 03:22:14

Preserve doc/en/introspect in sphinxify.  Apply to sagenb repository.



---

archive/issue_comments_061144.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T03:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7318#issuecomment-61144",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061145.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-27T03:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7318#issuecomment-61145",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061146.json:
```json
{
    "body": "I can confirm that before patching, doc/en/introspect is deleted, and afterwards it isn't.  The patch obviously does the right thing.",
    "created_at": "2009-10-27T03:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7318#issuecomment-61146",
    "user": "@jhpalmieri"
}
```

I can confirm that before patching, doc/en/introspect is deleted, and afterwards it isn't.  The patch obviously does the right thing.



---

archive/issue_comments_061147.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7318#issuecomment-61147",
    "user": "@williamstein"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_comments_061148.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7318#issuecomment-61148",
    "user": "@williamstein"
}
```

Resolution: fixed
