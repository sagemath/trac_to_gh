# Issue 7120: [with patch, needs review] document Sphinx/reST markup for INPUT/OUTPUT

archive/issues_007120.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nCC:  mhansen\n\nInstead of using\n\n```\nINPUT:\n\n- ``x`` - integer (default: 1) blah\n```\n\nSphinx has specific markup for this:\n\n```\n:param x: blah\n:type x: integer, default 1\n```\n\nThe resulting output isn't quite the same, but it looks nice.\n\nThere are two patches here; one adds a little to the developer's guide to document this.  The other patch implements this (applied to the file sage/homology/simplicial_complex.py) so you can build the documentation and see what it looks like.  The patches are independent; either or both could be merged, although it would not really accomplish the purpose of the ticket to just merge the simplicial complex patch...\n\nIssue created by migration from https://trac.sagemath.org/ticket/7120\n\n",
    "created_at": "2009-10-05T05:20:03Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] document Sphinx/reST markup for INPUT/OUTPUT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7120",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

CC:  mhansen

Instead of using

```
INPUT:

- ``x`` - integer (default: 1) blah
```

Sphinx has specific markup for this:

```
:param x: blah
:type x: integer, default 1
```

The resulting output isn't quite the same, but it looks nice.

There are two patches here; one adds a little to the developer's guide to document this.  The other patch implements this (applied to the file sage/homology/simplicial_complex.py) so you can build the documentation and see what it looks like.  The patches are independent; either or both could be merged, although it would not really accomplish the purpose of the ticket to just merge the simplicial complex patch...

Issue created by migration from https://trac.sagemath.org/ticket/7120





---

archive/issue_comments_059024.json:
```json
{
    "body": "Attachment [trac_7120-developer.patch](tarball://root/attachments/some-uuid/ticket7120/trac_7120-developer.patch) by jhpalmieri created at 2009-10-05 05:20:41",
    "created_at": "2009-10-05T05:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7120#issuecomment-59024",
    "user": "jhpalmieri"
}
```

Attachment [trac_7120-developer.patch](tarball://root/attachments/some-uuid/ticket7120/trac_7120-developer.patch) by jhpalmieri created at 2009-10-05 05:20:41



---

archive/issue_comments_059025.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-10T10:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7120#issuecomment-59025",
    "user": "awebb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059026.json:
```json
{
    "body": "Attachment [trac_7120-simplicial.patch](tarball://root/attachments/some-uuid/ticket7120/trac_7120-simplicial.patch) by awebb created at 2009-10-10 10:44:14\n\nThe patch looks good to me and -docbuild works. I take it that is just an introduction and some information and not a conversion. I like the style though. Is the intent to slowly convert or to have both styles? ~Adam",
    "created_at": "2009-10-10T10:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7120#issuecomment-59026",
    "user": "awebb"
}
```

Attachment [trac_7120-simplicial.patch](tarball://root/attachments/some-uuid/ticket7120/trac_7120-simplicial.patch) by awebb created at 2009-10-10 10:44:14

The patch looks good to me and -docbuild works. I take it that is just an introduction and some information and not a conversion. I like the style though. Is the intent to slowly convert or to have both styles? ~Adam



---

archive/issue_comments_059027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T10:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7120#issuecomment-59027",
    "user": "mhansen"
}
```

Resolution: fixed
