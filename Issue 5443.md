# Issue 5443: [with patch, needs review] Segfault in congruence subgroup element code

archive/issues_005443.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @loefflerd\n\nDavid Loeffler ran into the following segfault earlier:\n\n\n```\nsage: r,s,t,u = Gamma0(2).gens()\nsage: r**(-1)*u**(-1) == t\nBOOM\n```\n\n\nThe attached patch fixes this, and adds a doctest. There's more work to be done: `matrix_integer_2x2` should inherit from `matrix_integer_dense`, but it doesn't yet. I have 98% of the code to do it done, but it needs to get cleaned up and submitted.\n\n**HOWEVER**: I don't have a copy of sage-3.3 on my machine, so the patch is against sage-3.2.3. I\n\nIssue created by migration from https://trac.sagemath.org/ticket/5443\n\n",
    "created_at": "2009-03-05T17:32:30Z",
    "labels": [
        "component: modular forms",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] Segfault in congruence subgroup element code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5443",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @loefflerd

David Loeffler ran into the following segfault earlier:


```
sage: r,s,t,u = Gamma0(2).gens()
sage: r**(-1)*u**(-1) == t
BOOM
```


The attached patch fixes this, and adds a doctest. There's more work to be done: `matrix_integer_2x2` should inherit from `matrix_integer_dense`, but it doesn't yet. I have 98% of the code to do it done, but it needs to get cleaned up and submitted.

**HOWEVER**: I don't have a copy of sage-3.3 on my machine, so the patch is against sage-3.2.3. I

Issue created by migration from https://trac.sagemath.org/ticket/5443





---

archive/issue_comments_042003.json:
```json
{
    "body": "(I apparently forgot to finish the description.)",
    "created_at": "2009-03-05T17:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42003",
    "user": "https://github.com/craigcitro"
}
```

(I apparently forgot to finish the description.)



---

archive/issue_comments_042004.json:
```json
{
    "body": "Hi Craig,\n\nThanks for looking at this so quickly; but as I mentioned in my email to sage-devel, the problem doesn't occur under pre-3.3 versions because the output of Gamma0(2).gens() isn't the same. In 3.3 and 3.4, the matrices returned by Gamma0(2).gens() *should* satisfy r**(-1) * u**(-1) == t. \n\nIn 3.4 with congroup_element's __cmp__ changed to _cmp_ as in your patch, it no longer segfaults; but the answer is False, even though the matrices have the same entries, which isn't great either. And one gets the same crash as before by doing\n\nsage: (r**(-1) * u**(-1)).matrix() == t.matrix()\n\nSo I'm afraid I'm giving this a \"needs work\". I will do some further tinkering myself tomorrow.\n\nDavid",
    "created_at": "2009-03-05T22:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42004",
    "user": "https://github.com/loefflerd"
}
```

Hi Craig,

Thanks for looking at this so quickly; but as I mentioned in my email to sage-devel, the problem doesn't occur under pre-3.3 versions because the output of Gamma0(2).gens() isn't the same. In 3.3 and 3.4, the matrices returned by Gamma0(2).gens() *should* satisfy r**(-1) * u**(-1) == t. 

In 3.4 with congroup_element's __cmp__ changed to _cmp_ as in your patch, it no longer segfaults; but the answer is False, even though the matrices have the same entries, which isn't great either. And one gets the same crash as before by doing

sage: (r**(-1) * u**(-1)).matrix() == t.matrix()

So I'm afraid I'm giving this a "needs work". I will do some further tinkering myself tomorrow.

David



---

archive/issue_comments_042005.json:
```json
{
    "body": "Ah, touche. Actually, in 3.2.3, I was getting a different crash (a `SIGBUS` instead of a `SIGSEGV`) ... \n\nIn any event, I've written a much better fix now (I hope!). The underlying problem was that there were two ways to create elements of congruence subgroups whose underlying matrix was of type `Matrix_integer_dense` instead of `Matrix_integer_2x2` (and, as I said, the latter sadly doesn't yet derive from the former). Those came from places where `M2Z` was used to create matrices; these have been replaced by calls to create objects of the appropriate type. (I also had to add a wee bit of code so that congruence subgroup elements could determine their underlying list.) \n\nHopefully this will fix the issues -- let me know if you run into anything else!",
    "created_at": "2009-03-06T00:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42005",
    "user": "https://github.com/craigcitro"
}
```

Ah, touche. Actually, in 3.2.3, I was getting a different crash (a `SIGBUS` instead of a `SIGSEGV`) ... 

In any event, I've written a much better fix now (I hope!). The underlying problem was that there were two ways to create elements of congruence subgroups whose underlying matrix was of type `Matrix_integer_dense` instead of `Matrix_integer_2x2` (and, as I said, the latter sadly doesn't yet derive from the former). Those came from places where `M2Z` was used to create matrices; these have been replaced by calls to create objects of the appropriate type. (I also had to add a wee bit of code so that congruence subgroup elements could determine their underlying list.) 

Hopefully this will fix the issues -- let me know if you run into anything else!



---

archive/issue_comments_042006.json:
```json
{
    "body": "Attachment [trac-5443.patch](tarball://root/attachments/some-uuid/ticket5443/trac-5443.patch) by mabshoff created at 2009-03-08 06:20:43\n\nThe patch applies to my 3.4.rc1 merge tree without any rebase problems, so all we need is a review to get this in.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T06:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-5443.patch](tarball://root/attachments/some-uuid/ticket5443/trac-5443.patch) by mabshoff created at 2009-03-08 06:20:43

The patch applies to my 3.4.rc1 merge tree without any rebase problems, so all we need is a review to get this in.

Cheers,

Michael



---

archive/issue_comments_042007.json:
```json
{
    "body": "It looks good to my eyes.",
    "created_at": "2009-03-08T06:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42007",
    "user": "https://github.com/williamstein"
}
```

It looks good to my eyes.



---

archive/issue_comments_042008.json:
```json
{
    "body": "Doctests fine in my current merge tree, so positive review via William's comment.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T06:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests fine in my current merge tree, so positive review via William's comment.

Cheers,

Michael



---

archive/issue_comments_042009.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T07:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_042010.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-08T07:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5443#issuecomment-42010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012718.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-08T07:13:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5443",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5443#event-12718"
}
```
