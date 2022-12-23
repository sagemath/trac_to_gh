# Issue 6255: update doc system to latex sphinx and improve build system

Issue created by migration from https://trac.sagemath.org/ticket/6255

Original creator: ncalexan

Original creation time: 2009-06-10 00:32:33

Assignee: tba

CC:  mhansen craigcitro

Keywords: documentation build sphinx parallel

This is a reminder ticket for mhansen.


---

Comment by mhansen created at 2009-06-10 00:36:07

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-10 00:36:07

Changing assignee from tba to mhansen.


---

Comment by mpatel created at 2009-11-29 20:24:32

Please see #6495 for a tentative approach to parallel doc builds


---

Comment by hivert created at 2012-04-20 22:16:54

I made an attempt to have parallel doc build. It seems that I have it for the **write** part of the doc generation process. Here is the diff

```diff
diff --git a/builders/__init__.py b/builders/__init__.py
--- a/builders/__init__.py
+++ b/builders/__init__.py
@@ -286,14 +286,27 @@ class Builder(object):
         # write target files
         warnings = []
         self.env.set_warnfunc(lambda *args: warnings.append(args))
+        #for docname in self.status_iterator(
+        #    sorted(docnames), 'writing output... ', darkgreen, len(docnames)):
+        #    doctree = self.env.get_and_resolve_doctree(docname, self)
+        #    self.write_doc(docname, doctree)
+        from sage.parallel.decorate import parallel
+        import itertools
+        worker = parallel('fork')(self.write_doc_parallel_worker)
+        pariter = itertools.imap(lambda x:x[1], worker(sorted(docnames)))
         for docname in self.status_iterator(
-            sorted(docnames), 'writing output... ', darkgreen, len(docnames)):
-            doctree = self.env.get_and_resolve_doctree(docname, self)
-            self.write_doc(docname, doctree)
+            pariter, 'writing output... ', darkgreen, len(docnames)):
+            # done in the iterator !!!
+            pass
         for warning in warnings:
             self.warn(*warning)
         self.env.set_warnfunc(self.warn)
 
+    def write_doc_parallel_worker(self, docname):
+        doctree = self.env.get_and_resolve_doctree(docname, self)
+        self.write_doc(docname, doctree)
+        return docname
+
     def prepare_writing(self, docnames):
         raise NotImplementedError
}}} 

The read part could be more tricky but it doesn't seems unfeasible. Note that I may be dreaming here.


---

Comment by hivert created at 2012-04-21 15:59:58

Experimental timing patch


---

Attachment

Experimental parallel doc output patch


---

Attachment

Hi there,

I just attached two patches. They need to be applied in

```
$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/
```

(I didn't regenerate a spkg yet). Those two packages are very experimental and
they certainly break a lot of things. The goal of `timing.patch` is to
improve Sphinx timning and progress report. The second one uses
``@`parallel` to parallelize the writing part of the doc generation. This is
very raw and could certainly be optimized using Pool, Queue and the
like. Still the improvement is allready here:
On a intel i7 8 multithreaded core:
- serie:

```
reading sources...  Elapsed time = 385.334967136
writing output...  Elapsed time = 1903.10733795
```

- parallel:

```
reading sources...  Elapsed time = 418.675282001
writing output...  Elapsed time = 253.907614946
```

On a 24 core server:
- serie:

```
reading sources...  Elapsed time = 243.982397079
writing output...  Elapsed time = 1366.98643208
```

- parallel:

```
reading sources...  Elapsed time = 243.729380131
writing output...  Elapsed time = 176.76424408
```


Florent


---

Comment by hivert created at 2012-04-21 20:40:17

With a little tunning I managed to have

```
serie    writing output...  Elapsed time = 1366.98643208
parallel writing output...  Elapsed time = 106.421586037
```

Looks efficient !


---

Comment by hivert created at 2013-06-28 22:04:41

This should be closed as a duplicate for #6495.


---

Comment by hivert created at 2013-06-28 22:04:41

Changing status from new to needs_review.


---

Comment by hivert created at 2013-06-28 22:05:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-13 08:41:09

Resolution: duplicate
