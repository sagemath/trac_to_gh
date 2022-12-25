# Issue 8925: __call__ for categories sets / enumeratedsets

archive/issues_008925.json:
```json
{
    "body": "Assignee: @hivert\n\nKeywords: Category call\n\nFrom `sets_cat.py`:\n\n```\nFIXME: the above behavior dates back from the first category\nwriteup. It is not consistent with :meth:`Category.__call__`.\nShould we change it to just return ``ZZ`` instead?\n```\nAlso `EnumeratedSets().__call__(...)` is missing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8925\n\n",
    "closed_at": "2011-01-12T06:32:11Z",
    "created_at": "2010-05-07T20:00:36Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "__call__ for categories sets / enumeratedsets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8925",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

Keywords: Category call

From `sets_cat.py`:

```
FIXME: the above behavior dates back from the first category
writeup. It is not consistent with :meth:`Category.__call__`.
Should we change it to just return ``ZZ`` instead?
```
Also `EnumeratedSets().__call__(...)` is missing.

Issue created by migration from https://trac.sagemath.org/ticket/8925





---

archive/issue_comments_082082.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-15T22:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82082",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082083.json:
```json
{
    "body": "Looks good except for some minor formatting issues.  I put a review patch up on the patch server.  Do you want to fold that in and reupload?",
    "created_at": "2010-11-25T22:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82083",
    "user": "https://github.com/mwhansen"
}
```

Looks good except for some minor formatting issues.  I put a review patch up on the patch server.  Do you want to fold that in and reupload?



---

archive/issue_comments_082084.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-25T22:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82084",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082085.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-26T10:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82085",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082086.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> Looks good except for some minor formatting issues.  I put a review patch up on the patch server.  Do you want to fold that in and reupload?\n\n\nDone ! I'm ok with your changes. Feel free to put a positive review if you are ok.",
    "created_at": "2010-11-26T10:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82086",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:2 mhansen]:
> Looks good except for some minor formatting issues.  I put a review patch up on the patch server.  Do you want to fold that in and reupload?


Done ! I'm ok with your changes. Feel free to put a positive review if you are ok.



---

archive/issue_comments_082087.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-26T19:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82087",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021787.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-26T22:33:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8925#event-21787"
}
```



---

archive/issue_comments_082088.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n\nThanks for the review !",
    "created_at": "2010-11-26T23:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82088",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:4 mhansen]:

Thanks for the review !



---

archive/issue_comments_082089.json:
```json
{
    "body": "Extremely picky, minor, minor thing, but these words: \"For now, list's, tuple's, set's, Set's are coerced into finite\" shouldn't have apostrophes in them, since the words are not possessive, but just plural.",
    "created_at": "2010-11-27T05:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82089",
    "user": "https://github.com/jasongrout"
}
```

Extremely picky, minor, minor thing, but these words: "For now, list's, tuple's, set's, Set's are coerced into finite" shouldn't have apostrophes in them, since the words are not possessive, but just plural.



---

archive/issue_comments_082090.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> Extremely picky, minor, minor thing, but these words: \"For now, list's, tuple's, set's, Set's are coerced into finite\" shouldn't have apostrophes in them, since the words are not possessive, but just plural.\n\n\nI reuploaded a new patche with the following diff folded:\n\n```\ndiff --git a/sage/categories/enumerated_sets.py b/sage/categories/enumerated_sets.py\n--- a/sage/categories/enumerated_sets.py\n+++ b/sage/categories/enumerated_sets.py\n@@ -103,7 +103,7 @@ class EnumeratedSets(Category):\n             sage: EnumeratedSets()(Primes())\n             Set of all prime numbers: 2, 3, 5, 7, ...\n \n-        For now, list's, tuple's, set's, Set's are coerced into finite\n+        For now, lists, tuples, sets, Sets are coerced into finite\n         enumerated sets::\n \n             sage: S = EnumeratedSets()([1, 2, 3]); S\n```\nSo now you have to review it ;-)",
    "created_at": "2010-11-27T18:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82090",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:7 jason]:
> Extremely picky, minor, minor thing, but these words: "For now, list's, tuple's, set's, Set's are coerced into finite" shouldn't have apostrophes in them, since the words are not possessive, but just plural.


I reuploaded a new patche with the following diff folded:

```
diff --git a/sage/categories/enumerated_sets.py b/sage/categories/enumerated_sets.py
--- a/sage/categories/enumerated_sets.py
+++ b/sage/categories/enumerated_sets.py
@@ -103,7 +103,7 @@ class EnumeratedSets(Category):
             sage: EnumeratedSets()(Primes())
             Set of all prime numbers: 2, 3, 5, 7, ...
 
-        For now, list's, tuple's, set's, Set's are coerced into finite
+        For now, lists, tuples, sets, Sets are coerced into finite
         enumerated sets::
 
             sage: S = EnumeratedSets()([1, 2, 3]); S
```
So now you have to review it ;-)



---

archive/issue_comments_082091.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-27T18:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82091",
    "user": "https://github.com/hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082092.json:
```json
{
    "body": "Attachment [trac_8925-call_set_enumset-fh.patch](tarball://root/attachments/some-uuid/ticket8925/trac_8925-call_set_enumset-fh.patch) by @hivert created at 2010-11-27 18:41:25\n\nReplying to [comment:8 hivert]:\n> Replying to [comment:7 jason]:\n> > Extremely picky, minor, minor thing, but these words: \"For now, list's, tuple's, set's, Set's are coerced into finite\" shouldn't have apostrophes in them, since the words are not possessive, but just plural.\n\n> \n> I reuploaded a new patche with the following diff folded:\n\n\nActually there where another occurrence in another file\n\n```\ndiff --git a/trac_8925-call_set_enumset-fh.patch b/trac_8925-call_set_enumset-fh.patch\n--- a/trac_8925-call_set_enumset-fh.patch\n+++ b/trac_8925-call_set_enumset-fh.patch\n@@ -83,7 +83,7 @@ diff --git a/sage/categories/finite_enum\n +            sage: FiniteEnumeratedSets()(Partitions(3)) # todo: not implemented: Partitions\n +            Partitions of 3\n +\n-+        For now, list's, tuple's, set's, Set's are coerced into finite\n++        For now, lists, tuples, sets, Sets are coerced into finite\n +        enumerated sets::\n +\n +            sage: FiniteEnumeratedSets()([1, 2, 3])\n```\nAgain I folded this change and resubmitted the patch. Please review.",
    "created_at": "2010-11-27T18:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82092",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8925-call_set_enumset-fh.patch](tarball://root/attachments/some-uuid/ticket8925/trac_8925-call_set_enumset-fh.patch) by @hivert created at 2010-11-27 18:41:25

Replying to [comment:8 hivert]:
> Replying to [comment:7 jason]:
> > Extremely picky, minor, minor thing, but these words: "For now, list's, tuple's, set's, Set's are coerced into finite" shouldn't have apostrophes in them, since the words are not possessive, but just plural.

> 
> I reuploaded a new patche with the following diff folded:


Actually there where another occurrence in another file

```
diff --git a/trac_8925-call_set_enumset-fh.patch b/trac_8925-call_set_enumset-fh.patch
--- a/trac_8925-call_set_enumset-fh.patch
+++ b/trac_8925-call_set_enumset-fh.patch
@@ -83,7 +83,7 @@ diff --git a/sage/categories/finite_enum
 +            sage: FiniteEnumeratedSets()(Partitions(3)) # todo: not implemented: Partitions
 +            Partitions of 3
 +
-+        For now, list's, tuple's, set's, Set's are coerced into finite
++        For now, lists, tuples, sets, Sets are coerced into finite
 +        enumerated sets::
 +
 +            sage: FiniteEnumeratedSets()([1, 2, 3])
```
Again I folded this change and resubmitted the patch. Please review.



---

archive/issue_comments_082093.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-27T18:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82093",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082094.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-27T19:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82094",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082095.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-11-27T19:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82095",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_comments_082096.json:
```json
{
    "body": "Looks good to me too.  Thanks for working on even the most minor nitpicky requests :).",
    "created_at": "2010-11-27T21:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82096",
    "user": "https://github.com/jasongrout"
}
```

Looks good to me too.  Thanks for working on even the most minor nitpicky requests :).



---

archive/issue_events_021788.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-12T06:32:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8925#event-21788"
}
```



---

archive/issue_comments_082097.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8925#issuecomment-82097",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
