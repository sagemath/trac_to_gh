# Issue 8467: move the document "Linear Programming in Sage" to "Sage HOWTOs"

archive/issues_008467.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @nathanncohen @jasongrout\n\nKeywords: linear programming\n\nMove the document \"Linear Programming in Sage\", found [here](http://www.sagemath.org/doc/constructions/linear_programming.html) and [here](http://www-sop.inria.fr/members/Nathann.Cohen/tut/LP/), to the classification \"Sage HOWTOs\". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8467\n\n",
    "created_at": "2010-03-07T02:18:58Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "move the document \"Linear Programming in Sage\" to \"Sage HOWTOs\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @nathanncohen @jasongrout

Keywords: linear programming

Move the document "Linear Programming in Sage", found [here](http://www.sagemath.org/doc/constructions/linear_programming.html) and [here](http://www-sop.inria.fr/members/Nathann.Cohen/tut/LP/), to the classification "Sage HOWTOs". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).

Issue created by migration from https://trac.sagemath.org/ticket/8467





---

archive/issue_comments_076115.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-09T12:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76115",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_076116.json:
```json
{
    "body": "Here is where I have for the moment. I still need to rewrite LP examples for some problems, but at least I reformatted everything for Sphinx.\n\nIt will require the new LP patch enabling a new syntax for constraints #7311\n\nNathann",
    "created_at": "2010-03-09T12:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76116",
    "user": "https://github.com/nathanncohen"
}
```

Here is where I have for the moment. I still need to rewrite LP examples for some problems, but at least I reformatted everything for Sphinx.

It will require the new LP patch enabling a new syntax for constraints #7311

Nathann



---

archive/issue_comments_076117.json:
```json
{
    "body": "Oh yes, and there is also something to take care of : the new patch for CPLEX support brings changes to the current LP document in the Constructions manual... Only a few lines concerning CPLEX at the end of it, and some fixes, but we should not lose it when deleting the current document and replacing it with this one in the HOWTO manual :-)\n\nNathann",
    "created_at": "2010-03-09T12:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76117",
    "user": "https://github.com/nathanncohen"
}
```

Oh yes, and there is also something to take care of : the new patch for CPLEX support brings changes to the current LP document in the Constructions manual... Only a few lines concerning CPLEX at the end of it, and some fixes, but we should not lose it when deleting the current document and replacing it with this one in the HOWTO manual :-)

Nathann



---

archive/issue_comments_076118.json:
```json
{
    "body": "this version passes doctests !\n\nNathann",
    "created_at": "2010-03-16T11:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76118",
    "user": "https://github.com/nathanncohen"
}
```

this version passes doctests !

Nathann



---

archive/issue_comments_076119.json:
```json
{
    "body": "Here it is ! :-)",
    "created_at": "2010-03-16T23:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76119",
    "user": "https://github.com/nathanncohen"
}
```

Here it is ! :-)



---

archive/issue_comments_076120.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-16T23:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76120",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076121.json:
```json
{
    "body": "Attachment [linear_programming2.rst](tarball://root/attachments/some-uuid/ticket8467/linear_programming2.rst) by @jasongrout created at 2010-05-14 21:04:13",
    "created_at": "2010-05-14T21:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76121",
    "user": "https://github.com/jasongrout"
}
```

Attachment [linear_programming2.rst](tarball://root/attachments/some-uuid/ticket8467/linear_programming2.rst) by @jasongrout created at 2010-05-14 21:04:13



---

archive/issue_comments_076122.json:
```json
{
    "body": "I've read up to the \"Maximum average degree\" problem, and I have some found some errata:\n\n* line 63: Errata on example LP\n* line 161: maximization instead of minimization\n* line 177: missing objective function\n* line 200-204: problem not written properly\n* line 204: alternative formulation with only one variable for each edge\n\nI adjoint a rst file with corrections. The example on \"Maximum average degree\" is correct but I find it harder to follow than the previous ones, for a non-expert in graph-theory. I don't know which is the target audience...",
    "created_at": "2010-07-20T16:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76122",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

I've read up to the "Maximum average degree" problem, and I have some found some errata:

* line 63: Errata on example LP
* line 161: maximization instead of minimization
* line 177: missing objective function
* line 200-204: problem not written properly
* line 204: alternative formulation with only one variable for each edge

I adjoint a rst file with corrections. The example on "Maximum average degree" is correct but I find it harder to follow than the previous ones, for a non-expert in graph-theory. I don't know which is the target audience...



---

archive/issue_comments_076123.json:
```json
{
    "body": "Attachment [linear_programming2_some_changes.rst](tarball://root/attachments/some-uuid/ticket8467/linear_programming2_some_changes.rst) by @nathanncohen created at 2010-07-21 02:29:03\n\nThank you very much for reading it until then !!! Actually, I will need to change some parts of it now that GLPK is a standard SPKG. I will also update the end of it, to give more natural examples :-)\n\nI am setting it to \"needs work\" until this is done !!\n\nNathann",
    "created_at": "2010-07-21T02:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76123",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [linear_programming2_some_changes.rst](tarball://root/attachments/some-uuid/ticket8467/linear_programming2_some_changes.rst) by @nathanncohen created at 2010-07-21 02:29:03

Thank you very much for reading it until then !!! Actually, I will need to change some parts of it now that GLPK is a standard SPKG. I will also update the end of it, to give more natural examples :-)

I am setting it to "needs work" until this is done !!

Nathann



---

archive/issue_comments_076124.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-21T02:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76124",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076125.json:
```json
{
    "body": "When this is ready, could you produce it as a Mercurial patch file?",
    "created_at": "2010-07-28T01:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76125",
    "user": "https://github.com/jhpalmieri"
}
```

When this is ready, could you produce it as a Mercurial patch file?



---

archive/issue_comments_076126.json:
```json
{
    "body": "Of course of course ! :-)",
    "created_at": "2010-07-28T02:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76126",
    "user": "https://github.com/nathanncohen"
}
```

Of course of course ! :-)



---

archive/issue_comments_076127.json:
```json
{
    "body": "This ticket should be closed as a duplicate of #9836 `:-)`\n\nNathann",
    "created_at": "2010-09-04T11:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76127",
    "user": "https://github.com/nathanncohen"
}
```

This ticket should be closed as a duplicate of #9836 `:-)`

Nathann



---

archive/issue_events_008651.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-09-10T12:50:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8467#event-8651"
}
```



---

archive/issue_comments_076128.json:
```json
{
    "body": "Close as duplicate of #9836.",
    "created_at": "2010-09-10T12:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76128",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as duplicate of #9836.



---

archive/issue_comments_076129.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-10T12:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8467#issuecomment-76129",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate
