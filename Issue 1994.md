# Issue 1994: cython spyx files -- cinclude, clib, issues

archive/issues_001994.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @malb @robertwb\n\nThere are some issues with cython spyx files:\n\n1. There is *still* nothing in the documentation anywhere in sage about cinclude, clib, etc.  Here's a hint:\n\n```\nBasically you put\n# clang c\n# clib  cblas\n# cfile myfile.c\n# cinclude super.h standard.h\n```\n\nQuestions -- where can one put these?   Must the # be there?  \nHowever this is documented, at a bare minimum typing \n\n```\nsage: cython?\nsage: load?\nsage: attach?\n```\n\nshould give enough information to find docs that clearly explain this cinclude, etc. directives. \n\n2. Create a file a.pxi and a file b.pyx.  Put one of the # directives in the .pxi file and include the pxi file in the pyx file.  The directive is ignored.  This caused a ton of confusion today.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1994\n\n",
    "created_at": "2008-01-31T04:34:13Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cython spyx files -- cinclude, clib, issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1994",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @malb @robertwb

There are some issues with cython spyx files:

1. There is *still* nothing in the documentation anywhere in sage about cinclude, clib, etc.  Here's a hint:

```
Basically you put
# clang c
# clib  cblas
# cfile myfile.c
# cinclude super.h standard.h
```

Questions -- where can one put these?   Must the # be there?  
However this is documented, at a bare minimum typing 

```
sage: cython?
sage: load?
sage: attach?
```

should give enough information to find docs that clearly explain this cinclude, etc. directives. 

2. Create a file a.pxi and a file b.pyx.  Put one of the # directives in the .pxi file and include the pxi file in the pyx file.  The directive is ignored.  This caused a ton of confusion today.

Issue created by migration from https://trac.sagemath.org/ticket/1994





---

archive/issue_comments_012902.json:
```json
{
    "body": "Is there also a directive ccflags (analogous to cflags in C)? For instance, in order to compile an spkg using FLINT, one needs a line like\n\n```\n#ccflags -std=c99\n```\n",
    "created_at": "2008-02-14T22:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12902",
    "user": "@kedlaya"
}
```

Is there also a directive ccflags (analogous to cflags in C)? For instance, in order to compile an spkg using FLINT, one needs a line like

```
#ccflags -std=c99
```




---

archive/issue_comments_012903.json:
```json
{
    "body": "(1) should have been dealt via #3530, i.e. the documentation of the pragmas. \n\n(2) is potentially still valid and I am not sure whose fault it is: Sage or Cython. \n\nI am adding Martin and Robert to the CC field here.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T12:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12903",
    "user": "mabshoff"
}
```

(1) should have been dealt via #3530, i.e. the documentation of the pragmas. 

(2) is potentially still valid and I am not sure whose fault it is: Sage or Cython. 

I am adding Martin and Robert to the CC field here.

Cheers,

Michael



---

archive/issue_comments_012904.json:
```json
{
    "body": "Actually, (1) is not dealt with since it isn't necessarily easy to get to the new documentation. That should be addressed.",
    "created_at": "2008-07-06T12:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12904",
    "user": "@malb"
}
```

Actually, (1) is not dealt with since it isn't necessarily easy to get to the new documentation. That should be addressed.



---

archive/issue_comments_012905.json:
```json
{
    "body": "Note that [this stackoverflow.com post](http://stackoverflow.com/questions/6363978/cython-linking-to-custom-c-code) points to this ticket.  Apparently this is still something that could be documented within Sage better?",
    "created_at": "2012-05-18T03:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12905",
    "user": "@kcrisman"
}
```

Note that [this stackoverflow.com post](http://stackoverflow.com/questions/6363978/cython-linking-to-custom-c-code) points to this ticket.  Apparently this is still something that could be documented within Sage better?



---

archive/issue_comments_012906.json:
```json
{
    "body": "Those directives should be deprecated anyway: #22461",
    "created_at": "2017-06-02T09:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12906",
    "user": "@jdemeyer"
}
```

Those directives should be deprecated anyway: #22461



---

archive/issue_comments_012907.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-06-02T09:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12907",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012908.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-06-02T09:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12908",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012909.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12909",
    "user": "@embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).



---

archive/issue_comments_012910.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1994#issuecomment-12910",
    "user": "@embray"
}
```

Resolution: wontfix
