# Issue 7705: graphs: replace the worldmap sobj by some code (or something else that is transparent)

archive/issues_007705.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ncohen\n\nThis command in sage-4.3 returns a loaded sobj:\n\n```\nsage: graphs.WorldMap()\nGraph on 251 vertices\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7705\n\n",
    "created_at": "2009-12-16T08:45:55Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "graphs: replace the worldmap sobj by some code (or something else that is transparent)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7705",
    "user": "was"
}
```
Assignee: rlm

CC:  ncohen

This command in sage-4.3 returns a loaded sobj:

```
sage: graphs.WorldMap()
Graph on 251 vertices
```


Issue created by migration from https://trac.sagemath.org/ticket/7705





---

archive/issue_comments_066121.json:
```json
{
    "body": "See also #7706.",
    "created_at": "2009-12-16T08:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66121",
    "user": "was"
}
```

See also #7706.



---

archive/issue_comments_066122.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T18:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66122",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066123.json:
```json
{
    "body": "With this patch applied, the file SAGE_DATA+\"graphs/graph_world.sobj\" could be removed !\n\nNathann",
    "created_at": "2009-12-16T18:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66123",
    "user": "ncohen"
}
```

With this patch applied, the file SAGE_DATA+"graphs/graph_world.sobj" could be removed !

Nathann



---

archive/issue_comments_066124.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T18:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66124",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066125.json:
```json
{
    "body": "Thanks.  However, you forgot to include the gps_coordinates attribute that was in graph_world.sobj.",
    "created_at": "2009-12-17T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66125",
    "user": "was"
}
```

Thanks.  However, you forgot to include the gps_coordinates attribute that was in graph_world.sobj.



---

archive/issue_comments_066126.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-17T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66126",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066127.json:
```json
{
    "body": "You're absolutely right !! With some luck, someone will take the time to translate these GPS coordinates using the Mercator projection to obtain good plottings of the world :-)\n\nNathann",
    "created_at": "2009-12-17T09:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66127",
    "user": "ncohen"
}
```

You're absolutely right !! With some luck, someone will take the time to translate these GPS coordinates using the Mercator projection to obtain good plottings of the world :-)

Nathann



---

archive/issue_comments_066128.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-17T09:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66128",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066129.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-17T21:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66129",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_066130.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-17T21:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66130",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_066131.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-17T21:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66131",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T20:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7705#issuecomment-66132",
    "user": "mhansen"
}
```

Resolution: fixed
