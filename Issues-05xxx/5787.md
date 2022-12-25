# Issue 5787: [with third patch, with positive review] Improve doctest coverage for sage/modular/hecke (continued)

archive/issues_005787.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: doctests\n\nThis is a continuation of #5736. The patch which I am about to upload contains more doctests and bugfixes for sage/modular/hecke. The main change this makes is in the methods for constructing elements of Hecke algebras: previously these accepted more or less arbitrary matrices as input (despite the fact that all Hecke algebras in Sage are supposed to be commutative). Similarly, any element of a full Hecke algebra could be coerced into the corresponding anemic algebra -- including the Hecke operators at primes dividing the level -- which is not great.\n\nI've also added an extra check into the !__mul!__ method of the MatrixMorphism class; what's the point of having morphism objects that remember their domain and codomain if one doesn't check compatibility when composing them?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5787\n\n",
    "closed_at": "2009-05-11T08:28:35Z",
    "created_at": "2009-04-14T21:06:02Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with third patch, with positive review] Improve doctest coverage for sage/modular/hecke (continued)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5787",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd

Keywords: doctests

This is a continuation of #5736. The patch which I am about to upload contains more doctests and bugfixes for sage/modular/hecke. The main change this makes is in the methods for constructing elements of Hecke algebras: previously these accepted more or less arbitrary matrices as input (despite the fact that all Hecke algebras in Sage are supposed to be commutative). Similarly, any element of a full Hecke algebra could be coerced into the corresponding anemic algebra -- including the Hecke operators at primes dividing the level -- which is not great.

I've also added an extra check into the !__mul!__ method of the MatrixMorphism class; what's the point of having morphism objects that remember their domain and codomain if one doesn't check compatibility when composing them?

Issue created by migration from https://trac.sagemath.org/ticket/5787





---

archive/issue_comments_045207.json:
```json
{
    "body": "Oops -- sorry, I messed up, that patch was incomplete (it applies OK but doctests do not pass). Please use both the patches above; then it will work.",
    "created_at": "2009-04-15T14:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45207",
    "user": "https://github.com/loefflerd"
}
```

Oops -- sorry, I messed up, that patch was incomplete (it applies OK but doctests do not pass). Please use both the patches above; then it will work.



---

archive/issue_comments_045208.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-15T14:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45208",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045209.json:
```json
{
    "body": "replaces all previous patches",
    "created_at": "2009-05-04T16:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45209",
    "user": "https://github.com/loefflerd"
}
```

replaces all previous patches



---

archive/issue_comments_045210.json:
```json
{
    "body": "Attachment [trac_5787-all.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787-all.patch) by @loefflerd created at 2009-05-04 16:49:46\n\nThe patch I've just uploaded unifies the previous two patches, and adds some more doctests to bring the coverage higher still (although not quite to 100% as I don't have time right now to understand some of the weirder things that are going on in hecke/submodule.py). Note that again this patch is designed to be applied over the patches at #5736.",
    "created_at": "2009-05-04T16:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45210",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5787-all.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787-all.patch) by @loefflerd created at 2009-05-04 16:49:46

The patch I've just uploaded unifies the previous two patches, and adds some more doctests to bring the coverage higher still (although not quite to 100% as I don't have time right now to understand some of the weirder things that are going on in hecke/submodule.py). Note that again this patch is designed to be applied over the patches at #5736.



---

archive/issue_comments_045211.json:
```json
{
    "body": "Attachment [trac_5787_pt2.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787_pt2.patch) by @craigcitro created at 2009-05-08 09:44:31",
    "created_at": "2009-05-08T09:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45211",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_5787_pt2.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787_pt2.patch) by @craigcitro created at 2009-05-08 09:44:31



---

archive/issue_comments_045212.json:
```json
{
    "body": "This looks good. I started adding a few changes while refereeing, and then I got motivated and went ahead and finished doctesting `sage/modular/hecke`. So positive review for David's part, and now someone needs to review my (much shorter) patch. After this, the only part of `sage/modular` still needing any doctesting is the `modsym` directory.",
    "created_at": "2009-05-08T09:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45212",
    "user": "https://github.com/craigcitro"
}
```

This looks good. I started adding a few changes while refereeing, and then I got motivated and went ahead and finished doctesting `sage/modular/hecke`. So positive review for David's part, and now someone needs to review my (much shorter) patch. After this, the only part of `sage/modular` still needing any doctesting is the `modsym` directory.



---

archive/issue_comments_045213.json:
```json
{
    "body": "Replying to [comment:3 craigcitro]:\n> This looks good. I started adding a few changes while refereeing, and then I got motivated and went ahead and finished doctesting `sage/modular/hecke`. So positive review for David's part, and now someone needs to review my (much shorter) patch. After this, the only part of `sage/modular` still needing any doctesting is the `modsym` directory. \n\n\nI think it would be better for David to review Craig's extra patch rather than a newcomer.\n\nLast docdays I started properly doctesting modsym, but only got two of the files done.  I do intend to do more.",
    "created_at": "2009-05-09T17:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45213",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 craigcitro]:
> This looks good. I started adding a few changes while refereeing, and then I got motivated and went ahead and finished doctesting `sage/modular/hecke`. So positive review for David's part, and now someone needs to review my (much shorter) patch. After this, the only part of `sage/modular` still needing any doctesting is the `modsym` directory. 


I think it would be better for David to review Craig's extra patch rather than a newcomer.

Last docdays I started properly doctesting modsym, but only got two of the files done.  I do intend to do more.



---

archive/issue_comments_045214.json:
```json
{
    "body": "At a glance, I can spot two small problems: firstly, the new doctest for `__cmp__` in submodule.py fails on my machine; secondly, Craig's patch changes the intersection method (so it works for modular forms spaces as well as modular symbols) but I also did the same in #4357, so those are going to conflict.\n\nI'm not entirely sure why the first failure happens: although `__cmp__` doctests are always irritatingly machine-dependent when comparing objects of different types, the comparison order for submodules of a common ambient module should be consistent, surely? I'm changing this back to \"needs work\" until we can get to the bottom of this. Once that's sorted I'll do a rebased version that combines this with #4357.\n\nDavid",
    "created_at": "2009-05-10T12:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45214",
    "user": "https://github.com/loefflerd"
}
```

At a glance, I can spot two small problems: firstly, the new doctest for `__cmp__` in submodule.py fails on my machine; secondly, Craig's patch changes the intersection method (so it works for modular forms spaces as well as modular symbols) but I also did the same in #4357, so those are going to conflict.

I'm not entirely sure why the first failure happens: although `__cmp__` doctests are always irritatingly machine-dependent when comparing objects of different types, the comparison order for submodules of a common ambient module should be consistent, surely? I'm changing this back to "needs work" until we can get to the bottom of this. Once that's sorted I'll do a rebased version that combines this with #4357.

David



---

archive/issue_comments_045215.json:
```json
{
    "body": "Attachment [trac_5787_pt2_rebased.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787_pt2_rebased.patch) by @loefflerd created at 2009-05-10 21:32:24\n\nrebased not  to conflict with #4357",
    "created_at": "2009-05-10T21:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45215",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5787_pt2_rebased.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787_pt2_rebased.patch) by @loefflerd created at 2009-05-10 21:32:24

rebased not  to conflict with #4357



---

archive/issue_comments_045216.json:
```json
{
    "body": "Attachment [trac_5787_pt3.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787_pt3.patch) by @loefflerd created at 2009-05-10 21:47:58\n\nOn inspection, it turns out that the `__cmp__` routine was written stupidly anyway, so I rewrote it. Hence the third patch above. So now applying trac_5787-all.patch, trac_5787_pt2_rebased.patch, and trac_5787_pt3.patch (on top of the already-merged #5736 patches and #4357) should not conflict -- at least it doesn't on my machine.\n\nCraig: I'm entirely happy with the rest of your changes, so if you could just check to make sure that applying #5736 + #4357 + the patches here works for you and passes doctests, I think we can call this a positive review at last.",
    "created_at": "2009-05-10T21:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45216",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5787_pt3.patch](tarball://root/attachments/some-uuid/ticket5787/trac_5787_pt3.patch) by @loefflerd created at 2009-05-10 21:47:58

On inspection, it turns out that the `__cmp__` routine was written stupidly anyway, so I rewrote it. Hence the third patch above. So now applying trac_5787-all.patch, trac_5787_pt2_rebased.patch, and trac_5787_pt3.patch (on top of the already-merged #5736 patches and #4357) should not conflict -- at least it doesn't on my machine.

Craig: I'm entirely happy with the rest of your changes, so if you could just check to make sure that applying #5736 + #4357 + the patches here works for you and passes doctests, I think we can call this a positive review at last.



---

archive/issue_comments_045217.json:
```json
{
    "body": "Yep, I'm happy with the changes. I didn't get a chance to do a full doctest run, but Michael surely will when he commits, so I'm going to leave that to him. :)",
    "created_at": "2009-05-11T06:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45217",
    "user": "https://github.com/craigcitro"
}
```

Yep, I'm happy with the changes. I didn't get a chance to do a full doctest run, but Michael surely will when he commits, so I'm going to leave that to him. :)



---

archive/issue_events_013580.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-11T08:28:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5787#event-13580"
}
```



---

archive/issue_comments_045218.json:
```json
{
    "body": "Merged \n\n* trac_5787-all.patch\n* trac_5787_pt2_rebased.patch\n* trac_5787_pt3.patch\n\nin Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T08:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45218",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 

* trac_5787-all.patch
* trac_5787_pt2_rebased.patch
* trac_5787_pt3.patch

in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_045219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T08:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5787#issuecomment-45219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
