# Issue 6764: Independent Set of Representatives

archive/issues_006764.json:
```json
{
    "body": "Assignee: @rlmill\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/9d9b09274f1eab83/79938a2139ba25d9?lnk=gst&q=isr#79938a2139ba25d9\n\nThis patch add the ISR() function for graphs. The Independent Set of Representatives is a generalisation of graph coloring and list coloring, but goes way further ! I tried to take care of the documentation, so you will find some more informations in the docstrings if you need it ! ;-)\n\nThis patch uses Linear Programming, so you will have to first install GLPK (see #6867), then the patch for numerical.MIP at #6869 ;-) \n\nIssue created by migration from https://trac.sagemath.org/ticket/6764\n\n",
    "closed_at": "2009-12-20T07:26:57Z",
    "created_at": "2009-08-16T17:06:55Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Independent Set of Representatives",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6764",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

See http://groups.google.com/group/sage-devel/browse_thread/thread/9d9b09274f1eab83/79938a2139ba25d9?lnk=gst&q=isr#79938a2139ba25d9

This patch add the ISR() function for graphs. The Independent Set of Representatives is a generalisation of graph coloring and list coloring, but goes way further ! I tried to take care of the documentation, so you will find some more informations in the docstrings if you need it ! ;-)

This patch uses Linear Programming, so you will have to first install GLPK (see #6867), then the patch for numerical.MIP at #6869 ;-) 

Issue created by migration from https://trac.sagemath.org/ticket/6764





---

archive/issue_comments_055595.json:
```json
{
    "body": "As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.\n\nSorry for the trouble, I'll try to make it quick !\n\nNathann",
    "created_at": "2009-08-31T15:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55595",
    "user": "https://github.com/nathanncohen"
}
```

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann



---

archive/issue_comments_055596.json:
```json
{
    "body": "Just updated, everything is ready for review :-)\n\nThanks again for your help !\n\nNathann",
    "created_at": "2009-09-06T16:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55596",
    "user": "https://github.com/nathanncohen"
}
```

Just updated, everything is ready for review :-)

Thanks again for your help !

Nathann



---

archive/issue_comments_055597.json:
```json
{
    "body": "rebased for 4.3.rc1",
    "created_at": "2009-12-15T16:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55597",
    "user": "https://github.com/rlmill"
}
```

rebased for 4.3.rc1



---

archive/issue_comments_055598.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T16:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55598",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055599.json:
```json
{
    "body": "Attachment [ISR.patch](tarball://root/attachments/some-uuid/ticket6764/ISR.patch) by @rlmill created at 2009-12-15 16:38:01\n\n1. The doctest needs to be marked as optional.\n\n2. There should be more examples.\n\n3. Whether or not GLPK is installed, the import `from sage.numerical.mip import MIP` fails. I suppose this is a rather old patch, should `MIP` be `MixedIntegerLinearProgram`?\n\n4. \"rebased for 4.3.rc1\" means 4.3.rc0 + #7640 + #7674 + #7673, all of which are merged in rc1.",
    "created_at": "2009-12-15T16:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55599",
    "user": "https://github.com/rlmill"
}
```

Attachment [ISR.patch](tarball://root/attachments/some-uuid/ticket6764/ISR.patch) by @rlmill created at 2009-12-15 16:38:01

1. The doctest needs to be marked as optional.

2. There should be more examples.

3. Whether or not GLPK is installed, the import `from sage.numerical.mip import MIP` fails. I suppose this is a rather old patch, should `MIP` be `MixedIntegerLinearProgram`?

4. "rebased for 4.3.rc1" means 4.3.rc0 + #7640 + #7674 + #7673, all of which are merged in rc1.



---

archive/issue_comments_055600.json:
```json
{
    "body": "This is a rather old patch. I'll update it immediately !",
    "created_at": "2009-12-15T16:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55600",
    "user": "https://github.com/nathanncohen"
}
```

This is a rather old patch. I'll update it immediately !



---

archive/issue_comments_055601.json:
```json
{
    "body": "Updated !",
    "created_at": "2009-12-15T18:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55601",
    "user": "https://github.com/nathanncohen"
}
```

Updated !



---

archive/issue_comments_055602.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-15T18:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55602",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055603.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T19:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55603",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055604.json:
```json
{
    "body": "You haven't really addressed #2.",
    "created_at": "2009-12-15T19:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55604",
    "user": "https://github.com/rlmill"
}
```

You haven't really addressed #2.



---

archive/issue_comments_055605.json:
```json
{
    "body": "(item 2 not ticket # 2)",
    "created_at": "2009-12-15T19:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55605",
    "user": "https://github.com/rlmill"
}
```

(item 2 not ticket # 2)



---

archive/issue_comments_055606.json:
```json
{
    "body": "This one should be better then :-)",
    "created_at": "2009-12-16T00:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55606",
    "user": "https://github.com/nathanncohen"
}
```

This one should be better then :-)



---

archive/issue_comments_055607.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T00:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55607",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055608.json:
```json
{
    "body": "Attachment [trac_6764.patch](tarball://root/attachments/some-uuid/ticket6764/trac_6764.patch) by @nathanncohen created at 2009-12-16 00:41:57",
    "created_at": "2009-12-16T00:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55608",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_6764.patch](tarball://root/attachments/some-uuid/ticket6764/trac_6764.patch) by @nathanncohen created at 2009-12-16 00:41:57



---

archive/issue_comments_055609.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T02:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55609",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055610.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-20T07:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6764#issuecomment-55610",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_015941.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:26:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6764#event-15941"
}
```



---

archive/issue_events_015942.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:26:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6764",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6764#event-15942"
}
```
