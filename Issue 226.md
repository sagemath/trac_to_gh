# Issue 226: sagex enum issue and solution

archive/issues_000226.json:
```json
{
    "body": "Assignee: was\n\n\n```\nThe following code compiled just fine with 0.9.4.1\n \ncdef extern from \"whatever.h\":\n    ctypedef enum someenum_t:\n        ENUMVALUE_1\n        ENUMVALUE_2\n \ncdef somefunction(someenum_t val):\n    if val == ENUMVALUE_1:\n        print \"1\"\n    else:\n        print \"2\"\n \n \nWith 0.9.5 it gives the following error:\n/tmp/Pyrex-0.9.5/regression.pyx:8:11: Invalid types for '=='\n(someenum_t, someenum_t)\n \n \n anders\n \n \n_______________________________________________\nPyrex mailing list\nPyrex@lists.copyleft.no\nhttp://lists.copyleft.no/mailman/listinfo/pyrex\n--------\n\nI wrote:\n> /tmp/Pyrex-0.9.5/regression.pyx:8:11: Invalid types for '=='\n> (someenum_t, someenum_t)\n \nThis patch seems to help, but I don't know enough pyrex internals to\ntell if it is the correct solution.\n \n--- Pyrex-0.9.5/Pyrex/Compiler/ExprNodes.py     2007-01-27\n05:21:03.000000000 +0100\n+++ Pyrex-0.9.5-enumcmpfix/Pyrex/Compiler/ExprNodes.py  2007-01-28\n16:14:45.366599915 +0100\n@@ -2594,6 +2594,8 @@\n         elif (type1.is_numeric and type2.is_numeric\n                 and op not in ('is', 'is_not')):\n             return 1\n+        elif (type1.is_enum and type2.is_enum):\n+            return 1\n         else:\n             return 0\n \n \n \n_______________________________________________\nPyrex mailing list\nPyrex@lists.copyleft.no\nhttp://lists.copyleft.no/mailman/listinfo/pyrex\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/226\n\n",
    "created_at": "2007-01-28T20:27:20Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "sagex enum issue and solution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/226",
    "user": "was"
}
```
Assignee: was


```
The following code compiled just fine with 0.9.4.1
 
cdef extern from "whatever.h":
    ctypedef enum someenum_t:
        ENUMVALUE_1
        ENUMVALUE_2
 
cdef somefunction(someenum_t val):
    if val == ENUMVALUE_1:
        print "1"
    else:
        print "2"
 
 
With 0.9.5 it gives the following error:
/tmp/Pyrex-0.9.5/regression.pyx:8:11: Invalid types for '=='
(someenum_t, someenum_t)
 
 
 anders
 
 
_______________________________________________
Pyrex mailing list
Pyrex@lists.copyleft.no
http://lists.copyleft.no/mailman/listinfo/pyrex
--------

I wrote:
> /tmp/Pyrex-0.9.5/regression.pyx:8:11: Invalid types for '=='
> (someenum_t, someenum_t)
 
This patch seems to help, but I don't know enough pyrex internals to
tell if it is the correct solution.
 
--- Pyrex-0.9.5/Pyrex/Compiler/ExprNodes.py     2007-01-27
05:21:03.000000000 +0100
+++ Pyrex-0.9.5-enumcmpfix/Pyrex/Compiler/ExprNodes.py  2007-01-28
16:14:45.366599915 +0100
@@ -2594,6 +2594,8 @@
         elif (type1.is_numeric and type2.is_numeric
                 and op not in ('is', 'is_not')):
             return 1
+        elif (type1.is_enum and type2.is_enum):
+            return 1
         else:
             return 0
 
 
 
_______________________________________________
Pyrex mailing list
Pyrex@lists.copyleft.no
http://lists.copyleft.no/mailman/listinfo/pyrex
```


Issue created by migration from https://trac.sagemath.org/ticket/226





---

archive/issue_comments_001007.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T17:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/226#issuecomment-1007",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001008.json:
```json
{
    "body": "The problem has been fixed in a previous release of cython.\ncython regression.pyx now works fine.",
    "created_at": "2007-08-18T17:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/226#issuecomment-1008",
    "user": "mabshoff"
}
```

The problem has been fixed in a previous release of cython.
cython regression.pyx now works fine.
