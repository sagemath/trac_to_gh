# Issue 7535: Errors should be raised, not returned.

archive/issues_007535.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: error return\n\nThe following issue was considered in at least two threads, the latest at [http://groups.google.com/group/sage-devel/browse_thread/thread/3661fde739474fdb](http://groups.google.com/group/sage-devel/browse_thread/thread/3661fde739474fdb).\n\nThere are several places in the Sage code where errors are not raised but returned. A hopefully exhaustive search brought up the following:\n\n```\nsage: import exceptions\nsage: for E in dir(exceptions):\n....:     if not E.startswith('__'):\n....:         s = search_src(\"return \"+E)\n....:         if s:\n....:             print s\n....:\nrings/finite_field_element.py:384:                return ArithmeticError, \"Multiplicative order of 0 not defined.\"\nrings/finite_field_givaro.pyx:1956:                return ArithmeticError, \"Multiplicative order of 0 not defined.\"\nstructure/element.pyx:2601:            return ArithmeticError, \"Multiplicative order of 0 not defined.\"\n\nrings/ring.pyx:687:            return NotImplementedError\nmodular/hecke/module.py:706:        abstract base class, return NotImplementedError.\nmodular/arithgroup/congroup_gammaH.py:928:            return NotImplementedError\ngeometry/polyhedra.py:1068:            return NotImplementedError\nsymbolic/expression.pyx:1524:        return NotImplementedError\nsymbolic/expression_conversions.py:638:            return NotImplementedError(\"SymPy function '%s' doesn't exist\" % f)\n\ninterfaces/gap.py:580:            return RuntimeError, \"Error evaluating %s in %s\"%(line, self)\n\nmodular/abvar/finite_subgroup.py:280:            return ValueError, \"self and other must be in the same ambient Jacobian\"\ngroups/perm_gps/permgroup_named.py:945:            return ValueError, \"Degree must be 2.\"\ngroups/perm_gps/permgroup_named.py:988:            return ValueError, \"Degree must be 2.\"\n```\n\n\nOf course, if an error is returned it can't be catched, which implies obvious problems.\n\nI have no idea what component that ticket should be associated with. \"Performance\" seemed the least inappropriate description to me.\n\nIs there any of the above cases in which the error should really be returned, not raised?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7535\n\n",
    "created_at": "2009-11-26T10:24:15Z",
    "labels": [
        "performance",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Errors should be raised, not returned.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7535",
    "user": "@simon-king-jena"
}
```
Assignee: tbd

Keywords: error return

The following issue was considered in at least two threads, the latest at [http://groups.google.com/group/sage-devel/browse_thread/thread/3661fde739474fdb](http://groups.google.com/group/sage-devel/browse_thread/thread/3661fde739474fdb).

There are several places in the Sage code where errors are not raised but returned. A hopefully exhaustive search brought up the following:

```
sage: import exceptions
sage: for E in dir(exceptions):
....:     if not E.startswith('__'):
....:         s = search_src("return "+E)
....:         if s:
....:             print s
....:
rings/finite_field_element.py:384:                return ArithmeticError, "Multiplicative order of 0 not defined."
rings/finite_field_givaro.pyx:1956:                return ArithmeticError, "Multiplicative order of 0 not defined."
structure/element.pyx:2601:            return ArithmeticError, "Multiplicative order of 0 not defined."

rings/ring.pyx:687:            return NotImplementedError
modular/hecke/module.py:706:        abstract base class, return NotImplementedError.
modular/arithgroup/congroup_gammaH.py:928:            return NotImplementedError
geometry/polyhedra.py:1068:            return NotImplementedError
symbolic/expression.pyx:1524:        return NotImplementedError
symbolic/expression_conversions.py:638:            return NotImplementedError("SymPy function '%s' doesn't exist" % f)

interfaces/gap.py:580:            return RuntimeError, "Error evaluating %s in %s"%(line, self)

modular/abvar/finite_subgroup.py:280:            return ValueError, "self and other must be in the same ambient Jacobian"
groups/perm_gps/permgroup_named.py:945:            return ValueError, "Degree must be 2."
groups/perm_gps/permgroup_named.py:988:            return ValueError, "Degree must be 2."
```


Of course, if an error is returned it can't be catched, which implies obvious problems.

I have no idea what component that ticket should be associated with. "Performance" seemed the least inappropriate description to me.

Is there any of the above cases in which the error should really be returned, not raised?


Issue created by migration from https://trac.sagemath.org/ticket/7535





---

archive/issue_comments_063905.json:
```json
{
    "body": "See also #7532.",
    "created_at": "2009-11-26T15:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63905",
    "user": "@jhpalmieri"
}
```

See also #7532.



---

archive/issue_comments_063906.json:
```json
{
    "body": "Changing component from performance to misc.",
    "created_at": "2010-01-18T19:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63906",
    "user": "@TimDumol"
}
```

Changing component from performance to misc.



---

archive/issue_comments_063907.json:
```json
{
    "body": "This should do the trick.",
    "created_at": "2010-01-18T20:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63907",
    "user": "@TimDumol"
}
```

This should do the trick.



---

archive/issue_comments_063908.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T20:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63908",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063909.json:
```json
{
    "body": "Makes all remaining returns of exceptions into raising.",
    "created_at": "2010-01-18T20:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63909",
    "user": "@TimDumol"
}
```

Makes all remaining returns of exceptions into raising.



---

archive/issue_comments_063910.json:
```json
{
    "body": "Attachment [trac_7535-errors-raise.patch](tarball://root/attachments/some-uuid/ticket7535/trac_7535-errors-raise.patch) by @jhpalmieri created at 2010-01-19 00:44:35\n\nI'm not sure what you mean by \"remaining\", since there is no patch at #7532 (or elsewhere?) fixing any other instances of this.  I'm attaching a patch dealing with two more of these, leaving, I think, just the one in rings.pyx.  See #7532 for that one.\n\nPositive review for timdumol's patch, so if mine is okay, this whole ticket can get a positive review.",
    "created_at": "2010-01-19T00:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63910",
    "user": "@jhpalmieri"
}
```

Attachment [trac_7535-errors-raise.patch](tarball://root/attachments/some-uuid/ticket7535/trac_7535-errors-raise.patch) by @jhpalmieri created at 2010-01-19 00:44:35

I'm not sure what you mean by "remaining", since there is no patch at #7532 (or elsewhere?) fixing any other instances of this.  I'm attaching a patch dealing with two more of these, leaving, I think, just the one in rings.pyx.  See #7532 for that one.

Positive review for timdumol's patch, so if mine is okay, this whole ticket can get a positive review.



---

archive/issue_comments_063911.json:
```json
{
    "body": "apply on top of the other patch",
    "created_at": "2010-01-19T00:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63911",
    "user": "@jhpalmieri"
}
```

apply on top of the other patch



---

archive/issue_comments_063912.json:
```json
{
    "body": "Attachment [trac_7535-part2.patch](tarball://root/attachments/some-uuid/ticket7535/trac_7535-part2.patch) by @JohnCremona created at 2010-01-19 12:43:09\n\nI am about to add a patch to #7532 which fixes (for me) the remaining issue in schemes/elliptic_curves.",
    "created_at": "2010-01-19T12:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63912",
    "user": "@JohnCremona"
}
```

Attachment [trac_7535-part2.patch](tarball://root/attachments/some-uuid/ticket7535/trac_7535-part2.patch) by @JohnCremona created at 2010-01-19 12:43:09

I am about to add a patch to #7532 which fixes (for me) the remaining issue in schemes/elliptic_curves.



---

archive/issue_comments_063913.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63913",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063914.json:
```json
{
    "body": "Doctests pass with the latter patch and the one in #7532, so I'll mark both as positive review.",
    "created_at": "2010-01-20T09:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63914",
    "user": "@TimDumol"
}
```

Doctests pass with the latter patch and the one in #7532, so I'll mark both as positive review.



---

archive/issue_comments_063915.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_7535-errors-raise.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7535/trac_7535-errors-raise.patch) --- timdumol: please remember to put  your username in your patch. I have merged this patch in your name.\n2. [trac_7535-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7535/trac_7535-part2.patch)",
    "created_at": "2010-01-23T19:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63915",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_7535-errors-raise.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7535/trac_7535-errors-raise.patch) --- timdumol: please remember to put  your username in your patch. I have merged this patch in your name.
2. [trac_7535-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7535/trac_7535-part2.patch)



---

archive/issue_comments_063916.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T19:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7535#issuecomment-63916",
    "user": "mvngu"
}
```

Resolution: fixed
