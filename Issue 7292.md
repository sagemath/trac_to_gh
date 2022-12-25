# Issue 7292: Max Vertex/Edge disjoint st-paths

archive/issues_007292.json:
```json
{
    "body": "Assignee: @rlmill\n\nWith the flow function from #7592, functions returning a maximal number of Vertex/Edge disjoint st-path should be defined. The will obviously use the flow functions, but in many applications the user is just interested in these paths, and so there should be an easy way to find them in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7292\n\n",
    "closed_at": "2010-01-13T11:39:11Z",
    "created_at": "2009-10-25T09:23:47Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Max Vertex/Edge disjoint st-paths",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7292",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

With the flow function from #7592, functions returning a maximal number of Vertex/Edge disjoint st-path should be defined. The will obviously use the flow functions, but in many applications the user is just interested in these paths, and so there should be an easy way to find them in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/7292





---

archive/issue_comments_060592.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-15T14:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60592",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060593.json:
```json
{
    "body": "`vertex_disjoint_paths` loops forever...",
    "created_at": "2009-12-15T18:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60593",
    "user": "https://github.com/rlmill"
}
```

`vertex_disjoint_paths` loops forever...



---

archive/issue_comments_060594.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T18:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60594",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060595.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T00:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60595",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060596.json:
```json
{
    "body": "not anymore :-)",
    "created_at": "2009-12-16T00:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60596",
    "user": "https://github.com/nathanncohen"
}
```

not anymore :-)



---

archive/issue_comments_060597.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T02:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60597",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060598.json:
```json
{
    "body": "Attachment [trac_7292.patch](tarball://root/attachments/some-uuid/ticket7292/trac_7292.patch) by @rlmill created at 2009-12-16 02:56:13",
    "created_at": "2009-12-16T02:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60598",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7292.patch](tarball://root/attachments/some-uuid/ticket7292/trac_7292.patch) by @rlmill created at 2009-12-16 02:56:13



---

archive/issue_comments_060599.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-19T23:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60599",
    "user": "https://github.com/mwhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_060600.json:
```json
{
    "body": "I get the following failure:\n\n```\n**********************************************************************\nFile \"/scratch/mhansen/release/4.3/rc1/sage-4.3.rc1/devel/sage-main/sage/graphs/graph.py\", line 3581:\n    sage: g.vertex_cover(value_only=True)\nExpected:\n    9\nGot nothing\n**********************************************************************\n```",
    "created_at": "2009-12-19T23:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60600",
    "user": "https://github.com/mwhansen"
}
```

I get the following failure:

```
**********************************************************************
File "/scratch/mhansen/release/4.3/rc1/sage-4.3.rc1/devel/sage-main/sage/graphs/graph.py", line 3581:
    sage: g.vertex_cover(value_only=True)
Expected:
    9
Got nothing
**********************************************************************
```



---

archive/issue_comments_060601.json:
```json
{
    "body": "This is because of an odd thing : when this patch is applied over #7600, the body of vertex_cover totally disappears : only the docstring remains, and the function returns nothing. I will send an updated version of the patch \"after\" #7600 has been applied :-)",
    "created_at": "2009-12-20T16:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60601",
    "user": "https://github.com/nathanncohen"
}
```

This is because of an odd thing : when this patch is applied over #7600, the body of vertex_cover totally disappears : only the docstring remains, and the function returns nothing. I will send an updated version of the patch "after" #7600 has been applied :-)



---

archive/issue_comments_060602.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-20T16:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60602",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060603.json:
```json
{
    "body": "Here it is !!\n\nPlease check, when appying it, that nothing disappears \"above\" and \"after\" the added sections ! If this version is not easier to apply, I think the best way would be to create a patch based upon the version you are working on and the patch you already applied (this should not be long though, this patch just adds two consecutive functions)\n\nSorry for the trouble ! :-)\n\nNathann",
    "created_at": "2009-12-20T16:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60603",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !!

Please check, when appying it, that nothing disappears "above" and "after" the added sections ! If this version is not easier to apply, I think the best way would be to create a patch based upon the version you are working on and the patch you already applied (this should not be long though, this patch just adds two consecutive functions)

Sorry for the trouble ! :-)

Nathann



---

archive/issue_comments_060604.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T16:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60604",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060605.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-10T08:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60605",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060606.json:
```json
{
    "body": "Rebased !\n\nNathann",
    "created_at": "2010-01-10T08:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60606",
    "user": "https://github.com/nathanncohen"
}
```

Rebased !

Nathann



---

archive/issue_comments_060607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T11:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60607",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_017246.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T11:39:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7292#event-17246"
}
```



---

archive/issue_comments_060608.json:
```json
{
    "body": "Attachment [trac_7292-2.patch](tarball://root/attachments/some-uuid/ticket7292/trac_7292-2.patch) by @rlmill created at 2010-01-13 11:39:11\n\npositive review",
    "created_at": "2010-01-13T11:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7292#issuecomment-60608",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7292-2.patch](tarball://root/attachments/some-uuid/ticket7292/trac_7292-2.patch) by @rlmill created at 2010-01-13 11:39:11

positive review
