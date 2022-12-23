# Issue 7379: layout interact controls

Issue created by migration from https://trac.sagemath.org/ticket/7379

Original creator: jason

Original creation time: 2009-11-03 09:54:31

Assignee: boothby

CC:  mpatel robert.marik timdumol mhansen was mhampton

A user should be able to specify a layout for interact controls.


---

Comment by jason created at 2009-11-03 09:55:43

Here is a patch to the sagenb directory which allows for the following:


```
@interact(layout=[['a','b'],['c','d']])
def _(a=(1,2),b=(3,10),c=["test","button"],d=x^2+1):
    print a,b,c,d
```



```
diff -r 69309549b229 notebook/interact.py
--- a/notebook/interact.py	Tue Nov 03 03:14:01 2009 -0600
+++ b/notebook/interact.py	Tue Nov 03 03:48:40 2009 -0600
@@ -1795,15 +1795,25 @@
             sage: sagenb.notebook.interact.InteractCanvas([B], 3).render_controls()
             '<table>...'
         """
+        layout = self.__options.get('layout',None)
         tbl_body = ''
-        for c in self.__controls:
-            if c.label() == '':
-                tbl_body += '<tr><td colspan=2>%s</td></tr>\n'%c.render()
-            else:
-                tbl_body += '<tr><td align=right><font color="black">%s&nbsp;</font></td><td>%s</td></tr>\n'%(
-                c.label(), c.render())
+        if layout is None:
+            layout = [[c.var()] for c in self.__controls]
+
+        controls = dict([c.var(), c] for c in self.__controls)
+        for row in layout:
+            tbl_body += '<tr>'
+            for c_name in row:
+                c = controls[c_name]
+                if c.label() == '':
+                    tbl_body += '<td colspan=2>%s</td>\n'%c.render()
+                else:
+                    tbl_body += '<td align=right><font color="black">%s&nbsp;</font></td><td>%s</td>\n'%(c.label(), c.render())
+
+            tbl_body += '</tr>'
+                
         return '<table>%s</table>'%tbl_body
-
+            
     def wrap_in_outside_frame(self, inside):
         """
         Return the entire HTML for the interactive canvas, obtained by
@@ -1907,8 +1917,15 @@
         """
         s = 'interact(%s, "_interact_.recompute(%s)")'%(cell_id, cell_id)
         JavascriptCodeButton.__init__(self, "Update", s)                                     
-        
-def interact(f):
+     
+def interact(*args,**kwds):
+    if len(kwds)==0 and len(args)==1:
+        # call without parentheses
+        return _interact(*args)
+    else:
+        return lambda f: _interact(f, **kwds)
+   
+def _interact(f,**kwds):
     r"""
     Use interact as a decorator to create interactive Sage notebook
     cells with sliders, text boxes, radio buttons, check boxes, and
@@ -2281,7 +2298,9 @@
         i = args.index('auto_update')
         controls[i] = UpdateButton(SAGE_CELL_ID)
 
-    C = InteractCanvas(controls, SAGE_CELL_ID, auto_update=auto_update)
+    layout = kwds.get('layout',None)
+
+    C = InteractCanvas(controls, SAGE_CELL_ID, auto_update=auto_update, layout=layout)
     html(C.render())
 
     def _():
```



---

Attachment

FOR SAGENB REPOSITORY


---

Attachment

FOR SAGE DEVEL REPOSITORY


---

Comment by jason created at 2010-05-13 07:50:32

Two patches are attached: one for sagenb, and one for sage devel repository.  

CCing timdumol (naturally, for the notebook/decorator stuff), and mhansen (for the decorator trickery) and was


---

Comment by jason created at 2010-05-13 07:50:32

Changing status from new to needs_review.


---

Comment by jason created at 2010-05-13 07:54:12

CCing mhampton, who has expressed interest in looking at this patch before.


---

Comment by jason created at 2010-05-13 09:06:41

See #8959 for further extensions of this idea that allow arbitrary HTML in the layout.


---

Comment by jason created at 2010-05-14 07:17:28

The patch at #8959 doesn't quite allow the user to specify arbitrary HTML yet, but does allow the controls to be placed on any of the four sides of the interact.

Please, please review the patch at #8959 after reviewing this patch.  The patch there extends the functionality of the patch here, and should be easy to review after you've looked at this patch.


---

Comment by mhampton created at 2010-05-15 21:08:16

This is great, thanks very much for working on it.  The only problem I've seen so far is the following doctest failure for the notebook:



```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py"
**********************************************************************
File "/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py", line 2205:
    sage: @interact
    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
        show(factor(x**n - Integer(1)))
Exception raised:
    Traceback (most recent call last):
      File "/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4-x/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_99[9]>", line 2, in <module>
        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/misc/misc.py", line 2632, in my_wrap
        return func(*args)
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py", line 2519, in interact
        html(C.render())
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py", line 2058, in render
        s = "%s%s"%(self.render_controls(), self.render_output())
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py", line 1994, in render_controls
        layout = [[c.var()] for c in self.__controls]
    AttributeError: 'UpdateButton' object has no attribute 'var'

```


I'll try to do a little more testing and look at #8959 this weekend.


---

Comment by jason created at 2010-05-15 21:31:26

mhampton: that's a corner case in the `@`interact functionality (a magic parameter).  I see two possible fixes: fix `@`interact to make this not a corner case (i.e., not a magic parameter), or move the auto_update switch into the `@`interact arguments:


```
@interact(auto_update=False)
def _(...)
    ...
```



---

Comment by jason created at 2010-05-15 22:03:00

The reason auto_update was included in the function arguments, rather than the `@`interact arguments, is given here: http://groups.google.com/group/sage-devel/browse_thread/thread/9ff935e0d6a729b3/b295d52d195ac9ec?lnk=gst&q=interact#b295d52d195ac9ec

However, with this patch is a decorator that transparently and easily takes care of the objection.  Are there any objections now to moving the auto_update argument up to the `@`interact decorator (other than backwards compatibility)?

Mike? William? You guys were the ones that objected to `@`interact(auto_update=False) in the thread listed above.


---

Comment by mhansen created at 2010-05-15 22:07:56

I think it's fine with the decorator defaults patch.


---

Comment by jason created at 2010-05-15 22:17:25

I just posted a long message to sage-notebook for a vote.


---

Comment by jason created at 2010-05-16 04:46:17

I'm posting a fix to the auto_update doctest that Marshall mentioned on #8959.


---

Comment by jason created at 2010-05-16 04:46:17

Changing assignee from boothby to jason.


---

Comment by mhampton created at 2010-05-16 14:29:19

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-05-16 14:29:19

OK, with the fix in 8959 I see no problems with this.  I've tested a bunch of interacts from the wiki, and there seem to be no back-compatibility issues.  So I think I can give this a positive review.


---

Comment by timdumol created at 2010-07-07 14:31:15

The patch causes the followinger doctest error:


```
File "/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2209:
    sage: @interact
    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
        show(factor(x**n - Integer(1)))
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/opt/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/opt/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_99[9]>", line 2, in <module>
        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
      File "/opt/sage/local/lib/python/site-packages/sage/misc/misc.py", line 2666, in my_wrap
        return func(*args)
      File "/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2523, in interact
        html(C.render())
      File "/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2062, in render
        s = "%s%s"%(self.render_controls(), self.render_output())
      File "/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 1998, in render_controls
        layout = [[c.var()] for c in self.__controls]
    AttributeError: 'UpdateButton' object has no attribute 'var'
```


Marking this as "needs work."


---

Comment by timdumol created at 2010-07-07 14:31:15

Changing status from positive_review to needs_work.


---

Comment by jason created at 2010-07-07 14:43:57

Changing status from needs_work to needs_info.


---

Comment by jason created at 2010-07-07 14:43:57

In the two comments above yours, it says that the doctest is fixed in #8959.  Did you apply that patch as well?


---

Comment by timdumol created at 2010-07-07 14:51:13

I didn't notice the comment. Sorry! The doctests do pass now. Marking as positive review (we really do need to add a pathway from needs_info to positive review).


---

Comment by timdumol created at 2010-07-07 14:51:13

Changing status from needs_info to needs_review.


---

Comment by timdumol created at 2010-07-07 14:51:37

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-07-11 06:05:46

Resolution: fixed


---

Comment by rlm created at 2010-07-12 08:13:34

Merged the sage-devel patch in sage-4.5.rc1.
