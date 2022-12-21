# Issue 1423: bug/issue in python.eval from sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-08 02:09:59

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



---

Attachment


---

Comment by cwitty created at 2007-12-15 02:34:51

This patch does make the given test pass, but now a variable defined in a Sage block is not accessible in a following Python block.  IMHO, that's a serious bug.


---

Attachment

Passes the original test case, and fixes the complaints I had.  I approve.

(apply both patches)


---

Comment by mabshoff created at 2007-12-15 04:42:51

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 04:42:51

Merged in 2.9.rc0.
