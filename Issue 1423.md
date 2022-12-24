# Issue 1423: bug/issue in python.eval from sage

archive/issues_001423.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n\n\nOn Dec 7, 2007 9:32 AM, pgdoyle <peter doyle> wrote:\n> \n> Consider this python program:\n> \n> ----------------\n> def foo():\n>   return 'foo'\n> \n> print foo()\n> \n> def mumble():\n>   print 'mumble',foo()\n> \n> mumble()\n> ----------------\n> \n> If put this in a file foo.py and type `python foo.py'  it prints\n> \n> foo\n> mumble foo\n> \n> Same thing if I type 'sage foo.py'.  Same thing if I put it in a cell\n> of a sage notebook and evaluate with sage.\n> But if switch the evaluation option for the notebook from sage to\n> python I get an error:\n> \n> foo\n> mumble\n> Traceback (most recent call last):\n>   File \"<stdin>\", line 1, in <module>\n>   File \"/home/doyle/.sage/sage_notebook/worksheets/admin/2/code/\n> 68.py\", line 12, in <module>\n>     print mumble()''', '/home/doyle/.sage/sage_notebook/worksheets/\n> admin/2/cells/5')\n>   File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/server/\n> support.py\", line 258, in syseval\n>     return system.eval(cmd, locals = sage_globals)\n>   File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/\n> python.py\", line 21, in eval\n>     eval(z, globals, locals)\n>   File \"/usr/local/sage-2.8.15-ubuntu32bit-i686-Linux/data/extcode/\n> sage/\", line 1, in <module>\n> \n>   File \"/usr/local/sage-2.8.15-ubuntu32bit-i686-Linux/data/extcode/\n> sage/\", line 7, in mumble\n> \n> NameError: global name 'foo' is not defined\n> \n> I get the same error if I change the notebook evaluation option back\n> to sage, put %python at the beginning of the cell, and evaluate.\n> \n> Is this a bug or a feature?\n\nI declare it a bug no matter what, since I don't like it at all.\nI only have a minute at the moment, but just want to remark\nthat when you do %python in the notebook or use python\nmode, here is the Python code that actually evaluates the\ninput to the cell:\n\nsage: python.eval??\n\n\nFile: /Users/was/s/local/lib/python2.5/site-packages/sage/misc/python.py\nSource Code (starting at line 5):\n    def eval(self, x, globals={}, locals={}):\n        x = x.strip()\n        y = x.split('\\n')\n        if len(y) == 0:\n            return ''\n        s = '\\n'.join(y[:-1]) + '\\n'\n        t = y[-1]\n        try:\n            z = compile(t + '\\n', '', 'single')\n        except SyntaxError:\n            s += '\\n' + t\n            z = None\n        #else:\n        #    s += '\\n' + t\n        eval(compile(s, '', 'exec'), globals, locals)\n        if not z is None:\n            eval(z, globals, locals)\n        return ''\n\nLooking at that code, does anybody see why the second global foo gets ignored inside\nthe function body of mumble?  I don't immediately see why. \n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1423\n\n",
    "created_at": "2007-12-08T02:09:59Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "bug/issue in python.eval from sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1423",
    "user": "was"
}
```
Assignee: boothby


```


On Dec 7, 2007 9:32 AM, pgdoyle <peter doyle> wrote:
> 
> Consider this python program:
> 
> ----------------
> def foo():
>   return 'foo'
> 
> print foo()
> 
> def mumble():
>   print 'mumble',foo()
> 
> mumble()
> ----------------
> 
> If put this in a file foo.py and type `python foo.py'  it prints
> 
> foo
> mumble foo
> 
> Same thing if I type 'sage foo.py'.  Same thing if I put it in a cell
> of a sage notebook and evaluate with sage.
> But if switch the evaluation option for the notebook from sage to
> python I get an error:
> 
> foo
> mumble
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/home/doyle/.sage/sage_notebook/worksheets/admin/2/code/
> 68.py", line 12, in <module>
>     print mumble()''', '/home/doyle/.sage/sage_notebook/worksheets/
> admin/2/cells/5')
>   File "/usr/local/sage/local/lib/python2.5/site-packages/sage/server/
> support.py", line 258, in syseval
>     return system.eval(cmd, locals = sage_globals)
>   File "/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/
> python.py", line 21, in eval
>     eval(z, globals, locals)
>   File "/usr/local/sage-2.8.15-ubuntu32bit-i686-Linux/data/extcode/
> sage/", line 1, in <module>
> 
>   File "/usr/local/sage-2.8.15-ubuntu32bit-i686-Linux/data/extcode/
> sage/", line 7, in mumble
> 
> NameError: global name 'foo' is not defined
> 
> I get the same error if I change the notebook evaluation option back
> to sage, put %python at the beginning of the cell, and evaluate.
> 
> Is this a bug or a feature?

I declare it a bug no matter what, since I don't like it at all.
I only have a minute at the moment, but just want to remark
that when you do %python in the notebook or use python
mode, here is the Python code that actually evaluates the
input to the cell:

sage: python.eval??


File: /Users/was/s/local/lib/python2.5/site-packages/sage/misc/python.py
Source Code (starting at line 5):
    def eval(self, x, globals={}, locals={}):
        x = x.strip()
        y = x.split('\n')
        if len(y) == 0:
            return ''
        s = '\n'.join(y[:-1]) + '\n'
        t = y[-1]
        try:
            z = compile(t + '\n', '', 'single')
        except SyntaxError:
            s += '\n' + t
            z = None
        #else:
        #    s += '\n' + t
        eval(compile(s, '', 'exec'), globals, locals)
        if not z is None:
            eval(z, globals, locals)
        return ''

Looking at that code, does anybody see why the second global foo gets ignored inside
the function body of mumble?  I don't immediately see why. 

William
```


Issue created by migration from https://trac.sagemath.org/ticket/1423





---

archive/issue_comments_009173.json:
```json
{
    "body": "Attachment [trac-1423.patch](tarball://root/attachments/some-uuid/ticket1423/trac-1423.patch) by was created at 2007-12-12 06:50:20",
    "created_at": "2007-12-12T06:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1423#issuecomment-9173",
    "user": "was"
}
```

Attachment [trac-1423.patch](tarball://root/attachments/some-uuid/ticket1423/trac-1423.patch) by was created at 2007-12-12 06:50:20



---

archive/issue_comments_009174.json:
```json
{
    "body": "This patch does make the given test pass, but now a variable defined in a Sage block is not accessible in a following Python block.  IMHO, that's a serious bug.",
    "created_at": "2007-12-15T02:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1423#issuecomment-9174",
    "user": "cwitty"
}
```

This patch does make the given test pass, but now a variable defined in a Sage block is not accessible in a following Python block.  IMHO, that's a serious bug.



---

archive/issue_comments_009175.json:
```json
{
    "body": "Attachment [trac-1423-part2.patch](tarball://root/attachments/some-uuid/ticket1423/trac-1423-part2.patch) by cwitty created at 2007-12-15 03:00:19\n\nPasses the original test case, and fixes the complaints I had.  I approve.\n\n(apply both patches)",
    "created_at": "2007-12-15T03:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1423#issuecomment-9175",
    "user": "cwitty"
}
```

Attachment [trac-1423-part2.patch](tarball://root/attachments/some-uuid/ticket1423/trac-1423-part2.patch) by cwitty created at 2007-12-15 03:00:19

Passes the original test case, and fixes the complaints I had.  I approve.

(apply both patches)



---

archive/issue_comments_009176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T04:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1423#issuecomment-9176",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009177.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T04:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1423#issuecomment-9177",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.
