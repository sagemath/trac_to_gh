# Issue 253: Add Integral closure for ideals

archive/issues_000253.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nOn Fri, 09 Feb 2007 11:04:16 -0700, Milena Hering wrote:\n\n> Hi William,\n>\n> Is it possible to compute the integral closure of an ideal in sage?\n\nIt's not nicely integrated into SAGE yet, but the capability is there\nvia Singular, which is included in SAGE.  For example:\n\nsage: singular.load('reesclos.lib')\nsage: R.<x,y> = QQ[]\nsage: i = ideal([x^2,x*y^4,y^5])\nsage: singular(i).normalI()         # the [1] part gives the normalization\n[1]:\n   _[1]=x^2\n   _[2]=y^5\n   _[3]=x*y^3\n\n---\n\nVery likely somebody will add this functionality to the next version of SAGE,\ni.e., so you could type i.integral_closure(), and get back the ideal as a SAGE ideal.\n\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/253\n\n",
    "created_at": "2007-02-09T18:39:43Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "Add Integral closure for ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/253",
    "user": "@williamstein"
}
```
Assignee: somebody


```
On Fri, 09 Feb 2007 11:04:16 -0700, Milena Hering wrote:

> Hi William,
>
> Is it possible to compute the integral closure of an ideal in sage?

It's not nicely integrated into SAGE yet, but the capability is there
via Singular, which is included in SAGE.  For example:

sage: singular.load('reesclos.lib')
sage: R.<x,y> = QQ[]
sage: i = ideal([x^2,x*y^4,y^5])
sage: singular(i).normalI()         # the [1] part gives the normalization
[1]:
   _[1]=x^2
   _[2]=y^5
   _[3]=x*y^3

---

Very likely somebody will add this functionality to the next version of SAGE,
i.e., so you could type i.integral_closure(), and get back the ideal as a SAGE ideal.


William
```


Issue created by migration from https://trac.sagemath.org/ticket/253





---

archive/issue_comments_001142.json:
```json
{
    "body": "See http://www.singular.uni-kl.de/Manual/3-0-1/sing_788.htm",
    "created_at": "2007-02-09T18:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/253#issuecomment-1142",
    "user": "@williamstein"
}
```

See http://www.singular.uni-kl.de/Manual/3-0-1/sing_788.htm



---

archive/issue_comments_001143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-09T20:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/253#issuecomment-1143",
    "user": "@malb"
}
```

Resolution: fixed



---

archive/issue_comments_001144.json:
```json
{
    "body": "Done in r2854.",
    "created_at": "2007-02-09T20:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/253#issuecomment-1144",
    "user": "@malb"
}
```

Done in r2854.
