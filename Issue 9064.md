# Issue 9064: remove p-adic matrix directory

archive/issues_009064.json:
```json
{
    "body": "Assignee: jason, was\n\nThere's a single file in matrix/padics and it is an empty __init__.py.\n\nSays David Roe: \"Yeah, oversight.\u00a0 At some point I was planning on working on p-adic matrices, and I guess the __init__.py file got put in then.\u00a0 Since I'm not going to work on it anytime soon, it can safely be removed.\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/9064\n\n",
    "created_at": "2010-05-27T08:20:44Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "title": "remove p-adic matrix directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9064",
    "user": "was"
}
```
Assignee: jason, was

There's a single file in matrix/padics and it is an empty __init__.py.

Says David Roe: "Yeah, oversight.  At some point I was planning on working on p-adic matrices, and I guess the __init__.py file got put in then.  Since I'm not going to work on it anytime soon, it can safely be removed."

Issue created by migration from https://trac.sagemath.org/ticket/9064





---

archive/issue_comments_084114.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-11T18:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9064#issuecomment-84114",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084115.json:
```json
{
    "body": "Since the file is empty, I can't do think of any way to actually do this with HG.  It seems impossible.  \n\n```\nflat:matrix wstein$ hg rm  padics\nremoving padics/__init__.py\nflat:matrix wstein$ \nflat:matrix wstein$ \nflat:matrix wstein$ hg ci\nflat:matrix wstein$ hg export ip\nabort: unknown revision 'ip'!\nflat:matrix wstein$ hg export tip\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1281549848 25200\n# Node ID 029114d1f8a76cbd4d88b2a9a28fecadac170205\n# Parent  5b338f2e484f2065d3d30d47bc204d6e9ed13d12\ntrac 9064 -- remove p-adic matrix directory\n```\n\n(see nothing!)\n\nSo there is no patch to post, and I take David Roe's statement (above) as a positive review.\n\nSo to the release manager merging this, just do the following:\n\n\n```\ncd SAGE_ROOT/devel/sage/sage/matrix\nsage -hg rm  padics\nsage -hg ci\n```\n\n\nand checkin the resulting empty patch.    Unfortunately, this won't do anything for people doing \"sage -upgrade\".  Anyway, it's an empty directory so whatever happens is pretty harmless.",
    "created_at": "2010-08-11T18:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9064#issuecomment-84115",
    "user": "was"
}
```

Since the file is empty, I can't do think of any way to actually do this with HG.  It seems impossible.  

```
flat:matrix wstein$ hg rm  padics
removing padics/__init__.py
flat:matrix wstein$ 
flat:matrix wstein$ 
flat:matrix wstein$ hg ci
flat:matrix wstein$ hg export ip
abort: unknown revision 'ip'!
flat:matrix wstein$ hg export tip
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1281549848 25200
# Node ID 029114d1f8a76cbd4d88b2a9a28fecadac170205
# Parent  5b338f2e484f2065d3d30d47bc204d6e9ed13d12
trac 9064 -- remove p-adic matrix directory
```

(see nothing!)

So there is no patch to post, and I take David Roe's statement (above) as a positive review.

So to the release manager merging this, just do the following:


```
cd SAGE_ROOT/devel/sage/sage/matrix
sage -hg rm  padics
sage -hg ci
```


and checkin the resulting empty patch.    Unfortunately, this won't do anything for people doing "sage -upgrade".  Anyway, it's an empty directory so whatever happens is pretty harmless.



---

archive/issue_comments_084116.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-11T18:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9064#issuecomment-84116",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084117.json:
```json
{
    "body": "Remove matrix/padics.",
    "created_at": "2010-08-31T01:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9064#issuecomment-84117",
    "user": "mpatel"
}
```

Remove matrix/padics.



---

archive/issue_comments_084118.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:1 was]:\n> So there is no patch to post, and I take David Roe's statement (above) as a positive review.\n\nI've attached a patch made with the Mercurial queues extension.",
    "created_at": "2010-08-31T02:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9064#issuecomment-84118",
    "user": "mpatel"
}
```

Attachment

Replying to [comment:1 was]:
> So there is no patch to post, and I take David Roe's statement (above) as a positive review.

I've attached a patch made with the Mercurial queues extension.



---

archive/issue_comments_084119.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-31T03:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9064#issuecomment-84119",
    "user": "mpatel"
}
```

Resolution: fixed
