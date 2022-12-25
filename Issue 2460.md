# Issue 2460: some issues with factorization.py

archive/issues_002460.json:
```json
{
    "body": "Assignee: somebody\n\nVarious people worked on factorization.py and unfortunately ignored some implicit \nassumptions in what that code is supposed to do.  In particular, this function\n\n```\n    def base_ring(self):\n        if len(self) > 0:\n            return self[0][0].parent()\n        else:\n            return self.unit().parent()\n```\n\nassumes that (1) ever element has the same parent, and (2) the parent is a ring.\nNeither assumption need be satisfied.   \n\nThis is_commutative function then relies on base_ring working.  \nHere's an example of this leading to *wrong* answers:\n\n```\nsage: R.<x,y> = FreeAlgebra(QQ,2)\nsage: Factorization([(3,1), (x,2), (y,3), (x,1), (y,2)])\n3 * x^3 * y^5\n```\n\n\nProposal: Simply call Sequence on the list of bases in the factorization\nto get a new list where the basis lie in a common university.  Then refine\nis_commutative to mean that the universe is a commuative ring, and only then\ncommute factors automatically.\n\nSecond, after the above is resolved, the sort function for comparison \nshould call universe() (not base_ring) and use some sensible defaults,\nbefore resorting to that mess of code in the current sort method. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2460\n\n",
    "created_at": "2008-03-10T16:02:43Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "some issues with factorization.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2460",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

Various people worked on factorization.py and unfortunately ignored some implicit 
assumptions in what that code is supposed to do.  In particular, this function

```
    def base_ring(self):
        if len(self) > 0:
            return self[0][0].parent()
        else:
            return self.unit().parent()
```

assumes that (1) ever element has the same parent, and (2) the parent is a ring.
Neither assumption need be satisfied.   

This is_commutative function then relies on base_ring working.  
Here's an example of this leading to *wrong* answers:

```
sage: R.<x,y> = FreeAlgebra(QQ,2)
sage: Factorization([(3,1), (x,2), (y,3), (x,1), (y,2)])
3 * x^3 * y^5
```


Proposal: Simply call Sequence on the list of bases in the factorization
to get a new list where the basis lie in a common university.  Then refine
is_commutative to mean that the universe is a commuative ring, and only then
commute factors automatically.

Second, after the above is resolved, the sort function for comparison 
should call universe() (not base_ring) and use some sensible defaults,
before resorting to that mess of code in the current sort method. 



Issue created by migration from https://trac.sagemath.org/ticket/2460





---

archive/issue_comments_016620.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T16:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16620",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016621.json:
```json
{
    "body": "Changing assignee from somebody to @williamstein.",
    "created_at": "2008-03-10T16:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16621",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from somebody to @williamstein.



---

archive/issue_comments_016622.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-10T16:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16622",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_016623.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-10T16:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16623",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from assigned to new.



---

archive/issue_comments_016624.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T16:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16624",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016625.json:
```json
{
    "body": "Attachment [trac_2460.patch](tarball://root/attachments/some-uuid/ticket2460/trac_2460.patch) by @garyfurnish created at 2008-03-10 16:29:45",
    "created_at": "2008-03-10T16:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16625",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2460.patch](tarball://root/attachments/some-uuid/ticket2460/trac_2460.patch) by @garyfurnish created at 2008-03-10 16:29:45



---

archive/issue_comments_016626.json:
```json
{
    "body": "There is a possibility that fixing commutativity may other things.",
    "created_at": "2008-03-10T16:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16626",
    "user": "https://github.com/garyfurnish"
}
```

There is a possibility that fixing commutativity may other things.



---

archive/issue_comments_016627.json:
```json
{
    "body": "Changing assignee from @garyfurnish to @williamstein.",
    "created_at": "2008-03-10T17:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16627",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @garyfurnish to @williamstein.



---

archive/issue_comments_016628.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-10T17:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16628",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from assigned to new.



---

archive/issue_comments_016629.json:
```json
{
    "body": "There are non-trivial issues involved with fixing this (namely, moving things to the universe causes issues with repr and commutes, and I can't find a way to fix those issues without refactoring other code to make this work well, so this should probably see some discussion.",
    "created_at": "2008-03-10T17:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16629",
    "user": "https://github.com/garyfurnish"
}
```

There are non-trivial issues involved with fixing this (namely, moving things to the universe causes issues with repr and commutes, and I can't find a way to fix those issues without refactoring other code to make this work well, so this should probably see some discussion.



---

archive/issue_events_005798.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2008-06-20T04:46:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2460#event-5798"
}
```



---

archive/issue_comments_016630.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-20T04:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16630",
    "user": "https://github.com/craigcitro"
}
```

Resolution: invalid



---

archive/issue_comments_016631.json:
```json
{
    "body": "Hi Carig,\n\nnot to be prickly Pete, but can give a reason why this was invalidated?\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T05:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16631",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Carig,

not to be prickly Pete, but can give a reason why this was invalidated?

Cheers,

Michael



---

archive/issue_comments_016632.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-06-27T20:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16632",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_016633.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-06-27T20:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16633",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005799.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-06-27T20:20:25Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2460#event-5799"
}
```



---

archive/issue_comments_016634.json:
```json
{
    "body": "Woah -- I incorrectly thought this had long since been fixed.  NOT.\n\n```\nsage: R.<x,y> = FreeAlgebra(QQ,2)\nsage: sage: Factorization([(3,1), (x,2), (y,3), (x,1), (y,2)])\n3 * x^3 * y^5\n```\n",
    "created_at": "2008-06-27T20:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16634",
    "user": "https://github.com/williamstein"
}
```

Woah -- I incorrectly thought this had long since been fixed.  NOT.

```
sage: R.<x,y> = FreeAlgebra(QQ,2)
sage: sage: Factorization([(3,1), (x,2), (y,3), (x,1), (y,2)])
3 * x^3 * y^5
```




---

archive/issue_comments_016635.json:
```json
{
    "body": "Ok, moving this back to a current milestone so that it can be seen :)\n\nCheers,\n\nMichael",
    "created_at": "2008-07-03T07:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16635",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, moving this back to a current milestone so that it can be seen :)

Cheers,

Michael



---

archive/issue_events_005800.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-03T07:08:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2460#event-5800"
}
```



---

archive/issue_comments_016636.json:
```json
{
    "body": "William, \n\ncan you be the editor of this patch? Feel free to bounce it back to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T11:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16636",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William, 

can you be the editor of this patch? Feel free to bounce it back to me.

Cheers,

Michael



---

archive/issue_comments_016637.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-07-06T11:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16637",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_016638.json:
```json
{
    "body": "Looking at factorization.py I was all ready to fix all the problems I could see -- using Sequence to get a common universe for the bases on construction, cache this base_ring, only allow operations between factorizations with the same base_ring, and so on.\n\nBut then I saw what appeared to be a totally weird example:\n\n\n```\nsage: F = Factorization([(ZZ^3, 2), (ZZ^2, 5)], cr=True); F\n(Ambient free module of rank 2 over the principal ideal domain Integer Ring)^5 * \n(Ambient free module of rank 3 over the principal ideal domain Integer Ring)^2            \n```\n\nThis bears no relation at all to what I thought the Factorization class was for.  Doing a search_src showed that this is designed in to support splitting of modular symbols spaces (and similar).\n\nThis leaves a question almost certainly for William:  is it really sensible to have one class serve both as the structure to hold \"prime factorizations\" for UFDs and other rings, as well as to hold lists of subspaces with multiplicities?\n\nIf so, perhaps we need to refactor this to have a base class which just handles the basics, with (at least) 2 derived classes, one for rings factorizations and one for additive decompositions?\n\nJohn\n\n# I have added this posting to trac#2460 too.",
    "created_at": "2008-08-22T17:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16638",
    "user": "https://github.com/JohnCremona"
}
```

Looking at factorization.py I was all ready to fix all the problems I could see -- using Sequence to get a common universe for the bases on construction, cache this base_ring, only allow operations between factorizations with the same base_ring, and so on.

But then I saw what appeared to be a totally weird example:


```
sage: F = Factorization([(ZZ^3, 2), (ZZ^2, 5)], cr=True); F
(Ambient free module of rank 2 over the principal ideal domain Integer Ring)^5 * 
(Ambient free module of rank 3 over the principal ideal domain Integer Ring)^2            
```

This bears no relation at all to what I thought the Factorization class was for.  Doing a search_src showed that this is designed in to support splitting of modular symbols spaces (and similar).

This leaves a question almost certainly for William:  is it really sensible to have one class serve both as the structure to hold "prime factorizations" for UFDs and other rings, as well as to hold lists of subspaces with multiplicities?

If so, perhaps we need to refactor this to have a base class which just handles the basics, with (at least) 2 derived classes, one for rings factorizations and one for additive decompositions?

John

# I have added this posting to trac#2460 too.



---

archive/issue_comments_016639.json:
```json
{
    "body": "I think the issues raised here have all been dealt with by the patches I put up at #3927 (which started out as a separate enhancement, hence the new ticket).  In particular the good parts of the patch attached to this ticket have been used there.\n\nI suggest that this ticket be closed, with a link to #3927 instead.",
    "created_at": "2008-08-23T16:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16639",
    "user": "https://github.com/JohnCremona"
}
```

I think the issues raised here have all been dealt with by the patches I put up at #3927 (which started out as a separate enhancement, hence the new ticket).  In particular the good parts of the patch attached to this ticket have been used there.

I suggest that this ticket be closed, with a link to #3927 instead.



---

archive/issue_events_005801.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:52:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2460#event-5801"
}
```



---

archive/issue_events_005802.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:52:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2460#event-5802"
}
```



---

archive/issue_events_005803.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:52:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2460#event-5803"
}
```



---

archive/issue_comments_016640.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T08:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16640",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_016641.json:
```json
{
    "body": "I think that this can be closed as well due to #3927.",
    "created_at": "2008-11-14T08:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2460#issuecomment-16641",
    "user": "https://github.com/mwhansen"
}
```

I think that this can be closed as well due to #3927.
