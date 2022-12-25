# Issue 6141: [with patch, positive review] simplicial complexes: change 'facets' from an attribute to a method

archive/issues_006141.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nSee [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/b5f9b4e58cce0c6b) from sage-devel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6141\n\n",
    "closed_at": "2009-06-01T01:12:12Z",
    "created_at": "2009-05-27T22:00:42Z",
    "labels": [
        "component: algebraic topology",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] simplicial complexes: change 'facets' from an attribute to a method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6141",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

See [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/b5f9b4e58cce0c6b) from sage-devel.

Issue created by migration from https://trac.sagemath.org/ticket/6141





---

archive/issue_comments_048941.json:
```json
{
    "body": "Attachment [facets.patch](tarball://root/attachments/some-uuid/ticket6141/facets.patch) by @jhpalmieri created at 2009-05-27 22:00:57",
    "created_at": "2009-05-27T22:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-48941",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [facets.patch](tarball://root/attachments/some-uuid/ticket6141/facets.patch) by @jhpalmieri created at 2009-05-27 22:00:57



---

archive/issue_comments_048942.json:
```json
{
    "body": "The patch makes a simple change.  The attribute self.facet is changed to self._facet in all files in the homology directory, and a facets() method is added.  I checked the new code, ran the doctests in homology, and tried a few examples of my own.  Everything was OK.\n\nI was using Sage Version 4.0.alpha0, Release Date: 2009-05-15 under Fedora 10.",
    "created_at": "2009-05-28T05:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-48942",
    "user": "https://trac.sagemath.org/admin/accounts/users/dperkinson"
}
```

The patch makes a simple change.  The attribute self.facet is changed to self._facet in all files in the homology directory, and a facets() method is added.  I checked the new code, ran the doctests in homology, and tried a few examples of my own.  Everything was OK.

I was using Sage Version 4.0.alpha0, Release Date: 2009-05-15 under Fedora 10.



---

archive/issue_comments_048943.json:
```json
{
    "body": "While this does represent a backwards incompatible change, I think it is better to resolve it now while the code is newer.\n\nMerged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T01:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-48943",
    "user": "https://github.com/mwhansen"
}
```

While this does represent a backwards incompatible change, I think it is better to resolve it now while the code is newer.

Merged in 4.0.1.alpha0.



---

archive/issue_comments_048944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T01:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6141#issuecomment-48944",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_014458.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-01T01:12:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6141#event-14458"
}
```
