# Issue 5614: [with patch, not ready for review] add top-of-stack caching for fast_callable

archive/issues_005614.json:
```json
{
    "body": "Assignee: somebody\n\nTop-of-stack caching is a standard optimization for stack interpreters; it typically significantly reduces the number of memory loads/stores.  This patch adds top-of-stack caching for the fast_callable float/RDF interpreter.\n\nUnfortunately, on my machine (32-bit x86, with Debian's gcc-4.3 version 4.3.3-3), this interacts poorly with gcc's register allocation heuristics, so the resulting interpreter is actually slower than before the patch.\n\nDoctests do NOT pass, and the patch is not fully documented.  (I believe the patch works; the doctests that fail are looking at fast_callable internals that changed.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5614\n\n",
    "created_at": "2009-03-26T04:22:58Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "[with patch, not ready for review] add top-of-stack caching for fast_callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5614",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

Top-of-stack caching is a standard optimization for stack interpreters; it typically significantly reduces the number of memory loads/stores.  This patch adds top-of-stack caching for the fast_callable float/RDF interpreter.

Unfortunately, on my machine (32-bit x86, with Debian's gcc-4.3 version 4.3.3-3), this interacts poorly with gcc's register allocation heuristics, so the resulting interpreter is actually slower than before the patch.

Doctests do NOT pass, and the patch is not fully documented.  (I believe the patch works; the doctests that fail are looking at fast_callable internals that changed.)

Issue created by migration from https://trac.sagemath.org/ticket/5614





---

archive/issue_comments_043766.json:
```json
{
    "body": "Attachment [preliminary-tos-cache.patch](tarball://root/attachments/some-uuid/ticket5614/preliminary-tos-cache.patch) by @saraedum created at 2013-07-23 15:53:30",
    "created_at": "2013-07-23T15:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5614#issuecomment-43766",
    "user": "https://github.com/saraedum"
}
```

Attachment [preliminary-tos-cache.patch](tarball://root/attachments/some-uuid/ticket5614/preliminary-tos-cache.patch) by @saraedum created at 2013-07-23 15:53:30
