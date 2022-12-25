# Issue 9741: Sorting vertices of a graph

archive/issues_009741.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis patch adds a \"key\" argument to allow custom sorting of the output of the graph method vertices().  It adds to the documentation to make it clear that vertices will not always have a default sort order.\n\nSee:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/40ac90ee3f28d723/\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/5adbb850f787373c/\n\nIssue created by migration from https://trac.sagemath.org/ticket/9741\n\n",
    "created_at": "2010-08-13T17:17:45Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Sorting vertices of a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9741",
    "user": "https://github.com/rbeezer"
}
```
Assignee: jason, ncohen, rlm

This patch adds a "key" argument to allow custom sorting of the output of the graph method vertices().  It adds to the documentation to make it clear that vertices will not always have a default sort order.

See:

http://groups.google.com/group/sage-devel/browse_thread/thread/40ac90ee3f28d723/
http://groups.google.com/group/sage-devel/browse_thread/thread/5adbb850f787373c/

Issue created by migration from https://trac.sagemath.org/ticket/9741





---

archive/issue_comments_095214.json:
```json
{
    "body": "Attachment [trac_9741-graph-vertices-sort.patch](tarball://root/attachments/some-uuid/ticket9741/trac_9741-graph-vertices-sort.patch) by @rbeezer created at 2010-08-13 17:26:38",
    "created_at": "2010-08-13T17:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95214",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9741-graph-vertices-sort.patch](tarball://root/attachments/some-uuid/ticket9741/trac_9741-graph-vertices-sort.patch) by @rbeezer created at 2010-08-13 17:26:38



---

archive/issue_comments_095215.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-13T17:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95215",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095216.json:
```json
{
    "body": "Great idea!  So what about those functions that call vertices(), like adjacency matrix, for example?  Will they have a default key?",
    "created_at": "2010-08-14T02:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95216",
    "user": "https://github.com/jasongrout"
}
```

Great idea!  So what about those functions that call vertices(), like adjacency matrix, for example?  Will they have a default key?



---

archive/issue_comments_095217.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Great idea!  So what about those functions that call vertices(), like adjacency matrix, for example?  Will they have a default key?\n\n\nThe default value for key (in Python) is None.  I've specified None as the default for the key argument in this new function, so the behavior should be unchanged in other places that call vertices(), though after this patch that could be changed easily.  This patch is really just a convenience, but more about highlighting that you should think about how the sorting is going to work (or not work) if you have \"exotic\" objects for vertices.",
    "created_at": "2010-08-14T03:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95217",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:2 jason]:
> Great idea!  So what about those functions that call vertices(), like adjacency matrix, for example?  Will they have a default key?


The default value for key (in Python) is None.  I've specified None as the default for the key argument in this new function, so the behavior should be unchanged in other places that call vertices(), though after this patch that could be changed easily.  This patch is really just a convenience, but more about highlighting that you should think about how the sorting is going to work (or not work) if you have "exotic" objects for vertices.



---

archive/issue_comments_095218.json:
```json
{
    "body": "Hello !!!\n\nWould it be possible to make a \n\n\"Return the list of vertices\"\n\nout of your\n\n\"Return a list of the vertices, usually as a sorted list\" (Why \"usually as\") ?\n\nWhen key=None, it is sorted using the \"default\" order...  And anyway your docstrings make it perfectly clear later `:-)`\n\nNathann",
    "created_at": "2010-09-07T15:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95218",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

Would it be possible to make a 

"Return the list of vertices"

out of your

"Return a list of the vertices, usually as a sorted list" (Why "usually as") ?

When key=None, it is sorted using the "default" order...  And anyway your docstrings make it perfectly clear later `:-)`

Nathann



---

archive/issue_comments_095219.json:
```json
{
    "body": "Attachment [trac_9741-graph-vertices-sort-v2.patch](tarball://root/attachments/some-uuid/ticket9741/trac_9741-graph-vertices-sort-v2.patch) by @rbeezer created at 2010-09-07 19:11:20\n\nStandalone patch, apply only this",
    "created_at": "2010-09-07T19:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95219",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9741-graph-vertices-sort-v2.patch](tarball://root/attachments/some-uuid/ticket9741/trac_9741-graph-vertices-sort-v2.patch) by @rbeezer created at 2010-09-07 19:11:20

Standalone patch, apply only this



---

archive/issue_comments_095220.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n> Would it be possible to make a \n> \n> \"Return the list of vertices\"\n> \n> out of your\n> \n> \"Return a list of the vertices, usually as a sorted list\" (Why \"usually as\") ?\n\n\nYes, new v2 patch has this change.  My original goal was to make the default sorting behavior more obvious, but you are right that the doctests should do the job of explaining that.\n\nThanks,\nRob",
    "created_at": "2010-09-07T19:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95220",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:4 ncohen]:
> Would it be possible to make a 
> 
> "Return the list of vertices"
> 
> out of your
> 
> "Return a list of the vertices, usually as a sorted list" (Why "usually as") ?


Yes, new v2 patch has this change.  My original goal was to make the default sorting behavior more obvious, but you are right that the doctests should do the job of explaining that.

Thanks,
Rob



---

archive/issue_comments_095221.json:
```json
{
    "body": "Nothing to add ! Positive review `:-)`\n\nNathann",
    "created_at": "2010-09-07T20:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95221",
    "user": "https://github.com/nathanncohen"
}
```

Nothing to add ! Positive review `:-)`

Nathann



---

archive/issue_comments_095222.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-07T20:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95222",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024393.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T22:52:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9741#event-24393"
}
```



---

archive/issue_comments_095223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95223",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_095224.json:
```json
{
    "body": "We'll need to add a patch at #4000 to update this test line:\n\n```python\n    sage: dsc = sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense.discriminant\n```\nI think we can use `Polynomial_rational_flint`, instead. See [comment:ticket:4000:88 comment 88].",
    "created_at": "2010-09-18T23:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95224",
    "user": "https://github.com/qed777"
}
```

We'll need to add a patch at #4000 to update this test line:

```python
    sage: dsc = sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense.discriminant
```
I think we can use `Polynomial_rational_flint`, instead. See [comment:ticket:4000:88 comment 88].



---

archive/issue_comments_095225.json:
```json
{
    "body": "Mitesh ? Did you really intend to comment this ticket ? `O_o`\n\nNathann",
    "created_at": "2010-09-18T23:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95225",
    "user": "https://github.com/nathanncohen"
}
```

Mitesh ? Did you really intend to comment this ticket ? `O_o`

Nathann



---

archive/issue_comments_095226.json:
```json
{
    "body": "Yes, in case the suggested change somehow compromises the test.  Or was the `dsc = ...` line introduced elsewhere?",
    "created_at": "2010-09-18T23:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95226",
    "user": "https://github.com/qed777"
}
```

Yes, in case the suggested change somehow compromises the test.  Or was the `dsc = ...` line introduced elsewhere?



---

archive/issue_comments_095227.json:
```json
{
    "body": "I really have no idea what this line is about... `O_o`\n\nNathann",
    "created_at": "2010-09-18T23:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95227",
    "user": "https://github.com/nathanncohen"
}
```

I really have no idea what this line is about... `O_o`

Nathann



---

archive/issue_comments_095228.json:
```json
{
    "body": "I made a graph with polynomials as vertices.  The discriminant is a function on polynomials that I used as the key in a sort, to demo the new sorting capability of this ticket in the doctests.\n\nDid something change elsewhere?  This was passing tests before.\n\nI could change this to something different.  I'm traveling with family right now, but could work on it tomorrow night.  How urgent is a fix?\n\nRob",
    "created_at": "2010-09-19T03:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95228",
    "user": "https://github.com/rbeezer"
}
```

I made a graph with polynomials as vertices.  The discriminant is a function on polynomials that I used as the key in a sort, to demo the new sorting capability of this ticket in the doctests.

Did something change elsewhere?  This was passing tests before.

I could change this to something different.  I'm traveling with family right now, but could work on it tomorrow night.  How urgent is a fix?

Rob



---

archive/issue_comments_095229.json:
```json
{
    "body": "Replying to [comment:13 rbeezer]:\n> Did something change elsewhere?  This was passing tests before.\n\n\nTicket #4000 implements fast polynomial arithmetic over the rationals via FLINT1.  It removes the class `Polynomial_rational_dense` but \"replaces\" it with `Polynomial_rational_flint`.  \n\nWould `dsc = lambda x: x.discriminant()` work in the sorting test?  If it does, it could shield the test against changes to a lower-level API.\n\n> I could change this to something different.  I'm traveling with family right now, but could work on it tomorrow night.  How urgent is a fix?\n\n\nIt's not very urgent, though we're hoping to merge #4000 in 4.6.alpha2, which I plan to release at least a week from now (alpha1 is not yet out).  Currently, however, there's a more serious build error at #4000.",
    "created_at": "2010-09-19T05:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95229",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:13 rbeezer]:
> Did something change elsewhere?  This was passing tests before.


Ticket #4000 implements fast polynomial arithmetic over the rationals via FLINT1.  It removes the class `Polynomial_rational_dense` but "replaces" it with `Polynomial_rational_flint`.  

Would `dsc = lambda x: x.discriminant()` work in the sorting test?  If it does, it could shield the test against changes to a lower-level API.

> I could change this to something different.  I'm traveling with family right now, but could work on it tomorrow night.  How urgent is a fix?


It's not very urgent, though we're hoping to merge #4000 in 4.6.alpha2, which I plan to release at least a week from now (alpha1 is not yet out).  Currently, however, there's a more serious build error at #4000.



---

archive/issue_comments_095230.json:
```json
{
    "body": "(oops...sorry for my interruption then `^^;` )\n\nNathann",
    "created_at": "2010-09-19T08:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95230",
    "user": "https://github.com/nathanncohen"
}
```

(oops...sorry for my interruption then `^^;` )

Nathann



---

archive/issue_comments_095231.json:
```json
{
    "body": "Replying to [comment:14 mpatel]:\n\nMitesh,\n\nThanks for the explanation and suggestion.  I'll try to get something up in the next 12-24 hours.\n\nRob",
    "created_at": "2010-09-19T15:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95231",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:14 mpatel]:

Mitesh,

Thanks for the explanation and suggestion.  I'll try to get something up in the next 12-24 hours.

Rob



---

archive/issue_comments_095232.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-09-19T15:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95232",
    "user": "https://github.com/rbeezer"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_024394.json:
```json
{
    "actor": "https://github.com/rbeezer",
    "created_at": "2010-09-19T15:21:22Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9741#event-24394"
}
```



---

archive/issue_events_024395.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-19T21:57:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9741#event-24395"
}
```



---

archive/issue_comments_095233.json:
```json
{
    "body": "Thanks, Rob.  This ticket is actually already in the released 4.6.alpha1, so we probably just need to change the key function in a small patch at #4000.  I apologize for not being clear about this.",
    "created_at": "2010-09-19T21:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95233",
    "user": "https://github.com/qed777"
}
```

Thanks, Rob.  This ticket is actually already in the released 4.6.alpha1, so we probably just need to change the key function in a small patch at #4000.  I apologize for not being clear about this.



---

archive/issue_comments_095234.json:
```json
{
    "body": "Mitesh,\n\nSorry - not thinking clearly.  I got it now.  I thought carefully about messing with the ticket status - shoulda known not to!  \n\nI'll attach a fix to #4000 then.  Maybe later tonight.\n\nThanks,\nRob",
    "created_at": "2010-09-20T03:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95234",
    "user": "https://github.com/rbeezer"
}
```

Mitesh,

Sorry - not thinking clearly.  I got it now.  I thought carefully about messing with the ticket status - shoulda known not to!  

I'll attach a fix to #4000 then.  Maybe later tonight.

Thanks,
Rob



---

archive/issue_comments_095235.json:
```json
{
    "body": "Mitesh,\n\nIt would appear the `dsc = lambda ...` change would certainly fix this.  But looking at the doctests, I remember now why I did what I did.  All the other tests have keys made from lambda functions.  I wanted to show how you could write out the fully-qualified name of some function (I could have imported it, as well) and use that as the `key` function.\n\nWould it be so bad to just adjust the modules to the new names?  I could add some documentation to make it clear why this construct looks a bit odd.  But I think it would be educational for people not 100% familiar with Python having functions as first-class objects.\n\nRob",
    "created_at": "2010-09-20T05:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95235",
    "user": "https://github.com/rbeezer"
}
```

Mitesh,

It would appear the `dsc = lambda ...` change would certainly fix this.  But looking at the doctests, I remember now why I did what I did.  All the other tests have keys made from lambda functions.  I wanted to show how you could write out the fully-qualified name of some function (I could have imported it, as well) and use that as the `key` function.

Would it be so bad to just adjust the modules to the new names?  I could add some documentation to make it clear why this construct looks a bit odd.  But I think it would be educational for people not 100% familiar with Python having functions as first-class objects.

Rob



---

archive/issue_comments_095236.json:
```json
{
    "body": "No, that's sounds good to me.  Thanks for your explanation.\n\nOops:  I suppose I should have written `dsc = discriminant` or `dsc = sage.misc.functional.discriminant` above.",
    "created_at": "2010-09-20T07:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95236",
    "user": "https://github.com/qed777"
}
```

No, that's sounds good to me.  Thanks for your explanation.

Oops:  I suppose I should have written `dsc = discriminant` or `dsc = sage.misc.functional.discriminant` above.



---

archive/issue_comments_095237.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> No, that's sounds good to me.  Thanks for your explanation.\n> \n> Oops:  I suppose I should have written `dsc = discriminant` or `dsc = sage.misc.functional.discriminant` above.\n\n\nPatch to fix this, with a bit more explanation, up at #4000.\n\nThanks, Mitesh, for guiding me through this one.  First time I've had a mid-release conflict to resolve.\n\nRob",
    "created_at": "2010-09-20T18:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95237",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:20 mpatel]:
> No, that's sounds good to me.  Thanks for your explanation.
> 
> Oops:  I suppose I should have written `dsc = discriminant` or `dsc = sage.misc.functional.discriminant` above.


Patch to fix this, with a bit more explanation, up at #4000.

Thanks, Mitesh, for guiding me through this one.  First time I've had a mid-release conflict to resolve.

Rob



---

archive/issue_comments_095238.json:
```json
{
    "body": "Why should vertices be sorted in the first place? This is going to break badly in Python 3: #22349",
    "created_at": "2017-02-10T16:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9741#issuecomment-95238",
    "user": "https://github.com/jdemeyer"
}
```

Why should vertices be sorted in the first place? This is going to break badly in Python 3: #22349
