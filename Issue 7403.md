# Issue 7403: adds FiniteEnumeratedSet

archive/issues_007403.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nKeywords: finite enumerated sets\n\nThis patch adds sage.sets.finite_enumerated_set.FiniteEnumeratedSet\n\ndepends on #5891\n\nIssue created by migration from https://trac.sagemath.org/ticket/7403\n\n",
    "created_at": "2009-11-06T15:56:12Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "adds FiniteEnumeratedSet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7403",
    "user": "nthiery"
}
```
Assignee: mhansen

CC:  sage-combinat

Keywords: finite enumerated sets

This patch adds sage.sets.finite_enumerated_set.FiniteEnumeratedSet

depends on #5891

Issue created by migration from https://trac.sagemath.org/ticket/7403





---

archive/issue_comments_062289.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T15:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62289",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062290.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T15:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62290",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062291.json:
```json
{
    "body": "Attachment [trac_7403-finite-enumeratedsets-fh.2.patch](tarball://root/attachments/some-uuid/ticket7403/trac_7403-finite-enumeratedsets-fh.2.patch) by nthiery created at 2009-11-06 16:17:53",
    "created_at": "2009-11-06T16:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62291",
    "user": "nthiery"
}
```

Attachment [trac_7403-finite-enumeratedsets-fh.2.patch](tarball://root/attachments/some-uuid/ticket7403/trac_7403-finite-enumeratedsets-fh.2.patch) by nthiery created at 2009-11-06 16:17:53



---

archive/issue_comments_062292.json:
```json
{
    "body": "Attachment [trac_7403-finite-enumeratedsets-fh.patch](tarball://root/attachments/some-uuid/ticket7403/trac_7403-finite-enumeratedsets-fh.patch) by nthiery created at 2009-11-06 16:18:51\n\nApply only this one (ignore the next one)",
    "created_at": "2009-11-06T16:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62292",
    "user": "nthiery"
}
```

Attachment [trac_7403-finite-enumeratedsets-fh.patch](tarball://root/attachments/some-uuid/ticket7403/trac_7403-finite-enumeratedsets-fh.patch) by nthiery created at 2009-11-06 16:18:51

Apply only this one (ignore the next one)



---

archive/issue_comments_062293.json:
```json
{
    "body": "Since it's not yet integrated, I take the chance to solve this stupid bug:\n\n```\nsage: FiniteEnumeratedSet([1])\n{1,}\n```\n\nI'm re-uploading a patch with the following folded in\n\n```\ndiff --git a/sage/sets/finite_enumerated_set.py b/sage/sets/finite_enumerated_set.py\n--- a/sage/sets/finite_enumerated_set.py\n+++ b/sage/sets/finite_enumerated_set.py\n@@ -123,8 +123,13 @@ class FiniteEnumeratedSet(UniqueRepresen\n             sage: S = FiniteEnumeratedSet([1,2,3])\n             sage: repr(S)\n             '{1, 2, 3}'\n+            sage: S = FiniteEnumeratedSet([1])\n+            sage: repr(S)\n+            '{1}'\n         \"\"\"\n-        return \"{\"+str(self._elements)[1:-1] + '}'\n+        if len(self._elements) == 1: # avoid printing '{1,}'\n+            return \"{\" + str(self._elements[0]) + '}'\n+        return \"{\" + str(self._elements)[1:-1] + '}'\n \n     def __contains__(self, x):\n         \"\"\"\n```\n\n\nFlorent",
    "created_at": "2009-11-09T07:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62293",
    "user": "hivert"
}
```

Since it's not yet integrated, I take the chance to solve this stupid bug:

```
sage: FiniteEnumeratedSet([1])
{1,}
```

I'm re-uploading a patch with the following folded in

```
diff --git a/sage/sets/finite_enumerated_set.py b/sage/sets/finite_enumerated_set.py
--- a/sage/sets/finite_enumerated_set.py
+++ b/sage/sets/finite_enumerated_set.py
@@ -123,8 +123,13 @@ class FiniteEnumeratedSet(UniqueRepresen
             sage: S = FiniteEnumeratedSet([1,2,3])
             sage: repr(S)
             '{1, 2, 3}'
+            sage: S = FiniteEnumeratedSet([1])
+            sage: repr(S)
+            '{1}'
         """
-        return "{"+str(self._elements)[1:-1] + '}'
+        if len(self._elements) == 1: # avoid printing '{1,}'
+            return "{" + str(self._elements[0]) + '}'
+        return "{" + str(self._elements)[1:-1] + '}'
 
     def __contains__(self, x):
         """
```


Florent



---

archive/issue_comments_062294.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-09T07:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62294",
    "user": "hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062295.json:
```json
{
    "body": "Attachment [trac_7403-finite-enumeratedsets-fh.3.patch](tarball://root/attachments/some-uuid/ticket7403/trac_7403-finite-enumeratedsets-fh.3.patch) by hivert created at 2009-11-09 07:55:54\n\nPlease Nicolas (or anyone else re-view the small change. \n\nOnly trac_7403-finite-enumeratedsets-fh.3.patch should be applied on top of #5891\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-09T07:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62295",
    "user": "hivert"
}
```

Attachment [trac_7403-finite-enumeratedsets-fh.3.patch](tarball://root/attachments/some-uuid/ticket7403/trac_7403-finite-enumeratedsets-fh.3.patch) by hivert created at 2009-11-09 07:55:54

Please Nicolas (or anyone else re-view the small change. 

Only trac_7403-finite-enumeratedsets-fh.3.patch should be applied on top of #5891

Cheers,

Florent



---

archive/issue_comments_062296.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-09T07:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62296",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062297.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T10:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62297",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062298.json:
```json
{
    "body": "Changing assignee from mhansen to hivert.",
    "created_at": "2009-11-13T15:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62298",
    "user": "hivert"
}
```

Changing assignee from mhansen to hivert.



---

archive/issue_comments_062299.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T16:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7403#issuecomment-62299",
    "user": "mhansen"
}
```

Resolution: fixed
