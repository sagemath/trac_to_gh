# Issue 7379: layout interact controls

archive/issues_007379.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777 @robert-marik @TimDumol @mwhansen @williamstein mhampton\n\nA user should be able to specify a layout for interact controls.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7379\n\n",
    "created_at": "2009-11-03T09:54:31Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "layout interact controls",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7379",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @qed777 @robert-marik @TimDumol @mwhansen @williamstein mhampton

A user should be able to specify a layout for interact controls.

Issue created by migration from https://trac.sagemath.org/ticket/7379





---

archive/issue_comments_061938.json:
```json
{
    "body": "Here is a patch to the sagenb directory which allows for the following:\n\n```\n@interact(layout=[['a','b'],['c','d']])\ndef _(a=(1,2),b=(3,10),c=[\"test\",\"button\"],d=x^2+1):\n    print a,b,c,d\n```\n\n```\ndiff -r 69309549b229 notebook/interact.py\n--- a/notebook/interact.py\tTue Nov 03 03:14:01 2009 -0600\n+++ b/notebook/interact.py\tTue Nov 03 03:48:40 2009 -0600\n@@ -1795,15 +1795,25 @@\n             sage: sagenb.notebook.interact.InteractCanvas([B], 3).render_controls()\n             '<table>...'\n         \"\"\"\n+        layout = self.__options.get('layout',None)\n         tbl_body = ''\n-        for c in self.__controls:\n-            if c.label() == '':\n-                tbl_body += '<tr><td colspan=2>%s</td></tr>\\n'%c.render()\n-            else:\n-                tbl_body += '<tr><td align=right><font color=\"black\">%s&nbsp;</font></td><td>%s</td></tr>\\n'%(\n-                c.label(), c.render())\n+        if layout is None:\n+            layout = [[c.var()] for c in self.__controls]\n+\n+        controls = dict([c.var(), c] for c in self.__controls)\n+        for row in layout:\n+            tbl_body += '<tr>'\n+            for c_name in row:\n+                c = controls[c_name]\n+                if c.label() == '':\n+                    tbl_body += '<td colspan=2>%s</td>\\n'%c.render()\n+                else:\n+                    tbl_body += '<td align=right><font color=\"black\">%s&nbsp;</font></td><td>%s</td>\\n'%(c.label(), c.render())\n+\n+            tbl_body += '</tr>'\n+                \n         return '<table>%s</table>'%tbl_body\n-\n+            \n     def wrap_in_outside_frame(self, inside):\n         \"\"\"\n         Return the entire HTML for the interactive canvas, obtained by\n@@ -1907,8 +1917,15 @@\n         \"\"\"\n         s = 'interact(%s, \"_interact_.recompute(%s)\")'%(cell_id, cell_id)\n         JavascriptCodeButton.__init__(self, \"Update\", s)                                     \n-        \n-def interact(f):\n+     \n+def interact(*args,**kwds):\n+    if len(kwds)==0 and len(args)==1:\n+        # call without parentheses\n+        return _interact(*args)\n+    else:\n+        return lambda f: _interact(f, **kwds)\n+   \n+def _interact(f,**kwds):\n     r\"\"\"\n     Use interact as a decorator to create interactive Sage notebook\n     cells with sliders, text boxes, radio buttons, check boxes, and\n@@ -2281,7 +2298,9 @@\n         i = args.index('auto_update')\n         controls[i] = UpdateButton(SAGE_CELL_ID)\n \n-    C = InteractCanvas(controls, SAGE_CELL_ID, auto_update=auto_update)\n+    layout = kwds.get('layout',None)\n+\n+    C = InteractCanvas(controls, SAGE_CELL_ID, auto_update=auto_update, layout=layout)\n     html(C.render())\n \n     def _():\n```",
    "created_at": "2009-11-03T09:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61938",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_061939.json:
```json
{
    "body": "Attachment [trac-7379-interact-table-layout.patch](tarball://root/attachments/some-uuid/ticket7379/trac-7379-interact-table-layout.patch) by @jasongrout created at 2010-05-13 07:47:10\n\nFOR SAGENB REPOSITORY",
    "created_at": "2010-05-13T07:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61939",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7379-interact-table-layout.patch](tarball://root/attachments/some-uuid/ticket7379/trac-7379-interact-table-layout.patch) by @jasongrout created at 2010-05-13 07:47:10

FOR SAGENB REPOSITORY



---

archive/issue_comments_061940.json:
```json
{
    "body": "Attachment [trac-7379-decorator-defaults.patch](tarball://root/attachments/some-uuid/ticket7379/trac-7379-decorator-defaults.patch) by @jasongrout created at 2010-05-13 07:48:51\n\nFOR SAGE DEVEL REPOSITORY",
    "created_at": "2010-05-13T07:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61940",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7379-decorator-defaults.patch](tarball://root/attachments/some-uuid/ticket7379/trac-7379-decorator-defaults.patch) by @jasongrout created at 2010-05-13 07:48:51

FOR SAGE DEVEL REPOSITORY



---

archive/issue_comments_061941.json:
```json
{
    "body": "Two patches are attached: one for sagenb, and one for sage devel repository.  \n\nCCing timdumol (naturally, for the notebook/decorator stuff), and mhansen (for the decorator trickery) and was",
    "created_at": "2010-05-13T07:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61941",
    "user": "https://github.com/jasongrout"
}
```

Two patches are attached: one for sagenb, and one for sage devel repository.  

CCing timdumol (naturally, for the notebook/decorator stuff), and mhansen (for the decorator trickery) and was



---

archive/issue_comments_061942.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-13T07:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61942",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061943.json:
```json
{
    "body": "CCing mhampton, who has expressed interest in looking at this patch before.",
    "created_at": "2010-05-13T07:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61943",
    "user": "https://github.com/jasongrout"
}
```

CCing mhampton, who has expressed interest in looking at this patch before.



---

archive/issue_comments_061944.json:
```json
{
    "body": "See #8959 for further extensions of this idea that allow arbitrary HTML in the layout.",
    "created_at": "2010-05-13T09:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61944",
    "user": "https://github.com/jasongrout"
}
```

See #8959 for further extensions of this idea that allow arbitrary HTML in the layout.



---

archive/issue_comments_061945.json:
```json
{
    "body": "The patch at #8959 doesn't quite allow the user to specify arbitrary HTML yet, but does allow the controls to be placed on any of the four sides of the interact.\n\nPlease, please review the patch at #8959 after reviewing this patch.  The patch there extends the functionality of the patch here, and should be easy to review after you've looked at this patch.",
    "created_at": "2010-05-14T07:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61945",
    "user": "https://github.com/jasongrout"
}
```

The patch at #8959 doesn't quite allow the user to specify arbitrary HTML yet, but does allow the controls to be placed on any of the four sides of the interact.

Please, please review the patch at #8959 after reviewing this patch.  The patch there extends the functionality of the patch here, and should be easy to review after you've looked at this patch.



---

archive/issue_comments_061946.json:
```json
{
    "body": "This is great, thanks very much for working on it.  The only problem I've seen so far is the following doctest failure for the notebook:\n\n\n```\nsage -t  \"local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py\"\n**********************************************************************\nFile \"/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py\", line 2205:\n    sage: @interact\n    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):\n        show(factor(x**n - Integer(1)))\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mh/sagestuff/sage-4-x/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_99[9]>\", line 2, in <module>\n        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/misc/misc.py\", line 2632, in my_wrap\n        return func(*args)\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py\", line 2519, in interact\n        html(C.render())\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py\", line 2058, in render\n        s = \"%s%s\"%(self.render_controls(), self.render_output())\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/interact.py\", line 1994, in render_controls\n        layout = [[c.var()] for c in self.__controls]\n    AttributeError: 'UpdateButton' object has no attribute 'var'\n\n```\n\nI'll try to do a little more testing and look at #8959 this weekend.",
    "created_at": "2010-05-15T21:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61946",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

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

archive/issue_comments_061947.json:
```json
{
    "body": "mhampton: that's a corner case in the `@`interact functionality (a magic parameter).  I see two possible fixes: fix `@`interact to make this not a corner case (i.e., not a magic parameter), or move the auto_update switch into the `@`interact arguments:\n\n```\n@interact(auto_update=False)\ndef _(...)\n    ...\n```",
    "created_at": "2010-05-15T21:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61947",
    "user": "https://github.com/jasongrout"
}
```

mhampton: that's a corner case in the `@`interact functionality (a magic parameter).  I see two possible fixes: fix `@`interact to make this not a corner case (i.e., not a magic parameter), or move the auto_update switch into the `@`interact arguments:

```
@interact(auto_update=False)
def _(...)
    ...
```



---

archive/issue_comments_061948.json:
```json
{
    "body": "The reason auto_update was included in the function arguments, rather than the `@`interact arguments, is given here: http://groups.google.com/group/sage-devel/browse_thread/thread/9ff935e0d6a729b3/b295d52d195ac9ec?lnk=gst&q=interact#b295d52d195ac9ec\n\nHowever, with this patch is a decorator that transparently and easily takes care of the objection.  Are there any objections now to moving the auto_update argument up to the `@`interact decorator (other than backwards compatibility)?\n\nMike? William? You guys were the ones that objected to `@`interact(auto_update=False) in the thread listed above.",
    "created_at": "2010-05-15T22:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61948",
    "user": "https://github.com/jasongrout"
}
```

The reason auto_update was included in the function arguments, rather than the `@`interact arguments, is given here: http://groups.google.com/group/sage-devel/browse_thread/thread/9ff935e0d6a729b3/b295d52d195ac9ec?lnk=gst&q=interact#b295d52d195ac9ec

However, with this patch is a decorator that transparently and easily takes care of the objection.  Are there any objections now to moving the auto_update argument up to the `@`interact decorator (other than backwards compatibility)?

Mike? William? You guys were the ones that objected to `@`interact(auto_update=False) in the thread listed above.



---

archive/issue_comments_061949.json:
```json
{
    "body": "I think it's fine with the decorator defaults patch.",
    "created_at": "2010-05-15T22:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61949",
    "user": "https://github.com/mwhansen"
}
```

I think it's fine with the decorator defaults patch.



---

archive/issue_comments_061950.json:
```json
{
    "body": "I just posted a long message to sage-notebook for a vote.",
    "created_at": "2010-05-15T22:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61950",
    "user": "https://github.com/jasongrout"
}
```

I just posted a long message to sage-notebook for a vote.



---

archive/issue_comments_061951.json:
```json
{
    "body": "I'm posting a fix to the auto_update doctest that Marshall mentioned on #8959.",
    "created_at": "2010-05-16T04:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61951",
    "user": "https://github.com/jasongrout"
}
```

I'm posting a fix to the auto_update doctest that Marshall mentioned on #8959.



---

archive/issue_comments_061952.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2010-05-16T04:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61952",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_061953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T14:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61953",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061954.json:
```json
{
    "body": "OK, with the fix in 8959 I see no problems with this.  I've tested a bunch of interacts from the wiki, and there seem to be no back-compatibility issues.  So I think I can give this a positive review.",
    "created_at": "2010-05-16T14:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61954",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, with the fix in 8959 I see no problems with this.  I've tested a bunch of interacts from the wiki, and there seem to be no back-compatibility issues.  So I think I can give this a positive review.



---

archive/issue_comments_061955.json:
```json
{
    "body": "The patch causes the followinger doctest error:\n\n```\nFile \"/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 2209:\n    sage: @interact\n    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):\n        show(factor(x**n - Integer(1)))\nException raised:\n    Traceback (most recent call last):\n      File \"/opt/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/opt/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/opt/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_99[9]>\", line 2, in <module>\n        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):\n      File \"/opt/sage/local/lib/python/site-packages/sage/misc/misc.py\", line 2666, in my_wrap\n        return func(*args)\n      File \"/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 2523, in interact\n        html(C.render())\n      File \"/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 2062, in render\n        s = \"%s%s\"%(self.render_controls(), self.render_output())\n      File \"/opt/sage/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 1998, in render_controls\n        layout = [[c.var()] for c in self.__controls]\n    AttributeError: 'UpdateButton' object has no attribute 'var'\n```\n\nMarking this as \"needs work.\"",
    "created_at": "2010-07-07T14:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61955",
    "user": "https://github.com/TimDumol"
}
```

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

archive/issue_comments_061956.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-07T14:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61956",
    "user": "https://github.com/TimDumol"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061957.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-07-07T14:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61957",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_061958.json:
```json
{
    "body": "In the two comments above yours, it says that the doctest is fixed in #8959.  Did you apply that patch as well?",
    "created_at": "2010-07-07T14:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61958",
    "user": "https://github.com/jasongrout"
}
```

In the two comments above yours, it says that the doctest is fixed in #8959.  Did you apply that patch as well?



---

archive/issue_comments_061959.json:
```json
{
    "body": "I didn't notice the comment. Sorry! The doctests do pass now. Marking as positive review (we really do need to add a pathway from needs_info to positive review).",
    "created_at": "2010-07-07T14:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61959",
    "user": "https://github.com/TimDumol"
}
```

I didn't notice the comment. Sorry! The doctests do pass now. Marking as positive review (we really do need to add a pathway from needs_info to positive review).



---

archive/issue_comments_061960.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-07T14:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61960",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_061961.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-07T14:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61961",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T06:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61962",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_017446.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-07-11T06:05:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7379#event-17446"
}
```



---

archive/issue_comments_061963.json:
```json
{
    "body": "Merged the sage-devel patch in sage-4.5.rc1.",
    "created_at": "2010-07-12T08:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7379#issuecomment-61963",
    "user": "https://github.com/rlmill"
}
```

Merged the sage-devel patch in sage-4.5.rc1.
