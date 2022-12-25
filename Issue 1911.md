# Issue 1911: [with patch; with positive review] elliptic curves -- make heegner_index command return index instead of square of index; clarify why sometimes results is not an integer (it's not a bug, it's part of the algorithm)

archive/issues_001911.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1911\n\n",
    "closed_at": "2008-01-26T11:21:14Z",
    "created_at": "2008-01-24T15:18:51Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch; with positive review] elliptic curves -- make heegner_index command return index instead of square of index; clarify why sometimes results is not an integer (it's not a bug, it's part of the algorithm)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1911",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/1911





---

archive/issue_comments_012075.json:
```json
{
    "body": "Attachment [trac-1911-heegner_index.patch](tarball://root/attachments/some-uuid/ticket1911/trac-1911-heegner_index.patch) by @aghitza created at 2008-01-26 03:28:26\n\nLooks good to me, except for a very minor point: you changed the description of the output from \"an interval that contains the index\" to \"an Integer\", but the function is indeed returning an interval, not an integer.",
    "created_at": "2008-01-26T03:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1911#issuecomment-12075",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac-1911-heegner_index.patch](tarball://root/attachments/some-uuid/ticket1911/trac-1911-heegner_index.patch) by @aghitza created at 2008-01-26 03:28:26

Looks good to me, except for a very minor point: you changed the description of the output from "an interval that contains the index" to "an Integer", but the function is indeed returning an interval, not an integer.



---

archive/issue_comments_012076.json:
```json
{
    "body": "Several comments, but positive review with the additional patch:\n\n- I've gone ahead and corrected the typo Alex pointed out, and a few more to boot. \n\n- There was a small problem with the patch -- there were one or two places that IR(...) was used, but IR was only defined in one of the functions there. I went ahead and moved that definition to the top, so that it worked everywhere, and added doctests to catch that in the future. I also made sure that every function in ell_rational_field that had the word \"heegner\" in it had at least one doctest.\n\n- I changed the satisfies_heegner_hypothesis method to use legendre symbols instead of factoring in a quadratic extension of QQ, since that was overkill. This gives something like a 10X speedup to that one little function, which is probably completely irrelevant compared to the runtime for the rest of the code that actually uses it. There's the argument that the other method works over any base -- first, since this is in ell_rational_field, that shouldn't matter, and second, since the QuadraticField(...) was hardcoded to be over QQ, this code would need revisited anyway.\n\n- Also corrected a silly typo I found in integer.pyx, which I just happened to notice while looking at code for this patch. I didn't think \"returs -> returns\" merited its own ticket.\n\n- There's one thing that leaves me feeling a little unsettled -- E.heegner_index_bound() defaults to verbose=True. Given that William and his coauthors are the only people actively using this code, it's fine to leave it that way if it's the behavior they're used to. However, it's pretty shocking when you're not prepared for it; for something with that much output, I'd argue that verbose=False should be the default.\n\n-cc",
    "created_at": "2008-01-26T09:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1911#issuecomment-12076",
    "user": "https://github.com/craigcitro"
}
```

Several comments, but positive review with the additional patch:

- I've gone ahead and corrected the typo Alex pointed out, and a few more to boot. 

- There was a small problem with the patch -- there were one or two places that IR(...) was used, but IR was only defined in one of the functions there. I went ahead and moved that definition to the top, so that it worked everywhere, and added doctests to catch that in the future. I also made sure that every function in ell_rational_field that had the word "heegner" in it had at least one doctest.

- I changed the satisfies_heegner_hypothesis method to use legendre symbols instead of factoring in a quadratic extension of QQ, since that was overkill. This gives something like a 10X speedup to that one little function, which is probably completely irrelevant compared to the runtime for the rest of the code that actually uses it. There's the argument that the other method works over any base -- first, since this is in ell_rational_field, that shouldn't matter, and second, since the QuadraticField(...) was hardcoded to be over QQ, this code would need revisited anyway.

- Also corrected a silly typo I found in integer.pyx, which I just happened to notice while looking at code for this patch. I didn't think "returs -> returns" merited its own ticket.

- There's one thing that leaves me feeling a little unsettled -- E.heegner_index_bound() defaults to verbose=True. Given that William and his coauthors are the only people actively using this code, it's fine to leave it that way if it's the behavior they're used to. However, it's pretty shocking when you're not prepared for it; for something with that much output, I'd argue that verbose=False should be the default.

-cc



---

archive/issue_events_004601.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-26T11:21:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1911",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1911#event-4601"
}
```



---

archive/issue_comments_012077.json:
```json
{
    "body": "Attachment [1911-pt2.patch](tarball://root/attachments/some-uuid/ticket1911/1911-pt2.patch) by mabshoff created at 2008-01-26 11:21:14\n\nMerged in Sage 2.10.1.rc0",
    "created_at": "2008-01-26T11:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1911#issuecomment-12077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [1911-pt2.patch](tarball://root/attachments/some-uuid/ticket1911/1911-pt2.patch) by mabshoff created at 2008-01-26 11:21:14

Merged in Sage 2.10.1.rc0



---

archive/issue_comments_012078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-26T11:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1911",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1911#issuecomment-12078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
