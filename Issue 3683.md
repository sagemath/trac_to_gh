# Issue 3683: meataxe interface [with patch, not ready for review]

archive/issues_003683.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @wdjoyner\n\nThis is a start for anyone interested in G-module decompositions using GAP's Meataxe implementations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3683\n\n",
    "created_at": "2008-07-20T03:02:11Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "meataxe interface [with patch, not ready for review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3683",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: joyner

CC:  @wdjoyner

This is a start for anyone interested in G-module decompositions using GAP's Meataxe implementations.

Issue created by migration from https://trac.sagemath.org/ticket/3683





---

archive/issue_comments_026029.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-07-20T20:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26029",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_026030.json:
```json
{
    "body": "The patch 10104 contains all the changes, is based on 3.0.6.rc0, and passed sage -testall. It does not require 10092, so you should ignore that one. This patch adds module_composition_factors (an interface to GAP's meataxe implementation) and as_permutation_group (which returns an isomorphic PermutationGroup). The function module_composition_factors is needed for a research paper (in progress, joint with Amy Ksir and Darren Glass) which will probably be presented at the AMS national meeting in January 2009.",
    "created_at": "2008-07-27T14:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26030",
    "user": "https://github.com/wdjoyner"
}
```

The patch 10104 contains all the changes, is based on 3.0.6.rc0, and passed sage -testall. It does not require 10092, so you should ignore that one. This patch adds module_composition_factors (an interface to GAP's meataxe implementation) and as_permutation_group (which returns an isomorphic PermutationGroup). The function module_composition_factors is needed for a research paper (in progress, joint with Amy Ksir and Darren Glass) which will probably be presented at the AMS national meeting in January 2009.



---

archive/issue_comments_026031.json:
```json
{
    "body": "Sorry that i was unable to look at this earlier. I'll wait for a patch based on a more recent sage-version before writing a full review.\n\nNote, however, that patch 10104 doesn't do what it is supposed to do. \n\nThe doc-string says:\nReturns a *list of triples* consisting of [base field, dimension, irreducibility], \nfor each of the Meataxe composition factors modules.\n\nBut it only returns a list, as can be seen in the example from the doc-string:\n\n```\nsage: G.module_composition_factors() \n[Finite Field of size 7, 2, True] \n```\n\n\nThe reason is the line 896:\n\n`L = L + [sage_eval(gap.eval(\"MCF.field\")), eval(gap.eval(\"MCF.dimension\")), sage_eval(gap.eval(\"MCF.IsIrreducible\"))]`\n\nwhich should be\n\n`L = L + [This is the Trac macro *sage_eval* that was inherited from the migration called with arguments (gap.eval)](https://trac.sagemath.org/wiki/WikiMacros#sage_eval-macro)`",
    "created_at": "2008-08-02T21:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26031",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry that i was unable to look at this earlier. I'll wait for a patch based on a more recent sage-version before writing a full review.

Note, however, that patch 10104 doesn't do what it is supposed to do. 

The doc-string says:
Returns a *list of triples* consisting of [base field, dimension, irreducibility], 
for each of the Meataxe composition factors modules.

But it only returns a list, as can be seen in the example from the doc-string:

```
sage: G.module_composition_factors() 
[Finite Field of size 7, 2, True] 
```


The reason is the line 896:

`L = L + [sage_eval(gap.eval("MCF.field")), eval(gap.eval("MCF.dimension")), sage_eval(gap.eval("MCF.IsIrreducible"))]`

which should be

`L = L + [This is the Trac macro *sage_eval* that was inherited from the migration called with arguments (gap.eval)](https://trac.sagemath.org/wiki/WikiMacros#sage_eval-macro)`



---

archive/issue_comments_026032.json:
```json
{
    "body": "This is a new patch based on sage 3.1.alpha0. Does not require other patches.",
    "created_at": "2008-08-03T02:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26032",
    "user": "https://github.com/wdjoyner"
}
```

This is a new patch based on sage 3.1.alpha0. Does not require other patches.



---

archive/issue_comments_026033.json:
```json
{
    "body": "Attachment [10128.patch](tarball://root/attachments/some-uuid/ticket3683/10128.patch) by @wdjoyner created at 2008-08-03 02:57:32\n\nThe attached patch 10128 fixes the bug Simon found (thanks Simon!).",
    "created_at": "2008-08-03T02:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26033",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [10128.patch](tarball://root/attachments/some-uuid/ticket3683/10128.patch) by @wdjoyner created at 2008-08-03 02:57:32

The attached patch 10128 fixes the bug Simon found (thanks Simon!).



---

archive/issue_comments_026034.json:
```json
{
    "body": "The patch applies cleanly to SAGE Version 3.1.alpha0, Release Date: 2008-08-01. It seems to do what it is supposed to do, and the doc-tests for matrix_group.py pass.\n\nTherefore, i recommend inclusion of the patch.\n\nHowever, i would be glad about \"stronger\" examples.\n\n\n* Is there an example for `as_permutation_group` where the option `method=\"smaller\"` actually yields a smaller result? Then it would be nice to include such example.\n\n\n* It would be nice to see an example where `module_composition_factors` yields a non-trivial decomposition. Such as here:\n\n```\nsage: F=GF(3);MS=MatrixSpace(F,4,4)\nsage: M=MS(0)\nsage: M[0,1]=1;M[1,2]=1;M[2,3]=1;M[3,0]=1\nsage: G.module_composition_factors()\n\n[[Finite Field of size 3, 1, True],\n [Finite Field of size 3, 1, True],\n [Finite Field of size 3, 2, True]]\n```\n",
    "created_at": "2008-08-12T13:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26034",
    "user": "https://github.com/simon-king-jena"
}
```

The patch applies cleanly to SAGE Version 3.1.alpha0, Release Date: 2008-08-01. It seems to do what it is supposed to do, and the doc-tests for matrix_group.py pass.

Therefore, i recommend inclusion of the patch.

However, i would be glad about "stronger" examples.


* Is there an example for `as_permutation_group` where the option `method="smaller"` actually yields a smaller result? Then it would be nice to include such example.


* It would be nice to see an example where `module_composition_factors` yields a non-trivial decomposition. Such as here:

```
sage: F=GF(3);MS=MatrixSpace(F,4,4)
sage: M=MS(0)
sage: M[0,1]=1;M[1,2]=1;M[2,3]=1;M[3,0]=1
sage: G.module_composition_factors()

[[Finite Field of size 3, 1, True],
 [Finite Field of size 3, 1, True],
 [Finite Field of size 3, 2, True]]
```




---

archive/issue_comments_026035.json:
```json
{
    "body": "Definitely, I'm happy to add the example to the dcstring of module_composition_factors. Thanks for that.\n\nRegarding a \"better\" \"smaller\" example, they are not so easy to find! I did find one though. The problem is that the generators are returned randomly. Michael Abshoff told me he doesn't like \" # random output\" comments in docstrings, so I added a the command current_randstate().set_seed_gap(). This does not work as I think it should, so I don't know the right way to proceed. I guess I'll post a patch that pases tests and worry about the random output stuff later.",
    "created_at": "2008-08-12T15:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26035",
    "user": "https://github.com/wdjoyner"
}
```

Definitely, I'm happy to add the example to the dcstring of module_composition_factors. Thanks for that.

Regarding a "better" "smaller" example, they are not so easy to find! I did find one though. The problem is that the generators are returned randomly. Michael Abshoff told me he doesn't like " # random output" comments in docstrings, so I added a the command current_randstate().set_seed_gap(). This does not work as I think it should, so I don't know the right way to proceed. I guess I'll post a patch that pases tests and worry about the random output stuff later.



---

archive/issue_comments_026036.json:
```json
{
    "body": "Attachment [10129.patch](tarball://root/attachments/some-uuid/ticket3683/10129.patch) by @wdjoyner created at 2008-08-12 18:36:47\n\nbased on 3.1.alpha0",
    "created_at": "2008-08-12T18:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26036",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [10129.patch](tarball://root/attachments/some-uuid/ticket3683/10129.patch) by @wdjoyner created at 2008-08-12 18:36:47

based on 3.1.alpha0



---

archive/issue_comments_026037.json:
```json
{
    "body": "This latest patch passes sage -testall and adds the examples suggested by the referee. Thanks Simon!",
    "created_at": "2008-08-12T18:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26037",
    "user": "https://github.com/wdjoyner"
}
```

This latest patch passes sage -testall and adds the examples suggested by the referee. Thanks Simon!



---

archive/issue_comments_026038.json:
```json
{
    "body": "Replying to [comment:7 wdj]:\n> Regarding a \"better\" \"smaller\" example, they are not so easy to find! I did find one though. The problem is that the generators are returned randomly. Michael Abshoff told me he doesn't like \" # random output\" comments in docstrings, \n\nCc to Michael Abshoff.\n\nI understand that Gap uses a randomized algorithm when getting method=\"smaller\". Hence, if one wants to show the full functionality of a method to the user (which i find important!), one can not avoid to have #random in the doc-tests.\n\nMichael, what do you think?\n\nI think: \n* Starting with 3.1.alpha0, applying patch 10128 and then applying patch 10129 works.\n* The methods are useful.\n* The doc-string shows the functionality\n* The doc-tests pass\nHence i give it a positive review, but make it dependent on Michael's opinion on random doc-tests and/or on the idea to use current_randstate().set_seed_gap().",
    "created_at": "2008-08-13T11:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26038",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:7 wdj]:
> Regarding a "better" "smaller" example, they are not so easy to find! I did find one though. The problem is that the generators are returned randomly. Michael Abshoff told me he doesn't like " # random output" comments in docstrings, 

Cc to Michael Abshoff.

I understand that Gap uses a randomized algorithm when getting method="smaller". Hence, if one wants to show the full functionality of a method to the user (which i find important!), one can not avoid to have #random in the doc-tests.

Michael, what do you think?

I think: 
* Starting with 3.1.alpha0, applying patch 10128 and then applying patch 10129 works.
* The methods are useful.
* The doc-string shows the functionality
* The doc-tests pass
Hence i give it a positive review, but make it dependent on Michael's opinion on random doc-tests and/or on the idea to use current_randstate().set_seed_gap().



---

archive/issue_comments_026039.json:
```json
{
    "body": "David,\n\nno need to CC me, I read every ticket anyway. \n\nAbout randomness: GAP should behave deterministically unless there is a third rng we do not know about. For now it seems fine to add the #random to the doctests, but you might want to raise the issue on sage-devel so that Carl Witty can give his input on the problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T15:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David,

no need to CC me, I read every ticket anyway. 

About randomness: GAP should behave deterministically unless there is a third rng we do not know about. For now it seems fine to add the #random to the doctests, but you might want to raise the issue on sage-devel so that Carl Witty can give his input on the problem.

Cheers,

Michael



---

archive/issue_comments_026040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T16:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26040",
    "user": "https://github.com/simon-king-jena"
}
```

Resolution: fixed



---

archive/issue_comments_026041.json:
```json
{
    "body": "Replying to [comment:10 mabshoff]:\n> no need to CC me, I read every ticket anyway. \n\nVery impressive!\n\n> ... For now it seems fine to add the #random to the doctests, ...\n\nThen there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).",
    "created_at": "2008-08-13T16:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26041",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:10 mabshoff]:
> no need to CC me, I read every ticket anyway. 

Very impressive!

> ... For now it seems fine to add the #random to the doctests, ...

Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).



---

archive/issue_events_003903.json:
```json
{
    "actor": "@simon-king-jena",
    "created_at": "2008-08-13T16:15:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3683#event-3903"
}
```



---

archive/issue_comments_026042.json:
```json
{
    "body": "based on sage-3.1.alpha0, as the others",
    "created_at": "2008-08-13T20:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26042",
    "user": "https://github.com/wdjoyner"
}
```

based on sage-3.1.alpha0, as the others



---

archive/issue_comments_026043.json:
```json
{
    "body": "Attachment [10130.patch](tarball://root/attachments/some-uuid/ticket3683/10130.patch) by @wdjoyner created at 2008-08-13 20:57:39\n\nThe last patch 10130 is a docstring change only. \n\nFollowing Michael Abshoff's suggestion, I emailed sage-devel and mentioned the problem I was having with the random comments. It seems I was using the current_randstate().set_seed_gap() command incorrectly for the situation. I added some set_random_seed(n) statements (where n is chosen in a specific way) and removed the \"# random output\" comments. I did multiple test passes and this seems to work each time now.\n\nHopefully, with 10130, everyone is okay with this now.",
    "created_at": "2008-08-13T20:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26043",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [10130.patch](tarball://root/attachments/some-uuid/ticket3683/10130.patch) by @wdjoyner created at 2008-08-13 20:57:39

The last patch 10130 is a docstring change only. 

Following Michael Abshoff's suggestion, I emailed sage-devel and mentioned the problem I was having with the random comments. It seems I was using the current_randstate().set_seed_gap() command incorrectly for the situation. I added some set_random_seed(n) statements (where n is chosen in a specific way) and removed the "# random output" comments. I did multiple test passes and this seems to work each time now.

Hopefully, with 10130, everyone is okay with this now.



---

archive/issue_comments_026044.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-14T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26044",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003904.json:
```json
{
    "actor": "aginiewicz",
    "created_at": "2008-08-14T17:36:28Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3683#event-3904"
}
```



---

archive/issue_comments_026045.json:
```json
{
    "body": "Replying to [comment:11 SimonKing]:\n> Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).\n\niirc it was that only things that get merged in are closed by admins? :)",
    "created_at": "2008-08-14T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26045",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Replying to [comment:11 SimonKing]:
> Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).

iirc it was that only things that get merged in are closed by admins? :)



---

archive/issue_comments_026046.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-08-14T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26046",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_026047.json:
```json
{
    "body": "Replying to [comment:13 aginiewicz]:\n> Replying to [comment:11 SimonKing]:\n> > Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).\n> \n> iirc it was that only things that get merged in are closed by admins? :)\n\nYes, the release manager closes tickets once the patch/spkg has been merged. How else would be keep track of all the patches?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T19:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:13 aginiewicz]:
> Replying to [comment:11 SimonKing]:
> > Then there is a positive review from my side and (if i am allowed to do so) I resolve the ticket as fixed (or is this only allowed to administrators?).
> 
> iirc it was that only things that get merged in are closed by admins? :)

Yes, the release manager closes tickets once the patch/spkg has been merged. How else would be keep track of all the patches?

Cheers,

Michael



---

archive/issue_comments_026048.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-22T20:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026049.json:
```json
{
    "body": "Merged 10128.patch, 10129.patch and 10130.patch in Sage 3.1.2.alpha0",
    "created_at": "2008-08-22T20:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3683#issuecomment-26049",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 10128.patch, 10129.patch and 10130.patch in Sage 3.1.2.alpha0



---

archive/issue_events_003905.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-22T20:01:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3683",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3683#event-3905"
}
```
