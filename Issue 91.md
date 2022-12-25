# Issue 91: gcd for polynomials over ZZ

archive/issues_000091.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  jdc@uwo.ca\n\nIf I start with this example from a sage docstring:                                                              \n                                                                                                                 \n  sage: x, y = PolynomialRing(RationalField(), 2, ['x','y']).gens()                                              \n  sage: f = (x^3 + 2*y<sup>2*x)</sup>2                                                                                    \n  sage: g = x<sup>2*y</sup>2                                                                                              \n  sage: f.gcd(g)                                                                                                 \n  x^2                                                                                                            \n                                                                                                                 \nbut change RationalField to IntegerRing, I get an error when executing                                           \nthe last line:                                                                                                   \n                                                                                                                 \n  TypeError: no conversion of this ring to a Singular ring defined                                               \n\nI could of course work over Q, but I was wondering if it would\nbe easy to make sage handle this.\n\nDan\n\nIssue created by migration from https://trac.sagemath.org/ticket/91\n\n",
    "created_at": "2006-09-27T19:26:49Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "title": "gcd for polynomials over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/91",
    "user": "https://github.com/jdchristensen"
}
```
Assignee: somebody

CC:  jdc@uwo.ca

If I start with this example from a sage docstring:                                                              
                                                                                                                 
  sage: x, y = PolynomialRing(RationalField(), 2, ['x','y']).gens()                                              
  sage: f = (x^3 + 2*y<sup>2*x)</sup>2                                                                                    
  sage: g = x<sup>2*y</sup>2                                                                                              
  sage: f.gcd(g)                                                                                                 
  x^2                                                                                                            
                                                                                                                 
but change RationalField to IntegerRing, I get an error when executing                                           
the last line:                                                                                                   
                                                                                                                 
  TypeError: no conversion of this ring to a Singular ring defined                                               

I could of course work over Q, but I was wondering if it would
be easy to make sage handle this.

Dan

Issue created by migration from https://trac.sagemath.org/ticket/91





---

archive/issue_events_000091.json:
```json
{
    "actor": "@ncalexan",
    "created_at": "2007-02-19T04:51:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/91",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/91#event-91"
}
```



---

archive/issue_comments_000444.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-19T04:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/91",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/91#issuecomment-444",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_000445.json:
```json
{
    "body": "Fixed and doctested as of 2.1.5.",
    "created_at": "2007-02-19T04:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/91",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/91#issuecomment-445",
    "user": "https://github.com/ncalexan"
}
```

Fixed and doctested as of 2.1.5.
