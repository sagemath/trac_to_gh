# Issue 4894: [with patch; needs review] save_session -- bug when saving %cython functions, etc.

archive/issues_004894.json:
```json
{
    "body": "Assignee: boothby\n\nI was easily able to replicate the following:\n\n```\nM. Yurko\n to sage-support\n\t\nshow details 1:32 PM (1 hour ago)\n\t\n\t\nReply\n\t\n\t\n\nI have recently been using save_session a bit, and I uncovered what I\nbelieve is a bug. If the worksheet of the session that I'm trying to\nsave contains a cython function, then load_session chokes. For\nexample:\n\nvar1 = 1\nvar2 = 2\nvar3 = srange(1,10000)\nvar4 = range(1,3000)\nvar5 = 1234.123456\n\n%cython\ndef test(double x):\n   return x\n\nsave_session('test_session')\n\nand then I save and exit, and re-enter the worksheet\n\nload_session('test_session')\n\nand I get\n\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"/home/myurko/.sage/sage_notebook/worksheets/admin/28/code/\n1.py\", line 6, in <module>\n   load_session(\\u0027test_session\\u0027)\n File \"/home/myurko/sage-3.2.1/local/lib/python2.5/site-packages/\nSQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n\n File \"session.pyx\", line 300, in sage.misc.session.load_session\n(sage/misc/session.c:1403)\n File \"sage_object.pyx\", line 477, in sage.structure.sage_object.load\n(sage/structure/sage_object.c:4865)\n File \"sage_object.pyx\", line 598, in\nsage.structure.sage_object.loads (sage/structure/sage_object.c:6121)\nRuntimeError: No module named\n_home_myurko__sage_sage_notebook_worksheets_admin_28_code_sage8_spyx_0\ninvalid data stream\ninvalid load key, 'x'.\nUnable to load pickled data.\n\nWhen I ran save_session with verbose = true, I noticed that it saved\ntest, which according to the docstring shouldn't have happened. Does\nanyone have any workarounds for this issue?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4894\n\n",
    "created_at": "2008-12-30T22:51:08Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch; needs review] save_session -- bug when saving %cython functions, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4894",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

I was easily able to replicate the following:

```
M. Yurko
 to sage-support
	
show details 1:32 PM (1 hour ago)
	
	
Reply
	
	

I have recently been using save_session a bit, and I uncovered what I
believe is a bug. If the worksheet of the session that I'm trying to
save contains a cython function, then load_session chokes. For
example:

var1 = 1
var2 = 2
var3 = srange(1,10000)
var4 = range(1,3000)
var5 = 1234.123456

%cython
def test(double x):
   return x

save_session('test_session')

and then I save and exit, and re-enter the worksheet

load_session('test_session')

and I get

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/myurko/.sage/sage_notebook/worksheets/admin/28/code/
1.py", line 6, in <module>
   load_session(\u0027test_session\u0027)
 File "/home/myurko/sage-3.2.1/local/lib/python2.5/site-packages/
SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>

 File "session.pyx", line 300, in sage.misc.session.load_session
(sage/misc/session.c:1403)
 File "sage_object.pyx", line 477, in sage.structure.sage_object.load
(sage/structure/sage_object.c:4865)
 File "sage_object.pyx", line 598, in
sage.structure.sage_object.loads (sage/structure/sage_object.c:6121)
RuntimeError: No module named
_home_myurko__sage_sage_notebook_worksheets_admin_28_code_sage8_spyx_0
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.

When I ran save_session with verbose = true, I noticed that it saved
test, which according to the docstring shouldn't have happened. Does
anyone have any workarounds for this issue?
```


Issue created by migration from https://trac.sagemath.org/ticket/4894





---

archive/issue_comments_037038.json:
```json
{
    "body": "The attached patch fixes the problem by explicitly not saving builtin (or not)) functions or classes, since in fact defining classes also breaks load_session and save_session.\n\nIt just occurred to me that one can still make sessions that can't be reloaded.  E.g.,\n\n```\nclass Foo:\n    pass\n\nf = Foo()\n```\n\n\nThen save_session followed by quit and load_session fails.  However, I doubt there is any good way to deal with this.  Fortunately, in the above case, unlike in the case that this bug is about, one can simply re-evaluate the code to define Foo, and suddenly load_session works fine. \nI've put a comment abou this in the patch.",
    "created_at": "2008-12-30T23:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4894#issuecomment-37038",
    "user": "https://github.com/williamstein"
}
```

The attached patch fixes the problem by explicitly not saving builtin (or not)) functions or classes, since in fact defining classes also breaks load_session and save_session.

It just occurred to me that one can still make sessions that can't be reloaded.  E.g.,

```
class Foo:
    pass

f = Foo()
```


Then save_session followed by quit and load_session fails.  However, I doubt there is any good way to deal with this.  Fortunately, in the above case, unlike in the case that this bug is about, one can simply re-evaluate the code to define Foo, and suddenly load_session works fine. 
I've put a comment abou this in the patch.



---

archive/issue_comments_037039.json:
```json
{
    "body": "Attachment [trac_4894.patch](tarball://root/attachments/some-uuid/ticket4894/trac_4894.patch) by mabshoff created at 2009-01-02 21:57:33",
    "created_at": "2009-01-02T21:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4894#issuecomment-37039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4894.patch](tarball://root/attachments/some-uuid/ticket4894/trac_4894.patch) by mabshoff created at 2009-01-02 21:57:33



---

archive/issue_comments_037040.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-03T06:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4894#issuecomment-37040",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_037041.json:
```json
{
    "body": "Merged in Sage 3.2.3.final",
    "created_at": "2009-01-03T06:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4894#issuecomment-37041",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.final



---

archive/issue_events_005138.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-03T06:01:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4894",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4894#event-5138"
}
```



---

archive/issue_comments_037042.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-03T06:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4894#issuecomment-37042",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
