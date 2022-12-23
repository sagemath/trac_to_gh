# Issue 9745: Pickling of FFELT (finite field element) PARI/GP elements broken

archive/issues_009745.json:
```json
{
    "body": "Assignee: was\n\nKeywords: pari gp\n\nThe new version of PARI (see #9343) introduces a new type t_FFELT (finite field element).  Unfortunately, they pickle badly in Sage:\n\n\n```\nsage: gp_el = gp('ffgen(ffinit(2,3))')\nsage: gp_el.type()\nt_FFELT\nsage: loads(dumps(gp_el)).type()\nt_POL\n```\n\n\nA possible solution would be to implement pickling using PARI's `writebin()` and `read()`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9745\n\n",
    "created_at": "2010-08-14T11:08:12Z",
    "labels": [
        "pickling",
        "major",
        "bug"
    ],
    "title": "Pickling of FFELT (finite field element) PARI/GP elements broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9745",
    "user": "jdemeyer"
}
```
Assignee: was

Keywords: pari gp

The new version of PARI (see #9343) introduces a new type t_FFELT (finite field element).  Unfortunately, they pickle badly in Sage:


```
sage: gp_el = gp('ffgen(ffinit(2,3))')
sage: gp_el.type()
t_FFELT
sage: loads(dumps(gp_el)).type()
t_POL
```


A possible solution would be to implement pickling using PARI's `writebin()` and `read()`.

Issue created by migration from https://trac.sagemath.org/ticket/9745


