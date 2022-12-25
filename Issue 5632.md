# Issue 5632: [with spkg; needs review] doc fixes for quaternion algebra element

archive/issues_005632.json:
```json
{
    "body": "Assignee: tbd\n\nAlong the lines of #5541, here are some doc fixes for quaternion_algebra_element.pyx.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5632\n\n",
    "created_at": "2009-03-29T15:39:54Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with spkg; needs review] doc fixes for quaternion algebra element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5632",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

Along the lines of #5541, here are some doc fixes for quaternion_algebra_element.pyx.

Issue created by migration from https://trac.sagemath.org/ticket/5632





---

archive/issue_comments_043899.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T16:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43899",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043900.json:
```json
{
    "body": "Changing assignee from tbd to @jhpalmieri.",
    "created_at": "2009-03-29T16:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43900",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tbd to @jhpalmieri.



---

archive/issue_comments_043901.json:
```json
{
    "body": "jhpalmieri: Can you please provide a link to the spkg you mentioned above? I seem to not find a link or the spkg anywhere on this ticket. Sorry if I've missed anything.",
    "created_at": "2009-03-30T06:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43901",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

jhpalmieri: Can you please provide a link to the spkg you mentioned above? I seem to not find a link or the spkg anywhere on this ticket. Sorry if I've missed anything.



---

archive/issue_comments_043902.json:
```json
{
    "body": "Sorry, should have said \"with patch\", not \"with spkg\".",
    "created_at": "2009-03-30T13:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43902",
    "user": "https://github.com/jhpalmieri"
}
```

Sorry, should have said "with patch", not "with spkg".



---

archive/issue_comments_043903.json:
```json
{
    "body": "Looks good, applies OK against Sage 3.4.1.alpha0, all doctests passed. Positive review.",
    "created_at": "2009-03-31T05:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43903",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good, applies OK against Sage 3.4.1.alpha0, all doctests passed. Positive review.



---

archive/issue_comments_043904.json:
```json
{
    "body": "Due to #5520 this patch needs to be rebased:\n\n```\nsage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5632_quaternion.patch \npatching file sage/algebras/quatalg/quaternion_algebra_element.pyx\nHunk #1 succeeded at 171 (offset 4 lines).\nHunk #2 succeeded at 354 (offset 140 lines).\nHunk #3 succeeded at 398 (offset 140 lines).\nHunk #4 succeeded at 410 (offset 140 lines).\nHunk #5 succeeded at 422 (offset 140 lines).\nHunk #6 succeeded at 437 (offset 140 lines).\nHunk #7 succeeded at 496 (offset 140 lines).\nHunk #8 succeeded at 537 (offset 167 lines).\nHunk #9 succeeded at 685 (offset 167 lines).\nHunk #10 succeeded at 712 (offset 167 lines).\nHunk #11 succeeded at 797 (offset 224 lines).\nHunk #12 succeeded at 1149 (offset 261 lines).\nHunk #13 succeeded at 1219 (offset 260 lines).\nHunk #14 succeeded at 1244 (offset 260 lines).\nHunk #15 succeeded at 1494 (offset 441 lines).\nHunk #16 succeeded at 1854 (offset 441 lines).\nHunk #17 FAILED at 1912.\n1 out of 17 hunks FAILED -- saving rejects to file sage/algebras/quatalg/quaternion_algebra_element.pyx.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T07:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43904",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Due to #5520 this patch needs to be rebased:

```
sage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5632_quaternion.patch 
patching file sage/algebras/quatalg/quaternion_algebra_element.pyx
Hunk #1 succeeded at 171 (offset 4 lines).
Hunk #2 succeeded at 354 (offset 140 lines).
Hunk #3 succeeded at 398 (offset 140 lines).
Hunk #4 succeeded at 410 (offset 140 lines).
Hunk #5 succeeded at 422 (offset 140 lines).
Hunk #6 succeeded at 437 (offset 140 lines).
Hunk #7 succeeded at 496 (offset 140 lines).
Hunk #8 succeeded at 537 (offset 167 lines).
Hunk #9 succeeded at 685 (offset 167 lines).
Hunk #10 succeeded at 712 (offset 167 lines).
Hunk #11 succeeded at 797 (offset 224 lines).
Hunk #12 succeeded at 1149 (offset 261 lines).
Hunk #13 succeeded at 1219 (offset 260 lines).
Hunk #14 succeeded at 1244 (offset 260 lines).
Hunk #15 succeeded at 1494 (offset 441 lines).
Hunk #16 succeeded at 1854 (offset 441 lines).
Hunk #17 FAILED at 1912.
1 out of 17 hunks FAILED -- saving rejects to file sage/algebras/quatalg/quaternion_algebra_element.pyx.rej
```


Cheers,

Michael



---

archive/issue_comments_043905.json:
```json
{
    "body": "Here's a rebased version.  Since the previous one had a positive review, I assume this one does, too.\n\nHowever, I think we also need something like the attached 'quatalg-reference.patch' to process the moved files for inclusion into the reference manual, but when I apply it and try to build the docs, I get error messages like\n\n```\nTraceback (most recent call last):\n  File \"/Applications/sage/devel/sage/doc/common/builder.py\", line 668, in <module>\n    getattr(get_builder(name), type)()\n  File \"/Applications/sage/devel/sage/doc/common/builder.py\", line 348, in _wrapper\n    for module_name in self.get_modified_modules():\n  File \"/Applications/sage/devel/sage/doc/common/builder.py\", line 415, in get_modified_modules\n    added, changed, removed = env.get_outdated_files(False)\n  File \"/Applications/sage_builds/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py\", line 400, in get_outdated_files\n    newmtime = path.getmtime(self.doc2path(docname))\n  File \"/Applications/sage_builds/sage-3.4.1.alpha0/local/lib/python2.5/posixpath.py\", line 143, in getmtime\n    return os.stat(filename).st_mtime\nOSError: [Errno 2] No such file or directory: '/Applications/sage_builds/sage-3.4.1.alpha0/devel/sage-main/doc/en/reference/sage/algebras/quaternion_algebra.rst'\n```\n\n(This fix should have been part of #5520, I think.)",
    "created_at": "2009-03-31T15:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43905",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a rebased version.  Since the previous one had a positive review, I assume this one does, too.

However, I think we also need something like the attached 'quatalg-reference.patch' to process the moved files for inclusion into the reference manual, but when I apply it and try to build the docs, I get error messages like

```
Traceback (most recent call last):
  File "/Applications/sage/devel/sage/doc/common/builder.py", line 668, in <module>
    getattr(get_builder(name), type)()
  File "/Applications/sage/devel/sage/doc/common/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/Applications/sage/devel/sage/doc/common/builder.py", line 415, in get_modified_modules
    added, changed, removed = env.get_outdated_files(False)
  File "/Applications/sage_builds/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py", line 400, in get_outdated_files
    newmtime = path.getmtime(self.doc2path(docname))
  File "/Applications/sage_builds/sage-3.4.1.alpha0/local/lib/python2.5/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: '/Applications/sage_builds/sage-3.4.1.alpha0/devel/sage-main/doc/en/reference/sage/algebras/quaternion_algebra.rst'
```

(This fix should have been part of #5520, I think.)



---

archive/issue_comments_043906.json:
```json
{
    "body": "Attachment [quaternion.patch](tarball://root/attachments/some-uuid/ticket5632/quaternion.patch) by @jhpalmieri created at 2009-03-31 15:38:05\n\nrebased post #5520, positive review for this patch",
    "created_at": "2009-03-31T15:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43906",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [quaternion.patch](tarball://root/attachments/some-uuid/ticket5632/quaternion.patch) by @jhpalmieri created at 2009-03-31 15:38:05

rebased post #5520, positive review for this patch



---

archive/issue_comments_043907.json:
```json
{
    "body": "Attachment [quatalg-reference.patch](tarball://root/attachments/some-uuid/ticket5632/quatalg-reference.patch) by mabshoff created at 2009-03-31 19:57:42\n\nFor the record: positive review quatalg-reference.patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T19:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [quatalg-reference.patch](tarball://root/attachments/some-uuid/ticket5632/quatalg-reference.patch) by mabshoff created at 2009-03-31 19:57:42

For the record: positive review quatalg-reference.patch.

Cheers,

Michael



---

archive/issue_events_013252.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-31T20:08:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5632#event-13252"
}
```



---

archive/issue_comments_043908.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43908",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_043909.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5632#issuecomment-43909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
