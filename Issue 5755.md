# Issue 5755: error converting symbolic expression to polynomial

archive/issues_005755.json:
```json
{
    "body": "CC:  jason mhansen\n\n\n```\nsage: xx = var('xx')\nsage: RDF['xx'](1.0*xx)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/12913/_Users_ncalexan_sage_3_4_rc0_devel_sage_main_sage_symbolic_test2_sage_3.py in <module>()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3627)()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _polynomial_(self, R)\n   2220                     not_found_v = False\n   2221             if not_found_v:\n-> 2222                 raise TypeError, \"%s is not a variable of %s\" %(v, R)\n   2223         if len(sub) == 0:\n   2224             try:\n\nTypeError: xx is not a variable of Univariate Polynomial Ring in xx over Real Double Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5755\n\n",
    "created_at": "2009-04-11T17:17:23Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "error converting symbolic expression to polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5755",
    "user": "ncalexan"
}
```
CC:  jason mhansen


```
sage: xx = var('xx')
sage: RDF['xx'](1.0*xx)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/12913/_Users_ncalexan_sage_3_4_rc0_devel_sage_main_sage_symbolic_test2_sage_3.py in <module>()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3627)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _polynomial_(self, R)
   2220                     not_found_v = False
   2221             if not_found_v:
-> 2222                 raise TypeError, "%s is not a variable of %s" %(v, R)
   2223         if len(sub) == 0:
   2224             try:

TypeError: xx is not a variable of Univariate Polynomial Ring in xx over Real Double Field
```


Issue created by migration from https://trac.sagemath.org/ticket/5755





---

archive/issue_comments_044984.json:
```json
{
    "body": "This will probably be fixed by the final resolution of #7007.",
    "created_at": "2009-09-29T18:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5755#issuecomment-44984",
    "user": "kcrisman"
}
```

This will probably be fixed by the final resolution of #7007.



---

archive/issue_comments_044985.json:
```json
{
    "body": "Since #7007 got positive review, here is the patch documenting the fix.",
    "created_at": "2009-09-30T18:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5755#issuecomment-44985",
    "user": "kcrisman"
}
```

Since #7007 got positive review, here is the patch documenting the fix.



---

archive/issue_comments_044986.json:
```json
{
    "body": "Attachment [trac_5755-symbolic-to-poly.patch](tarball://root/attachments/some-uuid/ticket5755/trac_5755-symbolic-to-poly.patch) by kcrisman created at 2009-09-30 18:59:33\n\nBased on 4.1.2.alpha4, depends on #7007",
    "created_at": "2009-09-30T18:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5755#issuecomment-44986",
    "user": "kcrisman"
}
```

Attachment [trac_5755-symbolic-to-poly.patch](tarball://root/attachments/some-uuid/ticket5755/trac_5755-symbolic-to-poly.patch) by kcrisman created at 2009-09-30 18:59:33

Based on 4.1.2.alpha4, depends on #7007



---

archive/issue_comments_044987.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-01T03:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5755#issuecomment-44987",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_044988.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T07:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5755#issuecomment-44988",
    "user": "mhansen"
}
```

Resolution: fixed
