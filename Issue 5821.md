# Issue 5821: preparser incorrectly handles backslash operator inside strings (sometimes)

archive/issues_005821.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nKeywords: preparser\n\nWhen reviewing #5595, I tried typing this:\n\n```\nsage: import re\nsage: dep_regex = re.compile(r'^ *(?:(?:cimport +([\\w\\. ,]+))|(?:from +(\\w+) +cimport)|(?:include *[\\'\"]([^\\'\"]+)[\\'\"])|(?:cdef *extern *from *[\\'\"]([^\\'\"]+)[\\'\"]))', re.M)\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     dep_regex = re.compile(r'^ *(?:(?:cimport +([\\w\\. ,]+))|(?:from +(\\w+) +cimport)|(?:include *[\\'\"]([^\\'\"]+)[ * BackslashOperator() * '\"])|(?:cdef *extern *from *[\\'\"]([^\\'\"]+)[\\'\"]))', re.M)\n                                                                                                                                                                          ^\nSyntaxError: invalid syntax\n```\n\n\nNote that the preparser has turned a backslash from the middle of the regular expression into `\" * BackslashOperator() * \"`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5821\n\n",
    "created_at": "2009-04-19T03:31:24Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "preparser incorrectly handles backslash operator inside strings (sometimes)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5821",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

CC:  @robertwb

Keywords: preparser

When reviewing #5595, I tried typing this:

```
sage: import re
sage: dep_regex = re.compile(r'^ *(?:(?:cimport +([\w\. ,]+))|(?:from +(\w+) +cimport)|(?:include *[\'"]([^\'"]+)[\'"])|(?:cdef *extern *from *[\'"]([^\'"]+)[\'"]))', re.M)
------------------------------------------------------------
   File "<ipython console>", line 1
     dep_regex = re.compile(r'^ *(?:(?:cimport +([\w\. ,]+))|(?:from +(\w+) +cimport)|(?:include *[\'"]([^\'"]+)[ * BackslashOperator() * '"])|(?:cdef *extern *from *[\'"]([^\'"]+)[\'"]))', re.M)
                                                                                                                                                                          ^
SyntaxError: invalid syntax
```


Note that the preparser has turned a backslash from the middle of the regular expression into `" * BackslashOperator() * "`.

Issue created by migration from https://trac.sagemath.org/ticket/5821





---

archive/issue_comments_045659.json:
```json
{
    "body": "It appears that even in raw strings the backslash escapes a potential end quote...\n\nhttp://docs.python.org/reference/lexical_analysis.html",
    "created_at": "2009-04-19T07:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5821#issuecomment-45659",
    "user": "https://github.com/robertwb"
}
```

It appears that even in raw strings the backslash escapes a potential end quote...

http://docs.python.org/reference/lexical_analysis.html



---

archive/issue_comments_045660.json:
```json
{
    "body": "Attachment [5821-preparse-raw.patch](tarball://root/attachments/some-uuid/ticket5821/5821-preparse-raw.patch) by @robertwb created at 2009-04-19 07:27:44",
    "created_at": "2009-04-19T07:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5821#issuecomment-45660",
    "user": "https://github.com/robertwb"
}
```

Attachment [5821-preparse-raw.patch](tarball://root/attachments/some-uuid/ticket5821/5821-preparse-raw.patch) by @robertwb created at 2009-04-19 07:27:44



---

archive/issue_comments_045661.json:
```json
{
    "body": "Code looks good (and fixes the problem); doctests pass.\n\nPositive review.",
    "created_at": "2009-04-19T18:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5821#issuecomment-45661",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good (and fixes the problem); doctests pass.

Positive review.



---

archive/issue_events_013684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-23T07:58:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5821#event-13684"
}
```



---

archive/issue_comments_045662.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5821#issuecomment-45662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045663.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T07:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5821#issuecomment-45663",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013685.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-23T07:58:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5821",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5821#event-13685"
}
```
