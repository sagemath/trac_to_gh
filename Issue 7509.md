# Issue 7509: notebook -- make it possible to debug Python code in the notebook, e.g., something like pdb that works in the notebook

archive/issues_007509.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  novoselt whuss\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7509\n\n",
    "created_at": "2009-11-21T13:11:41Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- make it possible to debug Python code in the notebook, e.g., something like pdb that works in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7509",
    "user": "was"
}
```
Assignee: boothby

CC:  novoselt whuss



Issue created by migration from https://trac.sagemath.org/ticket/7509





---

archive/issue_comments_063530.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-21T13:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63530",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_063531.json:
```json
{
    "body": "Paste the following code into any notebook cell (in any version of sage ever) and you have a debugger. \n\n\n```\nclass debug:\n    \"\"\"\n    If you get a traceback in the notebook, type ``d=debug()`` right\n    after the error to create a debugger object on that traceback.\n    Using the debugger you can move and down the call stack, and \n    evaluate arbitrary code anywhere in the call stack (typically\n    to inspect the value of variables).\n    \n        - printing ``d`` shows the call stack and some context\n        - ``d.up(n)`` (or ``d.u(n)``) moves up `n` frames in \n          the call stack\n        - ``d.down(n)`` (or ``d.d(n)``) moves down `n` frames\n          in the call stack\n        - ``d.list(n)`` (or ``d.l(n)``) displays `n` lines of source \n          code context around the current position in the stack trace\n        - ``d(\"some code\")`` executes the given code in the\n          context of the current position in the stack trace\n          \n    Notes:\n        - Input is not preparsed. \n        - You can define and work with many debug objects at the same time.\n    \"\"\"\n    def __init__(self):\n        import inspect, traceback\n        self.stack = inspect.getinnerframes(sys.last_traceback)\n        self.__curframe = len(self.stack) - 1\n        self.tb = traceback.format_tb(sys.last_traceback)\n        \n    def curframe(self):\n        return self.stack[self.__curframe][0]\n        \n    def frameno(self):\n        return self.__curframe\n        \n    def __call__(self, line):\n        locals = self.curframe().f_locals\n        globals = self.curframe().f_globals\n        try:\n            code = compile(line + '\\n', '<stdin>', 'single')\n            exec code in globals, locals\n        except:\n            t, v = sys.exc_info()[:2]\n            if type(t) == type(''):\n                exc_type_name = t\n            else: exc_type_name = t.__name__\n            print '***', exc_type_name + ':', v\n        \n    def _highlight(self, line):\n        from pygments import highlight\n        from pygments.lexers import PythonLexer\n        from pygments.formatters import HtmlFormatter\n        return highlight(line, PythonLexer(), HtmlFormatter())        \n\n    def __repr__(self):\n        v = ['  ' + str(i) + ':  ' + ' '*(2*i) + \n                 ('\\n'+' '*(2*i)).join(self.tb[i].splitlines()) \n                  for i in range(self.__curframe+1)]\n        if len(v) < len(self.stack):\n            v.append('  ............')\n            v.append('  ' + str(len(self.stack)-1) + ':  (bottom frame)')\n        s = '<b>Traceback:</b>' + self._highlight('\\n'.join(v)) + self._list()\n        return '<html>%s</html>'%s\n\n    def up(self, n=1):\n        self.__curframe -= n\n        if self.__curframe < 0:\n            self.__curframe = 0\n    u = up\n        \n    def down(self, n=1):\n        self.__curframe += n\n        if self.__curframe >= len(self.stack):\n            self.__curframe = len(self.stack)-1\n    d = down\n        \n    def _list(self, n=3):\n        curframe = self.curframe()\n        filename = curframe.f_code.co_filename\n        lineno = curframe.f_lineno\n        import linecache\n        code = ''.join('--> ' if i ==lineno else '    ' + \n                    linecache.getline(filename, i, curframe.f_globals) for\n                    i in range(lineno-n, lineno+n+1))\n        i = filename.rfind('site-packages/sage')\n        if i != -1:\n            fname = filename[i+len('site-packages/sage')+1:].rstrip('/')\n            file = '<a href=\"/src/%s\" target=\"_new\">%s</a>'%(fname,fname)\n        else:\n            file = '<pre>%s</pre>'%filename\n        t = \"\"\"<b>Frame:</b> %s\\n<b>File:  </b>%s<hr>%s<hr>\"\"\"%(\n                 self.frameno(),                \n                 file,self._highlight(code).strip())\n        return t\n                 \n    def list(self, n=3):\n        html(self._list(n))\n    l = list\n```\n",
    "created_at": "2009-11-21T13:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63531",
    "user": "was"
}
```

Paste the following code into any notebook cell (in any version of sage ever) and you have a debugger. 


```
class debug:
    """
    If you get a traceback in the notebook, type ``d=debug()`` right
    after the error to create a debugger object on that traceback.
    Using the debugger you can move and down the call stack, and 
    evaluate arbitrary code anywhere in the call stack (typically
    to inspect the value of variables).
    
        - printing ``d`` shows the call stack and some context
        - ``d.up(n)`` (or ``d.u(n)``) moves up `n` frames in 
          the call stack
        - ``d.down(n)`` (or ``d.d(n)``) moves down `n` frames
          in the call stack
        - ``d.list(n)`` (or ``d.l(n)``) displays `n` lines of source 
          code context around the current position in the stack trace
        - ``d("some code")`` executes the given code in the
          context of the current position in the stack trace
          
    Notes:
        - Input is not preparsed. 
        - You can define and work with many debug objects at the same time.
    """
    def __init__(self):
        import inspect, traceback
        self.stack = inspect.getinnerframes(sys.last_traceback)
        self.__curframe = len(self.stack) - 1
        self.tb = traceback.format_tb(sys.last_traceback)
        
    def curframe(self):
        return self.stack[self.__curframe][0]
        
    def frameno(self):
        return self.__curframe
        
    def __call__(self, line):
        locals = self.curframe().f_locals
        globals = self.curframe().f_globals
        try:
            code = compile(line + '\n', '<stdin>', 'single')
            exec code in globals, locals
        except:
            t, v = sys.exc_info()[:2]
            if type(t) == type(''):
                exc_type_name = t
            else: exc_type_name = t.__name__
            print '***', exc_type_name + ':', v
        
    def _highlight(self, line):
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import HtmlFormatter
        return highlight(line, PythonLexer(), HtmlFormatter())        

    def __repr__(self):
        v = ['  ' + str(i) + ':  ' + ' '*(2*i) + 
                 ('\n'+' '*(2*i)).join(self.tb[i].splitlines()) 
                  for i in range(self.__curframe+1)]
        if len(v) < len(self.stack):
            v.append('  ............')
            v.append('  ' + str(len(self.stack)-1) + ':  (bottom frame)')
        s = '<b>Traceback:</b>' + self._highlight('\n'.join(v)) + self._list()
        return '<html>%s</html>'%s

    def up(self, n=1):
        self.__curframe -= n
        if self.__curframe < 0:
            self.__curframe = 0
    u = up
        
    def down(self, n=1):
        self.__curframe += n
        if self.__curframe >= len(self.stack):
            self.__curframe = len(self.stack)-1
    d = down
        
    def _list(self, n=3):
        curframe = self.curframe()
        filename = curframe.f_code.co_filename
        lineno = curframe.f_lineno
        import linecache
        code = ''.join('--> ' if i ==lineno else '    ' + 
                    linecache.getline(filename, i, curframe.f_globals) for
                    i in range(lineno-n, lineno+n+1))
        i = filename.rfind('site-packages/sage')
        if i != -1:
            fname = filename[i+len('site-packages/sage')+1:].rstrip('/')
            file = '<a href="/src/%s" target="_new">%s</a>'%(fname,fname)
        else:
            file = '<pre>%s</pre>'%filename
        t = """<b>Frame:</b> %s\n<b>File:  </b>%s<hr>%s<hr>"""%(
                 self.frameno(),                
                 file,self._highlight(code).strip())
        return t
                 
    def list(self, n=3):
        html(self._list(n))
    l = list
```




---

archive/issue_comments_063532.json:
```json
{
    "body": "Here's a proof concept interact, assuming one did:\n\n```\nd1 = debug()\n```\n\nat some point.\n\n```\n@interact\ndef _(command=[None, 'up','down'], code=''):\n    if command == 'up':\n        d1.up()\n    if command == 'down':\n        d1.down()\n    if code:\n        print \"<html>>>> %s\"%code\n        d1(code)\n        print '<hr></html>'\n        \n    print d1\n```\n",
    "created_at": "2009-11-21T13:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63532",
    "user": "was"
}
```

Here's a proof concept interact, assuming one did:

```
d1 = debug()
```

at some point.

```
@interact
def _(command=[None, 'up','down'], code=''):
    if command == 'up':
        d1.up()
    if command == 'down':
        d1.down()
    if code:
        print "<html>>>> %s"%code
        d1(code)
        print '<hr></html>'
        
    print d1
```




---

archive/issue_comments_063533.json:
```json
{
    "body": "Steps to try this out interactively in the notebook:\n\n1. install the patch and rebuild Sage.\n\n2. Do anything that causes a traceback in the notebook, e.g., `EllipticCurve([0,0])`\n\n3. Type `debug()` in any other notebook cell.    You can move up and down the call stack, adjust the amount of context, and evaluate code in the box.   These are the *only* features currently supported -- no setting of breakpoints, stepping through execution, etc.  But this is a very useful first step. \n\nSource code display for Cython code isn't implemented yet.  That's for another ticket.  I think it's OK to put off, since the command line debugger doesn't support it anyways.",
    "created_at": "2012-01-30T03:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63533",
    "user": "was"
}
```

Steps to try this out interactively in the notebook:

1. install the patch and rebuild Sage.

2. Do anything that causes a traceback in the notebook, e.g., `EllipticCurve([0,0])`

3. Type `debug()` in any other notebook cell.    You can move up and down the call stack, adjust the amount of context, and evaluate code in the box.   These are the *only* features currently supported -- no setting of breakpoints, stepping through execution, etc.  But this is a very useful first step. 

Source code display for Cython code isn't implemented yet.  That's for another ticket.  I think it's OK to put off, since the command line debugger doesn't support it anyways.



---

archive/issue_comments_063534.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-30T03:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63534",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063535.json:
```json
{
    "body": "Attachment\n\nready to go",
    "created_at": "2012-01-30T03:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63535",
    "user": "was"
}
```

Attachment

ready to go



---

archive/issue_comments_063536.json:
```json
{
    "body": "Should line 192 of your patch contain the string as r\"\"\" \"\"\"?\n\n```\n        t = \"\"\"%s<hr>> %s\"\"\"%(code, file)\n```\n\nI see that \"< >\" constructs are eaten away by the browser. An example code which you can use to debug your `Debug()` (pun intended :)) is the following:\n\n```\nReedSolomonCode(15,2,GF(16,'a')).minimum_distance()\n```\n\nYou need to go to stack frame 8, and look at line 396 of the code that is printed.\n\nOtherwise, it functions very nicely!",
    "created_at": "2012-01-30T19:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63536",
    "user": "ppurka"
}
```

Should line 192 of your patch contain the string as r""" """?

```
        t = """%s<hr>> %s"""%(code, file)
```

I see that "< >" constructs are eaten away by the browser. An example code which you can use to debug your `Debug()` (pun intended :)) is the following:

```
ReedSolomonCode(15,2,GF(16,'a')).minimum_distance()
```

You need to go to stack frame 8, and look at line 396 of the code that is printed.

Otherwise, it functions very nicely!



---

archive/issue_comments_063537.json:
```json
{
    "body": "Replying to [comment:8 ppurka]:\n> Should line 192 of your patch contain the string as r\"\"\" \"\"\"?\n> {{{\n>         t = \"\"\"%s<hr>> %s\"\"\"%(code, file)\n> }}}\n\nNo.  r is *only* needed if your string contains backslashes and you don't want to escape them.  It has nothing to do with HTML tags at all. \n\n> I see that \"< >\" constructs are eaten away by the browser. \n\nAbove t is an HTML string that I'm construting, and output within an <html> block for the notebook.  It thus gets displayed properly. \n\n> An example code which you can use to debug your `Debug()` (pun intended :)) is the following:\n> {{{\n> ReedSolomonCode(15,2,GF(16,'a')).minimum_distance()\n> }}}\n> You need to go to stack frame 8, and look at line 396 of the code that is printed.\n\nAh, now I see what you mean. The stupid source code display needs to have some HTML escaping done, e.g., < turned to &lt;.  There is a function in the notebook that does that properly, and I'll fix the patch accordingly.  Thanks for finding a genuine bug.  I'll also modify my example functions to include something like. \n\n\n> \n> Otherwise, it functions very nicely!",
    "created_at": "2012-01-30T19:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63537",
    "user": "was"
}
```

Replying to [comment:8 ppurka]:
> Should line 192 of your patch contain the string as r""" """?
> {{{
>         t = """%s<hr>> %s"""%(code, file)
> }}}

No.  r is *only* needed if your string contains backslashes and you don't want to escape them.  It has nothing to do with HTML tags at all. 

> I see that "< >" constructs are eaten away by the browser. 

Above t is an HTML string that I'm construting, and output within an <html> block for the notebook.  It thus gets displayed properly. 

> An example code which you can use to debug your `Debug()` (pun intended :)) is the following:
> {{{
> ReedSolomonCode(15,2,GF(16,'a')).minimum_distance()
> }}}
> You need to go to stack frame 8, and look at line 396 of the code that is printed.

Ah, now I see what you mean. The stupid source code display needs to have some HTML escaping done, e.g., < turned to &lt;.  There is a function in the notebook that does that properly, and I'll fix the patch accordingly.  Thanks for finding a genuine bug.  I'll also modify my example functions to include something like. 


> 
> Otherwise, it functions very nicely!



---

archive/issue_comments_063538.json:
```json
{
    "body": "Attachment\n\nnew version addressing the bug that was found ppurka -- apply only this",
    "created_at": "2012-01-30T20:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63538",
    "user": "was"
}
```

Attachment

new version addressing the bug that was found ppurka -- apply only this



---

archive/issue_comments_063539.json:
```json
{
    "body": "ppurka  -- please continue to review the patch now.",
    "created_at": "2012-01-30T20:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63539",
    "user": "was"
}
```

ppurka  -- please continue to review the patch now.



---

archive/issue_comments_063540.json:
```json
{
    "body": "Replying to [comment:10 was]:\n>  ppurka  -- please continue to review the patch now.\n\nYes. The listing is fixed now. But the hyperlink to the file is broken. I fail to see why this should happen, since the `<hr>` and filename are not escaped. (Tested this functionality on sagenb.org.)",
    "created_at": "2012-01-30T20:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63540",
    "user": "ppurka"
}
```

Replying to [comment:10 was]:
>  ppurka  -- please continue to review the patch now.

Yes. The listing is fixed now. But the hyperlink to the file is broken. I fail to see why this should happen, since the `<hr>` and filename are not escaped. (Tested this functionality on sagenb.org.)



---

archive/issue_comments_063541.json:
```json
{
    "body": "address bug introduced by bugfix.  apply only this.",
    "created_at": "2012-01-30T20:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63541",
    "user": "was"
}
```

address bug introduced by bugfix.  apply only this.



---

archive/issue_comments_063542.json:
```json
{
    "body": "Attachment\n\nDoh -- fixed now.",
    "created_at": "2012-01-30T20:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63542",
    "user": "was"
}
```

Attachment

Doh -- fixed now.



---

archive/issue_comments_063543.json:
```json
{
    "body": "adds syntax highlighting",
    "created_at": "2012-01-30T20:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63543",
    "user": "whuss"
}
```

adds syntax highlighting



---

archive/issue_comments_063544.json:
```json
{
    "body": "Attachment\n\nThis is very nice und useful.\n\nThe patch [trac_7509_syntax_highlight.patch] adds syntax highlighting to the stack frame,\nand removes the first few frames, since they don't show anything interesting.\n\nThe <hr>> things are also fixed. Apply after the first patch [trac_7509.patch].",
    "created_at": "2012-01-30T20:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63544",
    "user": "whuss"
}
```

Attachment

This is very nice und useful.

The patch [trac_7509_syntax_highlight.patch] adds syntax highlighting to the stack frame,
and removes the first few frames, since they don't show anything interesting.

The <hr>> things are also fixed. Apply after the first patch [trac_7509.patch].



---

archive/issue_comments_063545.json:
```json
{
    "body": "Hi whuss.  Thanks.    I'm reluctant to do syntax hilighting that way (the way you do in your patch, just on code), since it is very often completely wrong if we don't hilight the whole file.   We need to hilight the whole file, then grab just the relevant part back.    Interesting about removing the first few frames -- I was concerned about doing that; is this now consistent with %debug on the command line?",
    "created_at": "2012-01-30T21:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63545",
    "user": "was"
}
```

Hi whuss.  Thanks.    I'm reluctant to do syntax hilighting that way (the way you do in your patch, just on code), since it is very often completely wrong if we don't hilight the whole file.   We need to hilight the whole file, then grab just the relevant part back.    Interesting about removing the first few frames -- I was concerned about doing that; is this now consistent with %debug on the command line?



---

archive/issue_comments_063546.json:
```json
{
    "body": "I think I agree that we should remove the first few frames.  In the example I was playing with they were actually empty.\n\nI don't know about syntax highlighting.  I think it may be best to focus on in a later ticket.",
    "created_at": "2012-01-31T00:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63546",
    "user": "roed"
}
```

I think I agree that we should remove the first few frames.  In the example I was playing with they were actually empty.

I don't know about syntax highlighting.  I think it may be best to focus on in a later ticket.



---

archive/issue_comments_063547.json:
```json
{
    "body": "apply only this -- includes shrinking the stack; also prints a message if source code not known.",
    "created_at": "2012-01-31T06:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63547",
    "user": "was"
}
```

apply only this -- includes shrinking the stack; also prints a message if source code not known.



---

archive/issue_comments_063548.json:
```json
{
    "body": "Attachment\n\nI made a new patch:\n\n* has the shrunk stack\n* prints something when source code not available (yet) \n* adds whuff as co-author.",
    "created_at": "2012-01-31T06:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63548",
    "user": "was"
}
```

Attachment

I made a new patch:

* has the shrunk stack
* prints something when source code not available (yet) 
* adds whuff as co-author.



---

archive/issue_comments_063549.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-31T23:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63549",
    "user": "roed"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063550.json:
```json
{
    "body": "This is while debugging the example\n\n```\nEllipticCurve([0,0])\n```\n\n\nIf you type in a command (e.g. \"print ainvs\"), execute it, switch to a different frame and press enter again, nothing happens: it doesn't execute the print statement in the new frame.  You can get it to execute by hitting the button though.  If you type in a different command, then it starts executing upon pressing enter again.\n\nThere are doctest failures in listing, since you updated the functions.\n\nAnother small request would be to add a doctest to the evaluate function that demonstrates the case that a user types in a command to the text box which raises an error.",
    "created_at": "2012-01-31T23:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63550",
    "user": "roed"
}
```

This is while debugging the example

```
EllipticCurve([0,0])
```


If you type in a command (e.g. "print ainvs"), execute it, switch to a different frame and press enter again, nothing happens: it doesn't execute the print statement in the new frame.  You can get it to execute by hitting the button though.  If you type in a different command, then it starts executing upon pressing enter again.

There are doctest failures in listing, since you updated the functions.

Another small request would be to add a doctest to the evaluate function that demonstrates the case that a user types in a command to the text box which raises an error.



---

archive/issue_comments_063551.json:
```json
{
    "body": "Replying to [comment:17 roed]:\n> This is while debugging the example\n> {{{\n> EllipticCurve([0,0])\n> }}}\n> \n> If you type in a command (e.g. \"print ainvs\"), execute it, switch to a different frame and press enter again, nothing happens: it doesn't execute the print statement in the new frame.  You can get it to execute by hitting the button though.  If you type in a different command, then it starts executing upon pressing enter again.\n> \n\nThis is a fundamental limitation of `@`interact right now.   I can make a remark about this in the docstring.\n\nI'll fix + improve the doctests and post a new patch.\n\n> There are doctest failures in listing, since you updated the functions.\n> \n> Another small request would be to add a doctest to the evaluate function that demonstrates the case that a user types in a command to the text box which raises an error.",
    "created_at": "2012-02-01T00:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63551",
    "user": "was"
}
```

Replying to [comment:17 roed]:
> This is while debugging the example
> {{{
> EllipticCurve([0,0])
> }}}
> 
> If you type in a command (e.g. "print ainvs"), execute it, switch to a different frame and press enter again, nothing happens: it doesn't execute the print statement in the new frame.  You can get it to execute by hitting the button though.  If you type in a different command, then it starts executing upon pressing enter again.
> 

This is a fundamental limitation of `@`interact right now.   I can make a remark about this in the docstring.

I'll fix + improve the doctests and post a new patch.

> There are doctest failures in listing, since you updated the functions.
> 
> Another small request would be to add a doctest to the evaluate function that demonstrates the case that a user types in a command to the text box which raises an error.



---

archive/issue_comments_063552.json:
```json
{
    "body": "Attachment\n\napply only this; addresses referee remarks.",
    "created_at": "2012-02-01T07:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63552",
    "user": "was"
}
```

Attachment

apply only this; addresses referee remarks.



---

archive/issue_comments_063553.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-01T07:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63553",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063554.json:
```json
{
    "body": "Testing...",
    "created_at": "2012-02-01T13:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63554",
    "user": "roed"
}
```

Testing...



---

archive/issue_comments_063555.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-01T20:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63555",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063556.json:
```json
{
    "body": "All tests pass.",
    "created_at": "2012-02-01T20:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63556",
    "user": "roed"
}
```

All tests pass.



---

archive/issue_comments_063557.json:
```json
{
    "body": "Replying to [comment:14 was]:\n> Hi whuss.  Thanks.    I'm reluctant to do syntax hilighting that way (the way you do in your patch, just on code), since it is very often completely wrong if we don't hilight the whole file.   We need to hilight the whole file, then grab just the relevant part back.\n\nI want to avoid highlighting the whole file, since this can be quite slow.\nOn my computer it takes about 2 seconds to load and highlight graphs/generic_graph.py.\n\nI think the main problem when one gets wrong highlighting is when the code fragment\nstarts in the middle of a docstring. At ticket:12451 there is an improved patch which\ndetects when the code fragments starts in the middle of a tripple quoted string, and does the correct highlighting in this case.",
    "created_at": "2012-02-06T11:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63557",
    "user": "whuss"
}
```

Replying to [comment:14 was]:
> Hi whuss.  Thanks.    I'm reluctant to do syntax hilighting that way (the way you do in your patch, just on code), since it is very often completely wrong if we don't hilight the whole file.   We need to hilight the whole file, then grab just the relevant part back.

I want to avoid highlighting the whole file, since this can be quite slow.
On my computer it takes about 2 seconds to load and highlight graphs/generic_graph.py.

I think the main problem when one gets wrong highlighting is when the code fragment
starts in the middle of a docstring. At ticket:12451 there is an improved patch which
detects when the code fragments starts in the middle of a tripple quoted string, and does the correct highlighting in this case.



---

archive/issue_comments_063558.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-02-06T16:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63558",
    "user": "jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_063559.json:
```json
{
    "body": "**Please report this patch to the SageNB developers**",
    "created_at": "2012-02-06T16:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63559",
    "user": "jdemeyer"
}
```

**Please report this patch to the SageNB developers**



---

archive/issue_comments_063560.json:
```json
{
    "body": "Reported: [http://code.google.com/p/sagenb/issues/detail?id=89](http://code.google.com/p/sagenb/issues/detail?id=89)",
    "created_at": "2012-02-06T16:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63560",
    "user": "jdemeyer"
}
```

Reported: [http://code.google.com/p/sagenb/issues/detail?id=89](http://code.google.com/p/sagenb/issues/detail?id=89)



---

archive/issue_comments_063561.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-02-06T16:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63561",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_063562.json:
```json
{
    "body": "Apologies, this is actually independent of the notebook.",
    "created_at": "2012-02-06T16:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63562",
    "user": "jdemeyer"
}
```

Apologies, this is actually independent of the notebook.



---

archive/issue_comments_063563.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2012-02-06T16:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63563",
    "user": "jdemeyer"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_063564.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2012-02-06T16:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63564",
    "user": "jdemeyer"
}
```

Changing component from notebook to interact.



---

archive/issue_comments_063565.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-06T16:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63565",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063566.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-06T16:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63566",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-07T13:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63567",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_063568.json:
```json
{
    "body": "i think there is a minor typo in the docstring line 264\n\nmissing word \"up\": Using the debugger you can move <up> and down the stack frame and\u00a0\n\n--\n\ni'm not sure what is the preferred convention for fixing typos, i can make a patch for this isolated line.",
    "created_at": "2012-02-09T14:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63568",
    "user": "aranc"
}
```

i think there is a minor typo in the docstring line 264

missing word "up": Using the debugger you can move <up> and down the stack frame and 

--

i'm not sure what is the preferred convention for fixing typos, i can make a patch for this isolated line.



---

archive/issue_comments_063569.json:
```json
{
    "body": "Replying to [comment:29 aranc]:\n> i think there is a minor typo in the docstring line 264\n> \n> missing word \"up\": Using the debugger you can move <up> and down the stack frame and\u00a0\n> \n> --\n> \n> i'm not sure what is the preferred convention for fixing typos, i can make a patch for this isolated line.\n\nSee #12506.  Please review!",
    "created_at": "2012-02-13T15:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7509#issuecomment-63569",
    "user": "was"
}
```

Replying to [comment:29 aranc]:
> i think there is a minor typo in the docstring line 264
> 
> missing word "up": Using the debugger you can move <up> and down the stack frame and 
> 
> --
> 
> i'm not sure what is the preferred convention for fixing typos, i can make a patch for this isolated line.

See #12506.  Please review!
