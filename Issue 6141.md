# Issue 6141: [with patch, needs review] simplicial complexes: change 'facets' from an attribute to a method

archive/issues_006141.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nSee [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/b5f9b4e58cce0c6b) from sage-devel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6141\n\n",
    "created_at": "2009-05-27T22:00:42Z",
    "labels": [
        "algebraic topology",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] simplicial complexes: change 'facets' from an attribute to a method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6141",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

See [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/b5f9b4e58cce0c6b) from sage-devel.

Issue created by migration from https://trac.sagemath.org/ticket/6141





---

archive/issue_comments_049036.json:
```json
{
    "body": "Attachment [facets.patch](tarball://root/attachments/some-uuid/ticket6141/facets.patch) by jhpalmieri created at 2009-05-27 22:00:57",
    "created_at": "2009-05-27T22:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-49036",
    "user": "jhpalmieri"
}
```

Attachment [facets.patch](tarball://root/attachments/some-uuid/ticket6141/facets.patch) by jhpalmieri created at 2009-05-27 22:00:57



---

archive/issue_comments_049037.json:
```json
{
    "body": "The patch makes a simple change.  The attribute self.facet is changed to self._facet in all files in the homology directory, and a facets() method is added.  I checked the new code, ran the doctests in homology, and tried a few examples of my own.  Everything was OK.\n\nI was using Sage Version 4.0.alpha0, Release Date: 2009-05-15 under Fedora 10.",
    "created_at": "2009-05-28T05:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-49037",
    "user": "dperkinson"
}
```

The patch makes a simple change.  The attribute self.facet is changed to self._facet in all files in the homology directory, and a facets() method is added.  I checked the new code, ran the doctests in homology, and tried a few examples of my own.  Everything was OK.

I was using Sage Version 4.0.alpha0, Release Date: 2009-05-15 under Fedora 10.



---

archive/issue_comments_049038.json:
```json
{
    "body": "While this does represent a backwards incompatible change, I think it is better to resolve it now while the code is newer.\n\nMerged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T01:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-49038",
    "user": "mhansen"
}
```

While this does represent a backwards incompatible change, I think it is better to resolve it now while the code is newer.

Merged in 4.0.1.alpha0.



---

archive/issue_comments_049039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T01:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-49039",
    "user": "mhansen"
}
```

Resolution: fixed
