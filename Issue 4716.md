# Issue 4716: [with patch, needs review] Small bug in KodairaSymbol

archive/issues_004716.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Elliptic curves\n\n#4412 had a buglet:  for Kodaira Class Im the _roman field was not being set (it should be 1).  This is only currently used in the tamagawa_exponent() function for elliptic curves over number fields.\n\nOne-line patch coming up, plus a corresponding doctest.\n\nThis was reported by Tobias Nagel:\n\n```\nsage: E=EllipticCurve('117a3');                        \nsage: E.tamagawa_exponent(13)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/tobi/test_Sint/<ipython console> in <module>()\n\n/home/tobi/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in tamagawa_exponent(self, p)\n 2190             return cp\n 2191         ks = self.kodaira_type(p)\n-> 2192         if ks._roman==1 and ks._n%2==0 and ks._starred:\n 2193             return 2\n 2194         return 4\n\nAttributeError: 'KodairaSymbol_class' object has no attribute '_roman'\n```\n\nThe patch is based on 3.2.1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4716\n\n",
    "created_at": "2008-12-05T12:02:53Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] Small bug in KodairaSymbol",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4716",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: Elliptic curves

#4412 had a buglet:  for Kodaira Class Im the _roman field was not being set (it should be 1).  This is only currently used in the tamagawa_exponent() function for elliptic curves over number fields.

One-line patch coming up, plus a corresponding doctest.

This was reported by Tobias Nagel:

```
sage: E=EllipticCurve('117a3');                        
sage: E.tamagawa_exponent(13)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/tobi/test_Sint/<ipython console> in <module>()

/home/tobi/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in tamagawa_exponent(self, p)
 2190             return cp
 2191         ks = self.kodaira_type(p)
-> 2192         if ks._roman==1 and ks._n%2==0 and ks._starred:
 2193             return 2
 2194         return 4

AttributeError: 'KodairaSymbol_class' object has no attribute '_roman'
```

The patch is based on 3.2.1.

Issue created by migration from https://trac.sagemath.org/ticket/4716





---

archive/issue_comments_035508.json:
```json
{
    "body": "Attachment [sage-trac-4715.patch](tarball://root/attachments/some-uuid/ticket4716/sage-trac-4715.patch) by mabshoff created at 2008-12-05 12:07:55\n\nThis is a dupe of #4715.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T12:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4716#issuecomment-35508",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-trac-4715.patch](tarball://root/attachments/some-uuid/ticket4716/sage-trac-4715.patch) by mabshoff created at 2008-12-05 12:07:55

This is a dupe of #4715.

Cheers,

Michael



---

archive/issue_comments_035509.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-12-05T12:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4716#issuecomment-35509",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_010778.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-05T12:08:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4716",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4716#event-10778"
}
```



---

archive/issue_events_010779.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-05T12:08:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4716",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4716#event-10779"
}
```
