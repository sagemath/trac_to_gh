# Issue 6605: sage -docbuild DOC FORMAT should do better error checking on DOC

archive/issues_006605.json:
```json
{
    "body": "Assignee: tba\n\nIf I run `sage -docbuild hello html`, then a directory \"hello\" is created in `SAGE_ROOT/devel/sage/doc/en`.  Then if I run `sage -docbuild -help`, \"hello\" is listed as one of the options.\n\nError-checking should be done on the \"document\" argument of `sage -docbuild` to make sure this doesn't happen.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6605\n\n",
    "created_at": "2009-07-23T17:48:39Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sage -docbuild DOC FORMAT should do better error checking on DOC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6605",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

If I run `sage -docbuild hello html`, then a directory "hello" is created in `SAGE_ROOT/devel/sage/doc/en`.  Then if I run `sage -docbuild -help`, "hello" is listed as one of the options.

Error-checking should be done on the "document" argument of `sage -docbuild` to make sure this doesn't happen.


Issue created by migration from https://trac.sagemath.org/ticket/6605





---

archive/issue_comments_053975.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-23T19:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53975",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053976.json:
```json
{
    "body": "Changing assignee from tba to @jhpalmieri.",
    "created_at": "2009-07-23T19:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53976",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tba to @jhpalmieri.



---

archive/issue_comments_053977.json:
```json
{
    "body": "As written, this depends on #6187 (although it would be easy enough to modify it to avoid this).   The new OMIT variable is for situations such as the one introduced by #5653, where there is a subdirectory \"introspect\" of SAGE_ROOT/doc/en/, which is not a document to be processed by \"sage -docbuild\", and so should be omitted from the list of all such documents.  (This patch doesn't depend on #5653, but it will be compatible with it, should #5653 be merged.)",
    "created_at": "2009-07-23T19:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53977",
    "user": "https://github.com/jhpalmieri"
}
```

As written, this depends on #6187 (although it would be easy enough to modify it to avoid this).   The new OMIT variable is for situations such as the one introduced by #5653, where there is a subdirectory "introspect" of SAGE_ROOT/doc/en/, which is not a document to be processed by "sage -docbuild", and so should be omitted from the list of all such documents.  (This patch doesn't depend on #5653, but it will be compatible with it, should #5653 be merged.)



---

archive/issue_comments_053978.json:
```json
{
    "body": "The patch works for me.  I think a non-zero exit value is the UNIX convention for an error.  I can make an updated patch.  Or I can wait for more feedback on #6187. \n\nNotes for other potential tickets:\n\n* We could also print a similar message in the less severe case of an invalid format.\n* Instead of using [sys.exit()](http://docs.python.org/library/sys.html#sys.exit), we could raise (and catch) some exception, so that the builder can loop over documents, formats, and commands, printing warnings as necessary.  At the moment, though, this feature is not implemented.",
    "created_at": "2009-07-24T09:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53978",
    "user": "https://github.com/qed777"
}
```

The patch works for me.  I think a non-zero exit value is the UNIX convention for an error.  I can make an updated patch.  Or I can wait for more feedback on #6187. 

Notes for other potential tickets:

* We could also print a similar message in the less severe case of an invalid format.
* Instead of using [sys.exit()](http://docs.python.org/library/sys.html#sys.exit), we could raise (and catch) some exception, so that the builder can loop over documents, formats, and commands, printing warnings as necessary.  At the moment, though, this feature is not implemented.



---

archive/issue_comments_053979.json:
```json
{
    "body": "Attachment [trac_6605-docbuild-check.patch](tarball://root/attachments/some-uuid/ticket6605/trac_6605-docbuild-check.patch) by @jhpalmieri created at 2009-07-24 15:18:19\n\nThis patch is identical, except it uses sys.exit(1) instead of sys.exit(0).",
    "created_at": "2009-07-24T15:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53979",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6605-docbuild-check.patch](tarball://root/attachments/some-uuid/ticket6605/trac_6605-docbuild-check.patch) by @jhpalmieri created at 2009-07-24 15:18:19

This patch is identical, except it uses sys.exit(1) instead of sys.exit(0).



---

archive/issue_comments_053980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T22:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53980",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006844.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-24T22:35:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6605#event-6844"
}
```



---

archive/issue_comments_053981.json:
```json
{
    "body": "The patch applies but with fuzz:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6605/trac_6605-docbuild-check.patch && hg qpush\nadding trac_6605-docbuild-check.patch to series file\napplying trac_6605-docbuild-check.patch\npatching file doc/common/builder.py\nHunk #3 succeeded at 614 with fuzz 1 (offset -44 lines).\nNow at: trac_6605-docbuild-check.patch\n```\n",
    "created_at": "2009-07-26T23:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53981",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch applies but with fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6605/trac_6605-docbuild-check.patch && hg qpush
adding trac_6605-docbuild-check.patch to series file
applying trac_6605-docbuild-check.patch
patching file doc/common/builder.py
Hunk #3 succeeded at 614 with fuzz 1 (offset -44 lines).
Now at: trac_6605-docbuild-check.patch
```




---

archive/issue_comments_053982.json:
```json
{
    "body": "The patch `trac_6605-docbuild-check.patch` is buggy when it comes to (re)building the documentation of a new release. Assume you have applied this patch to Sage 4.1.1.alpha0, then build a source release with\n\n```\nsage -sdist <version>\n```\n\nor a binary release with\n\n```\nsage -bdist <version>\n```\n\nAfter that, upgrade a previous release to this new release and rebuild the documentation. You then get this error message:\n\n```\n[mvngu@sage sage-4.1.1.alpha1-test-x86_64-Linux]$ ./sage -docbuild tutorial htmlTraceback (most recent call last):\n  File \"/scratch/mvngu/sage-4.1.1.alpha1-test-x86_64-Linux/devel/sage/doc/common/builder.py\", line 673, in <module>\n    getattr(get_builder(name), type)()\n  File \"/scratch/mvngu/sage-4.1.1.alpha1-test-x86_64-Linux/devel/sage/doc/common/builder.py\", line 616, in get_builder\n    elif name in get_documents() or name in AllBuilder().get_all_documents():\nNameError: global name 'get_documents' is not defined\n```\n\nThe same error is raised if you rebuild the documentation of the binary version of the new release. I'm reopening this ticket and marking it as needs work.",
    "created_at": "2009-07-27T05:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_6605-docbuild-check.patch` is buggy when it comes to (re)building the documentation of a new release. Assume you have applied this patch to Sage 4.1.1.alpha0, then build a source release with

```
sage -sdist <version>
```

or a binary release with

```
sage -bdist <version>
```

After that, upgrade a previous release to this new release and rebuild the documentation. You then get this error message:

```
[mvngu@sage sage-4.1.1.alpha1-test-x86_64-Linux]$ ./sage -docbuild tutorial htmlTraceback (most recent call last):
  File "/scratch/mvngu/sage-4.1.1.alpha1-test-x86_64-Linux/devel/sage/doc/common/builder.py", line 673, in <module>
    getattr(get_builder(name), type)()
  File "/scratch/mvngu/sage-4.1.1.alpha1-test-x86_64-Linux/devel/sage/doc/common/builder.py", line 616, in get_builder
    elif name in get_documents() or name in AllBuilder().get_all_documents():
NameError: global name 'get_documents' is not defined
```

The same error is raised if you rebuild the documentation of the binary version of the new release. I'm reopening this ticket and marking it as needs work.



---

archive/issue_comments_053983.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-27T05:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_053984.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-27T05:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006845.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-27T05:24:22Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6605#event-6845"
}
```



---

archive/issue_comments_053985.json:
```json
{
    "body": "It doesn't need work.  As I mentioned in the first comment, it depends on #6187.  That's where \"get_documents\" is defined.\n\nPlease wait for #6187 to merge.",
    "created_at": "2009-07-27T05:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53985",
    "user": "https://github.com/jhpalmieri"
}
```

It doesn't need work.  As I mentioned in the first comment, it depends on #6187.  That's where "get_documents" is defined.

Please wait for #6187 to merge.



---

archive/issue_comments_053986.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T16:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6605#issuecomment-53986",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006846.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-10-15T16:34:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6605",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6605#event-6846"
}
```
