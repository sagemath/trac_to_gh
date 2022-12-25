# Issue 4337: modular forms -- compute action of Hecke operators on Gamma_1(N) modular forms

archive/issues_004337.json:
```json
{
    "body": "Assignee: @craigcitro\n\n\n```\nsage: ModularForms(Gamma1(11),2).hecke_matrix(2)\nboom!\n```\n\n\nand a genuine bug:\n\n```\nsage: ModularForms(GammaH(11, [2]),2).hecke_matrix(2)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n...\nRuntimeError: maximum recursion depth exceeded in cmp\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4337\n\n",
    "created_at": "2008-10-22T17:46:16Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "modular forms -- compute action of Hecke operators on Gamma_1(N) modular forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4337",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro


```
sage: ModularForms(Gamma1(11),2).hecke_matrix(2)
boom!
```


and a genuine bug:

```
sage: ModularForms(GammaH(11, [2]),2).hecke_matrix(2)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
RuntimeError: maximum recursion depth exceeded in cmp
```


Issue created by migration from https://trac.sagemath.org/ticket/4337





---

archive/issue_comments_031744.json:
```json
{
    "body": "Attachment [trac_4337.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337.patch) by @loefflerd created at 2009-05-05 16:42:54\n\npatch against 3.4.2.final",
    "created_at": "2009-05-05T16:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31744",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_4337.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337.patch) by @loefflerd created at 2009-05-05 16:42:54

patch against 3.4.2.final



---

archive/issue_comments_031745.json:
```json
{
    "body": "Changing assignee from @craigcitro to @loefflerd.",
    "created_at": "2009-05-05T16:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31745",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @craigcitro to @loefflerd.



---

archive/issue_comments_031746.json:
```json
{
    "body": "I believe I've fixed the Gamma1 bug; I've checked the algorithm by comparing the output with the obvious algorithm of summing over the character spaces for all characters of the given modulus, and it seems to agree (and it's a lot quicker). \n\nThe GammaH one is more deep-rooted -- just about nothing works for spaces of GammaH forms, not even the basis() method. I've inserted a dummy routine that raises a NotImplementedError at an appropriate place, which is better than the current infinite loop. It will be easy to add computation of Hecke ops for modular forms for GammaH once we have them for the corresponding spaces of modular symbols.",
    "created_at": "2009-05-05T16:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31746",
    "user": "https://github.com/loefflerd"
}
```

I believe I've fixed the Gamma1 bug; I've checked the algorithm by comparing the output with the obvious algorithm of summing over the character spaces for all characters of the given modulus, and it seems to agree (and it's a lot quicker). 

The GammaH one is more deep-rooted -- just about nothing works for spaces of GammaH forms, not even the basis() method. I've inserted a dummy routine that raises a NotImplementedError at an appropriate place, which is better than the current infinite loop. It will be easy to add computation of Hecke ops for modular forms for GammaH once we have them for the corresponding spaces of modular symbols.



---

archive/issue_comments_031747.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-05T16:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31747",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031748.json:
```json
{
    "body": "Attachment [trac_4337_pt2.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337_pt2.patch) by @craigcitro created at 2009-05-08 06:51:35",
    "created_at": "2009-05-08T06:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31748",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_4337_pt2.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337_pt2.patch) by @craigcitro created at 2009-05-08 06:51:35



---

archive/issue_comments_031749.json:
```json
{
    "body": "This looks really good. Positive review! Here are my comments:\n\n* I'm really happy to see that this code is written! I'm very happy with how all the code works. This is actually functionality that Magma doesn't even have. Bravo, David!\n\n* I moved a few bits of code around, and did a few things to make the code run faster. On the (few) benchmarks I was running, I got a factor of 2 speedup for `_compute_hecke_matrix` on cuspidal subspaces, and about 1.5 on the Eisenstein part. (There's more post-processing to be done in the Eisenstein case.)\n\n* Unfortunately, this algorithm gets slow pretty fast. For instance, trying to compute the Hecke operators on something like `ModularForms(Gamma1(48),4)` is just hopeless in this case. We should try to talk about what else we could do that might scale a little better. But we **definitely** want this merged first!\n\nDavid, I've added a few changes in my referee patch -- could you look over the changes and make sure you're okay with them? Most of it is just cleanup; the only change I'd really demand is renaming the variable you called `QQ`, since I think it's pretty confusing to have a local variable named `QQ`, even if it's going to be the global `QQ` 99% of the time.",
    "created_at": "2009-05-08T06:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31749",
    "user": "https://github.com/craigcitro"
}
```

This looks really good. Positive review! Here are my comments:

* I'm really happy to see that this code is written! I'm very happy with how all the code works. This is actually functionality that Magma doesn't even have. Bravo, David!

* I moved a few bits of code around, and did a few things to make the code run faster. On the (few) benchmarks I was running, I got a factor of 2 speedup for `_compute_hecke_matrix` on cuspidal subspaces, and about 1.5 on the Eisenstein part. (There's more post-processing to be done in the Eisenstein case.)

* Unfortunately, this algorithm gets slow pretty fast. For instance, trying to compute the Hecke operators on something like `ModularForms(Gamma1(48),4)` is just hopeless in this case. We should try to talk about what else we could do that might scale a little better. But we **definitely** want this merged first!

David, I've added a few changes in my referee patch -- could you look over the changes and make sure you're okay with them? Most of it is just cleanup; the only change I'd really demand is renaming the variable you called `QQ`, since I think it's pretty confusing to have a local variable named `QQ`, even if it's going to be the global `QQ` 99% of the time.



---

archive/issue_comments_031750.json:
```json
{
    "body": "Thanks for reviewing this. I'd actually never come across the python \"for/else\" syntax before; it's a neat trick, I'll have to remember it. I'm happy with the changes you propose.\n\nUnfortunately, I've realised that there *is* a problem in my patch: in trying to prevent the infinite loop for GammaH, I've broken something else. The loop comes up because the default behaviour for the generic cuspidal submodule class is to get its q-expansions from its ambient space; and the generic ambient space class gets its q-expansions from its ambient modules.\n\nNow, for *most* derived classes it's the cuspidal and eisenstein subs that have this overridden, but for the \"ambient_R\" class, it's the ambient space that overrides it. So my patch breaks calculation of q-expansion bases -- and consequently everything else -- for forms over a non-minimal base ring.\n\nSo here's a third patch, which fixes this and adds a doctest.\n\nDavid",
    "created_at": "2009-05-08T09:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31750",
    "user": "https://github.com/loefflerd"
}
```

Thanks for reviewing this. I'd actually never come across the python "for/else" syntax before; it's a neat trick, I'll have to remember it. I'm happy with the changes you propose.

Unfortunately, I've realised that there *is* a problem in my patch: in trying to prevent the infinite loop for GammaH, I've broken something else. The loop comes up because the default behaviour for the generic cuspidal submodule class is to get its q-expansions from its ambient space; and the generic ambient space class gets its q-expansions from its ambient modules.

Now, for *most* derived classes it's the cuspidal and eisenstein subs that have this overridden, but for the "ambient_R" class, it's the ambient space that overrides it. So my patch breaks calculation of q-expansion bases -- and consequently everything else -- for forms over a non-minimal base ring.

So here's a third patch, which fixes this and adds a doctest.

David



---

archive/issue_comments_031751.json:
```json
{
    "body": "I think something is wrong with the third patch? trac tells me it's 225 bytes, which seems unlikely. Can you re-upload it?",
    "created_at": "2009-05-08T10:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31751",
    "user": "https://github.com/craigcitro"
}
```

I think something is wrong with the third patch? trac tells me it's 225 bytes, which seems unlikely. Can you re-upload it?



---

archive/issue_comments_031752.json:
```json
{
    "body": "Attachment [trac_4337_pt3.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337_pt3.patch) by @loefflerd created at 2009-05-08 10:07:38",
    "created_at": "2009-05-08T10:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31752",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_4337_pt3.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337_pt3.patch) by @loefflerd created at 2009-05-08 10:07:38



---

archive/issue_comments_031753.json:
```json
{
    "body": "Oops, I forgot to qrefresh before I exported. Here it is.",
    "created_at": "2009-05-08T10:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31753",
    "user": "https://github.com/loefflerd"
}
```

Oops, I forgot to qrefresh before I exported. Here it is.



---

archive/issue_comments_031754.json:
```json
{
    "body": "Nice catch! I'm happy with the `_R`-related changes ... positive review! (I was apparently sloppy while reviewing and only worked over `QQ` ... I'm glad you were experimenting with quadratic imaginary fields!)",
    "created_at": "2009-05-08T10:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31754",
    "user": "https://github.com/craigcitro"
}
```

Nice catch! I'm happy with the `_R`-related changes ... positive review! (I was apparently sloppy while reviewing and only worked over `QQ` ... I'm glad you were experimenting with quadratic imaginary fields!)



---

archive/issue_comments_031755.json:
```json
{
    "body": "Looks like you weren't the only one that was sloppy: neither of us ran a full doctest cycle, so neither of us spotted the fact that this causes a doctest failure in William's Bordeaux lectures. One of those specifically states, with a doctest to prove it, that computing Hecke matrices for Gamma1(N) raises a `NotImplementedError`.",
    "created_at": "2009-05-11T07:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31755",
    "user": "https://github.com/loefflerd"
}
```

Looks like you weren't the only one that was sloppy: neither of us ran a full doctest cycle, so neither of us spotted the fact that this causes a doctest failure in William's Bordeaux lectures. One of those specifically states, with a doctest to prove it, that computing Hecke matrices for Gamma1(N) raises a `NotImplementedError`.



---

archive/issue_comments_031756.json:
```json
{
    "body": "Attachment [trac_4337_docfix.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337_docfix.patch) by @loefflerd created at 2009-05-11 07:06:10\n\napply over previous three",
    "created_at": "2009-05-11T07:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31756",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_4337_docfix.patch](tarball://root/attachments/some-uuid/ticket4337/trac_4337_docfix.patch) by @loefflerd created at 2009-05-11 07:06:10

apply over previous three



---

archive/issue_comments_031757.json:
```json
{
    "body": "Merged all four patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T07:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all four patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_009813.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-11T07:47:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4337#event-9813"
}
```



---

archive/issue_comments_031758.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T07:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4337#issuecomment-31758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
