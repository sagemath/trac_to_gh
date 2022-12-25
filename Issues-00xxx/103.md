# Issue 103: sage -br  --- improve dependency checking (don't just check for changed .pyx files).

archive/issues_000103.json:
```json
{
    "body": "Assignee: @williamstein\n\n> There's a problem with rebuilding when you modify .pxd files but nothing  \n> else. i.e. it the build system doesn't seem to recognise when .pyx files  \n> depend on modified .pxd files. I had to manually remove all the .c files  \n> to force a rebuild.\n\n\nYou could touch the corresponding pyx file.\n\nAnyway, this is a NotImplementedError -- i.e., the build system that Python has doesn't\nknow anything about thins like pxd files.   What happens is that when you type\n\"sage -br\", SAGE runs setup.py (which I wrote from scratch).  setup.py looks\nat each .pyx and if it newer than the corresponding .c file, then it runs\npyrex on the pyx file.  This produces a new .c file.   Then Python's distutils\nsees the new .c file, hence rebuilds the module.    I haven't implemented\nsomething similar for .pxd or .pxi files yet.    One possibility would be to\nsimple check if there are any non .c files with the same name (except for the\nextension) that are newer than a given .c file.  If so, regenerate the .c files.\nThis would be pretty easy to implement (it's just a matter of adding some code\nto setup.py).  I'll put it on trac. \n\nIssue created by migration from https://trac.sagemath.org/ticket/103\n\n",
    "closed_at": "2006-10-04T22:06:29Z",
    "created_at": "2006-10-02T04:08:59Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "title": "sage -br  --- improve dependency checking (don't just check for changed .pyx files).",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/103",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

> There's a problem with rebuilding when you modify .pxd files but nothing  
> else. i.e. it the build system doesn't seem to recognise when .pyx files  
> depend on modified .pxd files. I had to manually remove all the .c files  
> to force a rebuild.


You could touch the corresponding pyx file.

Anyway, this is a NotImplementedError -- i.e., the build system that Python has doesn't
know anything about thins like pxd files.   What happens is that when you type
"sage -br", SAGE runs setup.py (which I wrote from scratch).  setup.py looks
at each .pyx and if it newer than the corresponding .c file, then it runs
pyrex on the pyx file.  This produces a new .c file.   Then Python's distutils
sees the new .c file, hence rebuilds the module.    I haven't implemented
something similar for .pxd or .pxi files yet.    One possibility would be to
simple check if there are any non .c files with the same name (except for the
extension) that are newer than a given .c file.  If so, regenerate the .c files.
This would be pretty easy to implement (it's just a matter of adding some code
to setup.py).  I'll put it on trac. 

Issue created by migration from https://trac.sagemath.org/ticket/103





---

archive/issue_comments_000482.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-04T22:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/103#issuecomment-482",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000483.json:
```json
{
    "body": "sha:~/d/sage/sage/structure was$ hg diff ~/d/sage/setup.py\ndiff -r 0c2736a0fd87 setup.py\n--- a/setup.py  Wed Oct 04 13:08:19 2006 -0700\n+++ b/setup.py  Wed Oct 04 14:55:03 2006 -0700\n`@``@` -232,8 +232,8 `@``@` ext_modules = [ \\\n     Extension('sage.groups.group',\n               sources = ['sage/groups/group.pyx']), \\\n \n-    Extension('sage.ext.sage_object',\n-              sources = ['sage/ext/sage_object.pyx']), \\\n+    Extension('sage.structure.sage_object',\n+              sources = ['sage/structure/sage_object.pyx']), \\\n \n     Extension('sage.structure.gens',\n               sources = ['sage/structure/gens.pyx']), \\\n`@``@` -343,10 +343,14 `@``@` def need_to_create(file1, file2):\n def need_to_create(file1, file2):\n     \"\"\"\n     Return True if either file2 does not exist or is older than file1.\n+\n+    If file1 does not exist, always return False. \n     \"\"\"\n+    if not os.path.exists(file1):\n+        return False\n     if not os.path.exists(file2):\n         return True\n-    if os.path.getctime(file2) <= os.path.getctime(file1):\n+    if os.path.getctime(file2) < os.path.getctime(file1):\n         return True\n     return False\n     \n`@``@` -387,6 +391,7 `@``@` def process_pyrexembed_file(f, m):\n \n def process_pyrex_file(f, m):\n     # This is a pyrex file, so process accordingly.\n+    g = os.path.splitext(f)[0]\n     pyx_inst_file = '%s/%s'%(SITE_PACKAGES, f)\n     if need_to_create(f, pyx_inst_file):\n         print \"%s --> %s\"%(f, pyx_inst_file)\n`@``@` -394,7 +399,7 `@``@` def process_pyrex_file(f, m):\n     out_file = f[:-4] + \".c\"\n     if m.language == 'c++':\n         out_file += 'pp'\n-    if need_to_create(f, out_file):\n+    if need_to_create(f, out_file) or need_to_create(g + '.pxd', out_file):\n         cmd = \"pyrexc -I%s %s\"%(os.getcwd(),f)\n         print cmd\n         ret = os.system(cmd)",
    "created_at": "2006-10-04T22:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/103#issuecomment-483",
    "user": "https://github.com/williamstein"
}
```

sha:~/d/sage/sage/structure was$ hg diff ~/d/sage/setup.py
diff -r 0c2736a0fd87 setup.py
--- a/setup.py  Wed Oct 04 13:08:19 2006 -0700
+++ b/setup.py  Wed Oct 04 14:55:03 2006 -0700
`@``@` -232,8 +232,8 `@``@` ext_modules = [ \
     Extension('sage.groups.group',
               sources = ['sage/groups/group.pyx']), \
 
-    Extension('sage.ext.sage_object',
-              sources = ['sage/ext/sage_object.pyx']), \
+    Extension('sage.structure.sage_object',
+              sources = ['sage/structure/sage_object.pyx']), \
 
     Extension('sage.structure.gens',
               sources = ['sage/structure/gens.pyx']), \
`@``@` -343,10 +343,14 `@``@` def need_to_create(file1, file2):
 def need_to_create(file1, file2):
     """
     Return True if either file2 does not exist or is older than file1.
+
+    If file1 does not exist, always return False. 
     """
+    if not os.path.exists(file1):
+        return False
     if not os.path.exists(file2):
         return True
-    if os.path.getctime(file2) <= os.path.getctime(file1):
+    if os.path.getctime(file2) < os.path.getctime(file1):
         return True
     return False
     
`@``@` -387,6 +391,7 `@``@` def process_pyrexembed_file(f, m):
 
 def process_pyrex_file(f, m):
     # This is a pyrex file, so process accordingly.
+    g = os.path.splitext(f)[0]
     pyx_inst_file = '%s/%s'%(SITE_PACKAGES, f)
     if need_to_create(f, pyx_inst_file):
         print "%s --> %s"%(f, pyx_inst_file)
`@``@` -394,7 +399,7 `@``@` def process_pyrex_file(f, m):
     out_file = f[:-4] + ".c"
     if m.language == 'c++':
         out_file += 'pp'
-    if need_to_create(f, out_file):
+    if need_to_create(f, out_file) or need_to_create(g + '.pxd', out_file):
         cmd = "pyrexc -I%s %s"%(os.getcwd(),f)
         print cmd
         ret = os.system(cmd)



---

archive/issue_events_000207.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2006-10-04T22:06:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/103",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/103#event-207"
}
```
