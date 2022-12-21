# Issue 6848: [with patch, needs review] "Definition:" messed up in notebook and command line in cython code

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-08-30 21:36:25

Assignee: jhpalmieri

Quoted from #5726:

```
sage: RDF.random_element?
...
Definition: RDF.random_element(min='-1', max='1')
```

Notice the stupid quotes around -1 and 1, which are very confusing!

Also, from the command line, if you type `RDF.random_element?`, you don't see a "Definition" line at all.  This patch fixes both issues: the first by using `eval(argument)`, as suggested by timdumol at #5726, and the second by setting 

```
IPython.OInspect.getargspec = sageinspect.sage_getargspec
```

in sage.misc.interpreter.  Note that `sage_getargspec` is a modified version of `getargspec` to start with, so this modification should work in general.  (It was already in use, essentially, in the notebook -- introspection in the notebook calls `sage_getdef`, which in turn calls `sage_getargspec`.  See the function `docstring` in `sage.server.support`.)



---

Attachment

depends on patch at #5726


---

Comment by mhansen created at 2009-09-08 23:01:06

Looks good to me.


---

Comment by mvngu created at 2009-09-09 10:09:39

Resolution: fixed
