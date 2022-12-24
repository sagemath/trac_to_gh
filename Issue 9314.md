# Issue 9314: LaTeX representation of negative symbolic fractions still broken

archive/issues_009314.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  was\n\nI think #9086 isn't completly fixed:\n\n {{{\n sage: var('x y')\n sage: latex(-x/y) \n \\frac{x}{y}\n }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/9314\n\n",
    "created_at": "2010-06-22T18:19:43Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "LaTeX representation of negative symbolic fractions still broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9314",
    "user": "damm"
}
```
Assignee: AlexGhitza

CC:  was

I think #9086 isn't completly fixed:

 {{{
 sage: var('x y')
 sage: latex(-x/y) 
 \frac{x}{y}
 }}}

Issue created by migration from https://trac.sagemath.org/ticket/9314





---

archive/issue_comments_087747.json:
```json
{
    "body": "Changing component from algebra to symbolics.",
    "created_at": "2010-06-22T19:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87747",
    "user": "leif"
}
```

Changing component from algebra to symbolics.



---

archive/issue_comments_087748.json:
```json
{
    "body": "Changing assignee from AlexGhitza to burcin.",
    "created_at": "2010-06-22T19:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87748",
    "user": "leif"
}
```

Changing assignee from AlexGhitza to burcin.



---

archive/issue_comments_087749.json:
```json
{
    "body": "Changing keywords from \"\" to \"latex, sign, minus, pynac\".",
    "created_at": "2010-06-22T19:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87749",
    "user": "leif"
}
```

Changing keywords from "" to "latex, sign, minus, pynac".



---

archive/issue_comments_087750.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-06-22T19:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87750",
    "user": "leif"
}
```

Changing priority from major to critical.



---

archive/issue_comments_087751.json:
```json
{
    "body": "These are correct, but don't look that nice:\n\n```\nsage: latex(-(-x^2/-x^5))\n\\frac{-1}{x^{3}}\nsage: latex(-(x^2/x^5))\n\\frac{-1}{x^{3}}\nsage: latex(-((-x)^2/x^5))\n\\frac{-1}{x^{3}}\nsage: latex(x^2/-x^5)\n\\frac{-1}{x^{3}}\nsage: latex(x^2/(-x)^5)\n\\frac{-1}{x^{3}}\nsage: latex(-(-2*x^2/-x^5))\n\\frac{-2}{x^{3}}\nsage: latex(-(-x^2/(-3*x^5)))\n\\frac{-1}{3 \\, x^{3}}\n```\n",
    "created_at": "2010-06-22T19:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87751",
    "user": "leif"
}
```

These are correct, but don't look that nice:

```
sage: latex(-(-x^2/-x^5))
\frac{-1}{x^{3}}
sage: latex(-(x^2/x^5))
\frac{-1}{x^{3}}
sage: latex(-((-x)^2/x^5))
\frac{-1}{x^{3}}
sage: latex(x^2/-x^5)
\frac{-1}{x^{3}}
sage: latex(x^2/(-x)^5)
\frac{-1}{x^{3}}
sage: latex(-(-2*x^2/-x^5))
\frac{-2}{x^{3}}
sage: latex(-(-x^2/(-3*x^5)))
\frac{-1}{3 \, x^{3}}
```




---

archive/issue_comments_087752.json:
```json
{
    "body": "(Note that the above are all broken, i.e. lose their sign, if one `x` is replaced by `y`.)",
    "created_at": "2010-06-22T19:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87752",
    "user": "leif"
}
```

(Note that the above are all broken, i.e. lose their sign, if one `x` is replaced by `y`.)



---

archive/issue_comments_087753.json:
```json
{
    "body": "i just got a report that this is also broken for\n\n```\nsage: var('a b')\nsage: latex(-1 * (a/b))\n```\n\n\ncan we make this a blocker?",
    "created_at": "2010-07-06T15:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87753",
    "user": "schilly"
}
```

i just got a report that this is also broken for

```
sage: var('a b')
sage: latex(-1 * (a/b))
```


can we make this a blocker?



---

archive/issue_comments_087754.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-07-08T09:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87754",
    "user": "burcin"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_087755.json:
```json
{
    "body": "This is really embarrassing. I'll fix this tonight.",
    "created_at": "2010-07-08T09:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87755",
    "user": "burcin"
}
```

This is really embarrassing. I'll fix this tonight.



---

archive/issue_comments_087756.json:
```json
{
    "body": "Ping.",
    "created_at": "2010-07-10T09:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87756",
    "user": "mhansen"
}
```

Ping.



---

archive/issue_comments_087757.json:
```json
{
    "body": "It ended up begin an extended night. I'm looking at it right now.",
    "created_at": "2010-07-10T10:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87757",
    "user": "burcin"
}
```

It ended up begin an extended night. I'm looking at it right now.



---

archive/issue_comments_087758.json:
```json
{
    "body": "Attachment [trac_9314-latex_mul.patch](tarball://root/attachments/some-uuid/ticket9314/trac_9314-latex_mul.patch) by burcin created at 2010-07-11 16:03:27",
    "created_at": "2010-07-11T16:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87758",
    "user": "burcin"
}
```

Attachment [trac_9314-latex_mul.patch](tarball://root/attachments/some-uuid/ticket9314/trac_9314-latex_mul.patch) by burcin created at 2010-07-11 16:03:27



---

archive/issue_comments_087759.json:
```json
{
    "body": "The pynac package at\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.p4.spkg\n\ncontains a fix for this. I want to keep this as easy to review as possible, so the only change is the following simple patch:\n\n\n```\ndiff --git a/ginac/mul.cpp b/ginac/mul.cpp\n--- a/ginac/mul.cpp\n+++ b/ginac/mul.cpp\n@@ -268,6 +268,10 @@\n \t\t\t     }\n \t\t\t} else {\n \t\t\t     if (numer.is_equal(_ex1) || numer.is_equal(_ex_1)) {\n+\t\t\t          const numeric &coeff = ex_to<numeric>(numer);\n+\t\t\t\t  if (coeff.is_equal(*_num_1_p) && !coeff.is_parent_pos_char()) {\n+\t\t\t\t        c.s<<\"-\";\n+\t\t\t\t  }\n \t\t\t         mul(others).eval().print(c);\n \t\t\t     } else {\n \t\t\t\t mul(numer,mul(others).eval()).hold().print(c);\n```\n\n\nattachment:trac_9314-latex_mul.patch has the doctest fixes for the Sage library.\n\nI will take care of the pretty printing issues from comment:3 later.",
    "created_at": "2010-07-11T16:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87759",
    "user": "burcin"
}
```

The pynac package at

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.p4.spkg

contains a fix for this. I want to keep this as easy to review as possible, so the only change is the following simple patch:


```
diff --git a/ginac/mul.cpp b/ginac/mul.cpp
--- a/ginac/mul.cpp
+++ b/ginac/mul.cpp
@@ -268,6 +268,10 @@
 			     }
 			} else {
 			     if (numer.is_equal(_ex1) || numer.is_equal(_ex_1)) {
+			          const numeric &coeff = ex_to<numeric>(numer);
+				  if (coeff.is_equal(*_num_1_p) && !coeff.is_parent_pos_char()) {
+				        c.s<<"-";
+				  }
 			         mul(others).eval().print(c);
 			     } else {
 				 mul(numer,mul(others).eval()).hold().print(c);
```


attachment:trac_9314-latex_mul.patch has the doctest fixes for the Sage library.

I will take care of the pretty printing issues from comment:3 later.



---

archive/issue_comments_087760.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-11T16:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87760",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087761.json:
```json
{
    "body": "The new spkg installed fine for me on 4.5.rc0 (+patches at #7379), then the patch applied fine and tests pass ( itested the whole library but without -long).  So, while I cannot tell whether the four lines of C++ added to ginac/mul.cpp are correct, this is certainly an improvement and enough to make me give it a positive review.",
    "created_at": "2010-07-12T13:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87761",
    "user": "cremona"
}
```

The new spkg installed fine for me on 4.5.rc0 (+patches at #7379), then the patch applied fine and tests pass ( itested the whole library but without -long).  So, while I cannot tell whether the four lines of C++ added to ginac/mul.cpp are correct, this is certainly an improvement and enough to make me give it a positive review.



---

archive/issue_comments_087762.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-12T13:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87762",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087763.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-13T16:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87763",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_087764.json:
```json
{
    "body": "Applied\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.p4.spkg\n\nand\n\nattachment:trac_9314-latex_mul.patch\n\nto sage-4.5.rc1.",
    "created_at": "2010-07-13T16:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9314#issuecomment-87764",
    "user": "rlm"
}
```

Applied

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.p4.spkg

and

attachment:trac_9314-latex_mul.patch

to sage-4.5.rc1.
