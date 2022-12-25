# Issue 6831: [with patch, needs review] No more maximal dimension requirement for lattice polytopes

archive/issues_006831.json:
```json
{
    "body": "Assignee: mhampton\n\nSince PALP requires polytopes to have the same dimension as the ambient space, LatticePolytope class required it as well. This patch drops this requirement by storing an internal copy of the same polytope in some sublattice basis and using it when necessary to call PALP. Quite a few functions had to be updated, I tried to add new doctests to check most of the new branches of code.\n\nThis patch will be a prerequisite for some code for working with nef partitions which I hope to submit in the future.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6831\n\n",
    "created_at": "2009-08-27T06:29:37Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch, needs review] No more maximal dimension requirement for lattice polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6831",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

Since PALP requires polytopes to have the same dimension as the ambient space, LatticePolytope class required it as well. This patch drops this requirement by storing an internal copy of the same polytope in some sublattice basis and using it when necessary to call PALP. Quite a few functions had to be updated, I tried to add new doctests to check most of the new branches of code.

This patch will be a prerequisite for some code for working with nef partitions which I hope to submit in the future.

Issue created by migration from https://trac.sagemath.org/ticket/6831





---

archive/issue_comments_056236.json:
```json
{
    "body": "Attachment [trac_6831_allow_non_full_dimensional_lattice_polytopes.patch](tarball://root/attachments/some-uuid/ticket6831/trac_6831_allow_non_full_dimensional_lattice_polytopes.patch) by mhampton created at 2009-10-29 18:47:19\n\nCan you rebase this against sage-4.2?  I reviewed some of your patches previously, and some made them in, which means this doesn't apply against the current version.  Sorry about that, I'm hoping to finish up reviewing your patches for 4.2.1.\n\n-Marshall",
    "created_at": "2009-10-29T18:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56236",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6831_allow_non_full_dimensional_lattice_polytopes.patch](tarball://root/attachments/some-uuid/ticket6831/trac_6831_allow_non_full_dimensional_lattice_polytopes.patch) by mhampton created at 2009-10-29 18:47:19

Can you rebase this against sage-4.2?  I reviewed some of your patches previously, and some made them in, which means this doesn't apply against the current version.  Sorry about that, I'm hoping to finish up reviewing your patches for 4.2.1.

-Marshall



---

archive/issue_comments_056237.json:
```json
{
    "body": "Actually, I have written this patch after all the previous ones were applied, I am not even sure if it will work without them.\n\nI'll check and rebase if it does not work for 4.2, but it will take me some time. \n\nThanks for all the other reviews!\nAndrey",
    "created_at": "2009-10-29T19:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56237",
    "user": "https://github.com/novoselt"
}
```

Actually, I have written this patch after all the previous ones were applied, I am not even sure if it will work without them.

I'll check and rebase if it does not work for 4.2, but it will take me some time. 

Thanks for all the other reviews!
Andrey



---

archive/issue_comments_056238.json:
```json
{
    "body": "My mercurial-foo is not that strong, so perhaps I made a mistake trying to apply the patch.  But I don't understand it if so.  It would be OK to have a rebased patch that included other changes - even if they aren't positively reviewed yet I could do them all at once, assuming they mainly affected lattice_polytope.py.\n\n-Marshall",
    "created_at": "2009-10-30T02:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

My mercurial-foo is not that strong, so perhaps I made a mistake trying to apply the patch.  But I don't understand it if so.  It would be OK to have a rebased patch that included other changes - even if they aren't positively reviewed yet I could do them all at once, assuming they mainly affected lattice_polytope.py.

-Marshall



---

archive/issue_comments_056239.json:
```json
{
    "body": "Rebased patch, also includes patches for tickets 6779, 6780, and 6805",
    "created_at": "2009-10-30T05:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56239",
    "user": "https://github.com/novoselt"
}
```

Rebased patch, also includes patches for tickets 6779, 6780, and 6805



---

archive/issue_comments_056240.json:
```json
{
    "body": "Attachment [trac_6831_allow_non_full_dimensional_lattice_polytopes-4.2-rebase.patch](tarball://root/attachments/some-uuid/ticket6831/trac_6831_allow_non_full_dimensional_lattice_polytopes-4.2-rebase.patch) by @novoselt created at 2009-10-30 05:33:08\n\nThis patch should work on 4.2 without any prior requirements, it includes changes made in 3 other small tickets which you have already given a positive review - I will put comments in those tickets. Let me know if I should do anything else.\n\nAndrey",
    "created_at": "2009-10-30T05:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56240",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_6831_allow_non_full_dimensional_lattice_polytopes-4.2-rebase.patch](tarball://root/attachments/some-uuid/ticket6831/trac_6831_allow_non_full_dimensional_lattice_polytopes-4.2-rebase.patch) by @novoselt created at 2009-10-30 05:33:08

This patch should work on 4.2 without any prior requirements, it includes changes made in 3 other small tickets which you have already given a positive review - I will put comments in those tickets. Let me know if I should do anything else.

Andrey



---

archive/issue_comments_056241.json:
```json
{
    "body": "Great, thanks.  I can't do it today but I'll try to review it this weekend.\n\n-Marshall",
    "created_at": "2009-10-30T15:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Great, thanks.  I can't do it today but I'll try to review it this weekend.

-Marshall



---

archive/issue_comments_056242.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-01T12:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056243.json:
```json
{
    "body": "OK, this looks good, positive review.  I've looked it over, did some manual tests, it passes its own doctests and has 100% coverage.  I rebuilt the reference manual and it looks good there.  Seems like all the changes are for the better.",
    "created_at": "2009-11-01T12:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, this looks good, positive review.  I've looked it over, did some manual tests, it passes its own doctests and has 100% coverage.  I rebuilt the reference manual and it looks good there.  Seems like all the changes are for the better.



---

archive/issue_comments_056244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T04:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6831#issuecomment-56244",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016082.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-02T04:35:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6831",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6831#event-16082"
}
```
