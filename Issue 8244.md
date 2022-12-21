# Issue 8244: Annoying warnings when building the HTML reference manual

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-11 21:43:46

Assignee: mvngu

CC:  mvngu jhpalmieri mhansen craigcitro robertwb

Let's fix or suppress these, so that it's easier to identify new problems.

See the attachment.


---

Attachment

HTML reference manual docbuild warnings for 4.3.3.alpha0.  Not a patch.


---

Comment by mpatel created at 2010-02-11 21:49:06

Should we follow #6419 for the nested classes?  We could use that approach for

```
sagenb.notebook.twist.UserToplevel.userchild_download_worksheets.zip
```



---

Comment by jhpalmieri created at 2010-02-11 22:40:49

I've looked at these a bit, but I have no idea how to fix them.   Oh, except for

```
plot/plot3d/base.rst:6: (WARNING/2) error while formatting signature for sage.plot.plot3d.base.Graphics3d.export_jmol: Could not parse cython argspec
```

This is because `_sage_getargspec_cython` in sage.misc.sageinspect is a little broken, and fixing it might be lot of work: right now it parses arguments to Cython function by doing basic string and regular expression manipulations, in particular separating arguments by splitting the line on commas.  The function `export_jmol` has argspec

```
    def export_jmol(self, filename='jmol_shape.jmol', force_reload=False,
                    zoom=100, spin=False, background=(1,1,1), stereo=False,
                    mesh=False, dots=False,
                    perspective_depth = True,
                    orientation = (-764,-346,-545,76.39), **ignored_kwds):
```

and so splitting at commas doesn't work.  To do this right, we either need to write a good parser (which deals with nested lists, tuples, etc.), or perhaps change the whole way we deal with argspecs for Cython functions; for example, just read off the entire string of all the arguments and pass that to the appropriate function, instead of trying to break it into arguments, default values, etc.  This is a pretty rare problem and it looks annoying to deal with, so I haven't felt like putting any time into it.

mhansen and craigcitro: any comments or ideas?


---

Comment by mvngu created at 2010-02-12 03:45:39

Ticket #8243 is a duplicate of this one.


---

Comment by mhansen created at 2010-02-12 20:07:39

Well, Cython itself has to parse such a thing, but I don't know how easy it is go get the data we need out of Cython.  Maybe Robert might have an idea?


---

Comment by mpatel created at 2010-02-13 14:48:34

I'm not very familiar with [ASTs](http://en.wikipedia.org/wiki/Abstract_syntax_tree) (or [ast](http://docs.python.org/library/ast.html)), but with

```python
import ast
import inspect
import sage.misc.sageinspect as sms

class SageVisitor(ast.NodeVisitor):
    def visit_Name(self, node):
        what = node.id
        if what == 'None':
            return None
        elif what == 'True':
            return True
        elif what == 'False':
            return False
        return node.id

    def visit_Num(self, node):
        return node.n

    def visit_Str(self, node):
        return node.s

    def visit_List(self, node):
        t = []
        for n in node.elts:
            t.append(self.visit(n))
        return t

    def visit_Tuple(self, node):
        t = []
        for n in node.elts:
            t.append(self.visit(n))
        return tuple(t)

    def visit_Dict(self, node):
        d = {}
        for k, v in zip(node.keys, node.values):
            d[self.visit(k)] = self.visit(v)
        return d


def getargspec_via_ast(source):
    if not isinstance(source, basestring):
        source = sms.sage_getsource(source)

    ast_args = ast.parse(source.lstrip()).body[0].args

    args = []
    defaults = []

    for a in ast_args.args:
        args.append(SageVisitor().visit(a))

    for d in ast_args.defaults:
        defaults.append(SageVisitor().visit(d))

    return inspect.ArgSpec(args, ast_args.vararg, ast_args.kwarg,
                           tuple(defaults) if defaults else None)
```

I get

```python
sage: inspect.getargspec(factor) == getargspec_via_ast(factor)
True
sage: getargspec_via_ast(sage.plot.plot3d.base.Graphics3d.export_jmol)
ArgSpec(args=['self', 'filename', 'force_reload', 'zoom', 'spin', 'background', 'stereo', 'mesh', 'dots', 'perspective_depth', 'orientation'], varargs=None, keywords='ignored_kwds', defaults=('jmol_shape.jmol', False, 100, False, (1, 1, 1), False, False, False, True, (-764, -346, -545, 76.390000000000001)))
```

Maybe we can use this as a last resort?  I think we'd first need to remove Cython-specific constructs.


---

Comment by mpatel created at 2010-02-14 19:34:01

It seems that nearly all of the warnings are from Cython files and that we really need a more robust analogue of `inspect.getargspec` for Cython source.

For the `ElementMethods`, `ParentMethods`, `userchild_download_worksheets.zip` warnings, we can expand the autodoc skip method handler.

The other warnings seem to be reST formatting problems, but I'm not sure about

```
<autodoc>:0: (ERROR/3) Unexpected indentation.
<autodoc>:0: (ERROR/3) Unexpected indentation.
```



---

Comment by mpatel created at 2010-02-15 13:20:16

Can autodoc [handle nested classes](http://groups.google.com/groups/search?q=group:sphinx-dev+nested+classes&btnG=Search&sitesearch=)?


---

Comment by jhpalmieri created at 2010-02-17 04:41:18

Replying to [comment:6 mpatel]:
> It seems that nearly all of the warnings are from Cython files and that we really need a more robust analogue of `inspect.getargspec` for Cython source.

Or for now, a way to suppress all of the error message.

I'm not sure about the `<autodoc>...` errors, either.


---

Comment by mpatel created at 2010-02-19 01:16:58

The following seems to remove the "arg is not a Python function" warnings:

```diff
--- autodoc.py.origg    2010-02-18 15:51:38.000000000 -0800
+++ autodoc.py  2010-02-18 17:03:58.000000000 -0800
`@``@` -1005,7 +1005,16 `@``@` class MethodDocumenter(ClassLevelDocumen
             else:
                 return None
         else:
-            argspec = inspect.getargspec(self.object)
+            # The check above misses ordinary Python methods in Cython
+            # files.
+            try:
+                argspec = inspect.getargspec(self.object)
+            except TypeError:
+                if (inspect.ismethod(self.object) and 
+                    self.env.config.autodoc_builtin_argspec):
+                    argspec = self.env.config.autodoc_builtin_argspec(self.object.im_func)
+                else:
+                    return None
         if argspec[0] and argspec[0][0] in ('cls', 'self'):
             del argspec[0][0]
         return inspect.formatargspec(*argspec)
```

Should we copy `autodoc.py` to `SAGE_DOC/common/sage_autodoc.py`, make all of our changes in the latter, and add the custom extension in `SAGE_DOC/common/conf.py`?


---

Comment by mpatel created at 2010-02-19 03:26:34

Handle `*.next` methods.  sage repo.


---

Attachment

The attached patch should remove the warnings that end in

```
.next: arg is not a module, class, method, function, traceback, frame, or code object
```



---

Comment by mpatel created at 2010-02-19 03:51:50

With the patches, I get about 10 non-reST warnings.  I think we can skip

  `sagenb.notebook.twist.UserToplevel.userchild_download_worksheets.zip`

in `conf.py`.  We should coordinate the spkg updates.


---

Comment by jhpalmieri created at 2010-02-19 21:15:32

This is great progress.  By the way, I know how to fix the warnings for `sage.misc.sagedoc.process_dollars`: we shouldn't run `process_dollars` on this function.  That is, change the first line of `process_dollars` in conf.py from

```
    if len(docstringlines) > 0:
```

to

```
    if len(docstringlines) > 0 and name.find("process_dollars") == -1:
```

Similarly for `process_mathtt`.  I've included this change in my patch.

> Should we copy autodoc.py to SAGE_DOC/common/sage_autodoc.py, make all of our changes in the latter, and add the custom extension in SAGE_DOC/common/conf.py?

This is an interesting idea since we're patching it so much.  Then it would be under Sage revision control.  We would just need to keep an eye on it whenever we upgrade Sphinx.  I'm posting a patch which adds it.  Actually, it doesn't add the whole thing, since I got an error when I tried that.  Instead, it does

```
from sphinx.ext.autodoc import *
```

and then it defines `FunctionDocumenter`, `MethodDocumenter`, `setup`, and `ClassDocumenter` (this one isn't patched right now, but it looks like it will be in #7448).


---

Comment by jhpalmieri created at 2010-02-19 21:23:12

My patch also skips `sagenb.notebook.twist.UserToplevel.userchild_download_worksheets.zip`.


---

Attachment

apply on top of other patch


---

Comment by jhpalmieri created at 2010-02-19 22:19:57

Here's one more patch: this fixes one last warning message about sage.misc.process_dollars.


---

Attachment

apply on top of other patches


---

Comment by mpatel created at 2010-02-20 19:45:56

Thanks!  Thanks also for making the extension patch.  To the extent it counts, my review is positive.

I'll rebase #7448.

To the release manager:  Please apply 

```
trac_8244-slot_wrapper_argspec.patch
trac_8244-conf-autodoc.patch
trac_8244-sagedoc.patch
```



---

Comment by jhpalmieri created at 2010-02-20 20:25:17

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-02-20 20:25:30

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-23 03:13:39

Replaces "conf_autodoc" patch.


---

Attachment

I've attached a replacement for the "conf-autodoc" patch that adds all of `autodoc` (as `sage_autodoc`) and, with some redefinition, avoids the `ExtensionError`.

A self-contained `sage_autodoc` should make it less likely that `sage_autodoc` stops working, when we upgrade or test new versions of Sphinx.  (I was just hit by this during experiments with [a development version](http://bitbucket.org/birkenfeld/sphinx/)).

What do you think?


---

Comment by jhpalmieri created at 2010-02-24 21:59:38

Replying to [comment:18 mpatel]:
> I've attached a replacement for the "conf-autodoc" patch that adds all of `autodoc` (as `sage_autodoc`) and, with some redefinition, avoids the `ExtensionError`.
> 
> A self-contained `sage_autodoc` should make it less likely that `sage_autodoc` stops working, when we upgrade or test new versions of Sphinx.  (I was just hit by this during experiments with [a development version](http://bitbucket.org/birkenfeld/sphinx/)).
> 
> What do you think?

Looks good to me.  Still a positive review.


---

Comment by mvngu created at 2010-03-02 22:04:09

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 22:04:09

Merged in this order:

 1. [trac_8244-slot_wrapper_argspec.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8244/trac_8244-slot_wrapper_argspec.patch)
 1. [trac_8244-conf-autodoc.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8244/trac_8244-conf-autodoc.2.patch)
 1. [trac_8244-sagedoc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8244/trac_8244-sagedoc.patch)
