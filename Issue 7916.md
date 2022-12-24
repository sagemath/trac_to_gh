# Issue 7916: change conjugate(X) to try X.conjugate()  [[this is easy!!]]

archive/issues_007916.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  rossk\n\n\n```\nOn Tue, Jan 12, 2010 at 8:36 PM, jtyard <> wrote:\n> Hi,\n>\n> I don't know if this counts as a bug, so sorry if I'm posting this to\n> the wrong list.  Say I define a cyclotomic field in Sage as follows:\n>\n> sage: Q3 = CyclotomicField(3)\n> sage: z3 = Q3.0\n>\n> Then Sage can compute the complex conjugate independent of an\n> embedding into the complexes:\n>\n> sage: z3.conjugate()\n> -zeta3 - 1\n>\n> But I get a different answer by typing:\n>\n> sage: conjugate(z3)\n> conjugate(e^(2/3*I*pi))\n>\n> Wouldn't it make sense for these to do the same thing?  Another\n> difference comes up as follows:\n>\n> sage: Q2.<s> = QuadraticField(-2)\n> sage: s.conjugate()\n> -s\n> sage: conjugate(s)\n> -I*sqrt(2)\n>\n> Yet, the problem doesn't exist with this slightly different\n> definition:\n>\n> sage: QQ2.<ss> = QQ[sqrt(-2)]\n> sage: ss.conjugate()\n> -a\n> sage: conjugate(ss)\n> -a\n\nYes, I agree that this is a bug.  \nWhat is happening is that the *symbolic* conjugate function is coercing its input X to the symbolic ring SR before applying itself.  It would be much better to test if X has a .conjugate method, and if so return that; if not, then return SR(X).conjugate().\n\nHere's the beginning of the course code for conjugate(X):\n\nsage: conjugate.__call__??\n        # we want to convert the result to the original parent if the input\n        # is not exact, so we store the parent here\n        org_parent = parent(args[0])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7916\n\n",
    "created_at": "2010-01-13T05:00:37Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "change conjugate(X) to try X.conjugate()  [[this is easy!!]]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7916",
    "user": "@williamstein"
}
```
Assignee: @burcin

CC:  rossk


```
On Tue, Jan 12, 2010 at 8:36 PM, jtyard <> wrote:
> Hi,
>
> I don't know if this counts as a bug, so sorry if I'm posting this to
> the wrong list.  Say I define a cyclotomic field in Sage as follows:
>
> sage: Q3 = CyclotomicField(3)
> sage: z3 = Q3.0
>
> Then Sage can compute the complex conjugate independent of an
> embedding into the complexes:
>
> sage: z3.conjugate()
> -zeta3 - 1
>
> But I get a different answer by typing:
>
> sage: conjugate(z3)
> conjugate(e^(2/3*I*pi))
>
> Wouldn't it make sense for these to do the same thing?  Another
> difference comes up as follows:
>
> sage: Q2.<s> = QuadraticField(-2)
> sage: s.conjugate()
> -s
> sage: conjugate(s)
> -I*sqrt(2)
>
> Yet, the problem doesn't exist with this slightly different
> definition:
>
> sage: QQ2.<ss> = QQ[sqrt(-2)]
> sage: ss.conjugate()
> -a
> sage: conjugate(ss)
> -a

Yes, I agree that this is a bug.  
What is happening is that the *symbolic* conjugate function is coercing its input X to the symbolic ring SR before applying itself.  It would be much better to test if X has a .conjugate method, and if so return that; if not, then return SR(X).conjugate().

Here's the beginning of the course code for conjugate(X):

sage: conjugate.__call__??
        # we want to convert the result to the original parent if the input
        # is not exact, so we store the parent here
        org_parent = parent(args[0])
```


Issue created by migration from https://trac.sagemath.org/ticket/7916





---

archive/issue_comments_068882.json:
```json
{
    "body": "Attachment [trac_7916-same_name_method.patch](tarball://root/attachments/some-uuid/ticket7916/trac_7916-same_name_method.patch) by @burcin created at 2010-01-17 11:39:25",
    "created_at": "2010-01-17T11:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68882",
    "user": "@burcin"
}
```

Attachment [trac_7916-same_name_method.patch](tarball://root/attachments/some-uuid/ticket7916/trac_7916-same_name_method.patch) by @burcin created at 2010-01-17 11:39:25



---

archive/issue_comments_068883.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T11:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68883",
    "user": "@burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068884.json:
```json
{
    "body": "Does [trac_7916-same_name_method.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.patch) depend on anything? I got one hunk failure when applying [trac_7916-same_name_method.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.patch) on top of Sage 4.3.1.rc0:\n\n```\n[mvngu@mod sage-main]$ pwd\n/dev/shm/mvngu/sage-4.3.1.rc0-7916/devel/sage-main\n[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7916/trac_7916-same_name_method.patch\nadding trac_7916-same_name_method.patch to series file\n[mvngu@mod sage-main]$ hg qpush\napplying trac_7916-same_name_method.patch\npatching file sage/symbolic/function.pyx\nHunk #1 FAILED at 550\n1 out of 1 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_7916-same_name_method.patch\n[mvngu@mod sage-main]$ cat sage/symbolic/function.pyx.rej\n--- function.pyx\n+++ function.pyx\n@@ -551,10 +551,30 @@\n             # we should never end up here\n             raise ValueError, \"cannot read pickle\"\n \n-    def __call__(self, *args, coerce=True, hold=False):\n+    def __call__(self, *args, coerce=True, hold=False,\n+            dont_call_method_on_arg=False):\n+        \"\"\"\n+        Evaluate this function on the given arguments and return the result.\n+\n+        EXAMPLES::\n+\n+            sage: exp(5)\n+            e^5\n+            sage: gamma(15)\n+            87178291200\n+        \"\"\"\n         # we want to convert the result to the original parent if the input\n         # is not exact, so we store the parent here\n         org_parent = parent_c(args[0])\n+        \n+        # if there is only one argument, and the argument has an attribute\n+        # with the same name as this function, try to call it to get the result\n+        # The argument dont_call_method_on_arg is used to prevent infinite loops\n+        # when .exp(), .log(), etc. methods call this symbolic function on \n+        # themselves\n+        if len(args) == 1 and not hold and not dont_call_method_on_arg and \\\n+                hasattr(args[0], self._name):\n+            return getattr(args[0], self._name)()\n \n         res = super(GinacFunction, self).__call__(*args, coerce=coerce,\n                 hold=hold)\n```\n",
    "created_at": "2010-01-18T02:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68884",
    "user": "mvngu"
}
```

Does [trac_7916-same_name_method.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.patch) depend on anything? I got one hunk failure when applying [trac_7916-same_name_method.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.patch) on top of Sage 4.3.1.rc0:

```
[mvngu@mod sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.1.rc0-7916/devel/sage-main
[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7916/trac_7916-same_name_method.patch
adding trac_7916-same_name_method.patch to series file
[mvngu@mod sage-main]$ hg qpush
applying trac_7916-same_name_method.patch
patching file sage/symbolic/function.pyx
Hunk #1 FAILED at 550
1 out of 1 hunks FAILED -- saving rejects to file sage/symbolic/function.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7916-same_name_method.patch
[mvngu@mod sage-main]$ cat sage/symbolic/function.pyx.rej
--- function.pyx
+++ function.pyx
@@ -551,10 +551,30 @@
             # we should never end up here
             raise ValueError, "cannot read pickle"
 
-    def __call__(self, *args, coerce=True, hold=False):
+    def __call__(self, *args, coerce=True, hold=False,
+            dont_call_method_on_arg=False):
+        """
+        Evaluate this function on the given arguments and return the result.
+
+        EXAMPLES::
+
+            sage: exp(5)
+            e^5
+            sage: gamma(15)
+            87178291200
+        """
         # we want to convert the result to the original parent if the input
         # is not exact, so we store the parent here
         org_parent = parent_c(args[0])
+        
+        # if there is only one argument, and the argument has an attribute
+        # with the same name as this function, try to call it to get the result
+        # The argument dont_call_method_on_arg is used to prevent infinite loops
+        # when .exp(), .log(), etc. methods call this symbolic function on 
+        # themselves
+        if len(args) == 1 and not hold and not dont_call_method_on_arg and \
+                hasattr(args[0], self._name):
+            return getattr(args[0], self._name)()
 
         res = super(GinacFunction, self).__call__(*args, coerce=coerce,
                 hold=hold)
```




---

archive/issue_comments_068885.json:
```json
{
    "body": "Sorry for the inconvenience. My patch queue contains all the fixes from yesterday. I forgot to check dependencies.\n\nThis depends on #7822. You can apply the patch there now, it doesn't depend on any changes in pynac. The timing will be better with the new pynac spkg though.",
    "created_at": "2010-01-18T04:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68885",
    "user": "@burcin"
}
```

Sorry for the inconvenience. My patch queue contains all the fixes from yesterday. I forgot to check dependencies.

This depends on #7822. You can apply the patch there now, it doesn't depend on any changes in pynac. The timing will be better with the new pynac spkg though.



---

archive/issue_comments_068886.json:
```json
{
    "body": "slightly faster - apply only this patch",
    "created_at": "2010-01-19T13:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68886",
    "user": "@burcin"
}
```

slightly faster - apply only this patch



---

archive/issue_comments_068887.json:
```json
{
    "body": "Attachment [trac_7916-same_name_method.take2.patch](tarball://root/attachments/some-uuid/ticket7916/trac_7916-same_name_method.take2.patch) by @burcin created at 2010-01-19 13:13:00\n\nattachment:trac_7916-same_name_method.take2.patch is slightly faster than the previous one.",
    "created_at": "2010-01-19T13:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68887",
    "user": "@burcin"
}
```

Attachment [trac_7916-same_name_method.take2.patch](tarball://root/attachments/some-uuid/ticket7916/trac_7916-same_name_method.take2.patch) by @burcin created at 2010-01-19 13:13:00

attachment:trac_7916-same_name_method.take2.patch is slightly faster than the previous one.



---

archive/issue_comments_068888.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T21:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68888",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068889.json:
```json
{
    "body": "A good solution.  The timing changes seem to be unavoidable, given that we don't want conjugate(e^(2/3*I*pi)) as the result, and they seem identical otherwise:\n\n```\nsage: %timeit z3.conjugate()\n625 loops, best of 3: 469 \u00b5s per loop\nsage: %timeit conjugate(z3)\n625 loops, best of 3: 469 \u00b5s per loop\n```\n",
    "created_at": "2010-01-28T21:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68889",
    "user": "@kcrisman"
}
```

A good solution.  The timing changes seem to be unavoidable, given that we don't want conjugate(e^(2/3*I*pi)) as the result, and they seem identical otherwise:

```
sage: %timeit z3.conjugate()
625 loops, best of 3: 469 µs per loop
sage: %timeit conjugate(z3)
625 loops, best of 3: 469 µs per loop
```




---

archive/issue_comments_068890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68890",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_068891.json:
```json
{
    "body": "Merged [trac_7916-same_name_method.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.take2.patch).",
    "created_at": "2010-02-18T21:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7916#issuecomment-68891",
    "user": "mvngu"
}
```

Merged [trac_7916-same_name_method.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.take2.patch).
