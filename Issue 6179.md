# Issue 6179: html -- doctest failure in sage-4.0.1.alpha0

archive/issues_006179.json:
```json
{
    "body": "Assignee: tbd\n\nWe have the following on 32-bit OS X Intel:\n\n\n```\nsage -t -long \"devel/sage/sage/misc/html.py\"\n**********************************************************************\nFile \"/Users/was/build/sage-4.0.1.alpha0/devel/sage/sage/misc/html.py\", line 157:\n    sage: html.table([(i, j, i == j) for i in [0..1] for j in [0..1]])\nExpected:\n    <html>\n    <div class=\"notruncate\">\n    <table class=\"table_form\">\n    <tbody>\n    <tr class =\"row-a\">\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">True</span></td>\n    </tr>\n    <tr class =\"row-b\">\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">False</span></td>\n    </tr>\n    <tr class =\"row-a\">\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">False</span></td>\n    </tr>\n    <tr class =\"row-b\">\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">True</span></td>\n    </tr>  \n    </tbody>\n    </table>\n    </div>\n    </html>\nGot:\n    <html>\n    <div class=\"notruncate\">\n    <table class=\"table_form\">\n    <tbody>\n    <tr class =\"row-a\">\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">\\mbox{\\rm True}</span></td>\n    </tr>\n    <tr class =\"row-b\">\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">\\mbox{\\rm False}</span></td>\n    </tr>\n    <tr class =\"row-a\">\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">0</span></td>\n    <td><span class=\"math\">\\mbox{\\rm False}</span></td>\n    </tr>\n    <tr class =\"row-b\">\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">1</span></td>\n    <td><span class=\"math\">\\mbox{\\rm True}</span></td>\n    </tr>\n    </tbody>\n    </table>\n    </div>\n    </html>\n**********************************************************************\n1 items had failures:\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6179\n\n",
    "created_at": "2009-06-01T14:37:18Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "html -- doctest failure in sage-4.0.1.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6179",
    "user": "was"
}
```
Assignee: tbd

We have the following on 32-bit OS X Intel:


```
sage -t -long "devel/sage/sage/misc/html.py"
**********************************************************************
File "/Users/was/build/sage-4.0.1.alpha0/devel/sage/sage/misc/html.py", line 157:
    sage: html.table([(i, j, i == j) for i in [0..1] for j in [0..1]])
Expected:
    <html>
    <div class="notruncate">
    <table class="table_form">
    <tbody>
    <tr class ="row-a">
    <td><span class="math">0</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">True</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">0</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">False</span></td>
    </tr>
    <tr class ="row-a">
    <td><span class="math">1</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">False</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">1</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">True</span></td>
    </tr>  
    </tbody>
    </table>
    </div>
    </html>
Got:
    <html>
    <div class="notruncate">
    <table class="table_form">
    <tbody>
    <tr class ="row-a">
    <td><span class="math">0</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">\mbox{\rm True}</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">0</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">\mbox{\rm False}</span></td>
    </tr>
    <tr class ="row-a">
    <td><span class="math">1</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">\mbox{\rm False}</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">1</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">\mbox{\rm True}</span></td>
    </tr>
    </tbody>
    </table>
    </div>
    </html>
**********************************************************************
1 items had failures:

```


Issue created by migration from https://trac.sagemath.org/ticket/6179





---

archive/issue_comments_049333.json:
```json
{
    "body": "NOTE: The expected values are *wrong*.  Math typesetting of bools should use \\mbox{\\rm ...}.",
    "created_at": "2009-06-04T00:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49333",
    "user": "was"
}
```

NOTE: The expected values are *wrong*.  Math typesetting of bools should use \mbox{\rm ...}.



---

archive/issue_comments_049334.json:
```json
{
    "body": "On my 32-bit Debian with sage-4.0.1.alpha0:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: latex(True)\nTrue\nsage: latex(False)\nFalse\n```\n\n| Sage Version 4.0.1.alpha0, Release Date: 2009-05-31                |\n| Type notebook() for the GUI, and license() for information.        |\nand also:\n\n\n```\n$ ./sage -t devel/sage/sage/misc/html.py\nsage -t  \"devel/sage/sage/misc/html.py\"\n         [1.1 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 1.1 seconds\n```\n",
    "created_at": "2009-06-04T08:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49334",
    "user": "whuss"
}
```

On my 32-bit Debian with sage-4.0.1.alpha0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: latex(True)
True
sage: latex(False)
False
```

| Sage Version 4.0.1.alpha0, Release Date: 2009-05-31                |
| Type notebook() for the GUI, and license() for information.        |
and also:


```
$ ./sage -t devel/sage/sage/misc/html.py
sage -t  "devel/sage/sage/misc/html.py"
         [1.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.1 seconds
```




---

archive/issue_comments_049335.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-05T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49335",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049336.json:
```json
{
    "body": "Attachment [trac_6179.patch](tarball://root/attachments/some-uuid/ticket6179/trac_6179.patch) by mhansen created at 2009-06-05 21:21:49\n\nThis issue is that\n\n\n```\nsage: isinstance(True, int)\nTrue\nsage: isinstance(True, bool)\nTrue\nsage: isinstance(1, bool)\nFalse\n```\n\n\nso the output depended on the order in which items of the latex_table dict were iterated.  This is fixed by changing latex_table to a list so that bool comes first.",
    "created_at": "2009-06-05T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49336",
    "user": "mhansen"
}
```

Attachment [trac_6179.patch](tarball://root/attachments/some-uuid/ticket6179/trac_6179.patch) by mhansen created at 2009-06-05 21:21:49

This issue is that


```
sage: isinstance(True, int)
True
sage: isinstance(True, bool)
True
sage: isinstance(1, bool)
False
```


so the output depended on the order in which items of the latex_table dict were iterated.  This is fixed by changing latex_table to a list so that bool comes first.



---

archive/issue_comments_049337.json:
```json
{
    "body": "Changing assignee from tbd to mhansen.",
    "created_at": "2009-06-05T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49337",
    "user": "mhansen"
}
```

Changing assignee from tbd to mhansen.



---

archive/issue_comments_049338.json:
```json
{
    "body": "Here's another possible fix for the latex_table issue:\n\n``` \n        try:\n            f = latex_table[type(x)]\n            return LatexExpr(f(x))\n        except KeyError:\n            if x is None:\n                return LatexExpr(\"\\\\mbox{\\\\mathrm{None}}\")\n            return LatexExpr(str_function(str(x)))\n```\n\nSince `type(True)` returns `bool`, this looks up the right thing.  Is this approach better or worse than the one in your patch?  \n\nThe try/except approach helps to avoid accidental lookups in the table, but were those being used intentionally for anything?  For example, does `isinstance(blah, int)` return True for other classes that we care about for typesetting?  I tend to think that we should be more explicit rather than implicit (so add more entries `new-type: str` if we want more types to behave the way ints do), so I would favor the dictionary lookup approach.  I could be convinced otherwise, though.",
    "created_at": "2009-06-05T21:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49338",
    "user": "jhpalmieri"
}
```

Here's another possible fix for the latex_table issue:

``` 
        try:
            f = latex_table[type(x)]
            return LatexExpr(f(x))
        except KeyError:
            if x is None:
                return LatexExpr("\\mbox{\\mathrm{None}}")
            return LatexExpr(str_function(str(x)))
```

Since `type(True)` returns `bool`, this looks up the right thing.  Is this approach better or worse than the one in your patch?  

The try/except approach helps to avoid accidental lookups in the table, but were those being used intentionally for anything?  For example, does `isinstance(blah, int)` return True for other classes that we care about for typesetting?  I tend to think that we should be more explicit rather than implicit (so add more entries `new-type: str` if we want more types to behave the way ints do), so I would favor the dictionary lookup approach.  I could be convinced otherwise, though.



---

archive/issue_comments_049339.json:
```json
{
    "body": "I have no strong feelings on this; your patch is a tad more efficient, but none of this is really time critical. The latex_table should really only be used for builtin types though; anything else would be coupling things too much.",
    "created_at": "2009-06-05T22:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49339",
    "user": "mhansen"
}
```

I have no strong feelings on this; your patch is a tad more efficient, but none of this is really time critical. The latex_table should really only be used for builtin types though; anything else would be coupling things too much.



---

archive/issue_comments_049340.json:
```json
{
    "body": "I don't care about the efficiency, but I like that my patch is less ambiguous: with yours, if some unexpected type returns True for `isinstance(blah, int)`, then the latex could get screwed up.  It also depends on the ordering in the table.  My change was already in a patch (\"needs work\") for #6089, and in that patch it also gets used when constructing jsmath expressions.  So if you don't have a strong preference, I'll post my version of the patch here.\n\nThis includes your changes to html.py and your new doctest in latex.py, which I give a positive review to.",
    "created_at": "2009-06-05T22:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49340",
    "user": "jhpalmieri"
}
```

I don't care about the efficiency, but I like that my patch is less ambiguous: with yours, if some unexpected type returns True for `isinstance(blah, int)`, then the latex could get screwed up.  It also depends on the ordering in the table.  My change was already in a patch ("needs work") for #6089, and in that patch it also gets used when constructing jsmath expressions.  So if you don't have a strong preference, I'll post my version of the patch here.

This includes your changes to html.py and your new doctest in latex.py, which I give a positive review to.



---

archive/issue_comments_049341.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-06-05T22:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49341",
    "user": "jhpalmieri"
}
```

apply only this patch



---

archive/issue_comments_049342.json:
```json
{
    "body": "Attachment [trac_6179_version2.patch](tarball://root/attachments/some-uuid/ticket6179/trac_6179_version2.patch) by mhansen created at 2009-06-05 22:23:21\n\nLooks good to me.",
    "created_at": "2009-06-05T22:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49342",
    "user": "mhansen"
}
```

Attachment [trac_6179_version2.patch](tarball://root/attachments/some-uuid/ticket6179/trac_6179_version2.patch) by mhansen created at 2009-06-05 22:23:21

Looks good to me.



---

archive/issue_comments_049343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-06T00:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49343",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049344.json:
```json
{
    "body": "Merged in 4.0.1.rc3.",
    "created_at": "2009-06-06T00:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6179#issuecomment-49344",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc3.
