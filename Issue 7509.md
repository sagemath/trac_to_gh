# Issue 7509: notebook -- make it possible to debug Python code in the notebook, e.g., something like pdb that works in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/7509

Original creator: was

Original creation time: 2009-11-21 13:11:41

Assignee: boothby

CC:  novoselt whuss




---

Comment by was created at 2009-11-21 13:11:49

Changing type from defect to enhancement.


---

Comment by was created at 2009-11-21 13:40:16

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

Comment by was created at 2009-11-21 13:54:27

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

Comment by was created at 2012-01-30 03:20:47

Steps to try this out interactively in the notebook:

1. install the patch and rebuild Sage.

2. Do anything that causes a traceback in the notebook, e.g., `EllipticCurve([0,0])`

3. Type `debug()` in any other notebook cell.    You can move up and down the call stack, adjust the amount of context, and evaluate code in the box.   These are the *only* features currently supported -- no setting of breakpoints, stepping through execution, etc.  But this is a very useful first step. 

Source code display for Cython code isn't implemented yet.  That's for another ticket.  I think it's OK to put off, since the command line debugger doesn't support it anyways.


---

Comment by was created at 2012-01-30 03:20:53

Changing status from new to needs_review.


---

Attachment

ready to go


---

Comment by ppurka created at 2012-01-30 19:29:49

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

Comment by was created at 2012-01-30 19:50:07

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

Attachment

new version addressing the bug that was found ppurka -- apply only this


---

Comment by was created at 2012-01-30 20:03:24

ppurka  -- please continue to review the patch now.


---

Comment by ppurka created at 2012-01-30 20:22:01

Replying to [comment:10 was]:
>  ppurka  -- please continue to review the patch now.

Yes. The listing is fixed now. But the hyperlink to the file is broken. I fail to see why this should happen, since the `<hr>` and filename are not escaped. (Tested this functionality on sagenb.org.)


---

Comment by was created at 2012-01-30 20:31:15

address bug introduced by bugfix.  apply only this.


---

Attachment

Doh -- fixed now.


---

Comment by whuss created at 2012-01-30 20:43:22

adds syntax highlighting


---

Attachment

This is very nice und useful.

The patch [trac_7509_syntax_highlight.patch] adds syntax highlighting to the stack frame,
and removes the first few frames, since they don't show anything interesting.

The <hr>> things are also fixed. Apply after the first patch [trac_7509.patch].


---

Comment by was created at 2012-01-30 21:03:44

Hi whuss.  Thanks.    I'm reluctant to do syntax hilighting that way (the way you do in your patch, just on code), since it is very often completely wrong if we don't hilight the whole file.   We need to hilight the whole file, then grab just the relevant part back.    Interesting about removing the first few frames -- I was concerned about doing that; is this now consistent with %debug on the command line?


---

Comment by roed created at 2012-01-31 00:28:03

I think I agree that we should remove the first few frames.  In the example I was playing with they were actually empty.

I don't know about syntax highlighting.  I think it may be best to focus on in a later ticket.


---

Comment by was created at 2012-01-31 06:51:00

apply only this -- includes shrinking the stack; also prints a message if source code not known.


---

Attachment

I made a new patch:

  * has the shrunk stack
  * prints something when source code not available (yet) 
  * adds whuff as co-author.


---

Comment by roed created at 2012-01-31 23:48:29

Changing status from needs_review to needs_work.


---

Comment by roed created at 2012-01-31 23:48:29

This is while debugging the example

```
EllipticCurve([0,0])
```


If you type in a command (e.g. "print ainvs"), execute it, switch to a different frame and press enter again, nothing happens: it doesn't execute the print statement in the new frame.  You can get it to execute by hitting the button though.  If you type in a different command, then it starts executing upon pressing enter again.

There are doctest failures in listing, since you updated the functions.

Another small request would be to add a doctest to the evaluate function that demonstrates the case that a user types in a command to the text box which raises an error.


---

Comment by was created at 2012-02-01 00:12:56

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

Attachment

apply only this; addresses referee remarks.


---

Comment by was created at 2012-02-01 07:12:13

Changing status from needs_work to needs_review.


---

Comment by roed created at 2012-02-01 13:22:30

Testing...


---

Comment by roed created at 2012-02-01 20:55:09

Changing status from needs_review to positive_review.


---

Comment by roed created at 2012-02-01 20:55:09

All tests pass.


---

Comment by whuss created at 2012-02-06 11:28:28

Replying to [comment:14 was]:
> Hi whuss.  Thanks.    I'm reluctant to do syntax hilighting that way (the way you do in your patch, just on code), since it is very often completely wrong if we don't hilight the whole file.   We need to hilight the whole file, then grab just the relevant part back.

I want to avoid highlighting the whole file, since this can be quite slow.
On my computer it takes about 2 seconds to load and highlight graphs/generic_graph.py.

I think the main problem when one gets wrong highlighting is when the code fragment
starts in the middle of a docstring. At ticket:12451 there is an improved patch which
detects when the code fragments starts in the middle of a tripple quoted string, and does the correct highlighting in this case.


---

Comment by jdemeyer created at 2012-02-06 16:19:29

Resolution: invalid


---

Comment by jdemeyer created at 2012-02-06 16:19:29

*Please report this patch to the SageNB developers*


---

Comment by jdemeyer created at 2012-02-06 16:21:27

Reported: [http://code.google.com/p/sagenb/issues/detail?id=89](http://code.google.com/p/sagenb/issues/detail?id=89)


---

Comment by jdemeyer created at 2012-02-06 16:41:23

Changing status from closed to new.


---

Comment by jdemeyer created at 2012-02-06 16:41:23

Apologies, this is actually independent of the notebook.


---

Comment by jdemeyer created at 2012-02-06 16:41:23

Resolution changed from invalid to 


---

Comment by jdemeyer created at 2012-02-06 16:41:23

Changing component from notebook to interact.


---

Comment by jdemeyer created at 2012-02-06 16:41:28

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-02-06 16:41:53

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-07 13:20:52

Resolution: fixed


---

Comment by aranc created at 2012-02-09 14:24:21

i think there is a minor typo in the docstring line 264

missing word "up": Using the debugger you can move <up> and down the stack frame and 

--

i'm not sure what is the preferred convention for fixing typos, i can make a patch for this isolated line.


---

Comment by was created at 2012-02-13 15:40:31

Replying to [comment:29 aranc]:
> i think there is a minor typo in the docstring line 264
> 
> missing word "up": Using the debugger you can move <up> and down the stack frame and 
> 
> --
> 
> i'm not sure what is the preferred convention for fixing typos, i can make a patch for this isolated line.

See #12506.  Please review!
