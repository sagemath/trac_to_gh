# Issue 4676: Polyhedral improvements

archive/issues_004676.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: polyhedra, polytopes\n\nThis adds more built-in polytopes (more Archimedean solids) and some new methods such as the Gale transform, bipyramid construction, edge truncation, and perspective projection with (optionally) hidden faces invisible.  The Schlegel projection code has also been somewhat refactored to make it more general in the future.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4676\n\n",
    "created_at": "2008-12-02T17:17:34Z",
    "labels": [
        "component: geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Polyhedral improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Keywords: polyhedra, polytopes

This adds more built-in polytopes (more Archimedean solids) and some new methods such as the Gale transform, bipyramid construction, edge truncation, and perspective projection with (optionally) hidden faces invisible.  The Schlegel projection code has also been somewhat refactored to make it more general in the future.

Issue created by migration from https://trac.sagemath.org/ticket/4676





---

archive/issue_comments_035159.json:
```json
{
    "body": "Attachment [4676_polyhedra_1.patch](tarball://root/attachments/some-uuid/ticket4676/4676_polyhedra_1.patch) by mhampton created at 2008-12-02 17:18:27\n\nbased against 3.2.1-rc1",
    "created_at": "2008-12-02T17:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [4676_polyhedra_1.patch](tarball://root/attachments/some-uuid/ticket4676/4676_polyhedra_1.patch) by mhampton created at 2008-12-02 17:18:27

based against 3.2.1-rc1



---

archive/issue_comments_035160.json:
```json
{
    "body": "Arnaud,\n\ncan you review this?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T09:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arnaud,

can you review this?

Cheers,

Michael



---

archive/issue_comments_035161.json:
```json
{
    "body": "I applied this to 3.2.2 successfully.  No doctests were broken in the affected file (there was one doctest that returned an error both before and after the patch, but the warning points to an error in my install, not in the code).  I generated lots of pretty pictures, one for each of the new polytopes.  Everything seemed to work.  However, it would probably be good to have someone who is more familiar with the math look at this.",
    "created_at": "2008-12-24T16:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35161",
    "user": "https://github.com/jasongrout"
}
```

I applied this to 3.2.2 successfully.  No doctests were broken in the affected file (there was one doctest that returned an error both before and after the patch, but the warning points to an error in my install, not in the code).  I generated lots of pretty pictures, one for each of the new polytopes.  Everything seemed to work.  However, it would probably be good to have someone who is more familiar with the math look at this.



---

archive/issue_comments_035162.json:
```json
{
    "body": "I like this too. I checked the Gale transform against section 5.3 in Ewald, Combinatorial convexity and algebraic geometry, and it agreed with the example there.\n\nI wish there was a way to use tachyon to plot the objects but the viewer='tachyon' option is ignored. I agree with Jason that the plots are beautiful anyway.\n\nI give this a thumbs up but maybe Arnaud should review this too? Based on a recent \"code freeze\" email from Michael Abshoff, it seems as though it will not make 3.3.",
    "created_at": "2008-12-25T16:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35162",
    "user": "https://github.com/wdjoyner"
}
```

I like this too. I checked the Gale transform against section 5.3 in Ewald, Combinatorial convexity and algebraic geometry, and it agreed with the example there.

I wish there was a way to use tachyon to plot the objects but the viewer='tachyon' option is ignored. I agree with Jason that the plots are beautiful anyway.

I give this a thumbs up but maybe Arnaud should review this too? Based on a recent "code freeze" email from Michael Abshoff, it seems as though it will not make 3.3.



---

archive/issue_comments_035163.json:
```json
{
    "body": "Only two small stylistic points:\n\n- Gale_transform() -> gale_transform()\n- Schlegel_transform() -> schlegel_transform()\n\nI don't think it's good style to have methods begin with a capital, even when they refer to a person's name.\n\nOtherwise, I don't know since when I was familiar with the math involved.  I did look up references though, and everything looks good.\n\nIf the two points above are fixed, then I give it a positive review.",
    "created_at": "2008-12-30T20:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35163",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

Only two small stylistic points:

- Gale_transform() -> gale_transform()
- Schlegel_transform() -> schlegel_transform()

I don't think it's good style to have methods begin with a capital, even when they refer to a person's name.

Otherwise, I don't know since when I was familiar with the math involved.  I did look up references though, and everything looks good.

If the two points above are fixed, then I give it a positive review.



---

archive/issue_comments_035164.json:
```json
{
    "body": "rebased on 3.2.3, supercedes previous patch, addresses review",
    "created_at": "2009-01-11T17:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

rebased on 3.2.3, supercedes previous patch, addresses review



---

archive/issue_comments_035165.json:
```json
{
    "body": "Attachment [4676_rebase.patch](tarball://root/attachments/some-uuid/ticket4676/4676_rebase.patch) by mhampton created at 2009-01-11 17:02:33",
    "created_at": "2009-01-11T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [4676_rebase.patch](tarball://root/attachments/some-uuid/ticket4676/4676_rebase.patch) by mhampton created at 2009-01-11 17:02:33



---

archive/issue_comments_035166.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T00:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010704.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T00:39:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4676#event-10704"
}
```



---

archive/issue_events_010705.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T00:39:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4676#event-10705"
}
```



---

archive/issue_comments_035167.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T00:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4676#issuecomment-35167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
