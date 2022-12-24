# Issue 3155: notebook postdata and behaviour of archive, delete and stop buttons

archive/issues_003155.json:
```json
{
    "body": "Assignee: boothby\n\nWhen I have just logged in to sage, the URL one is connected to is\n\"https://<sage server>/login\" and the relevant page apparently has post-data on it.\n\nIf I click one of the \"archive\", \"delete\" or \"stop\" buttons, apparently a reload of the page is triggered. The result is that firefox gives me a warning \"The page you are trying to reload contains POSTDATA ...\".\n\nIf I change the URL to \"https://<sage server>\" in the same browser I remain authenticated and everything still works. Now the page does not have POSTDATA on it and the reload is not a problem.\n\nPossible fixes:\n\n- Make sure that the POSTDATA is dumped as quickly as possible, so that reloading does not trigger warnings\n- reprogram the actions of the buttons so that they don't trigger a reload (for instance, force them to do a load of a new page instead)\n- something I cannot think of.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3155\n\n",
    "created_at": "2008-05-11T04:03:00Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook postdata and behaviour of archive, delete and stop buttons",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3155",
    "user": "nbruin"
}
```
Assignee: boothby

When I have just logged in to sage, the URL one is connected to is
"https://<sage server>/login" and the relevant page apparently has post-data on it.

If I click one of the "archive", "delete" or "stop" buttons, apparently a reload of the page is triggered. The result is that firefox gives me a warning "The page you are trying to reload contains POSTDATA ...".

If I change the URL to "https://<sage server>" in the same browser I remain authenticated and everything still works. Now the page does not have POSTDATA on it and the reload is not a problem.

Possible fixes:

- Make sure that the POSTDATA is dumped as quickly as possible, so that reloading does not trigger warnings
- reprogram the actions of the buttons so that they don't trigger a reload (for instance, force them to do a load of a new page instead)
- something I cannot think of.

Issue created by migration from https://trac.sagemath.org/ticket/3155





---

archive/issue_comments_021890.json:
```json
{
    "body": "Knoboo deals with this problem by redirecting the user to the bookshelf. See http://trac.knoboo.com/browser/trunk/knoboo/knoboo/resources/user.py\n\n\n```\ndef render(self, request):\n    response = http.RedirectResponse(\"/bookshelf\")\n    response.headers.setHeader(\"set-cookie\", [http_headers.Cookie(\"sid\", self.cookie)])\n    return response\n```\n",
    "created_at": "2008-05-11T13:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21890",
    "user": "TimothyClemans"
}
```

Knoboo deals with this problem by redirecting the user to the bookshelf. See http://trac.knoboo.com/browser/trunk/knoboo/knoboo/resources/user.py


```
def render(self, request):
    response = http.RedirectResponse("/bookshelf")
    response.headers.setHeader("set-cookie", [http_headers.Cookie("sid", self.cookie)])
    return response
```




---

archive/issue_comments_021891.json:
```json
{
    "body": "Fixed in #3050.",
    "created_at": "2008-05-17T15:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21891",
    "user": "TimothyClemans"
}
```

Fixed in #3050.



---

archive/issue_comments_021892.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T20:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21892",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021893.json:
```json
{
    "body": "Fixed in Sage 3.0.2.alpha1 by merging the patches at #3050.",
    "created_at": "2008-05-17T20:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21893",
    "user": "mabshoff"
}
```

Fixed in Sage 3.0.2.alpha1 by merging the patches at #3050.



---

archive/issue_comments_021894.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-18T16:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21894",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_021895.json:
```json
{
    "body": "Since #3050 got reverted I am reopening this ticket, too.",
    "created_at": "2008-05-18T16:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21895",
    "user": "mabshoff"
}
```

Since #3050 got reverted I am reopening this ticket, too.



---

archive/issue_comments_021896.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-18T16:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21896",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_021897.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-19T06:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21897",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021898.json:
```json
{
    "body": "Fixed in Sage 3.0.2.alpha1 by merging the new patches at #3050. ;)",
    "created_at": "2008-05-19T06:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3155#issuecomment-21898",
    "user": "mabshoff"
}
```

Fixed in Sage 3.0.2.alpha1 by merging the new patches at #3050. ;)
