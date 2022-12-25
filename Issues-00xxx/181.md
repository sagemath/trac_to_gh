# Issue 181: Recursive load makes symbol?? display the wrong File: information

archive/issues_000181.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: recursive load source file\n\nWe use the example in examples/programming/recursive_load.  \n\n(*Note: this file no longer exists, but one could recreate this situation*)\n\nfile1.sage defines a symbol foo.\nfile2.sage defines a symbol bar.\n\nEach file loads the other recursively.\n\nIf we load file2.sage first, then the source code for foo is displayed correctly by foo?? but the File: information is wrong.  The File: should read file1.sage.\n\n```\nsage: load file2.sage\nloaded file1.sage\nI'm now defining s\nloaded file1.sage\n\nsage: foo??\nType:           function\nBase Class:     <type 'function'>\nString Form:    <function foo at 0x8fd6db0>\nNamespace:      Interactive\nFile:           /Users/nalexand/Devel/sage-alpha8/examples/programming/recursive_load/file2.py\nDefinition:     foo(n)\nSource:\ndef foo(n):\n    print \"foo\"\n    return n**Integer(2)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/181\n\n",
    "created_at": "2006-12-11T18:58:16Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Recursive load makes symbol?? display the wrong File: information",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/181",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: recursive load source file

We use the example in examples/programming/recursive_load.  

(*Note: this file no longer exists, but one could recreate this situation*)

file1.sage defines a symbol foo.
file2.sage defines a symbol bar.

Each file loads the other recursively.

If we load file2.sage first, then the source code for foo is displayed correctly by foo?? but the File: information is wrong.  The File: should read file1.sage.

```
sage: load file2.sage
loaded file1.sage
I'm now defining s
loaded file1.sage

sage: foo??
Type:           function
Base Class:     <type 'function'>
String Form:    <function foo at 0x8fd6db0>
Namespace:      Interactive
File:           /Users/nalexand/Devel/sage-alpha8/examples/programming/recursive_load/file2.py
Definition:     foo(n)
Source:
def foo(n):
    print "foo"
    return n**Integer(2)
```

Issue created by migration from https://trac.sagemath.org/ticket/181





---

archive/issue_events_000343.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-19T09:57:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-1.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-343"
}
```



---

archive/issue_comments_000828.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-22T05:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/181#issuecomment-828",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000829.json:
```json
{
    "body": "This isn't really a bug.  What happens is that from file2.sage the file file2.py\nis created.  And file2.py is where the function foo is actually defined (it's the\npreparsed version).  So the File field above is actually correct about where that\nfunction is defined.  It's *confusing* though, because there is a non-preparsed\n.sage function that is defined in file1.sage, and it would be very nice if the\nFile: field instead listed that.  The only reasonable way I can think of to do\nthat would be to add to the preparser code that embeds original file location\nand line number info in the .py file after the definition of any function. \n\nSo I'm going to change this to an enhancement request rather than a defect, \nas it's not even clear what the right design should be, and currently no invalid\noutput is actually being produced.",
    "created_at": "2007-01-22T05:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/181#issuecomment-829",
    "user": "https://github.com/williamstein"
}
```

This isn't really a bug.  What happens is that from file2.sage the file file2.py
is created.  And file2.py is where the function foo is actually defined (it's the
preparsed version).  So the File field above is actually correct about where that
function is defined.  It's *confusing* though, because there is a non-preparsed
.sage function that is defined in file1.sage, and it would be very nice if the
File: field instead listed that.  The only reasonable way I can think of to do
that would be to add to the preparser code that embeds original file location
and line number info in the .py file after the definition of any function. 

So I'm going to change this to an enhancement request rather than a defect, 
as it's not even clear what the right design should be, and currently no invalid
output is actually being produced.



---

archive/issue_events_000344.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-22T05:01:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-1.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-344"
}
```



---

archive/issue_comments_000830.json:
```json
{
    "body": "Just pointing out to those looking at this that the examples directory no longer exists.  However, the request still makes sense.",
    "created_at": "2013-01-29T20:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/181#issuecomment-830",
    "user": "https://github.com/kcrisman"
}
```

Just pointing out to those looking at this that the examples directory no longer exists.  However, the request still makes sense.



---

archive/issue_events_000345.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-345"
}
```



---

archive/issue_events_000346.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-346"
}
```



---

archive/issue_events_000347.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-347"
}
```



---

archive/issue_events_000348.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-348"
}
```



---

archive/issue_events_000349.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-349"
}
```



---

archive/issue_events_000350.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-350"
}
```



---

archive/issue_events_000351.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/181",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/181#event-351"
}
```
