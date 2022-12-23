# Issue 2808: G2 fundamental weights were the negative of what they should be.

archive/issues_002808.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nIn combinat/root_system.py, the fundamental weights for the various root systems are entered by hand. For G2, the fundamental weights were the negatives of what they should be.\n\n```\n\ndiff -r 80b506b8e07c sage/combinat/root_system.py\n--- a/sage/combinat/root_system.py\tTue Apr 01 19:18:55 2008 -0700\n+++ b/sage/combinat/root_system.py\tSat Apr 05 08:40:46 2008 -0700\n@@ -788,11 +788,11 @@ class AmbientLattice_g(AmbientLattice_ge\n         \"\"\"\n         EXAMPLES:\n             sage: CartanType(['G',2]).root_system().ambient_lattice().fundamental_weights()\n-            [(-1, 0, 1), (-2, 1, 1)]\n+            [(1, 0, -1), (2, -1, -1)]\n         \"\"\"\n         return [ c0*self._term(0)+c1*self._term(1)+c2*self._term(2) \\\n                  for [c0,c1,c2] in\n-                 [[-1,0,1],[-2,1,1]]]\n+                 [[1,0,-1],[2,-1,-1]]]\n \n \n def WeylDim(type, coeffs):\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2808\n\n",
    "created_at": "2008-04-05T16:18:50Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "G2 fundamental weights were the negative of what they should be.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2808",
    "user": "bump"
}
```
Assignee: mhansen

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


Issue created by migration from https://trac.sagemath.org/ticket/2808





---

archive/issue_comments_019275.json:
```json
{
    "body": "Attachment\n\npatch correcting the G2 fundamental weights",
    "created_at": "2008-04-05T16:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2808#issuecomment-19275",
    "user": "bump"
}
```

Attachment

patch correcting the G2 fundamental weights



---

archive/issue_comments_019276.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-05T16:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2808#issuecomment-19276",
    "user": "bump"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019277.json:
```json
{
    "body": "Changing assignee from mhansen to bump.",
    "created_at": "2008-04-05T16:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2808#issuecomment-19277",
    "user": "bump"
}
```

Changing assignee from mhansen to bump.



---

archive/issue_comments_019278.json:
```json
{
    "body": "Quoting from the email to sage-devel:\n\n\n```\nI should have added some justification for this conclusion\nin the trac report. Instead I'm giving it here. You can\nlook the weights up in Bourbaki, Lie Groups and Lie\nAlgebras Ch 4-6 (Appendix) and you can also check\nthe inner products of the weights with the simple\nroots (which are correct). The inner product of\nthe i-th fundamental weight with the j-th simple\nroot should be positive if i=j and zero otherwise.\nI checked that all the other root systems are right\nby examining the output following program on the ambient\nlattices. This change had no effect on the output of\nthe Weyl dimension formula.\n\ndef test_lattice(L):\n   rank = L.ct[1]\n   roots = L.simple_roots()\n   weights = L.fundamental_weights()\n      return [[i,j, roots[i].inner_product(weights[j])] for i in range(rank) for j in range(rank)]\n```\n\n\nI am happy with this (small!) change.",
    "created_at": "2008-04-05T17:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2808#issuecomment-19278",
    "user": "cremona"
}
```

Quoting from the email to sage-devel:


```
I should have added some justification for this conclusion
in the trac report. Instead I'm giving it here. You can
look the weights up in Bourbaki, Lie Groups and Lie
Algebras Ch 4-6 (Appendix) and you can also check
the inner products of the weights with the simple
roots (which are correct). The inner product of
the i-th fundamental weight with the j-th simple
root should be positive if i=j and zero otherwise.
I checked that all the other root systems are right
by examining the output following program on the ambient
lattices. This change had no effect on the output of
the Weyl dimension formula.

def test_lattice(L):
   rank = L.ct[1]
   roots = L.simple_roots()
   weights = L.fundamental_weights()
      return [[i,j, roots[i].inner_product(weights[j])] for i in range(rank) for j in range(rank)]
```


I am happy with this (small!) change.



---

archive/issue_comments_019279.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T17:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2808#issuecomment-19279",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019280.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2.",
    "created_at": "2008-04-05T17:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2808#issuecomment-19280",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2.
