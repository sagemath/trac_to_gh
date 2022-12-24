# Issue 6774: [with patch, needs review] tour Graph Theory

archive/issues_006774.json:
```json
{
    "body": "Assignee: tba\n\nHello !\n\nI thought it was a pity Sage contained nothing yet about Graph theory. This is what I have written to fix it... Merge any of your ideas in it, it can not hope to be complete !\n\nAnd.... If I forgot your country when coloring the map of Western Europe, or if you do not stand to watch Western Europe being colored while your country is not, just add the data to the document ;-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/6774\n\n",
    "created_at": "2009-08-18T17:08:45Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] tour Graph Theory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6774",
    "user": "ncohen"
}
```
Assignee: tba

Hello !

I thought it was a pity Sage contained nothing yet about Graph theory. This is what I have written to fix it... Merge any of your ideas in it, it can not hope to be complete !

And.... If I forgot your country when coloring the map of Western Europe, or if you do not stand to watch Western Europe being colored while your country is not, just add the data to the document ;-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/6774





---

archive/issue_comments_055772.json:
```json
{
    "body": "Attachment [graph_tour.patch](tarball://root/attachments/some-uuid/ticket6774/graph_tour.patch) by ncohen created at 2009-08-18 17:09:01",
    "created_at": "2009-08-18T17:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55772",
    "user": "ncohen"
}
```

Attachment [graph_tour.patch](tarball://root/attachments/some-uuid/ticket6774/graph_tour.patch) by ncohen created at 2009-08-18 17:09:01



---

archive/issue_comments_055773.json:
```json
{
    "body": "Attachment [trac-6774-graph-tour-review.patch](tarball://root/attachments/some-uuid/ticket6774/trac-6774-graph-tour-review.patch) by jason created at 2009-09-17 09:31:37\n\napply on top of previous patch",
    "created_at": "2009-09-17T09:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55773",
    "user": "jason"
}
```

Attachment [trac-6774-graph-tour-review.patch](tarball://root/attachments/some-uuid/ticket6774/trac-6774-graph-tour-review.patch) by jason created at 2009-09-17 09:31:37

apply on top of previous patch



---

archive/issue_comments_055774.json:
```json
{
    "body": "I added stylistic/punctuation corrections.  Positive review pending the examples actually working (I believe they need ncohen's patches to be merged in).",
    "created_at": "2009-09-17T09:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55774",
    "user": "jason"
}
```

I added stylistic/punctuation corrections.  Positive review pending the examples actually working (I believe they need ncohen's patches to be merged in).



---

archive/issue_comments_055775.json:
```json
{
    "body": "I guess I should change this to \"positive review\", and just say it depends on whatever tickets implement the functionality in the examples.",
    "created_at": "2009-09-17T19:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55775",
    "user": "jason"
}
```

I guess I should change this to "positive review", and just say it depends on whatever tickets implement the functionality in the examples.



---

archive/issue_comments_055776.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `graph_tour.patch`\n2. `trac-6774-graph-tour-review.patch`\n\nSee #6952 for a follow-up to this ticket.",
    "created_at": "2009-09-17T23:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55776",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `graph_tour.patch`
2. `trac-6774-graph-tour-review.patch`

See #6952 for a follow-up to this ticket.



---

archive/issue_comments_055777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-17T23:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55777",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055778.json:
```json
{
    "body": "I assume that you merged the tickets that define the functions listed here (i.e., you were able to run doctests on this file and everything was okay).  The functions in this file did not work for me with 4.1.1.alpha1, presumably because they hadn't been merged at that point.",
    "created_at": "2009-09-19T02:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55778",
    "user": "jason"
}
```

I assume that you merged the tickets that define the functions listed here (i.e., you were able to run doctests on this file and everything was okay).  The functions in this file did not work for me with 4.1.1.alpha1, presumably because they hadn't been merged at that point.



---

archive/issue_comments_055779.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> I assume that you merged the tickets that define the functions listed here\nYes, I have done so.\n\n\n\n\n\n> (i.e., you were able to run doctests on this file and everything was okay).\nYes, with the two patches on this ticket all doctests in the tutorial pass.",
    "created_at": "2009-09-19T19:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55779",
    "user": "mvngu"
}
```

Replying to [comment:4 jason]:
> I assume that you merged the tickets that define the functions listed here
Yes, I have done so.





> (i.e., you were able to run doctests on this file and everything was okay).
Yes, with the two patches on this ticket all doctests in the tutorial pass.



---

archive/issue_comments_055780.json:
```json
{
    "body": "Replying to [comment:5 mvngu]:\n> Replying to [comment:4 jason]:\n> > I assume that you merged the tickets that define the functions listed here\n> Yes, I have done so.\n\nNo, you haven't.  These functions are defined in #6679 and #6680, which haven't been reviewed, let alone merged.  This ticket should have been marked as \"depends on #6679 and #6680\": we can't have functions mentioned in the tutorial which are not yet part of Sage.  For now, the graph theory tour has been removed from the tutorial -- see #7149.\n\nWhen the tickets #6679 and #6680 have been merged, then open up a new ticket to reinstate the graph theory tour (the corrected version, as of #6952).  Before running doctests, apply the script patches from #6572 to make sure that everything is getting tested -- the current doctesting system is broken, so many doctests in .rst files are inadvertently skipped.",
    "created_at": "2009-10-08T02:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55780",
    "user": "jhpalmieri"
}
```

Replying to [comment:5 mvngu]:
> Replying to [comment:4 jason]:
> > I assume that you merged the tickets that define the functions listed here
> Yes, I have done so.

No, you haven't.  These functions are defined in #6679 and #6680, which haven't been reviewed, let alone merged.  This ticket should have been marked as "depends on #6679 and #6680": we can't have functions mentioned in the tutorial which are not yet part of Sage.  For now, the graph theory tour has been removed from the tutorial -- see #7149.

When the tickets #6679 and #6680 have been merged, then open up a new ticket to reinstate the graph theory tour (the corrected version, as of #6952).  Before running doctests, apply the script patches from #6572 to make sure that everything is getting tested -- the current doctesting system is broken, so many doctests in .rst files are inadvertently skipped.



---

archive/issue_comments_055781.json:
```json
{
    "body": "I would have prefered the fixing to be \"let's review these two patches now to have a good Graph Theory Tour\", but removing it for the moment is a good solution too..\nPerhaps Minh just meant that he had applied the corresponding patches to test the tutorial..\n\nThe thing is that patches #6679 and #6680 define for Sage some of the most important functions in Graph Theory ( Flows, matching, graph coloring, connectivity, etc .. )\n\nThe first version is two month old, and since then I have had to update them each time class MIP is modified. I do not even know myself how many things I have yet to write based on these functions.. What could we do about it ? If the code is not commented enough, if the only things you need are references, tell me and they'll be there in a few seconds :-)",
    "created_at": "2009-10-08T06:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55781",
    "user": "ncohen"
}
```

I would have prefered the fixing to be "let's review these two patches now to have a good Graph Theory Tour", but removing it for the moment is a good solution too..
Perhaps Minh just meant that he had applied the corresponding patches to test the tutorial..

The thing is that patches #6679 and #6680 define for Sage some of the most important functions in Graph Theory ( Flows, matching, graph coloring, connectivity, etc .. )

The first version is two month old, and since then I have had to update them each time class MIP is modified. I do not even know myself how many things I have yet to write based on these functions.. What could we do about it ? If the code is not commented enough, if the only things you need are references, tell me and they'll be there in a few seconds :-)



---

archive/issue_comments_055782.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-11-24T23:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55782",
    "user": "ncohen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_055783.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-11-24T23:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55783",
    "user": "ncohen"
}
```

Changing status from closed to new.



---

archive/issue_comments_055784.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-24T23:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55784",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055785.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-29T10:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55785",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055786.json:
```json
{
    "body": "I thought that we didn't want things in the tutorial that depended on optional packages.",
    "created_at": "2009-11-29T10:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55786",
    "user": "mhansen"
}
```

I thought that we didn't want things in the tutorial that depended on optional packages.



---

archive/issue_comments_055787.json:
```json
{
    "body": "Replying to [comment:11 mhansen]:\n> I thought that we didn't want things in the tutorial that depended on optional packages.\nThat is correct. Anything in the attached patches that uses optional packages should be removed. A new patch should be attached that still gives a tour of graph theory in Sage, but without using any optional packages.",
    "created_at": "2009-11-29T10:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55787",
    "user": "mvngu"
}
```

Replying to [comment:11 mhansen]:
> I thought that we didn't want things in the tutorial that depended on optional packages.
That is correct. Anything in the attached patches that uses optional packages should be removed. A new patch should be attached that still gives a tour of graph theory in Sage, but without using any optional packages.



---

archive/issue_comments_055788.json:
```json
{
    "body": "Is it just because it would be a legal problem for Sage to claim as \"available\" functions that we cannot provide without the addition of a software we are not allowed to embed ?\n\nIn this case I understand this decision, but you have to consider the fact that it is very likely 99% of Sage's graph theoretical functions will depend on Linear Programming by the time people REWRITE the functions I defined using Linear Programming through other means.\n\nI'll just try again to find a free LP solver or an old version of GLPK. And in the meantine I'll just update my personnal tutorial on Graphs (available pretty soon).. :-)",
    "created_at": "2009-11-29T10:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55788",
    "user": "ncohen"
}
```

Is it just because it would be a legal problem for Sage to claim as "available" functions that we cannot provide without the addition of a software we are not allowed to embed ?

In this case I understand this decision, but you have to consider the fact that it is very likely 99% of Sage's graph theoretical functions will depend on Linear Programming by the time people REWRITE the functions I defined using Linear Programming through other means.

I'll just try again to find a free LP solver or an old version of GLPK. And in the meantine I'll just update my personnal tutorial on Graphs (available pretty soon).. :-)



---

archive/issue_comments_055789.json:
```json
{
    "body": "Besides, this can be updated because of ticket #6813 which just got merged... We have much more that eastern europe in Sage now :-)",
    "created_at": "2009-11-29T10:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55789",
    "user": "ncohen"
}
```

Besides, this can be updated because of ticket #6813 which just got merged... We have much more that eastern europe in Sage now :-)



---

archive/issue_comments_055790.json:
```json
{
    "body": "Replying to [comment:13 ncohen]:\n> Is it just because it would be a legal problem for Sage to claim as \"available\" functions that we cannot provide without the addition of a software we are not allowed to embed ?\n\nIt's because everything in the tutorial should \"just work\".  You shouldn't have to install anything extra, it should work right out of the box.",
    "created_at": "2009-11-29T16:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55790",
    "user": "jhpalmieri"
}
```

Replying to [comment:13 ncohen]:
> Is it just because it would be a legal problem for Sage to claim as "available" functions that we cannot provide without the addition of a software we are not allowed to embed ?

It's because everything in the tutorial should "just work".  You shouldn't have to install anything extra, it should work right out of the box.



---

archive/issue_comments_055791.json:
```json
{
    "body": "Can we close this as \"won't fix\"?",
    "created_at": "2009-12-22T00:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55791",
    "user": "jhpalmieri"
}
```

Can we close this as "won't fix"?



---

archive/issue_comments_055792.json:
```json
{
    "body": "The graph theory tour as is cannot be added to the tutorial since it depends on an optional package. However, you can open a ticket to add that tour to the Constructions document.",
    "created_at": "2009-12-22T03:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55792",
    "user": "mvngu"
}
```

The graph theory tour as is cannot be added to the tutorial since it depends on an optional package. However, you can open a ticket to add that tour to the Constructions document.



---

archive/issue_comments_055793.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-12-22T03:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6774#issuecomment-55793",
    "user": "mvngu"
}
```

Resolution: wontfix
