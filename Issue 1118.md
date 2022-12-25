# Issue 1118: cputime should include the cpu times of all subprocesses

archive/issues_001118.json:
```json
{
    "body": "Assignee: @williamstein\n\nPaul Zimmermann wrote:\n\"\"\"\nIt seems the cpu time reported by SAGE does not include that of the spawned\nprocesses\n\n\n```\nmermoz% sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.10, Release Date: 2007-10-28                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: p=65257526772644948764799212887702573391887715235981530343703506731\nsage: time FindGroupOrder(p,489731259)\nCPU times: user 0.87 s, sys: 0.07 s, total: 0.94 s\nWall time: 70.30\n2^2 * 3^2 * 7 * 13 * 5521 * 589213 * 1103171 * 1149307 * 1310261 * 10091759 * 63065897 * 120597437 * 48024231181\n```\n\nI doubt the given cpu times take into account the PARI/GP computations. As a  comparison, Magma takes 55s for that computation on my computer.\n\nThe wall time is not very useful (my machine has a load of 3-4). It would be more useful to have to cpu time used by the spawned processes, or simply the total cpu time used by SAGE and those processes.\n\"\"\"\n\nThus we should figure out how to do this in a portable way. May the POSIX gurus speak up!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1118\n\n",
    "created_at": "2007-11-07T13:57:55Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cputime should include the cpu times of all subprocesses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1118",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Paul Zimmermann wrote:
"""
It seems the cpu time reported by SAGE does not include that of the spawned
processes


```
mermoz% sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10, Release Date: 2007-10-28                      |
| Type notebook() for the GUI, and license() for information.        |
sage: p=65257526772644948764799212887702573391887715235981530343703506731
sage: time FindGroupOrder(p,489731259)
CPU times: user 0.87 s, sys: 0.07 s, total: 0.94 s
Wall time: 70.30
2^2 * 3^2 * 7 * 13 * 5521 * 589213 * 1103171 * 1149307 * 1310261 * 10091759 * 63065897 * 120597437 * 48024231181
```

I doubt the given cpu times take into account the PARI/GP computations. As a  comparison, Magma takes 55s for that computation on my computer.

The wall time is not very useful (my machine has a load of 3-4). It would be more useful to have to cpu time used by the spawned processes, or simply the total cpu time used by SAGE and those processes.
"""

Thus we should figure out how to do this in a portable way. May the POSIX gurus speak up!

Issue created by migration from https://trac.sagemath.org/ticket/1118





---

archive/issue_comments_006737.json:
```json
{
    "body": "I forgot to include the actual code that was run.\n\n\n```\ndef FindGroupOrder(p,s):\n   K = GF(p)\n   v = K(4*s)\n   u = K(s^2-5)\n   x = u^3\n   b = 4*x*v\n   a = (v-u)^3*(3*u+v)\n   A = a/b-2\n   x = x/v^3\n   b = x^3 + A*x^2 + x\n   E = EllipticCurve(K,[0,b*A,0,b^2,0])\n   return factor(E.cardinality())\n```\n",
    "created_at": "2007-11-07T14:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1118#issuecomment-6737",
    "user": "https://github.com/malb"
}
```

I forgot to include the actual code that was run.


```
def FindGroupOrder(p,s):
   K = GF(p)
   v = K(4*s)
   u = K(s^2-5)
   x = u^3
   b = 4*x*v
   a = (v-u)^3*(3*u+v)
   A = a/b-2
   x = x/v^3
   b = x^3 + A*x^2 + x
   E = EllipticCurve(K,[0,b*A,0,b^2,0])
   return factor(E.cardinality())
```




---

archive/issue_comments_006738.json:
```json
{
    "body": "This is a duplicate of #4761 and thus I am closing this ticket.",
    "created_at": "2009-08-25T19:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1118#issuecomment-6738",
    "user": "https://github.com/malb"
}
```

This is a duplicate of #4761 and thus I am closing this ticket.



---

archive/issue_comments_006739.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-08-25T19:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1118#issuecomment-6739",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate



---

archive/issue_events_001244.json:
```json
{
    "actor": "@malb",
    "created_at": "2009-08-25T19:20:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1118",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1118#event-1244"
}
```
