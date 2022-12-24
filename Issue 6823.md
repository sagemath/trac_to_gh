# Issue 6823: [with patch, needs review] Kneser Graph in graph_generators

archive/issues_006823.json:
```json
{
    "body": "Assignee: @rlmill\n\nKneser graphs for graph_generators ( http://en.wikipedia.org/wiki/Kneser_graph )\n\nI just define the new function graphs.KneserGraph()\n\nIssue created by migration from https://trac.sagemath.org/ticket/6823\n\n",
    "created_at": "2009-08-25T08:20:10Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] Kneser Graph in graph_generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6823",
    "user": "@nathanncohen"
}
```
Assignee: @rlmill

Kneser graphs for graph_generators ( http://en.wikipedia.org/wiki/Kneser_graph )

I just define the new function graphs.KneserGraph()

Issue created by migration from https://trac.sagemath.org/ticket/6823





---

archive/issue_comments_056270.json:
```json
{
    "body": "Attachment [knesergraph.patch](tarball://root/attachments/some-uuid/ticket6823/knesergraph.patch) by @nathanncohen created at 2009-08-25 08:20:18",
    "created_at": "2009-08-25T08:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56270",
    "user": "@nathanncohen"
}
```

Attachment [knesergraph.patch](tarball://root/attachments/some-uuid/ticket6823/knesergraph.patch) by @nathanncohen created at 2009-08-25 08:20:18



---

archive/issue_comments_056271.json:
```json
{
    "body": "Changing keywords from \"\" to \"graph generators kneser\".",
    "created_at": "2009-09-21T02:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56271",
    "user": "@rbeezer"
}
```

Changing keywords from "" to "graph generators kneser".



---

archive/issue_comments_056272.json:
```json
{
    "body": "Hi Nathann,\n\nThis will be a nice addition to the graph generators.  Some suggestions:\n\n1.  How about giving the graph a name with the parameters in the string, like \"Kneser graph with parameters 5 and 2\"?\n\n2.  The patch just seems to be a diff file, so it really should be a Mercurial patch with your name/email and a one-line comment.  Patch files now seem to uniformly have filenames that begin with \"trac_xxxx_\" and you should put the trac number in the one-line summary of the Mercurial patch.\n\n3.  I'd really like to see more robust handling of the inputs (and doctests to see that they work).  For example, a negative n will bomb in the subset code.  How about checking that `n >= 0` and then that  `0 <= k <= n`?\n\n4.  English is very good, but I'd suggest \"adjacent\" or \"joined\" instead of \"linked\" and \"with parameters\" instead of \"of parameters\" (three places).\n\nWith this completed, it'll be easy to add the Odd graphs - just Kneser graphs with n=2k+1.\n\nThis passes all tests in sage/graphs and the documentation builds fine.\n\nRob",
    "created_at": "2009-09-21T02:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56272",
    "user": "@rbeezer"
}
```

Hi Nathann,

This will be a nice addition to the graph generators.  Some suggestions:

1.  How about giving the graph a name with the parameters in the string, like "Kneser graph with parameters 5 and 2"?

2.  The patch just seems to be a diff file, so it really should be a Mercurial patch with your name/email and a one-line comment.  Patch files now seem to uniformly have filenames that begin with "trac_xxxx_" and you should put the trac number in the one-line summary of the Mercurial patch.

3.  I'd really like to see more robust handling of the inputs (and doctests to see that they work).  For example, a negative n will bomb in the subset code.  How about checking that `n >= 0` and then that  `0 <= k <= n`?

4.  English is very good, but I'd suggest "adjacent" or "joined" instead of "linked" and "with parameters" instead of "of parameters" (three places).

With this completed, it'll be easy to add the Odd graphs - just Kneser graphs with n=2k+1.

This passes all tests in sage/graphs and the documentation builds fine.

Rob



---

archive/issue_comments_056273.json:
```json
{
    "body": "New patch. Odds graphs are added, and with some luck each one of your remarks will find an answer in this new version. Hope you'll like it ! :-)\n\nNathann",
    "created_at": "2009-09-26T09:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56273",
    "user": "@nathanncohen"
}
```

New patch. Odds graphs are added, and with some luck each one of your remarks will find an answer in this new version. Hope you'll like it ! :-)

Nathann



---

archive/issue_comments_056274.json:
```json
{
    "body": "Attachment [trac_6823.patch](tarball://root/attachments/some-uuid/ticket6823/trac_6823.patch) by @nathanncohen created at 2009-09-29 11:07:12",
    "created_at": "2009-09-29T11:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56274",
    "user": "@nathanncohen"
}
```

Attachment [trac_6823.patch](tarball://root/attachments/some-uuid/ticket6823/trac_6823.patch) by @nathanncohen created at 2009-09-29 11:07:12



---

archive/issue_comments_056275.json:
```json
{
    "body": "New patch taking into account the comments from #6828",
    "created_at": "2009-09-29T11:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56275",
    "user": "@nathanncohen"
}
```

New patch taking into account the comments from #6828



---

archive/issue_comments_056276.json:
```json
{
    "body": "Attachment [trac_6823_reviewer.patch](tarball://root/attachments/some-uuid/ticket6823/trac_6823_reviewer.patch) by @rbeezer created at 2009-09-30 05:34:21\n\nReviewer patch to set odd graph name",
    "created_at": "2009-09-30T05:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56276",
    "user": "@rbeezer"
}
```

Attachment [trac_6823_reviewer.patch](tarball://root/attachments/some-uuid/ticket6823/trac_6823_reviewer.patch) by @rbeezer created at 2009-09-30 05:34:21

Reviewer patch to set odd graph name



---

archive/issue_comments_056277.json:
```json
{
    "body": "Nathann,\n\nLooks very good, builds on 4.1.2.alpha2, passes all tests, etc.\n\nRight now the name of an odd graph reports the Kneser graph parameters, etc.  I'd expect this to confuse someone who builds an odd graph, yet does not know the connection to the Kneser graphs.  I've attached a small patch that just sets the name on the odd graph routine.  If you agree with the change, then you can mark the ticket as positive review.  In other words, you can review my additional patch, and we'll be done.\n\nThanks,\nRob",
    "created_at": "2009-09-30T05:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56277",
    "user": "@rbeezer"
}
```

Nathann,

Looks very good, builds on 4.1.2.alpha2, passes all tests, etc.

Right now the name of an odd graph reports the Kneser graph parameters, etc.  I'd expect this to confuse someone who builds an odd graph, yet does not know the connection to the Kneser graphs.  I've attached a small patch that just sets the name on the odd graph routine.  If you agree with the change, then you can mark the ticket as positive review.  In other words, you can review my additional patch, and we'll be done.

Thanks,
Rob



---

archive/issue_comments_056278.json:
```json
{
    "body": "Good thinking ! ;-)\n\nNathann",
    "created_at": "2009-09-30T07:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56278",
    "user": "@nathanncohen"
}
```

Good thinking ! ;-)

Nathann



---

archive/issue_comments_056279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T16:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6823#issuecomment-56279",
    "user": "@mwhansen"
}
```

Resolution: fixed
