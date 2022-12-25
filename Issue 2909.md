# Issue 2909: notebook -- implement a way of parsing script tags in output as they appear (but none that already appeared)

archive/issues_002909.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777\n\nThe canonical example to get to work is the following (submitted by Jason Grout):\n\n\n```\nfor i in range(5):\n    print html('<script>alert(%s)</script>'%i)\n    sleep(1)\n```\n\n\nwould pop up a dialog box about every second.\n\n\nThis feature was requested by `gerhard <ge01705`@`yahoo.de>`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2909\n\n",
    "created_at": "2008-04-13T18:04:03Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "notebook -- implement a way of parsing script tags in output as they appear (but none that already appeared)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2909",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @qed777

The canonical example to get to work is the following (submitted by Jason Grout):


```
for i in range(5):
    print html('<script>alert(%s)</script>'%i)
    sleep(1)
```


would pop up a dialog box about every second.


This feature was requested by `gerhard <ge01705`@`yahoo.de>`.

Issue created by migration from https://trac.sagemath.org/ticket/2909





---

archive/issue_comments_020003.json:
```json
{
    "body": "I don't know the details of the notebook source code, but one possible way to run javascript code out of javascript is writing it dynamically into the source, because it get's evaluated. The hack: unescape escaped characters!\n\n\n```\n<html>\n<head>\n<script type=\"text/javascript\">\nfunction run() {\n   eval(cmd);\n}\n</script>\n</head>\n<body>\n\n<script type=\"text/javascript\">\ncmd = 'alert(\"I am an alert\")';\n</script>\n\n<script type=\"text/javascript\">\ndocument.write(unescape(\"%3Cscript type='text/javascript'%3E\" + \"run('\" + cmd + \"');\" + \"%3C/script%3E\"));\n</script>\n\n</body>\n</html>\n```\n\n\nthe generated source code, after running everything, relevant part:\n\n\n```\n<script type=\"text/javascript\">\ndocument.write(unescape(\"%3Cscript type='text/javascript'%3E\" + \"run('\" + cmd + \"');\" + \"%3C/script%3E\"));\n</script><script type=\"text/javascript\">run('alert(\"I am an alert\")');</script>\n```\n",
    "created_at": "2008-04-14T08:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2909#issuecomment-20003",
    "user": "https://github.com/haraldschilly"
}
```

I don't know the details of the notebook source code, but one possible way to run javascript code out of javascript is writing it dynamically into the source, because it get's evaluated. The hack: unescape escaped characters!


```
<html>
<head>
<script type="text/javascript">
function run() {
   eval(cmd);
}
</script>
</head>
<body>

<script type="text/javascript">
cmd = 'alert("I am an alert")';
</script>

<script type="text/javascript">
document.write(unescape("%3Cscript type='text/javascript'%3E" + "run('" + cmd + "');" + "%3C/script%3E"));
</script>

</body>
</html>
```


the generated source code, after running everything, relevant part:


```
<script type="text/javascript">
document.write(unescape("%3Cscript type='text/javascript'%3E" + "run('" + cmd + "');" + "%3C/script%3E"));
</script><script type="text/javascript">run('alert("I am an alert")');</script>
```




---

archive/issue_comments_020004.json:
```json
{
    "body": "ok, i'm confused, maybe my last comment is helpful for something else - just tested the cannonical exmaple, and it works for me.",
    "created_at": "2008-04-14T09:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2909#issuecomment-20004",
    "user": "https://github.com/haraldschilly"
}
```

ok, i'm confused, maybe my last comment is helpful for something else - just tested the cannonical exmaple, and it works for me.



---

archive/issue_comments_020005.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-17T00:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2909#issuecomment-20005",
    "user": "https://github.com/TimDumol"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020006.json:
```json
{
    "body": "> ok, i'm confused, maybe my last comment is helpful for something else - just tested the cannonical exmaple, and it works for me.\n\nAh, but *does* it?  For me, it first prints out the (empty) lines every second, and only then all the alerts come up (in order) at once.",
    "created_at": "2014-09-18T02:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2909#issuecomment-20006",
    "user": "https://github.com/kcrisman"
}
```

> ok, i'm confused, maybe my last comment is helpful for something else - just tested the cannonical exmaple, and it works for me.

Ah, but *does* it?  For me, it first prints out the (empty) lines every second, and only then all the alerts come up (in order) at once.



---

archive/issue_events_003111.json:
```json
{
    "actor": "boothby",
    "created_at": "2020-03-29T02:03:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2909#event-3111"
}
```



---

archive/issue_comments_020007.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2909#issuecomment-20007",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_020008.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2909#issuecomment-20008",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid
