# Issue 8033: add a README.txt for the graph_editor, to encourage development

archive/issues_008033.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  rkirov\n\n\n```\nHi,\n\nThe new graph editor in sage by Rado is AWESOME.  One can try it\neasily at http://sagenb.org by typing:\n\n g = graphs.CompleteGraph(10)\n graph_editor(g)\n\nThe actual source code is at\n\n  local/lib/python/site-packages/sagenb-0.6-py2.6.egg/sagenb/data/graph_editor/\n\nIt would be *GREAT* if there were a README.txt file in that directory\nthat explained what all the js files actually are, something about how\nthe graph editor works, where the code that does spring layout\ndynamically is located, etc.   I looked at the code for five minutes\nand couldn't deduce answers to any of those questions.\n\nSo, could somebody familiar with the graph editor write something and\npost a patch.  Or just respond to this email with what would go in a\nREADME.txt?   I have two undergrads who might want to work on that\ncode, but it would help a lot of there were some docs.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8033\n\n",
    "created_at": "2010-01-21T22:54:04Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "add a README.txt for the graph_editor, to encourage development",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8033",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  rkirov


```
Hi,

The new graph editor in sage by Rado is AWESOME.  One can try it
easily at http://sagenb.org by typing:

 g = graphs.CompleteGraph(10)
 graph_editor(g)

The actual source code is at

  local/lib/python/site-packages/sagenb-0.6-py2.6.egg/sagenb/data/graph_editor/

It would be *GREAT* if there were a README.txt file in that directory
that explained what all the js files actually are, something about how
the graph editor works, where the code that does spring layout
dynamically is located, etc.   I looked at the code for five minutes
and couldn't deduce answers to any of those questions.

So, could somebody familiar with the graph editor write something and
post a patch.  Or just respond to this email with what would go in a
README.txt?   I have two undergrads who might want to work on that
code, but it would help a lot of there were some docs.

```


Issue created by migration from https://trac.sagemath.org/ticket/8033





---

archive/issue_comments_070046.json:
```json
{
    "body": "And here is the content (from Mitesh Patel):\n\n```\nThe main files are\n\n       a. sage/graphs/graph_editor.py\n       b. graph_editor.html\n       c. graph_editor.js\n       d. processing.editor.min.js\n\nEvaluating graph_editor(G) (see (a)) in an input cell generates\ncode/markup for an inline frame, which the notebook inserts into the\ncorresponding output cell.  The iframe loads (b) as its content.  In\nturn, (b) draws in jQuery / UI, the layout algorithms in (c), and the\nHTML5 canvas rendering engine in (d).\n\nAccording to\n\n       http://trac.sagemath.org/sage_trac/ticket/1321#comment:31\n\nRado adapted (d) from a project called Processing.js\n\nhttp://processingjs.org/\nhttp://processingjs.org/reference\nhttp://processingjs.org/download\n\nwhose original and minified source files are\n\n       e. processing.js\n       f. processing.min.js\n\nTo make it somewhat easier to understand the differences between (f) and\n(d), I put (d) through a JS \"beautifier\"\n\n       http://jsbeautifier.org/\n\nThe result is\n\n       g. processing.editor.js\n\nBut I decided not to give the same treatment to (e) and attempt to make\na concise diff.\n```\n",
    "created_at": "2010-01-21T22:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70046",
    "user": "https://github.com/williamstein"
}
```

And here is the content (from Mitesh Patel):

```
The main files are

       a. sage/graphs/graph_editor.py
       b. graph_editor.html
       c. graph_editor.js
       d. processing.editor.min.js

Evaluating graph_editor(G) (see (a)) in an input cell generates
code/markup for an inline frame, which the notebook inserts into the
corresponding output cell.  The iframe loads (b) as its content.  In
turn, (b) draws in jQuery / UI, the layout algorithms in (c), and the
HTML5 canvas rendering engine in (d).

According to

       http://trac.sagemath.org/sage_trac/ticket/1321#comment:31

Rado adapted (d) from a project called Processing.js

http://processingjs.org/
http://processingjs.org/reference
http://processingjs.org/download

whose original and minified source files are

       e. processing.js
       f. processing.min.js

To make it somewhat easier to understand the differences between (f) and
(d), I put (d) through a JS "beautifier"

       http://jsbeautifier.org/

The result is

       g. processing.editor.js

But I decided not to give the same treatment to (e) and attempt to make
a concise diff.
```




---

archive/issue_comments_070047.json:
```json
{
    "body": "contains README.TXT",
    "created_at": "2010-01-22T08:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70047",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

contains README.TXT



---

archive/issue_comments_070048.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-22T08:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70048",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070049.json:
```json
{
    "body": "Attachment [8033.patch](tarball://root/attachments/some-uuid/ticket8033/8033.patch) by rkirov created at 2010-01-22 08:01:05\n\nAdded a small file README.txt that has a summary of how the graph_editor works. Comments are welcome.",
    "created_at": "2010-01-22T08:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70049",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Attachment [8033.patch](tarball://root/attachments/some-uuid/ticket8033/8033.patch) by rkirov created at 2010-01-22 08:01:05

Added a small file README.txt that has a summary of how the graph_editor works. Comments are welcome.



---

archive/issue_comments_070050.json:
```json
{
    "body": "Various changes.  Replaces previous.  sagenb repo.",
    "created_at": "2010-01-24T21:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70050",
    "user": "https://github.com/qed777"
}
```

Various changes.  Replaces previous.  sagenb repo.



---

archive/issue_comments_070051.json:
```json
{
    "body": "Attachment [trac_8033-graph_editor_readme.patch](tarball://root/attachments/some-uuid/ticket8033/trac_8033-graph_editor_readme.patch) by @qed777 created at 2010-01-24 21:55:26\n\nI've attached an update with some changes.  Feel free to make further changes!",
    "created_at": "2010-01-24T21:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70051",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8033-graph_editor_readme.patch](tarball://root/attachments/some-uuid/ticket8033/trac_8033-graph_editor_readme.patch) by @qed777 created at 2010-01-24 21:55:26

I've attached an update with some changes.  Feel free to make further changes!



---

archive/issue_comments_070052.json:
```json
{
    "body": "Just a quick thought: Using `$(window).load(...` instead of `$(document).ready(...` in `graph_editor.js` might resolve the \"mouse_out\" problem mentioned at the bottom of `graph_editor.py`.",
    "created_at": "2010-01-24T22:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70052",
    "user": "https://github.com/qed777"
}
```

Just a quick thought: Using `$(window).load(...` instead of `$(document).ready(...` in `graph_editor.js` might resolve the "mouse_out" problem mentioned at the bottom of `graph_editor.py`.



---

archive/issue_comments_070053.json:
```json
{
    "body": "Hi Rado -- If this looks good to you, we can change the status to \"positive review.\"",
    "created_at": "2010-02-05T01:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70053",
    "user": "https://github.com/qed777"
}
```

Hi Rado -- If this looks good to you, we can change the status to "positive review."



---

archive/issue_comments_070054.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T04:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70054",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070055.json:
```json
{
    "body": "definitively, its ready to be merged.",
    "created_at": "2010-02-07T04:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70055",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

definitively, its ready to be merged.



---

archive/issue_comments_070056.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T18:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8033#issuecomment-70056",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019250.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-10T18:32:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8033",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8033#event-19250"
}
```
