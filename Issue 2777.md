# Issue 2777: '??' can't always find the source

archive/issues_002777.json:
```json
{
    "body": "Assignee: @williamstein\n\nHere's an example:\n\n```\nsage: notebook??\n```\n\nThen the screen clears and is replaced by\n\n```\nType:             instance\nBase Class:       sage.server.notebook.notebook_object.NotebookObject\nString Form:   <sage.server.notebook.notebook_object.NotebookObject instance at 0xb5d66c0>\nNamespace:        Interactive\nDocstring [source file open failed]:\n    \n        Start the SAGE Notebook server. \n    \n        INPUT:\n...\n```\n\npiped through my PAGER ('less').  After quitting this, I see\n\n\n```\nError getting source: arg is not a module, class, method, function, traceback, frame, or code object\n\n```\n\n\nThis is in  $SAGE_ROOT for sage-2.11. \"./sage\" is not modified to fix SAGE_ROOT, and \".\" is in my PATH.  Oh, and I'm using the command-line, of course :-}\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2777\n\n",
    "created_at": "2008-04-02T17:54:30Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "'??' can't always find the source",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2777",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

Here's an example:

```
sage: notebook??
```

Then the screen clears and is replaced by

```
Type:             instance
Base Class:       sage.server.notebook.notebook_object.NotebookObject
String Form:   <sage.server.notebook.notebook_object.NotebookObject instance at 0xb5d66c0>
Namespace:        Interactive
Docstring [source file open failed]:
    
        Start the SAGE Notebook server. 
    
        INPUT:
...
```

piped through my PAGER ('less').  After quitting this, I see


```
Error getting source: arg is not a module, class, method, function, traceback, frame, or code object

```


This is in  $SAGE_ROOT for sage-2.11. "./sage" is not modified to fix SAGE_ROOT, and "." is in my PATH.  Oh, and I'm using the command-line, of course :-}




Issue created by migration from https://trac.sagemath.org/ticket/2777





---

archive/issue_comments_019038.json:
```json
{
    "body": "quick'n",
    "created_at": "2008-09-21T22:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2777#issuecomment-19038",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

quick'n



---

archive/issue_comments_019039.json:
```json
{
    "body": "Attachment [2777-1.diff](tarball://root/attachments/some-uuid/ticket2777/2777-1.diff) by aginiewicz created at 2008-09-21 22:22:37\n\nadded quick'n'dirty patch...\n\nthe case with notebook?? can be also seen with all class instances, I made quick patch that make sage.misc.sageinspect.sage_get* functions work with class instances by returning data of class coresponding to given instance... also made notebook version of ?? check for _sage_src_ like was already done in console version.\n\nI don't know if this covers all cases, but works for reported notebook (and also for R functions and probably more)",
    "created_at": "2008-09-21T22:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2777#issuecomment-19039",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Attachment [2777-1.diff](tarball://root/attachments/some-uuid/ticket2777/2777-1.diff) by aginiewicz created at 2008-09-21 22:22:37

added quick'n'dirty patch...

the case with notebook?? can be also seen with all class instances, I made quick patch that make sage.misc.sageinspect.sage_get* functions work with class instances by returning data of class coresponding to given instance... also made notebook version of ?? check for _sage_src_ like was already done in console version.

I don't know if this covers all cases, but works for reported notebook (and also for R functions and probably more)



---

archive/issue_comments_019040.json:
```json
{
    "body": "Works for me for instance classes. New style classes still don't work, but it's not immediately obvious how to handle that case (#4183) so I think this should be merged.",
    "created_at": "2008-09-24T01:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2777#issuecomment-19040",
    "user": "https://github.com/robertwb"
}
```

Works for me for instance classes. New style classes still don't work, but it's not immediately obvious how to handle that case (#4183) so I think this should be merged.



---

archive/issue_comments_019041.json:
```json
{
    "body": "Andrzej,\n\nplease post patches in the future and not diffs since I can accidentally import diffs and then the credit in the log would go to me. Not that I mind .... :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T02:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2777#issuecomment-19041",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Andrzej,

please post patches in the future and not diffs since I can accidentally import diffs and then the credit in the log would go to me. Not that I mind .... :)

Cheers,

Michael



---

archive/issue_comments_019042.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T02:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2777#issuecomment-19042",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_019043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T02:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2777#issuecomment-19043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
