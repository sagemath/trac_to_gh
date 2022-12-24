# Issue 3147: "Quit Worksheet" in notebook doesn't seem to work anymore

archive/issues_003147.json:
```json
{
    "body": "Assignee: anybody\n\nAction: Click on \"Quit worksheet\" when you have a worksheet open\n\nExpected result:\n* Sage process behind worksheet exits/gets killed (happed prior to 3.0)\n* Browser goes back to worksheet list (this would be an enhancement over previous behaviour)\n\nActual result:\n* drop down list keeps \"quit worksheet\" selection and no other result\n* if you return to worksheet list manually, the worksheet is still listed as \"(active)\"\n\nReproducible:\n* every time for me: vanilla RHEL Server 5.1 box (amd64) running sage notebook as \"nobody\".\nConnection made with Firefox 2.0.0.14 from a Fedora 7 machine.\n\nProblem:\n* machine fills up with sage processes. Restarting the sage server solves the problem, obviously, but is a bit draconian.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3147\n\n",
    "created_at": "2008-05-09T22:32:49Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "\"Quit Worksheet\" in notebook doesn't seem to work anymore",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3147",
    "user": "nbruin"
}
```
Assignee: anybody

Action: Click on "Quit worksheet" when you have a worksheet open

Expected result:
* Sage process behind worksheet exits/gets killed (happed prior to 3.0)
* Browser goes back to worksheet list (this would be an enhancement over previous behaviour)

Actual result:
* drop down list keeps "quit worksheet" selection and no other result
* if you return to worksheet list manually, the worksheet is still listed as "(active)"

Reproducible:
* every time for me: vanilla RHEL Server 5.1 box (amd64) running sage notebook as "nobody".
Connection made with Firefox 2.0.0.14 from a Fedora 7 machine.

Problem:
* machine fills up with sage processes. Restarting the sage server solves the problem, obviously, but is a bit draconian.

Issue created by migration from https://trac.sagemath.org/ticket/3147





---

archive/issue_comments_021834.json:
```json
{
    "body": "Note:  the \"save & quit\" and \"discard & quit\" buttons work for me, while using the pulldown does not.",
    "created_at": "2008-05-10T17:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3147#issuecomment-21834",
    "user": "boothby"
}
```

Note:  the "save & quit" and "discard & quit" buttons work for me, while using the pulldown does not.



---

archive/issue_comments_021835.json:
```json
{
    "body": "The patch for #1230 resolves the issue for me, so once that ticket is closed, I would not mind if this one gets closed too.",
    "created_at": "2008-05-10T23:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3147#issuecomment-21835",
    "user": "nbruin"
}
```

The patch for #1230 resolves the issue for me, so once that ticket is closed, I would not mind if this one gets closed too.



---

archive/issue_comments_021836.json:
```json
{
    "body": "I agree with Nils, this is a dup of #1230.",
    "created_at": "2008-05-10T23:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3147#issuecomment-21836",
    "user": "was"
}
```

I agree with Nils, this is a dup of #1230.



---

archive/issue_comments_021837.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-05-10T23:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3147#issuecomment-21837",
    "user": "was"
}
```

Resolution: duplicate
