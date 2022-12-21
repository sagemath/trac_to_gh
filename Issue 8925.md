# Issue 8925: __call__ for categories sets / enumeratedsets

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-07 20:00:36

Assignee: hivert

Keywords: Category call

From `sets_cat.py`:

```
FIXME: the above behavior dates back from the first category
writeup. It is not consistent with :meth:`Category.__call__`.
Should we change it to just return ``ZZ`` instead?
```

Also `EnumeratedSets().__call__(...)` is missing.


---

Comment by hivert created at 2010-06-15 22:52:22

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-11-25 22:34:12

Looks good except for some minor formatting issues.  I put a review patch up on the patch server.  Do you want to fold that in and reupload?


---

Comment by mhansen created at 2010-11-25 22:34:12

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-11-26 10:32:30

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-11-26 10:32:30

Replying to [comment:2 mhansen]:
> Looks good except for some minor formatting issues.  I put a review patch up on the patch server.  Do you want to fold that in and reupload?

Done ! I'm ok with your changes. Feel free to put a positive review if you are ok.


---

Comment by mhansen created at 2010-11-26 19:00:52

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-11-26 23:07:13

Replying to [comment:4 mhansen]:

Thanks for the review !


---

Comment by jason created at 2010-11-27 05:50:25

Extremely picky, minor, minor thing, but these words: "For now, list's, tuple's, set's, Set's are coerced into finite" shouldn't have apostrophes in them, since the words are not possessive, but just plural.


---

Comment by hivert created at 2010-11-27 18:32:09

Replying to [comment:7 jason]:
> Extremely picky, minor, minor thing, but these words: "For now, list's, tuple's, set's, Set's are coerced into finite" shouldn't have apostrophes in them, since the words are not possessive, but just plural.

I reuploaded a new patche with the following diff folded:

```
diff --git a/sage/categories/enumerated_sets.py b/sage/categories/enumerated_sets.py
--- a/sage/categories/enumerated_sets.py
+++ b/sage/categories/enumerated_sets.py
`@``@` -103,7 +103,7 `@``@` class EnumeratedSets(Category):
             sage: EnumeratedSets()(Primes())
             Set of all prime numbers: 2, 3, 5, 7, ...
 
-        For now, list's, tuple's, set's, Set's are coerced into finite
+        For now, lists, tuples, sets, Sets are coerced into finite
         enumerated sets::
 
             sage: S = EnumeratedSets()([1, 2, 3]); S
```

So now you have to review it ;-)


---

Comment by hivert created at 2010-11-27 18:32:09

Changing status from positive_review to needs_work.


---

Attachment

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
`@``@` -83,7 +83,7 `@``@` diff --git a/sage/categories/finite_enum
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

Comment by hivert created at 2010-11-27 18:41:25

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-11-27 19:40:45

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-11-27 19:40:45

Looks good.


---

Comment by jason created at 2010-11-27 21:09:38

Looks good to me too.  Thanks for working on even the most minor nitpicky requests :).


---

Comment by jdemeyer created at 2011-01-12 06:32:11

Resolution: fixed
