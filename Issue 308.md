# Issue 308: log_html() crashes because of an undefined variable

archive/issues_000308.json:
```json
{
    "body": "Assignee: @williamstein\n\n`log_html` crashes because of an undefined variable:\n\n\n```\nsage: log_html ()\n[..]\n   245         T = self._title()\n   246         inlog = os.path.split(self._input_log_name())[1]\n--> 247         return '<html>%s<title>%s</title>\\n<body><h1\nalign=center>%s</h1>\\n<h2 align=center><a\nhref=\"%s\">%s</a></h2><pre>'%(REFRESH,T,T, inlog, inlog)   \n<type 'exceptions.NameError'>: global name 'REFRESH' is not defined\n```\n\n\nI'm not sure what the variable `REFRESH` is referring to, but removing\nit takes care of the problem. A patch is available here:\nhttp://sage.math.washington.edu/home/dfdeshom/custom/patches/log.py.hg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/308\n\n",
    "created_at": "2007-03-04T06:39:51Z",
    "labels": [
        "component: user interface",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "log_html() crashes because of an undefined variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/308",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein

`log_html` crashes because of an undefined variable:


```
sage: log_html ()
[..]
   245         T = self._title()
   246         inlog = os.path.split(self._input_log_name())[1]
--> 247         return '<html>%s<title>%s</title>\n<body><h1
align=center>%s</h1>\n<h2 align=center><a
href="%s">%s</a></h2><pre>'%(REFRESH,T,T, inlog, inlog)   
<type 'exceptions.NameError'>: global name 'REFRESH' is not defined
```


I'm not sure what the variable `REFRESH` is referring to, but removing
it takes care of the problem. A patch is available here:
http://sage.math.washington.edu/home/dfdeshom/custom/patches/log.py.hg


Issue created by migration from https://trac.sagemath.org/ticket/308





---

archive/issue_comments_001459.json:
```json
{
    "body": "Mmmh, I get the following:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.2, Release Date: 2007-08-22                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: log_html ()\nHTML Logger\nsage: 1+1\n2\n```\n\nCan this be closed now? \n\nCheers,\n\nMichael",
    "created_at": "2007-08-24T23:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/308#issuecomment-1459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mmmh, I get the following:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: log_html ()
HTML Logger
sage: 1+1
2
```

Can this be closed now? 

Cheers,

Michael



---

archive/issue_comments_001460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T23:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/308#issuecomment-1460",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
