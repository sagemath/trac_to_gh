# Issue 304: another modular forms bug

archive/issues_000304.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: m = CuspForms(11*2^4,2); m.set_precision(13)\nsage: m.integral_basis()\n[\nq + O(q^13),\nq^2 + q^8 + O(q^13),\nq^3 + O(q^13),\nq^4 + O(q^13),\nq^5 + O(q^13),\nq^6 + 2*q^8 + O(q^13),\nq^7 + q^11 + O(q^13),\nq^8 + O(q^13),\nq^9 + O(q^13),\nq^10 + O(q^13),\nq^11 + O(q^13),\nq^12 + O(q^13),\n1 + O(q^13),\nq + 6*q^5 + 2*q^8 + 13*q^9 + O(q^13),\nq^2 + 4*q^6 + 6*q^10 + O(q^13),\nq^3 + 2*q^7 + O(q^13),\nq^4 + 4*q^12 + O(q^13),\n3*q^8 + O(q^13),\n2*q^11 + O(q^13)\n]\n```\n\n\nthere shouldn't be a series starting with 1.\n\nComputing everything to higher precision yields the right answer.  So ??\n\nIssue created by migration from https://trac.sagemath.org/ticket/304\n\n",
    "created_at": "2007-03-01T18:06:29Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "another modular forms bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/304",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: m = CuspForms(11*2^4,2); m.set_precision(13)
sage: m.integral_basis()
[
q + O(q^13),
q^2 + q^8 + O(q^13),
q^3 + O(q^13),
q^4 + O(q^13),
q^5 + O(q^13),
q^6 + 2*q^8 + O(q^13),
q^7 + q^11 + O(q^13),
q^8 + O(q^13),
q^9 + O(q^13),
q^10 + O(q^13),
q^11 + O(q^13),
q^12 + O(q^13),
1 + O(q^13),
q + 6*q^5 + 2*q^8 + 13*q^9 + O(q^13),
q^2 + 4*q^6 + 6*q^10 + O(q^13),
q^3 + 2*q^7 + O(q^13),
q^4 + 4*q^12 + O(q^13),
3*q^8 + O(q^13),
2*q^11 + O(q^13)
]
```


there shouldn't be a series starting with 1.

Computing everything to higher precision yields the right answer.  So ??

Issue created by migration from https://trac.sagemath.org/ticket/304





---

archive/issue_comments_001447.json:
```json
{
    "body": "Fixed for sage-2.8.2",
    "created_at": "2007-08-19T01:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/304#issuecomment-1447",
    "user": "https://github.com/williamstein"
}
```

Fixed for sage-2.8.2



---

archive/issue_events_000323.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-08-19T01:00:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/304",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/304#event-323"
}
```



---

archive/issue_comments_001448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T01:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/304#issuecomment-1448",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
