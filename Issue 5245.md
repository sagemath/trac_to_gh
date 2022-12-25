# Issue 5245: treat truncated HTML intelligently

archive/issues_005245.json:
```json
{
    "body": "Assignee: boothby\n\nfrom the [notebook \"report problem\" bugtracker](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1234452850833000&pt=1234452830833000&diffWidget=true&s=AJVazbVHq6MFP1rt4M9kABykB37gF_Uy_g)\n\nToo long HTML outputs are truncated in the notebook. A silly example:\n\n\n```\nhtml('<table>'+'<tr>'+\n'\\n'.join(('<td>'+'</td><td>'.join(\n'<font color=\"#0000ff\" style=\"background-color: #dddddd;\">%s</font>'\n% (row*column)\nfor column in range(1, 25))+'</td>')+'</tr>'\nfor row in range(1, 20))+'</table>')\n```\n\n\nThis produces \"WARNING: Output truncated! full_output.txt\" and the displayed HTML is somewhat garbled (truncation doesn't work so well for HTML, obviously). Wrapping the expression around show() changes nothing.\n\nExpected:\n\nProgram-generated HTML is a quite nice way to visualize some things quickly: The output may be long though (especially for quick & dirty scripts), even when the actually displayed content does not take much space on screen. Sage shouldn't be so quick to truncate HTML, and even if it does truncate sometimes (I'm not sure if it should), **the output should be a .html file, not .txt, so that the browser displays it correctly by default**.\n\n---\n\nNote by me: changing the ending isn't everything, also the mime-content type has to change. maybe it should not be a txt output in the first place and everything html as a default...\n\nIssue created by migration from https://trac.sagemath.org/ticket/5245\n\n",
    "created_at": "2009-02-12T15:49:47Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "treat truncated HTML intelligently",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5245",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: boothby

from the [notebook "report problem" bugtracker](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1234452850833000&pt=1234452830833000&diffWidget=true&s=AJVazbVHq6MFP1rt4M9kABykB37gF_Uy_g)

Too long HTML outputs are truncated in the notebook. A silly example:


```
html('<table>'+'<tr>'+
'\n'.join(('<td>'+'</td><td>'.join(
'<font color="#0000ff" style="background-color: #dddddd;">%s</font>'
% (row*column)
for column in range(1, 25))+'</td>')+'</tr>'
for row in range(1, 20))+'</table>')
```


This produces "WARNING: Output truncated! full_output.txt" and the displayed HTML is somewhat garbled (truncation doesn't work so well for HTML, obviously). Wrapping the expression around show() changes nothing.

Expected:

Program-generated HTML is a quite nice way to visualize some things quickly: The output may be long though (especially for quick & dirty scripts), even when the actually displayed content does not take much space on screen. Sage shouldn't be so quick to truncate HTML, and even if it does truncate sometimes (I'm not sure if it should), **the output should be a .html file, not .txt, so that the browser displays it correctly by default**.

---

Note by me: changing the ending isn't everything, also the mime-content type has to change. maybe it should not be a txt output in the first place and everything html as a default...

Issue created by migration from https://trac.sagemath.org/ticket/5245





---

archive/issue_comments_040134.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-17T10:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5245#issuecomment-40134",
    "user": "https://github.com/TimDumol"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_040135.json:
```json
{
    "body": "Just to add one datapoint: a student of mine got the following in the Sage 6.3 notebook:\n\n```\n    sage: solve?\n    ... output truncated ...\n```\n\n\nand due to the above the full output was displayed as text and thus rather unreadable.\n\nI was not able to reproduce this truncation happening, even in his own session a bit later.",
    "created_at": "2014-09-24T09:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5245#issuecomment-40135",
    "user": "https://github.com/nthiery"
}
```

Just to add one datapoint: a student of mine got the following in the Sage 6.3 notebook:

```
    sage: solve?
    ... output truncated ...
```


and due to the above the full output was displayed as text and thus rather unreadable.

I was not able to reproduce this truncation happening, even in his own session a bit later.



---

archive/issue_comments_040136.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5245#issuecomment-40136",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_040137.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5245#issuecomment-40137",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid
