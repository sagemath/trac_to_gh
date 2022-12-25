# Issue 9422: Slightly improving is_forest

archive/issues_009422.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @rlmill mvngu\n\nAs it is implemented at the moment, the method is_forest creates a new graph for each connected component of the graph, then calls the is_tree method for each of them, which checks again that the connected components are....connected !\n\nWe can do it a bit faster :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9422\n\n",
    "created_at": "2010-07-04T11:45:46Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Slightly improving is_forest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9422",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  @rlmill mvngu

As it is implemented at the moment, the method is_forest creates a new graph for each connected component of the graph, then calls the is_tree method for each of them, which checks again that the connected components are....connected !

We can do it a bit faster :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9422





---

archive/issue_comments_089721.json:
```json
{
    "body": "Attachment [trac_9422.patch](tarball://root/attachments/some-uuid/ticket9422/trac_9422.patch) by @nathanncohen created at 2010-07-04 11:46:46",
    "created_at": "2010-07-04T11:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89721",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9422.patch](tarball://root/attachments/some-uuid/ticket9422/trac_9422.patch) by @nathanncohen created at 2010-07-04 11:46:46



---

archive/issue_comments_089722.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-04T11:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89722",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089723.json:
```json
{
    "body": "Creating a large forest : \n\n\n```\ng = graphs.RandomGNP(300,.1)\ng = g.subgraph(edges=g.min_spanning_tree())\ng.delete_edges([e for e in g.edges() if random()<.5])\nsage: g.sparse6_string()\n':~?Ck_O?gF?MAo?_??W@_AC?D`G?oE_I@GU?EE??`s@GCa??gb?[CWQa[BW?ak?wp@AEGt?m@GE_IM_?_A?g?`Y@WA_aOoAcSDHH?QAgGc{CwI`AEgPdS?HW?QCWC_IVOCeCCXc@yAW@e_Axn?U[_DfOAhu?M]?\\\\fgDX}@y_??`e?Ga_m`o?ggIG@`EGGY_AcOBhK?IT?Ye?I_uAGNhwCwRiC?WGiO?Yf?A?g?ikEIl?]AGAjC@Ir@alOJ_YAwJ_AAGAk?AgF_I?W@\\\nkW?g@kk@JL?QroN_A?zX?U?WFlw@WAmG@GD`q@Zf?M{?G_y{oa_Q|oO_E~?IoC@KGBfA_@osEw@p??wF_BD?L_rE_?poCk]?NGoCqW?[h?aAWE'\n```\n\n\nThen using two different versions of is_forest \n\n\n```\nsage: %timeit g.is_forest()\n125 loops, best of 3: 5.06 ms per loop\n\nsage: %timeit g.is_forest()\n5 loops, best of 3: 43.8 ms per loop\n```\n\n\nShort and useful... All I love ! :-)\n\nNathann",
    "created_at": "2010-07-04T11:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89723",
    "user": "https://github.com/nathanncohen"
}
```

Creating a large forest : 


```
g = graphs.RandomGNP(300,.1)
g = g.subgraph(edges=g.min_spanning_tree())
g.delete_edges([e for e in g.edges() if random()<.5])
sage: g.sparse6_string()
':~?Ck_O?gF?MAo?_??W@_AC?D`G?oE_I@GU?EE??`s@GCa??gb?[CWQa[BW?ak?wp@AEGt?m@GE_IM_?_A?g?`Y@WA_aOoAcSDHH?QAgGc{CwI`AEgPdS?HW?QCWC_IVOCeCCXc@yAW@e_Axn?U[_DfOAhu?M]?\\fgDX}@y_??`e?Ga_m`o?ggIG@`EGGY_AcOBhK?IT?Ye?I_uAGNhwCwRiC?WGiO?Yf?A?g?ikEIl?]AGAjC@Ir@alOJ_YAwJ_AAGAk?AgF_I?W@\
kW?g@kk@JL?QroN_A?zX?U?WFlw@WAmG@GD`q@Zf?M{?G_y{oa_Q|oO_E~?IoC@KGBfA_@osEw@p??wF_BD?L_rE_?poCk]?NGoCqW?[h?aAWE'
```


Then using two different versions of is_forest 


```
sage: %timeit g.is_forest()
125 loops, best of 3: 5.06 ms per loop

sage: %timeit g.is_forest()
5 loops, best of 3: 43.8 ms per loop
```


Short and useful... All I love ! :-)

Nathann



---

archive/issue_comments_089724.json:
```json
{
    "body": "See [comment:ticket:9925:20 comment 20ff] at #9925 for a flaky doctest that #9422 and #10067 should fix.",
    "created_at": "2010-10-05T21:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89724",
    "user": "https://github.com/qed777"
}
```

See [comment:ticket:9925:20 comment 20ff] at #9925 for a flaky doctest that #9422 and #10067 should fix.



---

archive/issue_comments_089725.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> See [comment:ticket:9925:20 comment 20ff] at #9925 for a flaky doctest that #9422 and #10067 should fix.\n\nI've opened #10081 for this failure.",
    "created_at": "2010-10-06T04:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89725",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 mpatel]:
> See [comment:ticket:9925:20 comment 20ff] at #9925 for a flaky doctest that #9422 and #10067 should fix.

I've opened #10081 for this failure.



---

archive/issue_comments_089726.json:
```json
{
    "body": "\"Short and useful...\" \n... and quite easy to review :P",
    "created_at": "2010-10-12T08:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89726",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

"Short and useful..." 
... and quite easy to review :P



---

archive/issue_comments_089727.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-12T08:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89727",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089728.json:
```json
{
    "body": "Thanks !!!\n\nNathann",
    "created_at": "2010-10-12T08:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89728",
    "user": "https://github.com/nathanncohen"
}
```

Thanks !!!

Nathann



---

archive/issue_comments_089729.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-21T08:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9422#issuecomment-89729",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
