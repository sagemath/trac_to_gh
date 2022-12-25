# Issue 6255: update doc system to jsmath and improve build system (parallel doc builds)

archive/issues_006255.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @mwhansen @craigcitro\n\nKeywords: documentation build sphinx parallel\n\nThis is a reminder ticket for mhansen.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6255\n\n",
    "closed_at": "2013-08-13T08:41:09Z",
    "created_at": "2009-06-10T00:32:33Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update doc system to jsmath and improve build system (parallel doc builds)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6255",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @mwhansen

CC:  @mwhansen @craigcitro

Keywords: documentation build sphinx parallel

This is a reminder ticket for mhansen.

Issue created by migration from https://trac.sagemath.org/ticket/6255





---

archive/issue_comments_049862.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-10T00:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49862",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049863.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-06-10T00:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49863",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_049864.json:
```json
{
    "body": "Please see #6495 for a tentative approach to parallel doc builds",
    "created_at": "2009-11-29T20:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49864",
    "user": "https://github.com/qed777"
}
```

Please see #6495 for a tentative approach to parallel doc builds



---

archive/issue_comments_049865.json:
```json
{
    "body": "I made an attempt to have parallel doc build. It seems that I have it for the **write** part of the doc generation process. Here is the diff\n\n```diff\ndiff --git a/builders/__init__.py b/builders/__init__.py\n--- a/builders/__init__.py\n+++ b/builders/__init__.py\n@@ -286,14 +286,27 @@ class Builder(object):\n         # write target files\n         warnings = []\n         self.env.set_warnfunc(lambda *args: warnings.append(args))\n+        #for docname in self.status_iterator(\n+        #    sorted(docnames), 'writing output... ', darkgreen, len(docnames)):\n+        #    doctree = self.env.get_and_resolve_doctree(docname, self)\n+        #    self.write_doc(docname, doctree)\n+        from sage.parallel.decorate import parallel\n+        import itertools\n+        worker = parallel('fork')(self.write_doc_parallel_worker)\n+        pariter = itertools.imap(lambda x:x[1], worker(sorted(docnames)))\n         for docname in self.status_iterator(\n-            sorted(docnames), 'writing output... ', darkgreen, len(docnames)):\n-            doctree = self.env.get_and_resolve_doctree(docname, self)\n-            self.write_doc(docname, doctree)\n+            pariter, 'writing output... ', darkgreen, len(docnames)):\n+            # done in the iterator !!!\n+            pass\n         for warning in warnings:\n             self.warn(*warning)\n         self.env.set_warnfunc(self.warn)\n \n+    def write_doc_parallel_worker(self, docname):\n+        doctree = self.env.get_and_resolve_doctree(docname, self)\n+        self.write_doc(docname, doctree)\n+        return docname\n+\n     def prepare_writing(self, docnames):\n         raise NotImplementedError\n``` \n\nThe read part could be more tricky but it doesn't seems unfeasible. Note that I may be dreaming here.",
    "created_at": "2012-04-20T22:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49865",
    "user": "https://github.com/hivert"
}
```

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
``` 

The read part could be more tricky but it doesn't seems unfeasible. Note that I may be dreaming here.



---

archive/issue_comments_049866.json:
```json
{
    "body": "Experimental timing patch",
    "created_at": "2012-04-21T15:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49866",
    "user": "https://github.com/hivert"
}
```

Experimental timing patch



---

archive/issue_comments_049867.json:
```json
{
    "body": "Attachment [timing.patch](tarball://root/attachments/some-uuid/ticket6255/timing.patch) by @hivert created at 2012-04-21 16:00:24\n\nExperimental parallel doc output patch",
    "created_at": "2012-04-21T16:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49867",
    "user": "https://github.com/hivert"
}
```

Attachment [timing.patch](tarball://root/attachments/some-uuid/ticket6255/timing.patch) by @hivert created at 2012-04-21 16:00:24

Experimental parallel doc output patch



---

archive/issue_comments_049868.json:
```json
{
    "body": "Attachment [paral.patch](tarball://root/attachments/some-uuid/ticket6255/paral.patch) by @hivert created at 2012-04-21 16:09:56\n\nHi there,\n\nI just attached two patches. They need to be applied in\n\n```\n$SAGE_ROOT/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/\n```\n(I didn't regenerate a spkg yet). Those two packages are very experimental and\nthey certainly break a lot of things. The goal of `timing.patch` is to\nimprove Sphinx timning and progress report. The second one uses\n``@`parallel` to parallelize the writing part of the doc generation. This is\nvery raw and could certainly be optimized using Pool, Queue and the\nlike. Still the improvement is allready here:\nOn a intel i7 8 multithreaded core:\n- serie:\n\n```\nreading sources...  Elapsed time = 385.334967136\nwriting output...  Elapsed time = 1903.10733795\n```\n- parallel:\n\n```\nreading sources...  Elapsed time = 418.675282001\nwriting output...  Elapsed time = 253.907614946\n```\nOn a 24 core server:\n- serie:\n\n```\nreading sources...  Elapsed time = 243.982397079\nwriting output...  Elapsed time = 1366.98643208\n```\n- parallel:\n\n```\nreading sources...  Elapsed time = 243.729380131\nwriting output...  Elapsed time = 176.76424408\n```\n\nFlorent",
    "created_at": "2012-04-21T16:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49868",
    "user": "https://github.com/hivert"
}
```

Attachment [paral.patch](tarball://root/attachments/some-uuid/ticket6255/paral.patch) by @hivert created at 2012-04-21 16:09:56

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

archive/issue_comments_049869.json:
```json
{
    "body": "With a little tunning I managed to have\n\n```\nserie    writing output...  Elapsed time = 1366.98643208\nparallel writing output...  Elapsed time = 106.421586037\n```\nLooks efficient !",
    "created_at": "2012-04-21T20:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49869",
    "user": "https://github.com/hivert"
}
```

With a little tunning I managed to have

```
serie    writing output...  Elapsed time = 1366.98643208
parallel writing output...  Elapsed time = 106.421586037
```
Looks efficient !



---

archive/issue_comments_049870.json:
```json
{
    "body": "This should be closed as a duplicate for #6495.",
    "created_at": "2013-06-28T22:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49870",
    "user": "https://github.com/hivert"
}
```

This should be closed as a duplicate for #6495.



---

archive/issue_comments_049871.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-28T22:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49871",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049872.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-28T22:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49872",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_014650.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-07-21T21:05:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6255#event-14650"
}
```



---

archive/issue_events_014651.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T08:41:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6255#event-14651"
}
```



---

archive/issue_comments_049873.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-08-13T08:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6255#issuecomment-49873",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
