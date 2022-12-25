# Issue 7705: graphs: replace the worldmap sobj by some code (or something else that is transparent)

archive/issues_007705.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen\n\nThis command in sage-4.3 returns a loaded sobj:\n\n```\nsage: graphs.WorldMap()\nGraph on 251 vertices\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7705\n\n",
    "created_at": "2009-12-16T08:45:55Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "graphs: replace the worldmap sobj by some code (or something else that is transparent)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7705",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

CC:  @nathanncohen

This command in sage-4.3 returns a loaded sobj:

```
sage: graphs.WorldMap()
Graph on 251 vertices
```

Issue created by migration from https://trac.sagemath.org/ticket/7705





---

archive/issue_comments_066005.json:
```json
{
    "body": "See also #7706.",
    "created_at": "2009-12-16T08:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66005",
    "user": "https://github.com/williamstein"
}
```

See also #7706.



---

archive/issue_comments_066006.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T18:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66006",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066007.json:
```json
{
    "body": "With this patch applied, the file SAGE_DATA+\"graphs/graph_world.sobj\" could be removed !\n\nNathann",
    "created_at": "2009-12-16T18:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66007",
    "user": "https://github.com/nathanncohen"
}
```

With this patch applied, the file SAGE_DATA+"graphs/graph_world.sobj" could be removed !

Nathann



---

archive/issue_comments_066008.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T18:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66008",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066009.json:
```json
{
    "body": "Thanks.  However, you forgot to include the gps_coordinates attribute that was in graph_world.sobj.",
    "created_at": "2009-12-17T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66009",
    "user": "https://github.com/williamstein"
}
```

Thanks.  However, you forgot to include the gps_coordinates attribute that was in graph_world.sobj.



---

archive/issue_comments_066010.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-17T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66010",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066011.json:
```json
{
    "body": "You're absolutely right !! With some luck, someone will take the time to translate these GPS coordinates using the Mercator projection to obtain good plottings of the world :-)\n\nNathann",
    "created_at": "2009-12-17T09:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66011",
    "user": "https://github.com/nathanncohen"
}
```

You're absolutely right !! With some luck, someone will take the time to translate these GPS coordinates using the Mercator projection to obtain good plottings of the world :-)

Nathann



---

archive/issue_comments_066012.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-17T09:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66012",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066013.json:
```json
{
    "body": "Attachment [trac_7705.patch](tarball://root/attachments/some-uuid/ticket7705/trac_7705.patch) by @rlmill created at 2009-12-17 21:39:38",
    "created_at": "2009-12-17T21:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66013",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7705.patch](tarball://root/attachments/some-uuid/ticket7705/trac_7705.patch) by @rlmill created at 2009-12-17 21:39:38



---

archive/issue_comments_066014.json:
```json
{
    "body": "Attachment [trac_7705-docs.patch](tarball://root/attachments/some-uuid/ticket7705/trac_7705-docs.patch) by @rlmill created at 2009-12-17 21:40:03",
    "created_at": "2009-12-17T21:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66014",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7705-docs.patch](tarball://root/attachments/some-uuid/ticket7705/trac_7705-docs.patch) by @rlmill created at 2009-12-17 21:40:03



---

archive/issue_comments_066015.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-17T21:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66015",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066016.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T20:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66016",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018403.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-19T20:21:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7705#event-18403"
}
```



---

archive/issue_events_018404.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:43:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7705#event-18404"
}
```
