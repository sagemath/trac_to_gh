# Issue 1987: [with patch] unintuitive return values for "forall" and "exists"

archive/issues_001987.json:
```json
{
    "body": "Assignee: cwitty\n\nThe names of \"forall\" and \"exists\" suggest that these are predicates that can be used where a conditional is needed. In fact, doing so does not result in an error but in unintended results:\n`len([ i for i in [1..300] if forall(prime_divisors(i),lambda i: i<10)])`\nreturns\n`300`\nwhich does not reflect the apparent meaning of the expression. The proper result is returned by inserting an index:\n`len([ i for i in [1..300] if forall(prime_divisors(i),lambda i: i<10)[0]])`\nwhich returns\n`82`\n\nI would suggest an optional parameter to \"forall\" and \"exists\", say, witness=True to return a second return value giving the index. The default should be index=False in my opinion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1987\n\n",
    "created_at": "2008-01-30T22:28:41Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch] unintuitive return values for \"forall\" and \"exists\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1987",
    "user": "https://github.com/nbruin"
}
```
Assignee: cwitty

The names of "forall" and "exists" suggest that these are predicates that can be used where a conditional is needed. In fact, doing so does not result in an error but in unintended results:
`len([ i for i in [1..300] if forall(prime_divisors(i),lambda i: i<10)])`
returns
`300`
which does not reflect the apparent meaning of the expression. The proper result is returned by inserting an index:
`len([ i for i in [1..300] if forall(prime_divisors(i),lambda i: i<10)[0]])`
which returns
`82`

I would suggest an optional parameter to "forall" and "exists", say, witness=True to return a second return value giving the index. The default should be index=False in my opinion.

Issue created by migration from https://trac.sagemath.org/ticket/1987





---

archive/issue_comments_012835.json:
```json
{
    "body": "As Mike Hansen points out, use python natives \"all\" and \"any\" instead. Patch should probably not be merged.",
    "created_at": "2008-01-30T23:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12835",
    "user": "https://github.com/nbruin"
}
```

As Mike Hansen points out, use python natives "all" and "any" instead. Patch should probably not be merged.



---

archive/issue_comments_012836.json:
```json
{
    "body": "Attachment [witness.patch](tarball://root/attachments/some-uuid/ticket1987/witness.patch) by @nbruin created at 2008-02-01 02:00:05\n\nPatch to fix docstrings of forall and exists to refer to Python natives.",
    "created_at": "2008-02-01T02:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12836",
    "user": "https://github.com/nbruin"
}
```

Attachment [witness.patch](tarball://root/attachments/some-uuid/ticket1987/witness.patch) by @nbruin created at 2008-02-01 02:00:05

Patch to fix docstrings of forall and exists to refer to Python natives.



---

archive/issue_comments_012837.json:
```json
{
    "body": "Patch now changed to fix docstrings of \"forall\" and \"exists\". Please do consider this change for inclusion, so that other people have an easier time finding the more appropriate python natives.",
    "created_at": "2008-02-01T02:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12837",
    "user": "https://github.com/nbruin"
}
```

Patch now changed to fix docstrings of "forall" and "exists". Please do consider this change for inclusion, so that other people have an easier time finding the more appropriate python natives.



---

archive/issue_comments_012838.json:
```json
{
    "body": "I made some comments on sage-devel.  This patch should definitely be included\nthough, even if none of my comments are addressed.",
    "created_at": "2008-02-01T03:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12838",
    "user": "https://github.com/williamstein"
}
```

I made some comments on sage-devel.  This patch should definitely be included
though, even if none of my comments are addressed.



---

archive/issue_comments_012839.json:
```json
{
    "body": "The patch has sat in trac for about two weeks now. William suggested to merge, but maybe Nils has some more input?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12839",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch has sat in trac for about two weeks now. William suggested to merge, but maybe Nils has some more input?

Cheers,

Michael



---

archive/issue_comments_012840.json:
```json
{
    "body": "This patch can _certainly_ be applied as is, since it just adds some useful info to docstrings.\n\nThe only remaining issues from the sage-devel discussion that I can see are some odd timing issues.  But that does not seem a reason to hold back on this.",
    "created_at": "2008-02-16T20:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12840",
    "user": "https://github.com/JohnCremona"
}
```

This patch can _certainly_ be applied as is, since it just adds some useful info to docstrings.

The only remaining issues from the sage-devel discussion that I can see are some odd timing issues.  But that does not seem a reason to hold back on this.



---

archive/issue_comments_012841.json:
```json
{
    "body": "Ok, I consider John's review to be a positive one. Changing the subject accordingly. The patch applies cleanly against my current 2.10.2.alpha1 buil.d",
    "created_at": "2008-02-16T20:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I consider John's review to be a positive one. Changing the subject accordingly. The patch applies cleanly against my current 2.10.2.alpha1 buil.d



---

archive/issue_events_002143.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-16T20:45:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1987#event-2143"
}
```



---

archive/issue_comments_012842.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T20:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12842",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012843.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T20:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1987#issuecomment-12843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
