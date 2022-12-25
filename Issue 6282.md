# Issue 6282: document SAGE_CHECK

archive/issues_006282.json:
```json
{
    "body": "Assignee: tbd\n\nAdd the following to the SAGE_ROOT/README.txt, since right now the SAGE_CHECK flag is totally undocumented:\n\n\n```\nIf you want to run the test suite for each individual spkg as it is installed, do\n\n   export SAGE_CHECK=\"yes\"\n\nbefore starting the Sage build.  This will run each test suite, and will raise an error if any failures occur. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6282\n\n",
    "created_at": "2009-06-14T09:34:44Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "document SAGE_CHECK",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6282",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Add the following to the SAGE_ROOT/README.txt, since right now the SAGE_CHECK flag is totally undocumented:


```
If you want to run the test suite for each individual spkg as it is installed, do

   export SAGE_CHECK="yes"

before starting the Sage build.  This will run each test suite, and will raise an error if any failures occur. 
```


Issue created by migration from https://trac.sagemath.org/ticket/6282





---

archive/issue_comments_050062.json:
```json
{
    "body": "The \"patch\" is just the text in the description, which must be manually added to the README.txt by the release manager who closes this ticket.  Refereeing this means reading the text and making sure there are no typos and that it is not stupid.",
    "created_at": "2009-06-14T09:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6282#issuecomment-50062",
    "user": "https://github.com/williamstein"
}
```

The "patch" is just the text in the description, which must be manually added to the README.txt by the release manager who closes this ticket.  Refereeing this means reading the text and making sure there are no typos and that it is not stupid.



---

archive/issue_comments_050063.json:
```json
{
    "body": "By the way, in this part:\n\n```\nIf you have a machine with n processors, say, type  \n             export MAKE=\"make -j4\"\n```\n\nshould \"n\" be changed to \"4\"?",
    "created_at": "2009-06-14T15:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6282#issuecomment-50063",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, in this part:

```
If you have a machine with n processors, say, type  
             export MAKE="make -j4"
```

should "n" be changed to "4"?



---

archive/issue_comments_050064.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6282#issuecomment-50064",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_050065.json:
```json
{
    "body": "Done by ncalexan for 4.0.2.alpha0.",
    "created_at": "2009-06-14T22:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6282#issuecomment-50065",
    "user": "https://github.com/ncalexan"
}
```

Done by ncalexan for 4.0.2.alpha0.



---

archive/issue_events_006526.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-14T22:18:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6282",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6282#event-6526"
}
```
