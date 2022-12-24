# Issue 5174: _repr_ for large matrices should indicate how to see the entries

archive/issues_005174.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n[09:30] <jason-> on the other hand, I always get frustrated trying to see a 30x30 matrix in Sage\n[09:30] <wstein> print a.str()\n[09:30] <jason-> yeah, I never remember it.\n[09:30] <wstein> That will show you any matrix in sage of any size.\n[09:31] <wstein> Well then the output of a._repr_() should mention it so you can remember it.  make a ticket.\n[09:31] <jason-> good point.\n[09:31] <jason-> I think I usually end up doing a.rows()\n[09:32] <jason-> or list(a)\n[09:32] <jason-> so you're saying print a should do:\n[09:32] <jason-> 30 x 30 dense matrix over Integer Ring (to see the entries, do print a.str())\n[09:33] <wstein> Yep.\n[09:33] <jason-> 30 x 30 dense matrix over Integer Ring (to see the entries, type \"print a.str()\")\n[09:33] <wstein> Of course it's possibly confusing since \"a.str()\" is really \"yourvar.str()\"\n[09:33] <wstein> but hopefully people can understand that.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5174\n\n",
    "created_at": "2009-02-04T15:38:28Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "_repr_ for large matrices should indicate how to see the entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5174",
    "user": "@jasongrout"
}
```
Assignee: @williamstein


```
[09:30] <jason-> on the other hand, I always get frustrated trying to see a 30x30 matrix in Sage
[09:30] <wstein> print a.str()
[09:30] <jason-> yeah, I never remember it.
[09:30] <wstein> That will show you any matrix in sage of any size.
[09:31] <wstein> Well then the output of a._repr_() should mention it so you can remember it.  make a ticket.
[09:31] <jason-> good point.
[09:31] <jason-> I think I usually end up doing a.rows()
[09:32] <jason-> or list(a)
[09:32] <jason-> so you're saying print a should do:
[09:32] <jason-> 30 x 30 dense matrix over Integer Ring (to see the entries, do print a.str())
[09:33] <wstein> Yep.
[09:33] <jason-> 30 x 30 dense matrix over Integer Ring (to see the entries, type "print a.str()")
[09:33] <wstein> Of course it's possibly confusing since "a.str()" is really "yourvar.str()"
[09:33] <wstein> but hopefully people can understand that.
```


Issue created by migration from https://trac.sagemath.org/ticket/5174





---

archive/issue_comments_039634.json:
```json
{
    "body": "Idea:\n\n\n```\nsage: obj = random_matrix(ZZ,100)\nsage: str(obj) + \" ('print obj.str()' to see all entries)\"\n```\n",
    "created_at": "2009-12-11T23:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39634",
    "user": "@williamstein"
}
```

Idea:


```
sage: obj = random_matrix(ZZ,100)
sage: str(obj) + " ('print obj.str()' to see all entries)"
```




---

archive/issue_comments_039635.json:
```json
{
    "body": "Change this function in matrix/matrix0.pyx:\n\n```\n    def __repr__(self):\n        if self._nrows < max_rows and self._ncols < max_cols:\n            return self.str()\n        if self.is_sparse():\n            s = 'sparse'\n        else:\n            s = 'dense'\n        return \"%s x %s %s matrix over %s\"%(self._nrows, self._ncols, s, self.base_ring())\n```\n",
    "created_at": "2009-12-11T23:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39635",
    "user": "@williamstein"
}
```

Change this function in matrix/matrix0.pyx:

```
    def __repr__(self):
        if self._nrows < max_rows and self._ncols < max_cols:
            return self.str()
        if self.is_sparse():
            s = 'sparse'
        else:
            s = 'dense'
        return "%s x %s %s matrix over %s"%(self._nrows, self._ncols, s, self.base_ring())
```




---

archive/issue_comments_039636.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-12T20:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39636",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039637.json:
```json
{
    "body": "Attachment [trac_5174-matrixrep.patch](tarball://root/attachments/some-uuid/ticket5174/trac_5174-matrixrep.patch) by @jhpalmieri created at 2009-12-12 20:18:39\n\nHere's a patch.  The docstring to the `__repr__` method for matrices illustrates what the patch does:\n\n```\n        EXAMPLES::\n\n            sage: A = matrix([[1,2], [3,4], [5,6]])\n            sage: A.__repr__()\n            '[1 2]\\n[3 4]\\n[5 6]'\n            sage: print A\n            [1 2]\n            [3 4]\n            [5 6]\n\n        If the matrix is too big, don't print all of the elements::\n\n            sage: A = random_matrix(ZZ, 100)\n            sage: A.__repr__()\n            \"100 x 100 dense matrix over Integer Ring (type 'print A.str()' to see all of the entries)\"\n            sage: print A\n            100 x 100 dense matrix over Integer Ring (type 'print A.str()' to see all of the entries)\n\n        If there are several names for the same matrix, write it as \"obj\"::\n\n            sage: B = A; print B\n            100 x 100 dense matrix over Integer Ring (type 'print obj.str()' to see all of the entries)\n```\n\n\nI actually think that this looks a little funny in some situations; for example, in chain_complex.py, the old version did this:\n\n```\n            sage: C.differential()\n            {0: 40 x 40 dense matrix over Integer Ring, 1: []}\n```\n\nwhile the new version does this:\n\n```\n            sage: C.differential()\n            {0: 40 x 40 dense matrix over Integer Ring (type 'print obj.str()' to see all of the entries), 1: []}\n```\n\nIt would be pretty easy to change the print representation so if there were no name attached to the object (e.g., if it were produced by another method, as in this example), then the extra message about \"print ...\" would be omitted.  Opinions?",
    "created_at": "2009-12-12T20:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39637",
    "user": "@jhpalmieri"
}
```

Attachment [trac_5174-matrixrep.patch](tarball://root/attachments/some-uuid/ticket5174/trac_5174-matrixrep.patch) by @jhpalmieri created at 2009-12-12 20:18:39

Here's a patch.  The docstring to the `__repr__` method for matrices illustrates what the patch does:

```
        EXAMPLES::

            sage: A = matrix([[1,2], [3,4], [5,6]])
            sage: A.__repr__()
            '[1 2]\n[3 4]\n[5 6]'
            sage: print A
            [1 2]
            [3 4]
            [5 6]

        If the matrix is too big, don't print all of the elements::

            sage: A = random_matrix(ZZ, 100)
            sage: A.__repr__()
            "100 x 100 dense matrix over Integer Ring (type 'print A.str()' to see all of the entries)"
            sage: print A
            100 x 100 dense matrix over Integer Ring (type 'print A.str()' to see all of the entries)

        If there are several names for the same matrix, write it as "obj"::

            sage: B = A; print B
            100 x 100 dense matrix over Integer Ring (type 'print obj.str()' to see all of the entries)
```


I actually think that this looks a little funny in some situations; for example, in chain_complex.py, the old version did this:

```
            sage: C.differential()
            {0: 40 x 40 dense matrix over Integer Ring, 1: []}
```

while the new version does this:

```
            sage: C.differential()
            {0: 40 x 40 dense matrix over Integer Ring (type 'print obj.str()' to see all of the entries), 1: []}
```

It would be pretty easy to change the print representation so if there were no name attached to the object (e.g., if it were produced by another method, as in this example), then the extra message about "print ..." would be omitted.  Opinions?



---

archive/issue_comments_039638.json:
```json
{
    "body": "> It would be pretty easy to change the print representation so\n>  if there were no name attached to the object (e.g., if it were \n> produced by another method, as in this example), then the extra \n> message about \"print ...\" would be omitted. Opinions? \n\nHow do you do that?  I would have no clue.",
    "created_at": "2009-12-13T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39638",
    "user": "@williamstein"
}
```

> It would be pretty easy to change the print representation so
>  if there were no name attached to the object (e.g., if it were 
> produced by another method, as in this example), then the extra 
> message about "print ..." would be omitted. Opinions? 

How do you do that?  I would have no clue.



---

archive/issue_comments_039639.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> > It would be pretty easy to change the print representation so\n> >  if there were no name attached to the object (e.g., if it were \n> > produced by another method, as in this example), then the extra \n> > message about \"print ...\" would be omitted. Opinions? \n> \n> How do you do that?  I would have no clue.\n\nA web search led me to a code snippet (by Georg Brandl, the author of Sphinx) which more or less searches through the `locals()` dictionary for the object, making a list of the variable names bound to it.   (See the part of the patch for the file sageinspect.py.)  If you exclude the variable names starting with \"_\", then if the resulting list is empty, you don't print the message.",
    "created_at": "2009-12-14T00:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39639",
    "user": "@jhpalmieri"
}
```

Replying to [comment:4 was]:
> > It would be pretty easy to change the print representation so
> >  if there were no name attached to the object (e.g., if it were 
> > produced by another method, as in this example), then the extra 
> > message about "print ..." would be omitted. Opinions? 
> 
> How do you do that?  I would have no clue.

A web search led me to a code snippet (by Georg Brandl, the author of Sphinx) which more or less searches through the `locals()` dictionary for the object, making a list of the variable names bound to it.   (See the part of the patch for the file sageinspect.py.)  If you exclude the variable names starting with "_", then if the resulting list is empty, you don't print the message.



---

archive/issue_comments_039640.json:
```json
{
    "body": "Here's a new version of the patch.  This is similar to the old one, but it behaves like this:\n\n```\n     sage: C.differential()\n     {0: 40 x 40 dense matrix over Integer Ring, 1: []}\n```\n",
    "created_at": "2009-12-20T06:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39640",
    "user": "@jhpalmieri"
}
```

Here's a new version of the patch.  This is similar to the old one, but it behaves like this:

```
     sage: C.differential()
     {0: 40 x 40 dense matrix over Integer Ring, 1: []}
```




---

archive/issue_comments_039641.json:
```json
{
    "body": "Attachment [trac_5174-matrixrep-v2.patch](tarball://root/attachments/some-uuid/ticket5174/trac_5174-matrixrep-v2.patch) by @mwhansen created at 2009-12-27 15:38:23\n\nThe second patch looks good to me.",
    "created_at": "2009-12-27T15:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39641",
    "user": "@mwhansen"
}
```

Attachment [trac_5174-matrixrep-v2.patch](tarball://root/attachments/some-uuid/ticket5174/trac_5174-matrixrep-v2.patch) by @mwhansen created at 2009-12-27 15:38:23

The second patch looks good to me.



---

archive/issue_comments_039642.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-27T15:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39642",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5174#issuecomment-39643",
    "user": "@mwhansen"
}
```

Resolution: fixed
