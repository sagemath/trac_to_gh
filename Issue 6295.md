# Issue 6295: [with patch, needs review] build runs sphinx-build even on failure

archive/issues_006295.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  craigcitro\n\nThe build process runs sphinx-build even if a package fails to install. This hides the real error message from the spkg build.\n\nThis patch to spkg/install fixes the problem:\n\n\n```\n--- install.old 2009-06-12 08:46:55.000000000 +0200\n+++ install     2009-06-15 11:47:02.000000000 +0200\n@@ -357,6 +357,11 @@\n \n time make -f standard/deps $1\n \n+if [ $? -ne 0 ]; then\n+       echo \"Error building Sage.\"\n+       exit 1\n+fi\n+\n #Build the documentation\n rm -rf \"$SAGE_ROOT\"/devel/sage-main/doc/output/doctrees\n rm -rf \"$SAGE_ROOT\"/devel/sage-main/doc/en/reference/sage/*\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6295\n\n",
    "created_at": "2009-06-15T09:52:30Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] build runs sphinx-build even on failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6295",
    "user": "burcin"
}
```
Assignee: burcin

CC:  craigcitro

The build process runs sphinx-build even if a package fails to install. This hides the real error message from the spkg build.

This patch to spkg/install fixes the problem:


```
--- install.old 2009-06-12 08:46:55.000000000 +0200
+++ install     2009-06-15 11:47:02.000000000 +0200
@@ -357,6 +357,11 @@
 
 time make -f standard/deps $1
 
+if [ $? -ne 0 ]; then
+       echo "Error building Sage."
+       exit 1
+fi
+
 #Build the documentation
 rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
 rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
```


Issue created by migration from https://trac.sagemath.org/ticket/6295





---

archive/issue_comments_050236.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-18T00:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6295#issuecomment-50236",
    "user": "craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_050237.json:
```json
{
    "body": "Yep, this is a great idea. There's no hg repository there, but I've added the changes.",
    "created_at": "2009-06-18T00:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6295#issuecomment-50237",
    "user": "craigcitro"
}
```

Yep, this is a great idea. There's no hg repository there, but I've added the changes.
