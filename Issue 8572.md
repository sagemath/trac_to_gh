# Issue 8572: Doc of poset appear as void if called from the console.

archive/issues_008572.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri @qed777\n\nKeywords: Poset, sphinx\n\nTry\n\n```\nPoset?\n```\n\nunder the console and nothing appear.\nSee\n\n```\nhttp://groups.google.com/group/sage-devel/t/b9baaa6943fc0df4\n```\n\nfor a discussion: It is not clear if it's a sphinx bug or a Poset doc bug. I haven't been able to reproduce it from any other file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8572\n\n",
    "created_at": "2010-03-21T19:52:16Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Doc of poset appear as void if called from the console.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8572",
    "user": "https://github.com/hivert"
}
```
Assignee: mvngu

CC:  @jhpalmieri @qed777

Keywords: Poset, sphinx

Try

```
Poset?
```

under the console and nothing appear.
See

```
http://groups.google.com/group/sage-devel/t/b9baaa6943fc0df4
```

for a discussion: It is not clear if it's a sphinx bug or a Poset doc bug. I haven't been able to reproduce it from any other file.

Issue created by migration from https://trac.sagemath.org/ticket/8572





---

archive/issue_comments_077504.json:
```json
{
    "body": "A little more data:\n\n```\nsage: from sage.misc.sageinspect import _sage_getdoc_unformatted\nsage: from sagenb.misc.sphinxify import sphinxify\nsage: r = _sage_getdoc_unformatted(Poset)\nsage: len(sphinxify(r[:1438], format='text'))\n1382\nsage: len(sphinxify(r[:1439], format='text'))\n0\n```\n",
    "created_at": "2010-03-21T20:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77504",
    "user": "https://github.com/jhpalmieri"
}
```

A little more data:

```
sage: from sage.misc.sageinspect import _sage_getdoc_unformatted
sage: from sagenb.misc.sphinxify import sphinxify
sage: r = _sage_getdoc_unformatted(Poset)
sage: len(sphinxify(r[:1438], format='text'))
1382
sage: len(sphinxify(r[:1439], format='text'))
0
```




---

archive/issue_comments_077505.json:
```json
{
    "body": "Changing assignee from mvngu to @hivert.",
    "created_at": "2010-03-21T21:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77505",
    "user": "https://github.com/hivert"
}
```

Changing assignee from mvngu to @hivert.



---

archive/issue_comments_077506.json:
```json
{
    "body": "Attachment [trac_8572-poset_doc_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8572/trac_8572-poset_doc_fix-fh.patch) by @hivert created at 2010-03-21 21:57:33\n\nHi John,\n\n> A little more data:\n\n```\nsage: from sage.misc.sageinspect import _sage_getdoc_unformatted\nsage: from sagenb.misc.sphinxify import sphinxify\nsage: r = _sage_getdoc_unformatted(Poset)\nsage: len(sphinxify(r[:1438], format='text'))\n1382\nsage: len(sphinxify(r[:1439], format='text'))\n0\n```\n\n\nI don't know how you got it but this was exactly the problem: an extraneous space at the 1438th character ! Please review.\n\nFlorent",
    "created_at": "2010-03-21T21:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77506",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8572-poset_doc_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8572/trac_8572-poset_doc_fix-fh.patch) by @hivert created at 2010-03-21 21:57:33

Hi John,

> A little more data:

```
sage: from sage.misc.sageinspect import _sage_getdoc_unformatted
sage: from sagenb.misc.sphinxify import sphinxify
sage: r = _sage_getdoc_unformatted(Poset)
sage: len(sphinxify(r[:1438], format='text'))
1382
sage: len(sphinxify(r[:1439], format='text'))
0
```


I don't know how you got it but this was exactly the problem: an extraneous space at the 1438th character ! Please review.

Florent



---

archive/issue_comments_077507.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-21T22:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77507",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077508.json:
```json
{
    "body": "> I don't know how you got it but this was exactly the problem: an extraneous space at the 1438th character ! Please review.\n\nNote: it would be much better if sphinx raised a warning instead of failing silently. Should we open a ticket for this or report it upstream ?",
    "created_at": "2010-03-21T22:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77508",
    "user": "https://github.com/hivert"
}
```

> I don't know how you got it but this was exactly the problem: an extraneous space at the 1438th character ! Please review.

Note: it would be much better if sphinx raised a warning instead of failing silently. Should we open a ticket for this or report it upstream ?



---

archive/issue_comments_077509.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> > I don't know how you got it \n\nBinary search: `sphinxify(r[:n], format='text')` for various values of n.\n\n> but this was exactly the problem: an extraneous space at the 1438th character ! Please review.\n> \n> Note: it would be much better if sphinx raised a warning instead of failing silently. Should we open a ticket for this or report it upstream ?\n\nOr maybe it's how we're invoking Sphinx?  I'm not sure.  We could also add the hack I suggested on sage-devel, as a backup plan for similar situations.  That could go on another ticket.",
    "created_at": "2010-03-21T22:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77509",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:3 hivert]:
> > I don't know how you got it 

Binary search: `sphinxify(r[:n], format='text')` for various values of n.

> but this was exactly the problem: an extraneous space at the 1438th character ! Please review.
> 
> Note: it would be much better if sphinx raised a warning instead of failing silently. Should we open a ticket for this or report it upstream ?

Or maybe it's how we're invoking Sphinx?  I'm not sure.  We could also add the hack I suggested on sage-devel, as a backup plan for similar situations.  That could go on another ticket.



---

archive/issue_comments_077510.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-21T22:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77510",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077511.json:
```json
{
    "body": "Merged \"trac_8572-poset_doc_fix-fh.patch\" in 4.4.alpha0",
    "created_at": "2010-04-16T18:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77511",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8572-poset_doc_fix-fh.patch" in 4.4.alpha0



---

archive/issue_events_020694.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:48:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8572#event-20694"
}
```



---

archive/issue_comments_077512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8572#issuecomment-77512",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
