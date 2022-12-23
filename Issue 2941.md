# Issue 2941: sympy spkg updated + a test patch for Sage

archive/issues_002941.json:
```json
{
    "body": "Assignee: mabshoff\n\nApply the attached patch to Sage, then install the attached spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2941\n\n",
    "created_at": "2008-04-16T09:37:36Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "sympy spkg updated + a test patch for Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2941",
    "user": "certik"
}
```
Assignee: mabshoff

Apply the attached patch to Sage, then install the attached spkg.

Issue created by migration from https://trac.sagemath.org/ticket/2941





---

archive/issue_comments_020255.json:
```json
{
    "body": "Sage patch, fixing the tests",
    "created_at": "2008-04-16T09:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20255",
    "user": "certik"
}
```

Sage patch, fixing the tests



---

archive/issue_comments_020256.json:
```json
{
    "body": "Attachment\n\n**Important note**: execute this command\n\nrm -r sage/local/lib/python2.5/site-packages/sympy*\n\nbefore installing the spkg, otherwise sympy will be broken.",
    "created_at": "2008-04-16T09:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20256",
    "user": "certik"
}
```

Attachment

**Important note**: execute this command

rm -r sage/local/lib/python2.5/site-packages/sympy*

before installing the spkg, otherwise sympy will be broken.



---

archive/issue_comments_020257.json:
```json
{
    "body": "Changing component from Cygwin to packages.",
    "created_at": "2008-04-16T09:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20257",
    "user": "mabshoff"
}
```

Changing component from Cygwin to packages.



---

archive/issue_comments_020258.json:
```json
{
    "body": "Replying to [comment:1 certik]:\n> **Important note**: execute this command\n> \n> rm -r sage/local/lib/python2.5/site-packages/sympy*\n> \n> before installing the spkg, otherwise sympy will be broken.\n\nHi Ondrej,\n\nthis must be done in spkg-install, otherwise it will break people's install. \n\nOn another note: There already way #1633 assigned to you as the sympy upgrade ticket. I have closed that as a duplicate.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-16T09:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20258",
    "user": "mabshoff"
}
```

Replying to [comment:1 certik]:
> **Important note**: execute this command
> 
> rm -r sage/local/lib/python2.5/site-packages/sympy*
> 
> before installing the spkg, otherwise sympy will be broken.

Hi Ondrej,

this must be done in spkg-install, otherwise it will break people's install. 

On another note: There already way #1633 assigned to you as the sympy upgrade ticket. I have closed that as a duplicate.

Cheers,

Michael



---

archive/issue_comments_020259.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-16T11:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20259",
    "user": "certik"
}
```

Attachment



---

archive/issue_comments_020260.json:
```json
{
    "body": "Thanks I committed the patch below and attached a new spkg.\n\ndiff -r 029e5541f507 -r 2111fce6f538 spkg-install\n--- a/spkg-install\tWed Apr 16 11:28:19 2008 +0200\n+++ b/spkg-install\tWed Apr 16 13:44:47 2008 +0200\n`@``@` -1,4 +1,14 `@``@`\n #!/bin/sh\n+\n+# We need to delete the old path, so that there are no leftovers from the\n+# previous installation, otherwise sympy could get broken (for example by\n+# importing some local files instead of the standard library ones...)\n+if [ \"$SAGE_ROOT\" = \"\" ]; then\n+    echo \"Please set the SAGE_ROOT variable\"\n+    exit 1\n+fi\n+echo \"Deleting $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*\"\n+rm -rf $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*\n \n cd src/",
    "created_at": "2008-04-16T11:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20260",
    "user": "certik"
}
```

Thanks I committed the patch below and attached a new spkg.

diff -r 029e5541f507 -r 2111fce6f538 spkg-install
--- a/spkg-install	Wed Apr 16 11:28:19 2008 +0200
+++ b/spkg-install	Wed Apr 16 13:44:47 2008 +0200
`@``@` -1,4 +1,14 `@``@`
 #!/bin/sh
+
+# We need to delete the old path, so that there are no leftovers from the
+# previous installation, otherwise sympy could get broken (for example by
+# importing some local files instead of the standard library ones...)
+if [ "$SAGE_ROOT" = "" ]; then
+    echo "Please set the SAGE_ROOT variable"
+    exit 1
+fi
+echo "Deleting $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*"
+rm -rf $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*
 
 cd src/



---

archive/issue_comments_020261.json:
```json
{
    "body": "The patch got screwed up, so again:\n\n\n```\ndiff -r 029e5541f507 -r 2111fce6f538 spkg-install\n--- a/spkg-install\tWed Apr 16 11:28:19 2008 +0200\n+++ b/spkg-install\tWed Apr 16 13:44:47 2008 +0200\n@@ -1,4 +1,14 @@\n #!/bin/sh\n+\n+# We need to delete the old path, so that there are no leftovers from the\n+# previous installation, otherwise sympy could get broken (for example by\n+# importing some local files instead of the standard library ones...)\n+if [ \"$SAGE_ROOT\" = \"\" ]; then\n+    echo \"Please set the SAGE_ROOT variable\"\n+    exit 1\n+fi\n+echo \"Deleting $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*\"\n+rm -rf $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*\n \n cd src/\n```\n",
    "created_at": "2008-04-16T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20261",
    "user": "certik"
}
```

The patch got screwed up, so again:


```
diff -r 029e5541f507 -r 2111fce6f538 spkg-install
--- a/spkg-install	Wed Apr 16 11:28:19 2008 +0200
+++ b/spkg-install	Wed Apr 16 13:44:47 2008 +0200
@@ -1,4 +1,14 @@
 #!/bin/sh
+
+# We need to delete the old path, so that there are no leftovers from the
+# previous installation, otherwise sympy could get broken (for example by
+# importing some local files instead of the standard library ones...)
+if [ "$SAGE_ROOT" = "" ]; then
+    echo "Please set the SAGE_ROOT variable"
+    exit 1
+fi
+echo "Deleting $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*"
+rm -rf $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*
 
 cd src/
```




---

archive/issue_comments_020262.json:
```json
{
    "body": "Parch and spgk are good, pass doctests. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-17T06:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20262",
    "user": "mabshoff"
}
```

Parch and spgk are good, pass doctests. Positive review.

Cheers,

Michael



---

archive/issue_comments_020263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T06:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20263",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020264.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T06:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2941#issuecomment-20264",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6
