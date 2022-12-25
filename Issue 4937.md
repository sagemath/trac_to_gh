# Issue 4937: bug in _p_primary_torsion_basis() for elliptic curves

archive/issues_004937.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: elliptic curve torsion\n\nTesting for #4901 has revealed a bug (an embarrassing one in code of mine) in _p_primary_torsion_basis() as exemplified here:\n\n```\n sage: p=10^60+3201\nsage: K=GF(p)\nsage: a=804515977734860566494239770982282063895480484302363715494873\nsage: b=584772221603632866665682322899297141793188252000674256662071\nsage: E=EllipticCurve(K,[0,a,0,b,0])\nsage: E.cardinality().factor()\n2^17 * 13115567671 * 581705246972988608203110387504181554514650287\nsage: E._p_primary_torsion_basis(2)\n\n[[(656068448840236768725810484116830935925716002501543862440466 : 324360550482744921974063628110267202720852104214117741680354 : 1),\n  2],\n [(21059802536298599082171845328893691100757301985761775129713 : 0 : 1), 1]]\n```\nHere the 2-sylow subgroup has structure `2^16 * 2` but E._p_primary_torsion_basis(2) only gives `2<sup>2*2</sup>1`.  I know what the problem is and am working out how to fix it.\n\nNB This function is called in ell_torsion.py in computing torsion groups over number fields, which is rather likely to give wrong answers (though not over Q where pari is used ;)) until this is fixed.  Hence I made this a separate ticket marked \"major defect\"!\n\nMichael: I set the milestone for this as 3.3 since it's a potentially serious bug in this corner of Sage, but feel free to bump it up.  I hope I might be able to fix it tonight but if not then it will take a few days as teaching starts again tomorrow...\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4937\n\n",
    "created_at": "2009-01-04T19:21:48Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bug in _p_primary_torsion_basis() for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4937",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: elliptic curve torsion

Testing for #4901 has revealed a bug (an embarrassing one in code of mine) in _p_primary_torsion_basis() as exemplified here:

```
 sage: p=10^60+3201
sage: K=GF(p)
sage: a=804515977734860566494239770982282063895480484302363715494873
sage: b=584772221603632866665682322899297141793188252000674256662071
sage: E=EllipticCurve(K,[0,a,0,b,0])
sage: E.cardinality().factor()
2^17 * 13115567671 * 581705246972988608203110387504181554514650287
sage: E._p_primary_torsion_basis(2)

[[(656068448840236768725810484116830935925716002501543862440466 : 324360550482744921974063628110267202720852104214117741680354 : 1),
  2],
 [(21059802536298599082171845328893691100757301985761775129713 : 0 : 1), 1]]
```
Here the 2-sylow subgroup has structure `2^16 * 2` but E._p_primary_torsion_basis(2) only gives `2<sup>2*2</sup>1`.  I know what the problem is and am working out how to fix it.

NB This function is called in ell_torsion.py in computing torsion groups over number fields, which is rather likely to give wrong answers (though not over Q where pari is used ;)) until this is fixed.  Hence I made this a separate ticket marked "major defect"!

Michael: I set the milestone for this as 3.3 since it's a potentially serious bug in this corner of Sage, but feel free to bump it up.  I hope I might be able to fix it tonight but if not then it will take a few days as teaching starts again tomorrow...


Issue created by migration from https://trac.sagemath.org/ticket/4937





---

archive/issue_comments_037405.json:
```json
{
    "body": "John,\n\nthis is fine as long as it applies after the ReST conversion. There are already a bunch of tickets lined up, so 3.3 will contain a bunch of fixes besides the ReST conversion.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T19:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John,

this is fine as long as it applies after the ReST conversion. There are already a bunch of tickets lined up, so 3.3 will contain a bunch of fixes besides the ReST conversion.

Cheers,

Michael



---

archive/issue_comments_037406.json:
```json
{
    "body": "The patch which fixes this bug is actually at #4900 (sorry), based on 3.2.3 + #4926 (sphinxification).  So this one should not be applied until after those two.  All this one does is to add a doctest which shows that the bug reported here separately has been fixed.",
    "created_at": "2009-01-06T21:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37406",
    "user": "https://github.com/JohnCremona"
}
```

The patch which fixes this bug is actually at #4900 (sorry), based on 3.2.3 + #4926 (sphinxification).  So this one should not be applied until after those two.  All this one does is to add a doctest which shows that the bug reported here separately has been fixed.



---

archive/issue_comments_037407.json:
```json
{
    "body": "Works for me.",
    "created_at": "2009-01-24T14:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37407",
    "user": "https://github.com/roed314"
}
```

Works for me.



---

archive/issue_comments_037408.json:
```json
{
    "body": "There are other doctests that have been added in that docstring in 3.3.alphaX, so I will rebase this once 3.3.alpha2 is out.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T15:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are other doctests that have been added in that docstring in 3.3.alphaX, so I will rebase this once 3.3.alpha2 is out.

Cheers,

Michael



---

archive/issue_events_011376.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T15:51:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4937#event-11376"
}
```



---

archive/issue_comments_037409.json:
```json
{
    "body": "Attachment [trac_4937.patch](tarball://root/attachments/some-uuid/ticket4937/trac_4937.patch) by mabshoff created at 2009-01-28 17:41:27\n\nThis patch is the rebased version of John's patch.",
    "created_at": "2009-01-28T17:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4937.patch](tarball://root/attachments/some-uuid/ticket4937/trac_4937.patch) by mabshoff created at 2009-01-28 17:41:27

This patch is the rebased version of John's patch.



---

archive/issue_comments_037410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T17:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037411.json:
```json
{
    "body": "Merged the rebased trac_4937.patch in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T17:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4937#issuecomment-37411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged the rebased trac_4937.patch in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_events_011377.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T17:42:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4937",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4937#event-11377"
}
```
