# Issue 6096: [with patch, needs review] Fix subtle bug in partition refinement

archive/issues_006096.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  sage-combinat\n\nThis patch includes a module which gives an extremely simple example of using the `partn_ref` module, which exposed the bug, whose fix is:\n\n\n```\ndiff -r feb2d962bf2b -r f5d696c216ff sage/groups/perm_gps/partn_ref/double_coset.pyx\n--- a/sage/groups/perm_gps/partn_ref/double_coset.pyx\tMon May 18 12:46:23 2009 -0700\n+++ b/sage/groups/perm_gps/partn_ref/double_coset.pyx\tWed May 20 14:59:09 2009 -0700\n@@ -540,7 +540,7 @@\n         if not possible:\n             possible = 1\n             i = current_ps.depth\n-            current_ps.depth = min(first_kids_are_same-1, current_kids_are_same-1)\n+            current_ps.depth = current_kids_are_same-1\n             if i == current_kids_are_same:\n                 continue # main loop\n             if index_in_fp_and_mcr < len_of_fp_and_mcr - 1:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6096\n\n",
    "created_at": "2009-05-20T21:31:46Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] Fix subtle bug in partition refinement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6096",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  sage-combinat

This patch includes a module which gives an extremely simple example of using the `partn_ref` module, which exposed the bug, whose fix is:


```
diff -r feb2d962bf2b -r f5d696c216ff sage/groups/perm_gps/partn_ref/double_coset.pyx
--- a/sage/groups/perm_gps/partn_ref/double_coset.pyx	Mon May 18 12:46:23 2009 -0700
+++ b/sage/groups/perm_gps/partn_ref/double_coset.pyx	Wed May 20 14:59:09 2009 -0700
@@ -540,7 +540,7 @@
         if not possible:
             possible = 1
             i = current_ps.depth
-            current_ps.depth = min(first_kids_are_same-1, current_kids_are_same-1)
+            current_ps.depth = current_kids_are_same-1
             if i == current_kids_are_same:
                 continue # main loop
             if index_in_fp_and_mcr < len_of_fp_and_mcr - 1:
```


Issue created by migration from https://trac.sagemath.org/ticket/6096





---

archive/issue_comments_048510.json:
```json
{
    "body": "Attachment [trac_6096-partition_refinement_lists.patch](tarball://root/attachments/some-uuid/ticket6096/trac_6096-partition_refinement_lists.patch) by @rlmill created at 2009-05-20 21:35:24\n\nThe module `refinement_list` was written by Nicolas Borie, and I just cleaned it up a bit. He and Nicolas Thiery found the bug and reported it to me. The fix was mine.",
    "created_at": "2009-05-20T21:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6096#issuecomment-48510",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6096-partition_refinement_lists.patch](tarball://root/attachments/some-uuid/ticket6096/trac_6096-partition_refinement_lists.patch) by @rlmill created at 2009-05-20 21:35:24

The module `refinement_list` was written by Nicolas Borie, and I just cleaned it up a bit. He and Nicolas Thiery found the bug and reported it to me. The fix was mine.



---

archive/issue_comments_048511.json:
```json
{
    "body": "Good explanation of one-line fix at Allegro.  Patch resolves issue and new doctest module is included.  No doctest failures on 4.0alpha0.",
    "created_at": "2009-05-21T20:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6096#issuecomment-48511",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Good explanation of one-line fix at Allegro.  Patch resolves issue and new doctest module is included.  No doctest failures on 4.0alpha0.



---

archive/issue_comments_048512.json:
```json
{
    "body": "Merged in Sage 4.0.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T13:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6096#issuecomment-48512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc1.

Cheers,

Michael



---

archive/issue_events_006347.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-22T13:33:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6096",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6096#event-6347"
}
```



---

archive/issue_comments_048513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-22T13:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6096#issuecomment-48513",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
