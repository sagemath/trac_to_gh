# Issue 2519: Add support for posets, semi-lattices, etc. to Sage

archive/issues_002519.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2519\n\n",
    "created_at": "2008-03-14T19:49:15Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Add support for posets, semi-lattices, etc. to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2519",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/2519





---

archive/issue_comments_017147.json:
```json
{
    "body": "Attachment [posets.2008-04-23.patch](tarball://root/attachments/some-uuid/ticket2519/posets.2008-04-23.patch) by @saliola created at 2008-04-23 17:49:01\n\nInitial support for finite posets. (Patch against sage-3.0.)",
    "created_at": "2008-04-23T17:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17147",
    "user": "https://github.com/saliola"
}
```

Attachment [posets.2008-04-23.patch](tarball://root/attachments/some-uuid/ticket2519/posets.2008-04-23.patch) by @saliola created at 2008-04-23 17:49:01

Initial support for finite posets. (Patch against sage-3.0.)



---

archive/issue_comments_017148.json:
```json
{
    "body": "See announcement and discussion on sage-devel:\n\n  http://groups.google.com/group/sage-devel/browse_thread/thread/b6fcc3a134abe22c",
    "created_at": "2008-04-23T18:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17148",
    "user": "https://github.com/saliola"
}
```

See announcement and discussion on sage-devel:

  http://groups.google.com/group/sage-devel/browse_thread/thread/b6fcc3a134abe22c



---

archive/issue_comments_017149.json:
```json
{
    "body": "Some comments:\n\n1. `Lattice` should be `LatticePoset` or something similar. Same comment for `Chain`, `Antichain`, `Pentagon` and `Diamond`.\n\n2. This is a great example of good code. The docstrings are generous and everything is well tested. Nice work!",
    "created_at": "2008-05-10T21:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17149",
    "user": "https://github.com/rlmill"
}
```

Some comments:

1. `Lattice` should be `LatticePoset` or something similar. Same comment for `Chain`, `Antichain`, `Pentagon` and `Diamond`.

2. This is a great example of good code. The docstrings are generous and everything is well tested. Nice work!



---

archive/issue_comments_017150.json:
```json
{
    "body": ">  1. `Lattice` should be `LatticePoset` or something similar. Same comment for `Chain`, `Antichain`, `Pentagon` and `Diamond`.\n\nDone. As a remark: we eventually want to create a poset database similar to the graph\ndatabase. So these poset examples will be moved into the database.\n\n>  1. This is a great example of good code. The docstrings are generous and everything is well tested. Nice work!\n\nThank you!\n\n\n```\nThere are a few other differences between the original patch and the new patch:\n\n1. Added \"or equal to\" to the docstrings for is_gequal and is_lequal.\n\n2. I redefined the show methods for FinitePoset and HasseDiagram. Before it\nwas just show = plot, but I since realized this is wrong: show should show the\nGraphics object returned by the plot method.\n\n3. Added the methods interval, closed_interval and open_interval to the FinitePoset\nclass. These already existed for the HasseDiagram class; so the new methods\njust expose these methods from the FinitePoset class. It was an oversight not\nto have done this originally.\n\n4. I slightly modified HasseDiagram.antichains to return the empty list as an\nantichain. And added tests.\n```\n",
    "created_at": "2008-05-15T23:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17150",
    "user": "https://github.com/saliola"
}
```

>  1. `Lattice` should be `LatticePoset` or something similar. Same comment for `Chain`, `Antichain`, `Pentagon` and `Diamond`.

Done. As a remark: we eventually want to create a poset database similar to the graph
database. So these poset examples will be moved into the database.

>  1. This is a great example of good code. The docstrings are generous and everything is well tested. Nice work!

Thank you!


```
There are a few other differences between the original patch and the new patch:

1. Added "or equal to" to the docstrings for is_gequal and is_lequal.

2. I redefined the show methods for FinitePoset and HasseDiagram. Before it
was just show = plot, but I since realized this is wrong: show should show the
Graphics object returned by the plot method.

3. Added the methods interval, closed_interval and open_interval to the FinitePoset
class. These already existed for the HasseDiagram class; so the new methods
just expose these methods from the FinitePoset class. It was an oversight not
to have done this originally.

4. I slightly modified HasseDiagram.antichains to return the empty list as an
antichain. And added tests.
```




---

archive/issue_comments_017151.json:
```json
{
    "body": "Regarding `show` versus `plot`, you don't even really need a `show`: most Sage objects give LaTeX when you call `show`, and if you do `sage: P.plot()`, the graphics object will appear.\n\nAlso, it looks like you need both patches in order, right?",
    "created_at": "2008-05-16T04:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17151",
    "user": "https://github.com/rlmill"
}
```

Regarding `show` versus `plot`, you don't even really need a `show`: most Sage objects give LaTeX when you call `show`, and if you do `sage: P.plot()`, the graphics object will appear.

Also, it looks like you need both patches in order, right?



---

archive/issue_comments_017152.json:
```json
{
    "body": "Apply both patches in order!",
    "created_at": "2008-05-16T07:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17152",
    "user": "https://github.com/saliola"
}
```

Apply both patches in order!



---

archive/issue_comments_017153.json:
```json
{
    "body": "Attachment [posets.2008-05-15.patch](tarball://root/attachments/some-uuid/ticket2519/posets.2008-05-15.patch) by @saliola created at 2008-05-16 07:06:37\n\nReplying to [comment:5 rlm]:\n> Regarding `show` versus `plot`, you don't even really need a `show`: most Sage objects give LaTeX when you call `show`, and if you do `sage: P.plot()`, the graphics object will appear.\n\nI'll leave it as is, as this is how it is implemented for Graphs/DiGraphs.\n \n> Also, it looks like you need both patches in order, right?\n\nYes, I patched against the previous patch. I've corrected what I wrote.\n\nI can provide a single patch instead if that is easier.",
    "created_at": "2008-05-16T07:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17153",
    "user": "https://github.com/saliola"
}
```

Attachment [posets.2008-05-15.patch](tarball://root/attachments/some-uuid/ticket2519/posets.2008-05-15.patch) by @saliola created at 2008-05-16 07:06:37

Replying to [comment:5 rlm]:
> Regarding `show` versus `plot`, you don't even really need a `show`: most Sage objects give LaTeX when you call `show`, and if you do `sage: P.plot()`, the graphics object will appear.

I'll leave it as is, as this is how it is implemented for Graphs/DiGraphs.
 
> Also, it looks like you need both patches in order, right?

Yes, I patched against the previous patch. I've corrected what I wrote.

I can provide a single patch instead if that is easier.



---

archive/issue_comments_017154.json:
```json
{
    "body": "As long as it applies cleanly and passes all tests...",
    "created_at": "2008-05-22T23:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17154",
    "user": "https://github.com/rlmill"
}
```

As long as it applies cleanly and passes all tests...



---

archive/issue_comments_017155.json:
```json
{
    "body": "With both patches applied the doctests pass. Two comments:\n\n* sage/combinat/posets/__init__.py is zero bytes, so the patch doesn't create it. I fixed that manually\n* these patches are regular diffs and not mercurial patches, so I ended up with the formal credit when applying them. I did however state in the changelog:\n\n```\nchangeset:   9746:0f14afe7ba00\ntag:         tip\nuser:        mabshoff@sage.math.washington.edu\ndate:        Thu May 22 16:52:19 2008 -0700\nsummary:     Apply patch by Peter Jipsen and Franco Saliola: Add support for posets, semi-lattices, etc\n\nchangeset:   9745:0716b13a9e12\nuser:        mabshoff@sage.math.washington.edu\ndate:        Thu May 22 16:52:08 2008 -0700\nsummary:     Apply patch by Peter Jipsen and Franco Saliola: Add support for posets, semi-lattices, etc.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-05-22T23:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With both patches applied the doctests pass. Two comments:

* sage/combinat/posets/__init__.py is zero bytes, so the patch doesn't create it. I fixed that manually
* these patches are regular diffs and not mercurial patches, so I ended up with the formal credit when applying them. I did however state in the changelog:

```
changeset:   9746:0f14afe7ba00
tag:         tip
user:        mabshoff@sage.math.washington.edu
date:        Thu May 22 16:52:19 2008 -0700
summary:     Apply patch by Peter Jipsen and Franco Saliola: Add support for posets, semi-lattices, etc

changeset:   9745:0716b13a9e12
user:        mabshoff@sage.math.washington.edu
date:        Thu May 22 16:52:08 2008 -0700
summary:     Apply patch by Peter Jipsen and Franco Saliola: Add support for posets, semi-lattices, etc.
```


Cheers,

Michael



---

archive/issue_comments_017156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T00:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002700.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-23T00:07:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2519#event-2700"
}
```



---

archive/issue_comments_017157.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-23T00:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2519#issuecomment-17157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc0
