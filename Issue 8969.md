# Issue 8969: problems with maxima inequalities

archive/issues_008969.json:
```json
{
    "body": "Assignee: @burcin\n\n'Sage Version 4.4.1, Release Date: 2010-05-02'\nmac 10.4 32 bit running on 10.5.8.\n\nsage: solve([2*x==3, x < 10], x)\n[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)\nsage: solve([2*x==3, x > 10], x)\n[]\nsage: solve([2*x==3, x == 10], x)\n[]\nsage: solve([2*x==3, x == 3/2], x)\n[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)\n\nsage: solve([2*x==3, x < 4, x > 4], x)\n[]\n\n\nall work as expected, but:\n\nsage: solve([2*x==3, x != 5], x)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Applications/sage/devel/sage-main/build/sage/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)\n    670                 s = []\n    671 \n--> 672         sol_list = string_to_list_of_solutions(repr(s))\n    673         if 'solution_dict' in kwds and kwds!['solution_dict']==True:\n    674             if isinstance(sol_list![0], list):\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in string_to_list_of_solutions(s)\n    455     from sage.structure.sequence import Sequence\n    456     from sage.calculus.calculus import symbolic_expression_from_maxima_string\n--> 457     v = symbolic_expression_from_maxima_string(s, equals_sub=True)\n    458     return Sequence(v, universe=Objects(), cr_str=True)\n    459 \n\n/Applications/sage/local/lib/python2.6/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_string(x, equals_sub, maxima)\n   1527         return symbolic_expression_from_string(s, syms, accept_sequence=True)\n   1528     except !!SyntaxError:\n-> 1529         raise TypeError, \"unable to make sense of Maxima expression '%s' in Sage\"%s\n   1530     finally:\n   1531         is_simplified = False\n\nTypeError: unable to make sense of Maxima expression '[This is the Trac macro *x==3/2,-7/2!==0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x==3/2,-7/2!==0-macro)' in Sage\n\n--\n\nThe \"!==\" which is causing trouble is due to the\n\nif equals_sub:\n\u00a0\u00a0\u00a0\u00a0        s = s.replace('=','==')\n\nlines in  symbolic_expression_from_maxima_string.  This could be fixed by changing the replace to a regexp, or adding a hack s = s.replace('!==', '!=') afterwards.\n\nThis deals with the obvious problem but not the underlying one, which is that the result is still IMHO underprocessed: \n\nMODIFIED_sage: solve([2*x==3, x != 4], x)\n[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), )](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)\n\nwhen I wanted [This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro), or\n\nMODIFIED_sage: solve([2*x==3, x != 3/2], x)\n[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), 0 != 0)](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)\n\nwhen I wanted [].\n\nIn fact, even in cases not involving \"!=\", it's possible for maxima output -- %union([x = 3/2,\u00a0 -5/2 # 0]) --\u00a0 to be insufficiently processed,IMHO:\n\nsage: solve([2*x==3, (x-4)!^2 > 0], x)\n[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), )](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)\n\nISTM the extra information about what condition maxima used isn't worth the inconvenience of having to postprocess the solutions to see if one exists.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8969\n\n",
    "created_at": "2010-05-14T20:43:15Z",
    "labels": [
        "component: symbolics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "problems with maxima inequalities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8969",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```
Assignee: @burcin

'Sage Version 4.4.1, Release Date: 2010-05-02'
mac 10.4 32 bit running on 10.5.8.

sage: solve([2*x==3, x < 10], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)
sage: solve([2*x==3, x > 10], x)
[]
sage: solve([2*x==3, x == 10], x)
[]
sage: solve([2*x==3, x == 3/2], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

sage: solve([2*x==3, x < 4, x > 4], x)
[]


all work as expected, but:

sage: solve([2*x==3, x != 5], x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Applications/sage/devel/sage-main/build/sage/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)
    670                 s = []
    671 
--> 672         sol_list = string_to_list_of_solutions(repr(s))
    673         if 'solution_dict' in kwds and kwds!['solution_dict']==True:
    674             if isinstance(sol_list![0], list):

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in string_to_list_of_solutions(s)
    455     from sage.structure.sequence import Sequence
    456     from sage.calculus.calculus import symbolic_expression_from_maxima_string
--> 457     v = symbolic_expression_from_maxima_string(s, equals_sub=True)
    458     return Sequence(v, universe=Objects(), cr_str=True)
    459 

/Applications/sage/local/lib/python2.6/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_string(x, equals_sub, maxima)
   1527         return symbolic_expression_from_string(s, syms, accept_sequence=True)
   1528     except !!SyntaxError:
-> 1529         raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s
   1530     finally:
   1531         is_simplified = False

TypeError: unable to make sense of Maxima expression '[This is the Trac macro *x==3/2,-7/2!==0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x==3/2,-7/2!==0-macro)' in Sage

--

The "!==" which is causing trouble is due to the

if equals_sub:
            s = s.replace('=','==')

lines in  symbolic_expression_from_maxima_string.  This could be fixed by changing the replace to a regexp, or adding a hack s = s.replace('!==', '!=') afterwards.

This deals with the obvious problem but not the underlying one, which is that the result is still IMHO underprocessed: 

MODIFIED_sage: solve([2*x==3, x != 4], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), )](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

when I wanted [This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro), or

MODIFIED_sage: solve([2*x==3, x != 3/2], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), 0 != 0)](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

when I wanted [].

In fact, even in cases not involving "!=", it's possible for maxima output -- %union([x = 3/2,  -5/2 # 0]) --  to be insufficiently processed,IMHO:

sage: solve([2*x==3, (x-4)!^2 > 0], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), )](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

ISTM the extra information about what condition maxima used isn't worth the inconvenience of having to postprocess the solutions to see if one exists.

Issue created by migration from https://trac.sagemath.org/ticket/8969





---

archive/issue_comments_082519.json:
```json
{
    "body": "DSM, is this really all one ticket? It's kind of confusing.",
    "created_at": "2011-06-14T17:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82519",
    "user": "https://github.com/kcrisman"
}
```

DSM, is this really all one ticket? It's kind of confusing.



---

archive/issue_comments_082520.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-25T23:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82520",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_082521.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-25T23:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82521",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082522.json:
```json
{
    "body": "It was all one ticket in my head, but maybe it makes more sense to separate them.  Might as well address the low-hanging fruit.",
    "created_at": "2012-05-25T23:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82522",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

It was all one ticket in my head, but maybe it makes more sense to separate them.  Might as well address the low-hanging fruit.



---

archive/issue_comments_082523.json:
```json
{
    "body": "The problem wasn't really our translation of Maxima's inequality (`#`, which we finally fixed a while ago) but rather that we then had this little hack already.\n\nBut all of your tests already work in Sage 5.0, because of the `#` replacement.  It really has to test the original bug report example, otherwise this is trivial.  I suggest\n\n\n```\nsage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms \nsage: sefms(\"x != 3\") == SR(x != 3) \nTrue\nsage: sefms(\"x # 3\") == SR(x != 3) \nTrue\nsage:  solve([2*x==3, x != 5], x)\n[[x == (3/2), (-7/2) != 0]]\n```\n",
    "created_at": "2012-05-26T05:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82523",
    "user": "https://github.com/kcrisman"
}
```

The problem wasn't really our translation of Maxima's inequality (`#`, which we finally fixed a while ago) but rather that we then had this little hack already.

But all of your tests already work in Sage 5.0, because of the `#` replacement.  It really has to test the original bug report example, otherwise this is trivial.  I suggest


```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms 
sage: sefms("x != 3") == SR(x != 3) 
True
sage: sefms("x # 3") == SR(x != 3) 
True
sage:  solve([2*x==3, x != 5], x)
[[x == (3/2), (-7/2) != 0]]
```




---

archive/issue_comments_082524.json:
```json
{
    "body": "Oy, you're right that I truncated the original bug test (!).  But we do need to fix `!==` to round-trip neq, so I think it's worth doing.",
    "created_at": "2012-05-26T05:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82524",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Oy, you're right that I truncated the original bug test (!).  But we do need to fix `!==` to round-trip neq, so I think it's worth doing.



---

archive/issue_comments_082525.json:
```json
{
    "body": "revised version",
    "created_at": "2012-05-26T05:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82525",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

revised version



---

archive/issue_comments_082526.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T06:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82526",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082527.json:
```json
{
    "body": "Attachment [trac_8969_allow_neq_maxima_strings_v2.patch](tarball://root/attachments/some-uuid/ticket8969/trac_8969_allow_neq_maxima_strings_v2.patch) by @kcrisman created at 2012-05-26 06:36:26\n\nPositive review.",
    "created_at": "2012-05-26T06:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82527",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_8969_allow_neq_maxima_strings_v2.patch](tarball://root/attachments/some-uuid/ticket8969/trac_8969_allow_neq_maxima_strings_v2.patch) by @kcrisman created at 2012-05-26 06:36:26

Positive review.



---

archive/issue_events_009119.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-06-18T10:21:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8969#event-9119"
}
```



---

archive/issue_comments_082528.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-18T10:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8969#issuecomment-82528",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
