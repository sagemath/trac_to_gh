# Issue 6158: upgrading sphix problem: any upgrade to sage-4.0 ends this way

archive/issues_006158.json:
```json
{
    "body": "Assignee: tba\n\n\n```\nsphinx-build -b html -d /usr/local/sage/devel/sage/doc/output/doctrees/en/tutorial   .  /usr/local/sage/devel/sage/doc/output/html/en/tutorial\nSphinx v0.5.1, building html\nloading pickled environment... done\nbuilding [html]: targets for 0 source files that are out of date\nupdating environment: 0 added, 0 changed, 0 removed\nno targets are out of date.\nBuild finished.  The built documents can be found in /usr/local/sage/devel/sage/doc/output/html/en/tutorial\nTraceback (most recent call last):\n  File \"/usr/local/sage/devel/sage/doc/common/builder.py\", line 667, in <module>\n    getattr(get_builder(name), type)()\n  File \"/usr/local/sage/devel/sage/doc/common/builder.py\", line 258, in _wrapper\n    getattr(get_builder(document), name)(*args, **kwds)\n  File \"/usr/local/sage/devel/sage/doc/common/builder.py\", line 348, in _wrapper\n    for module_name in self.get_modified_modules():\n  File \"/usr/local/sage/devel/sage/doc/common/builder.py\", line 415, in get_modified_modules\n    added, changed, removed = env.get_outdated_files(False)\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py\", line 400, in get_outdated_files\n    newmtime = path.getmtime(self.doc2path(docname))\n  File \"/usr/local/sage/local/lib/python2.5/posixpath.py\", line 143, in getmtime\n    return os.stat(filename).st_mtime\nOSError: [Errno 2] No such file or directory: '/usr/local/sage/devel/sage-main/doc/en/reference/rings_padic.rst'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6158\n\n",
    "created_at": "2009-05-30T15:37:10Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "upgrading sphix problem: any upgrade to sage-4.0 ends this way",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6158",
    "user": "was"
}
```
Assignee: tba


```
sphinx-build -b html -d /usr/local/sage/devel/sage/doc/output/doctrees/en/tutorial   .  /usr/local/sage/devel/sage/doc/output/html/en/tutorial
Sphinx v0.5.1, building html
loading pickled environment... done
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
no targets are out of date.
Build finished.  The built documents can be found in /usr/local/sage/devel/sage/doc/output/html/en/tutorial
Traceback (most recent call last):
  File "/usr/local/sage/devel/sage/doc/common/builder.py", line 667, in <module>
    getattr(get_builder(name), type)()
  File "/usr/local/sage/devel/sage/doc/common/builder.py", line 258, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/usr/local/sage/devel/sage/doc/common/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/usr/local/sage/devel/sage/doc/common/builder.py", line 415, in get_modified_modules
    added, changed, removed = env.get_outdated_files(False)
  File "/usr/local/sage/local/lib/python2.5/site-packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py", line 400, in get_outdated_files
    newmtime = path.getmtime(self.doc2path(docname))
  File "/usr/local/sage/local/lib/python2.5/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: '/usr/local/sage/devel/sage-main/doc/en/reference/rings_padic.rst'
```



Issue created by migration from https://trac.sagemath.org/ticket/6158





---

archive/issue_comments_049124.json:
```json
{
    "body": "A temporary workaround is to just do \n\n```\ntouch /usr/local/sage/devel/sage-main/doc/en/reference/rings_padic.rst\n```\n\n(or whatever the path is to rings_padic.rst) and then things continue fine.",
    "created_at": "2009-05-30T17:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49124",
    "user": "was"
}
```

A temporary workaround is to just do 

```
touch /usr/local/sage/devel/sage-main/doc/en/reference/rings_padic.rst
```

(or whatever the path is to rings_padic.rst) and then things continue fine.



---

archive/issue_comments_049125.json:
```json
{
    "body": "I think we just need to remove the existing output directory before building the documentation.",
    "created_at": "2009-05-31T19:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49125",
    "user": "mhansen"
}
```

I think we just need to remove the existing output directory before building the documentation.



---

archive/issue_comments_049126.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-31T19:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49126",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049127.json:
```json
{
    "body": "Changing assignee from tba to mhansen.",
    "created_at": "2009-05-31T19:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49127",
    "user": "mhansen"
}
```

Changing assignee from tba to mhansen.



---

archive/issue_comments_049128.json:
```json
{
    "body": "Also, we should remove all of the autogenerated files in devel/sage/doc/en/reference/sage .",
    "created_at": "2009-05-31T19:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49128",
    "user": "mhansen"
}
```

Also, we should remove all of the autogenerated files in devel/sage/doc/en/reference/sage .



---

archive/issue_comments_049129.json:
```json
{
    "body": "These changes should do it:\n\n\n```\n--- install_old\t2009-05-31 12:40:34.000000000 -0700\n+++ install\t2009-05-31 12:40:37.000000000 -0700\n@@ -356,6 +356,11 @@\n # NOW do the actual build\n \n time make -f standard/deps $1\n+\n+\n+#Build the documentation\n+rm -rf \"$SAGE_ROOT\"/devel/sage-main/doc/output/doctrees\n+rm -rf \"$SAGE_ROOT\"/devel/sage-main/doc/en/reference/sage/*\n \"$SAGE_ROOT\"/sage -docbuild --jsmath all html\n \n if [ \"$1\" = \"all\" -a $? = 0 ]; then\n```\n",
    "created_at": "2009-05-31T19:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49129",
    "user": "mhansen"
}
```

These changes should do it:


```
--- install_old	2009-05-31 12:40:34.000000000 -0700
+++ install	2009-05-31 12:40:37.000000000 -0700
@@ -356,6 +356,11 @@
 # NOW do the actual build
 
 time make -f standard/deps $1
+
+
+#Build the documentation
+rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
+rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
 "$SAGE_ROOT"/sage -docbuild --jsmath all html
 
 if [ "$1" = "all" -a $? = 0 ]; then
```




---

archive/issue_comments_049130.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T00:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49130",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049131.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T00:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6158#issuecomment-49131",
    "user": "mhansen"
}
```

Merged in 4.0.1.alpha0.
