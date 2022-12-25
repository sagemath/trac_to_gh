# Issue 5017: graph.automorphism_group(translation=True) gives error in 3.2.3

archive/issues_005017.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nNikos Apostolakis wrote:\n> > The \"translation=True\" flag does not work after upgrading to sage 3.2.3\n> > I am not sure when this behaviour was introduced.  In version 2.10.2 it\n> > works fine, unfortunately I don't have a more recent old sage to check.\n> > \n> >   sage: foo = Graph()\n> >   sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])\n> >   sage: foo.automorphism_group(translation=True)\n\n\nThis worked in sage-3.1.2 and before, giving\n  (Permutation Group with generators [(1,2)(3,4)], {0: 4, 1: 1, 2: 2, 3: 3})\n\nIn sage-3.2.1 and later this fails.\n\nJaap\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5017\n\n",
    "created_at": "2009-01-18T18:29:03Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "graph.automorphism_group(translation=True) gives error in 3.2.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5017",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @rlmill


```
Nikos Apostolakis wrote:
> > The "translation=True" flag does not work after upgrading to sage 3.2.3
> > I am not sure when this behaviour was introduced.  In version 2.10.2 it
> > works fine, unfortunately I don't have a more recent old sage to check.
> > 
> >   sage: foo = Graph()
> >   sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])
> >   sage: foo.automorphism_group(translation=True)


This worked in sage-3.1.2 and before, giving
  (Permutation Group with generators [(1,2)(3,4)], {0: 4, 1: 1, 2: 2, 3: 3})

In sage-3.2.1 and later this fails.

Jaap
```


Issue created by migration from https://trac.sagemath.org/ticket/5017





---

archive/issue_comments_038153.json:
```json
{
    "body": "Attachment [trac_5017-graph_aut_gp_trans.patch](tarball://root/attachments/some-uuid/ticket5017/trac_5017-graph_aut_gp_trans.patch) by @rlmill created at 2009-01-18 20:36:18",
    "created_at": "2009-01-18T20:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5017#issuecomment-38153",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5017-graph_aut_gp_trans.patch](tarball://root/attachments/some-uuid/ticket5017/trac_5017-graph_aut_gp_trans.patch) by @rlmill created at 2009-01-18 20:36:18



---

archive/issue_comments_038154.json:
```json
{
    "body": "After the patch:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.3, Release Date: 2009-01-05                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: foo = Graph()\n\nsage:  sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])\n\nsage:  sage: foo.automorphism_group(translation=True)\n (Permutation Group with generators [(1,2)(3,4)], {0: 4, 1: 1, 2: 2, 3: 3})\n\nsage: \n\n```\n\n\nlooking at the code, patch seems ok.\n\nJaap",
    "created_at": "2009-01-18T21:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5017#issuecomment-38154",
    "user": "https://github.com/jaapspies"
}
```

After the patch:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: foo = Graph()

sage:  sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])

sage:  sage: foo.automorphism_group(translation=True)
 (Permutation Group with generators [(1,2)(3,4)], {0: 4, 1: 1, 2: 2, 3: 3})

sage: 

```


looking at the code, patch seems ok.

Jaap



---

archive/issue_comments_038155.json:
```json
{
    "body": "I can reproduce the error in sage-3.1.4 FWIW\n\nJaap",
    "created_at": "2009-01-18T23:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5017#issuecomment-38155",
    "user": "https://github.com/jaapspies"
}
```

I can reproduce the error in sage-3.1.4 FWIW

Jaap



---

archive/issue_events_011585.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-19T04:15:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5017",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5017#event-11585"
}
```



---

archive/issue_comments_038156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T04:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5017#issuecomment-38156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038157.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T04:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5017#issuecomment-38157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
