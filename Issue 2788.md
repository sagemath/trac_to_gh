# Issue 2788: [with patch, needs review] update hypellfrob to 2.1

archive/issues_002788.json:
```json
{
    "body": "Assignee: was\n\nThis patch updates hypellfrob to version 2.1, which is somewhat faster than the current 2.0.\n\nDepends on `zn_poly-0.8` (#2786).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2788\n\n",
    "created_at": "2008-04-03T03:27:43Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] update hypellfrob to 2.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2788",
    "user": "dmharvey"
}
```
Assignee: was

This patch updates hypellfrob to version 2.1, which is somewhat faster than the current 2.0.

Depends on `zn_poly-0.8` (#2786).


Issue created by migration from https://trac.sagemath.org/ticket/2788





---

archive/issue_comments_019151.json:
```json
{
    "body": "Attachment [hypellfrob.patch](tarball://root/attachments/some-uuid/ticket2788/hypellfrob.patch) by mabshoff created at 2008-04-03 18:28:38\n\nPatch looks good to me, applies cleanly. I understood all the trivial changes, but I am no expert on the finer details toward the end of the patch. So what I want to express is that somebody with a more detailed understanding ought to give this a second look. After updating to `zn_poly-0.8.spkg` and touching the right files all doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T18:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2788#issuecomment-19151",
    "user": "mabshoff"
}
```

Attachment [hypellfrob.patch](tarball://root/attachments/some-uuid/ticket2788/hypellfrob.patch) by mabshoff created at 2008-04-03 18:28:38

Patch looks good to me, applies cleanly. I understood all the trivial changes, but I am no expert on the finer details toward the end of the patch. So what I want to express is that somebody with a more detailed understanding ought to give this a second look. After updating to `zn_poly-0.8.spkg` and touching the right files all doctests pass.

Cheers,

Michael



---

archive/issue_comments_019152.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> Patch looks good to me, applies cleanly. I understood all the trivial changes, but I am no expert on the finer details toward the end of the patch. So what I want to express is that somebody with a more detailed understanding ought to give this a second look. After updating to `zn_poly-0.8.spkg` and touching the right files all doctests pass.\n\nHi michael,\n\nI think it would be difficult to find someone willing to sign off on all the \"finer details\". It's quite technical code... when I released this code separately (about six weeks ago), I wrote on the changelog:\n\n* improved memory consumption in zn_poly version (about 33% less memory)\n* improved speed via preconditioned middle products in zn_poly version\n* now requires zn_poly version 0.6\n\nSo most of the changes you are seeing there are just rearranging the memory layout of the computation, and eliminating redundant computations.\n\nBut this raises an interesting question: what is the difference between this patch and the `zn_poly` spkg I submitted earlier (the latter included about 10000-15000 lines of new code)? I consider both to be extremely technical code for which a proper peer review would be very difficult to perform in a reasonable amount of time. But for `zn_poly`, you didn't raise any questions about reviewing the new code.\n\nI'm not trying to criticise you here, I'm just trying to identify exactly what our procedures are. For example if I had put hypellfrob into an spkg, rather than integrating it directly into the sage library, does that change the standard for review?",
    "created_at": "2008-04-03T18:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2788#issuecomment-19152",
    "user": "dmharvey"
}
```

Replying to [comment:1 mabshoff]:
> Patch looks good to me, applies cleanly. I understood all the trivial changes, but I am no expert on the finer details toward the end of the patch. So what I want to express is that somebody with a more detailed understanding ought to give this a second look. After updating to `zn_poly-0.8.spkg` and touching the right files all doctests pass.

Hi michael,

I think it would be difficult to find someone willing to sign off on all the "finer details". It's quite technical code... when I released this code separately (about six weeks ago), I wrote on the changelog:

* improved memory consumption in zn_poly version (about 33% less memory)
* improved speed via preconditioned middle products in zn_poly version
* now requires zn_poly version 0.6

So most of the changes you are seeing there are just rearranging the memory layout of the computation, and eliminating redundant computations.

But this raises an interesting question: what is the difference between this patch and the `zn_poly` spkg I submitted earlier (the latter included about 10000-15000 lines of new code)? I consider both to be extremely technical code for which a proper peer review would be very difficult to perform in a reasonable amount of time. But for `zn_poly`, you didn't raise any questions about reviewing the new code.

I'm not trying to criticise you here, I'm just trying to identify exactly what our procedures are. For example if I had put hypellfrob into an spkg, rather than integrating it directly into the sage library, does that change the standard for review?



---

archive/issue_comments_019153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T19:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2788#issuecomment-19153",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019154.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-03T19:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2788#issuecomment-19154",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_019155.json:
```json
{
    "body": "Replying to [comment:2 dmharvey]:\n> Hi michael,\n> \n> I think it would be difficult to find someone willing to sign off on all the \"finer details\". It's quite technical code... when I released this code separately (about six weeks ago), I wrote on the changelog:\n> \n>  * improved memory consumption in zn_poly version (about 33% less memory)\n>  * improved speed via preconditioned middle products in zn_poly version\n>  * now requires zn_poly version 0.6\n> \n> So most of the changes you are seeing there are just rearranging the memory layout of the computation, and eliminating redundant computations.\n> \n> But this raises an interesting question: what is the difference between this patch and the `zn_poly` spkg I submitted earlier (the latter included about 10000-15000 lines of new code)? I consider both to be extremely technical code for which a proper peer review would be very difficult to perform in a reasonable amount of time. But for `zn_poly`, you didn't raise any questions about reviewing the new code.\n\nWell, we did discuss this in IRC and I think it boils down to this:\n\n* we do not have the man power to review SPKGs code in general\n* we have to rely on doctesting and valgrind to assure that the code doesn't do anything stupid\n* in an ideal world we could review SPKGs, but here we also rely on the authors and if it exists their test suite\n* If you had a close collaborator it would be the perfect person to review this\n\n> I'm not trying to criticise you here, I'm just trying to identify exactly what our procedures are. For example if I had put hypellfrob into an spkg, rather than integrating it directly into the sage library, does that change the standard for review?\n\n* theoretically: yes :)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T19:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2788#issuecomment-19155",
    "user": "mabshoff"
}
```

Replying to [comment:2 dmharvey]:
> Hi michael,
> 
> I think it would be difficult to find someone willing to sign off on all the "finer details". It's quite technical code... when I released this code separately (about six weeks ago), I wrote on the changelog:
> 
>  * improved memory consumption in zn_poly version (about 33% less memory)
>  * improved speed via preconditioned middle products in zn_poly version
>  * now requires zn_poly version 0.6
> 
> So most of the changes you are seeing there are just rearranging the memory layout of the computation, and eliminating redundant computations.
> 
> But this raises an interesting question: what is the difference between this patch and the `zn_poly` spkg I submitted earlier (the latter included about 10000-15000 lines of new code)? I consider both to be extremely technical code for which a proper peer review would be very difficult to perform in a reasonable amount of time. But for `zn_poly`, you didn't raise any questions about reviewing the new code.

Well, we did discuss this in IRC and I think it boils down to this:

* we do not have the man power to review SPKGs code in general
* we have to rely on doctesting and valgrind to assure that the code doesn't do anything stupid
* in an ideal world we could review SPKGs, but here we also rely on the authors and if it exists their test suite
* If you had a close collaborator it would be the perfect person to review this

> I'm not trying to criticise you here, I'm just trying to identify exactly what our procedures are. For example if I had put hypellfrob into an spkg, rather than integrating it directly into the sage library, does that change the standard for review?

* theoretically: yes :)

Cheers,

Michael
