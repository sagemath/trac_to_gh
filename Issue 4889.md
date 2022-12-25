# Issue 4889: deprecate matrix.list()

archive/issues_004889.json:
```json
{
    "body": "Assignee: @williamstein\n\nlist(M) and M.list() returning different lists is inconsistent. As discussed at http://groups.google.com/group/sage-support/browse_thread/thread/a7d8b439df769e7 we should have  M.entries() which replaces M.list() and deprecate the latter. \n\nThe behavior of list(M) will remain the same, and consistency with M[i]. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4889\n\n",
    "created_at": "2008-12-30T01:01:47Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "deprecate matrix.list()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4889",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

list(M) and M.list() returning different lists is inconsistent. As discussed at http://groups.google.com/group/sage-support/browse_thread/thread/a7d8b439df769e7 we should have  M.entries() which replaces M.list() and deprecate the latter. 

The behavior of list(M) will remain the same, and consistency with M[i]. 

Issue created by migration from https://trac.sagemath.org/ticket/4889





---

archive/issue_comments_036982.json:
```json
{
    "body": "A reason to have m.list() return the entries is that m.dict() returns the entries, but in \"sparse\" dictionary format.",
    "created_at": "2009-01-21T14:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36982",
    "user": "https://github.com/jasongrout"
}
```

A reason to have m.list() return the entries is that m.dict() returns the entries, but in "sparse" dictionary format.



---

archive/issue_comments_036983.json:
```json
{
    "body": "I was coding, and I realized that I very strongly object to this ticket -- or at least the nebulousness of it -- I can't even write the code i want the way I want since I know that it will just break for sure as soon as somebody closes this ticket :-(.  For me it is an incredibly important design pattern when working with matrices to turn the entire matrix into a list of its entries -- do something with them -- then use the resulting list to make another matrix. \n\nThis is exactly modeled on Magma's `Eltseq` command, which turns almost anything in Magma into a linear sequence, and almost anything in Magma can be reconstructed from that sequence.  \n\nAnyway, the list method is not just one off thing that doesn't matter -- it's central to matrices.  So either wontfix this ticket or do it asap to get the pain over with.\n\nI do worry that changing this is changing things for change sake, and I'm not convinced that is a good idea...",
    "created_at": "2009-01-30T07:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36983",
    "user": "https://github.com/williamstein"
}
```

I was coding, and I realized that I very strongly object to this ticket -- or at least the nebulousness of it -- I can't even write the code i want the way I want since I know that it will just break for sure as soon as somebody closes this ticket :-(.  For me it is an incredibly important design pattern when working with matrices to turn the entire matrix into a list of its entries -- do something with them -- then use the resulting list to make another matrix. 

This is exactly modeled on Magma's `Eltseq` command, which turns almost anything in Magma into a linear sequence, and almost anything in Magma can be reconstructed from that sequence.  

Anyway, the list method is not just one off thing that doesn't matter -- it's central to matrices.  So either wontfix this ticket or do it asap to get the pain over with.

I do worry that changing this is changing things for change sake, and I'm not convinced that is a good idea...



---

archive/issue_comments_036984.json:
```json
{
    "body": "I have a partial patch for this.  I also worry that we are just changing things to change things, though I agree slightly that the new name (M.entries) is better than M.list in that it is more descriptive.\n\nYour first paragraph seems to indicate that it would be much better for list(M) to return a list of entries, rather than a list of rows.  Is that correct?",
    "created_at": "2009-01-30T10:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36984",
    "user": "https://github.com/jasongrout"
}
```

I have a partial patch for this.  I also worry that we are just changing things to change things, though I agree slightly that the new name (M.entries) is better than M.list in that it is more descriptive.

Your first paragraph seems to indicate that it would be much better for list(M) to return a list of entries, rather than a list of rows.  Is that correct?



---

archive/issue_comments_036985.json:
```json
{
    "body": "For what it's worth, for a numpy array A, the iterator over all entries is given by A.flat",
    "created_at": "2009-01-30T10:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36985",
    "user": "https://github.com/jasongrout"
}
```

For what it's worth, for a numpy array A, the iterator over all entries is given by A.flat



---

archive/issue_comments_036986.json:
```json
{
    "body": "See http://www.wstein.org/home/wstein/build/sage-4.3.1.rc0-boxen-x86_64-Linux/4889-part1.out for the output of doctests on part1.  Fixing all those (many) issues is all that is left.",
    "created_at": "2010-01-17T14:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36986",
    "user": "https://github.com/williamstein"
}
```

See http://www.wstein.org/home/wstein/build/sage-4.3.1.rc0-boxen-x86_64-Linux/4889-part1.out for the output of doctests on part1.  Fixing all those (many) issues is all that is left.



---

archive/issue_comments_036987.json:
```json
{
    "body": "See also http://www.wstein.org/home/wstein/build/sage-4.3.1.rc0-boxen-x86_64-Linux/4889-part1-error_not_warn.out\n\nThough I just spent a substantial amount of time on this ticket, I'm *seriously* considering arguing again that this change should *not* be made.  The reason is simply if literally hundreds of files in the Sage distro are so intensely impacted, then lots of external code will be too.  And this change simply isn't *that* important.  Better could be to just document the list method better, and point out the subtlety.",
    "created_at": "2010-01-17T14:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36987",
    "user": "https://github.com/williamstein"
}
```

See also http://www.wstein.org/home/wstein/build/sage-4.3.1.rc0-boxen-x86_64-Linux/4889-part1-error_not_warn.out

Though I just spent a substantial amount of time on this ticket, I'm *seriously* considering arguing again that this change should *not* be made.  The reason is simply if literally hundreds of files in the Sage distro are so intensely impacted, then lots of external code will be too.  And this change simply isn't *that* important.  Better could be to just document the list method better, and point out the subtlety.



---

archive/issue_comments_036988.json:
```json
{
    "body": "Attachment [trac_4889-part1.patch](tarball://root/attachments/some-uuid/ticket4889/trac_4889-part1.patch) by @williamstein created at 2010-01-18 00:48:36\n\npart 1, which does what is needed in the matrix directory; another part will mop up.",
    "created_at": "2010-01-18T00:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36988",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4889-part1.patch](tarball://root/attachments/some-uuid/ticket4889/trac_4889-part1.patch) by @williamstein created at 2010-01-18 00:48:36

part 1, which does what is needed in the matrix directory; another part will mop up.



---

archive/issue_comments_036989.json:
```json
{
    "body": "OK, after working on this for hours and hours, and changing a ridiculous amount of little stuff (see attached patch, still called -part1), I even more strongly believe this \".list()\" usage is deeply entrenched throughout all of Sage.  I refuse to make this deprecation change, since it will certainly introduce subtle issues in SAge, and will likely break a lot of code that isn't in Sage.  Instead I'm posting a patch to document the subtlety clearly.",
    "created_at": "2010-01-18T01:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36989",
    "user": "https://github.com/williamstein"
}
```

OK, after working on this for hours and hours, and changing a ridiculous amount of little stuff (see attached patch, still called -part1), I even more strongly believe this ".list()" usage is deeply entrenched throughout all of Sage.  I refuse to make this deprecation change, since it will certainly introduce subtle issues in SAge, and will likely break a lot of code that isn't in Sage.  Instead I'm posting a patch to document the subtlety clearly.



---

archive/issue_comments_036990.json:
```json
{
    "body": "apply this instead of the previous",
    "created_at": "2010-01-18T01:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36990",
    "user": "https://github.com/williamstein"
}
```

apply this instead of the previous



---

archive/issue_comments_036991.json:
```json
{
    "body": "Attachment [trac_4889-document_instead_of_deprecate.patch](tarball://root/attachments/some-uuid/ticket4889/trac_4889-document_instead_of_deprecate.patch) by @williamstein created at 2010-01-18 01:08:24",
    "created_at": "2010-01-18T01:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36991",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4889-document_instead_of_deprecate.patch](tarball://root/attachments/some-uuid/ticket4889/trac_4889-document_instead_of_deprecate.patch) by @williamstein created at 2010-01-18 01:08:24



---

archive/issue_comments_036992.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T01:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36992",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036993.json:
```json
{
    "body": "I'll post a patch which makes .entries an alias for list.  I think it's a better name, and better enough that it's worth having two names and encouraging people to use M.entries().",
    "created_at": "2010-01-18T18:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36993",
    "user": "https://github.com/jasongrout"
}
```

I'll post a patch which makes .entries an alias for list.  I think it's a better name, and better enough that it's worth having two names and encouraging people to use M.entries().



---

archive/issue_comments_036994.json:
```json
{
    "body": "I agree with William that this is too big of a change to make, though +1 to encouraging an alias entries as it is more explicit.",
    "created_at": "2010-01-18T19:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36994",
    "user": "https://github.com/robertwb"
}
```

I agree with William that this is too big of a change to make, though +1 to encouraging an alias entries as it is more explicit.



---

archive/issue_comments_036995.json:
```json
{
    "body": "Yes, +1 to the alias.",
    "created_at": "2010-01-18T22:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36995",
    "user": "https://github.com/williamstein"
}
```

Yes, +1 to the alias.



---

archive/issue_comments_036996.json:
```json
{
    "body": "I don't really care if the alias goes in, but this looks fine to me.",
    "created_at": "2010-02-17T20:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36996",
    "user": "https://github.com/ncalexan"
}
```

I don't really care if the alias goes in, but this looks fine to me.



---

archive/issue_comments_036997.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T20:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36997",
    "user": "https://github.com/ncalexan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036998.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T22:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36998",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_005133.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-18T22:03:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4889#event-5133"
}
```



---

archive/issue_comments_036999.json:
```json
{
    "body": "Merged [trac_4889-document_instead_of_deprecate.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4889/trac_4889-document_instead_of_deprecate.patch).",
    "created_at": "2010-02-18T22:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-36999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_4889-document_instead_of_deprecate.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/4889/trac_4889-document_instead_of_deprecate.patch).



---

archive/issue_comments_037000.json:
```json
{
    "body": "Changing the title to reflect what was actually done.",
    "created_at": "2010-02-19T16:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-37000",
    "user": "https://github.com/jasongrout"
}
```

Changing the title to reflect what was actually done.



---

archive/issue_comments_037001.json:
```json
{
    "body": "I've made a new ticket to add the m.entries() alias: #8308.",
    "created_at": "2010-02-19T16:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4889#issuecomment-37001",
    "user": "https://github.com/jasongrout"
}
```

I've made a new ticket to add the m.entries() alias: #8308.
