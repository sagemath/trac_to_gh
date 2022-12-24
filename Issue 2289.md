# Issue 2289: [with doc patch, needs review] make the constructions document prettier and more consistent

archive/issues_002289.json:
```json
{
    "body": "Assignee: tba\n\nThe patch is somewhat big but most of the changes are cosmetic, aimed at making const.tex more consistent internally (and with the tutorial) and prettier to behold.\n\nI've also exposed a number of examples that were %skip-ped previously, tested them and fixed a few of them that were buggy.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2289\n\n",
    "created_at": "2008-02-24T04:08:14Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with doc patch, needs review] make the constructions document prettier and more consistent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2289",
    "user": "AlexGhitza"
}
```
Assignee: tba

The patch is somewhat big but most of the changes are cosmetic, aimed at making const.tex more consistent internally (and with the tutorial) and prettier to behold.

I've also exposed a number of examples that were %skip-ped previously, tested them and fixed a few of them that were buggy.


Issue created by migration from https://trac.sagemath.org/ticket/2289





---

archive/issue_comments_015179.json:
```json
{
    "body": "I think this patch should be made after applying the earlier patch at\nhttp://trac.sagemath.org/sage_trac/ticket/2274\n(which is still waiting for review) for const.tex. However, that patch requires the coding theory patch (also in ticket 2274) as well to pass sage -t.",
    "created_at": "2008-02-24T14:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15179",
    "user": "wdj"
}
```

I think this patch should be made after applying the earlier patch at
http://trac.sagemath.org/sage_trac/ticket/2274
(which is still waiting for review) for const.tex. However, that patch requires the coding theory patch (also in ticket 2274) as well to pass sage -t.



---

archive/issue_comments_015180.json:
```json
{
    "body": "The above-mentioned patch for 2274 just got a positive review, so it is okay to make your change on top of it now.",
    "created_at": "2008-02-24T19:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15180",
    "user": "wdj"
}
```

The above-mentioned patch for 2274 just got a positive review, so it is okay to make your change on top of it now.



---

archive/issue_comments_015181.json:
```json
{
    "body": "OK, so I incorporated David's 435.patch from #2274, and retested after applying 8672.patch also from #2274.\n\nI replaced my old patch with the new and improved one.",
    "created_at": "2008-02-24T20:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15181",
    "user": "AlexGhitza"
}
```

OK, so I incorporated David's 435.patch from #2274, and retested after applying 8672.patch also from #2274.

I replaced my old patch with the new and improved one.



---

archive/issue_comments_015182.json:
```json
{
    "body": "I applied this patch to const.tex in sage-2.10.3.alpha0 and got:\n4 out of 153 hunks FAILED -- saving rejects to file devel/doc/const/const.tex.rej\n\nI'm not sure that the problem is. Could the patch possibly be recreated using\nsage-2.10.3.alpha0?",
    "created_at": "2008-02-26T23:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15182",
    "user": "wdj"
}
```

I applied this patch to const.tex in sage-2.10.3.alpha0 and got:
4 out of 153 hunks FAILED -- saving rejects to file devel/doc/const/const.tex.rej

I'm not sure that the problem is. Could the patch possibly be recreated using
sage-2.10.3.alpha0?



---

archive/issue_comments_015183.json:
```json
{
    "body": "Hi, I know exactly what the problem is.  When your coding theory patch from #2274 got merged, so did your modifications to const.tex that you had made there.  But I had already merged them into my patch here, so mercurial got confused.\n\nBut no worries.  I've fixed things and rebased the patch against sage-2.10.3.alpha0, so it should all be good now.\n\nNote that if you take a look at const.pdf, there are still a few long lines.  They are trickier to deal with (wrapping them breaks doctests, etc.) so I'm still thinking about it.  This is also an issue with tut.tex (in a few places).  It will have to get fixed later...",
    "created_at": "2008-02-27T00:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15183",
    "user": "AlexGhitza"
}
```

Hi, I know exactly what the problem is.  When your coding theory patch from #2274 got merged, so did your modifications to const.tex that you had made there.  But I had already merged them into my patch here, so mercurial got confused.

But no worries.  I've fixed things and rebased the patch against sage-2.10.3.alpha0, so it should all be good now.

Note that if you take a look at const.pdf, there are still a few long lines.  They are trickier to deal with (wrapping them breaks doctests, etc.) so I'm still thinking about it.  This is also an issue with tut.tex (in a few places).  It will have to get fixed later...



---

archive/issue_comments_015184.json:
```json
{
    "body": "Attachment [doc_const_fixes.patch](tarball://root/attachments/some-uuid/ticket2289/doc_const_fixes.patch) by AlexGhitza created at 2008-02-27 04:45:54\n\nfixed some doctest failures",
    "created_at": "2008-02-27T04:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15184",
    "user": "AlexGhitza"
}
```

Attachment [doc_const_fixes.patch](tarball://root/attachments/some-uuid/ticket2289/doc_const_fixes.patch) by AlexGhitza created at 2008-02-27 04:45:54

fixed some doctest failures



---

archive/issue_comments_015185.json:
```json
{
    "body": "This patch is rather large and does not apply cleanly for me to the 2.10.3.alpha0 base (there were 4 rejects, but does now pass sage -t and I recommend acceptance.",
    "created_at": "2008-02-27T11:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15185",
    "user": "wdj"
}
```

This patch is rather large and does not apply cleanly for me to the 2.10.3.alpha0 base (there were 4 rejects, but does now pass sage -t and I recommend acceptance.



---

archive/issue_comments_015186.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T21:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15186",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015187.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T21:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2289#issuecomment-15187",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0
