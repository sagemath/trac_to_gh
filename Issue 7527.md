# Issue 7527: include graph_coloring in the reference manual.

archive/issues_007527.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  mvngu\n\nAs mentionned in #6679 the file graph_coloring is not included in the docstrings. Apply this patch, and this is fixed :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7527\n\n",
    "created_at": "2009-11-25T08:44:39Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "include graph_coloring in the reference manual.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7527",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  mvngu

As mentionned in #6679 the file graph_coloring is not included in the docstrings. Apply this patch, and this is fixed :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7527





---

archive/issue_comments_063802.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-25T08:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63802",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063803.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-25T08:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63803",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_063804.json:
```json
{
    "body": "Changing component from graph theory to documentation.",
    "created_at": "2009-11-25T10:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63804",
    "user": "mvngu"
}
```

Changing component from graph theory to documentation.



---

archive/issue_comments_063805.json:
```json
{
    "body": "rebased; based on Sage 4.3.alpha1",
    "created_at": "2009-12-08T19:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63805",
    "user": "mvngu"
}
```

rebased; based on Sage 4.3.alpha1



---

archive/issue_comments_063806.json:
```json
{
    "body": "Attachment\n\nreviewer patch",
    "created_at": "2009-12-08T19:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63806",
    "user": "mvngu"
}
```

Attachment

reviewer patch



---

archive/issue_comments_063807.json:
```json
{
    "body": "Attachment\n\nThe patch `trac_7527.patch` doesn't apply cleanly on top of Sage 4.3.alpha1:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7527/trac_7527.patch\nadding trac_7527.patch to series file\n[mvngu@sage sage-main]$ hg qpush\napplying trac_7527.patch\npatching file sage/graphs/graph_coloring.py\nHunk #3 FAILED at 143\nHunk #4 succeeded at 175 with fuzz 1 (offset 14 lines).\nHunk #7 succeeded at 651 with fuzz 1 (offset 416 lines).\n1 out of 7 hunks FAILED -- saving rejects to file sage/graphs/graph_coloring.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_7527.patch\n```\n\nThe rejected hunk is\n\n```\n[mvngu@sage ~]$ cat graph_coloring.py.rej \n--- graph_coloring.py\n+++ graph_coloring.py\n@@ -142,11 +144,12 @@\n         raise RuntimeError, \"Too much recursion!  Graph coloring failed.\"\n \n def first_coloring(G,n=0):\n-    \"\"\"\n-    Given a graph, and optionally a natural number n, returns\n-    the first coloring we find with at least n colors.\n+    r\"\"\"\n+    Given a graph, and optionally a natural number `n`, returns\n+    the first coloring we find with at least `n` colors.\n \n-    EXAMPLES:\n+    EXAMPLES::\n+\n         sage: from sage.graphs.graph_coloring import first_coloring\n         sage: G = Graph({0:[1,2,3],1:[2]})\n         sage: first_coloring(G,3)\n```\n\nwhich fails to apply because #6679 already takes care of that hunk. I have rebased ncohen's patch using Sage 4.3.alpha1; see `trac_7527-rebased.patch` which doesn't include the rejected hunk. I'm OK with ncohen's original patch, so only the rebased patch and my patch `trac_7527-reviewer.patch` needs reviewing. Patches should be applied in this order:\n\n1. `trac_7527-rebased.patch`\n2. `trac_7527-reviewer.patch`",
    "created_at": "2009-12-08T19:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63807",
    "user": "mvngu"
}
```

Attachment

The patch `trac_7527.patch` doesn't apply cleanly on top of Sage 4.3.alpha1:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7527/trac_7527.patch
adding trac_7527.patch to series file
[mvngu@sage sage-main]$ hg qpush
applying trac_7527.patch
patching file sage/graphs/graph_coloring.py
Hunk #3 FAILED at 143
Hunk #4 succeeded at 175 with fuzz 1 (offset 14 lines).
Hunk #7 succeeded at 651 with fuzz 1 (offset 416 lines).
1 out of 7 hunks FAILED -- saving rejects to file sage/graphs/graph_coloring.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7527.patch
```

The rejected hunk is

```
[mvngu@sage ~]$ cat graph_coloring.py.rej 
--- graph_coloring.py
+++ graph_coloring.py
@@ -142,11 +144,12 @@
         raise RuntimeError, "Too much recursion!  Graph coloring failed."
 
 def first_coloring(G,n=0):
-    """
-    Given a graph, and optionally a natural number n, returns
-    the first coloring we find with at least n colors.
+    r"""
+    Given a graph, and optionally a natural number `n`, returns
+    the first coloring we find with at least `n` colors.
 
-    EXAMPLES:
+    EXAMPLES::
+
         sage: from sage.graphs.graph_coloring import first_coloring
         sage: G = Graph({0:[1,2,3],1:[2]})
         sage: first_coloring(G,3)
```

which fails to apply because #6679 already takes care of that hunk. I have rebased ncohen's patch using Sage 4.3.alpha1; see `trac_7527-rebased.patch` which doesn't include the rejected hunk. I'm OK with ncohen's original patch, so only the rebased patch and my patch `trac_7527-reviewer.patch` needs reviewing. Patches should be applied in this order:

1. `trac_7527-rebased.patch`
2. `trac_7527-reviewer.patch`



---

archive/issue_comments_063808.json:
```json
{
    "body": "Perfect job, as usual... Thank you very much, and positive review to your added patch !\n\nNathann",
    "created_at": "2009-12-09T13:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63808",
    "user": "ncohen"
}
```

Perfect job, as usual... Thank you very much, and positive review to your added patch !

Nathann



---

archive/issue_comments_063809.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T13:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63809",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T15:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7527#issuecomment-63810",
    "user": "mhansen"
}
```

Resolution: fixed
