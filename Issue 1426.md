# Issue 1426: new trac view: tickets ***reported by*** given user

archive/issues_001426.json:
```json
{
    "body": "Assignee: was\n\nI don't know if this is possible, but I wish the possibility to view all tickets \nreported by a user logged in trac (either only active tickets, or active tickets first).\nThis would enable me to see progress made on those tickets.\n\nCurrently it is possible to view ***my tickets***, i.e., tickets ***assigned to me***,\nwhich is quite different :-)\n\nPS: I'm not sure the component \"website/wiki\" is the right one. Maybe one needs a new component\n\"trac\"?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1426\n\n",
    "created_at": "2007-12-08T10:44:15Z",
    "labels": [
        "website/wiki",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "new trac view: tickets ***reported by*** given user",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1426",
    "user": "zimmerma"
}
```
Assignee: was

I don't know if this is possible, but I wish the possibility to view all tickets 
reported by a user logged in trac (either only active tickets, or active tickets first).
This would enable me to see progress made on those tickets.

Currently it is possible to view ***my tickets***, i.e., tickets ***assigned to me***,
which is quite different :-)

PS: I'm not sure the component "website/wiki" is the right one. Maybe one needs a new component
"trac"?

Issue created by migration from https://trac.sagemath.org/ticket/1426





---

archive/issue_comments_009195.json:
```json
{
    "body": "Hey Paul,\n\nhow about `http://sagetrac.org/sage_trac/report/7`? Or do you wish to query for a user that isn't you also?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T02:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1426#issuecomment-9195",
    "user": "mabshoff"
}
```

Hey Paul,

how about `http://sagetrac.org/sage_trac/report/7`? Or do you wish to query for a user that isn't you also?

Cheers,

Michael



---

archive/issue_comments_009196.json:
```json
{
    "body": "Hi Michael,\n\nhttp://sagetrac.org/sage_trac/report/7 does not do what I want. If I click on it, I get no ticket,\nwhich is normal since no ticket was ***assigned*** to me.\n\nWhat I'd like to have is a list of ticket I've ***reported***.\n\nPaul",
    "created_at": "2007-12-09T21:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1426#issuecomment-9196",
    "user": "zimmerma"
}
```

Hi Michael,

http://sagetrac.org/sage_trac/report/7 does not do what I want. If I click on it, I get no ticket,
which is normal since no ticket was ***assigned*** to me.

What I'd like to have is a list of ticket I've ***reported***.

Paul



---

archive/issue_comments_009197.json:
```json
{
    "body": "Hi Paul,\n\nJust to try this out, I went to http://sagetrac.org/sage_trac/report/7 and noticed the link \"Custom Query\" toward the top right, underneath the main trac bar.\n\nBy default, it has only one field for searching, namely \"Owner is\".  But under that, to the right, there's an option \"Add filter\", and one of the possibilities is \"Reporter\".  You need to get rid of the \"Owner is\" field by clicking the minus sign at the right, and you're set to search for tickets reported by a certain person.\n\nSo good news: it can be done in trac.  Bad news: it's a pain to go through all that every time.  Maybe it's possible to have a short cut for this?\n\nAlex",
    "created_at": "2007-12-10T14:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1426#issuecomment-9197",
    "user": "AlexGhitza"
}
```

Hi Paul,

Just to try this out, I went to http://sagetrac.org/sage_trac/report/7 and noticed the link "Custom Query" toward the top right, underneath the main trac bar.

By default, it has only one field for searching, namely "Owner is".  But under that, to the right, there's an option "Add filter", and one of the possibilities is "Reporter".  You need to get rid of the "Owner is" field by clicking the minus sign at the right, and you're set to search for tickets reported by a certain person.

So good news: it can be done in trac.  Bad news: it's a pain to go through all that every time.  Maybe it's possible to have a short cut for this?

Alex



---

archive/issue_comments_009198.json:
```json
{
    "body": "Sorry, me again.\n\nIt should be almost trivial for someone who has privileges to do this, to copy the \"My Tickets\" report and replace \"Owned by\" by \"Reported by\".  We could then have something like \"Tickets I own\" and \"Tickets I reported\" as two reports easily accessible.\n\nAs far as I can tell, though, one needs administrator privileges in order to mess around with the reports.\n\nAlex",
    "created_at": "2007-12-10T14:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1426#issuecomment-9198",
    "user": "AlexGhitza"
}
```

Sorry, me again.

It should be almost trivial for someone who has privileges to do this, to copy the "My Tickets" report and replace "Owned by" by "Reported by".  We could then have something like "Tickets I own" and "Tickets I reported" as two reports easily accessible.

As far as I can tell, though, one needs administrator privileges in order to mess around with the reports.

Alex



---

archive/issue_comments_009199.json:
```json
{
    "body": "hmm ok I think I've done this now, it's report number 9, I'll see if people like it",
    "created_at": "2007-12-21T01:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1426#issuecomment-9199",
    "user": "dmharvey"
}
```

hmm ok I think I've done this now, it's report number 9, I'll see if people like it



---

archive/issue_comments_009200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-21T02:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1426#issuecomment-9200",
    "user": "rlm"
}
```

Resolution: fixed
