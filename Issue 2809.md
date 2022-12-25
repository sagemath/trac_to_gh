# Issue 2809: G2 fundamental weights were the negative of what they should be.

archive/issues_002809.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nIn combinat/root_system.py, the fundamental weights for the various root systems are entered by hand. For G2, the fundamental weights were the negatives of what they should be.\n\n```\n\ndiff -r 80b506b8e07c sage/combinat/root_system.py\n--- a/sage/combinat/root_system.py\tTue Apr 01 19:18:55 2008 -0700\n+++ b/sage/combinat/root_system.py\tSat Apr 05 08:40:46 2008 -0700\n@@ -788,11 +788,11 @@ class AmbientLattice_g(AmbientLattice_ge\n         \"\"\"\n         EXAMPLES:\n             sage: CartanType(['G',2]).root_system().ambient_lattice().fundamental_weights()\n-            [(-1, 0, 1), (-2, 1, 1)]\n+            [(1, 0, -1), (2, -1, -1)]\n         \"\"\"\n         return [ c0*self._term(0)+c1*self._term(1)+c2*self._term(2) \\\n                  for [c0,c1,c2] in\n-                 [[-1,0,1],[-2,1,1]]]\n+                 [[1,0,-1],[2,-1,-1]]]\n \n \n def WeylDim(type, coeffs):\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2809\n\n",
    "created_at": "2008-04-05T16:23:26Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "G2 fundamental weights were the negative of what they should be.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2809",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

In combinat/root_system.py, the fundamental weights for the various root systems are entered by hand. For G2, the fundamental weights were the negatives of what they should be.

```

diff -r 80b506b8e07c sage/combinat/root_system.py
--- a/sage/combinat/root_system.py	Tue Apr 01 19:18:55 2008 -0700
+++ b/sage/combinat/root_system.py	Sat Apr 05 08:40:46 2008 -0700
@@ -788,11 +788,11 @@ class AmbientLattice_g(AmbientLattice_ge
         """
         EXAMPLES:
             sage: CartanType(['G',2]).root_system().ambient_lattice().fundamental_weights()
-            [(-1, 0, 1), (-2, 1, 1)]
+            [(1, 0, -1), (2, -1, -1)]
         """
         return [ c0*self._term(0)+c1*self._term(1)+c2*self._term(2) \
                  for [c0,c1,c2] in
-                 [[-1,0,1],[-2,1,1]]]
+                 [[1,0,-1],[2,-1,-1]]]
 
 
 def WeylDim(type, coeffs):

```


Issue created by migration from https://trac.sagemath.org/ticket/2809





---

archive/issue_comments_019240.json:
```json
{
    "body": "Attachment [g2.patch](tarball://root/attachments/some-uuid/ticket2809/g2.patch) by mabshoff created at 2008-04-05 16:30:34\n\nThis is a dupe of #2808, so I am closing it. Dan: once you open a ticket and you hit \"submit\" you should remove the \"preview\" bit from the url before going on. This is a buglet in trac and you aren't the first one who has been bitten by it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T16:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2809#issuecomment-19240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [g2.patch](tarball://root/attachments/some-uuid/ticket2809/g2.patch) by mabshoff created at 2008-04-05 16:30:34

This is a dupe of #2808, so I am closing it. Dan: once you open a ticket and you hit "submit" you should remove the "preview" bit from the url before going on. This is a buglet in trac and you aren't the first one who has been bitten by it.

Cheers,

Michael



---

archive/issue_comments_019241.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-05T16:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2809#issuecomment-19241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_003000.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-05T16:30:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2809",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2809#event-3000"
}
```
