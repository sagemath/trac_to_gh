# Issue 2899: Make RDF round and friends return Integers

archive/issues_002899.json:
```json
{
    "body": "Assignee: @robertwb\n\n\n```\n> Also, round(RR(3.0)) returns an Integer...should RDF behave the same\n> > way? (currently round(RDF(3.0)) returns an RDF).\n\nWe recently changed round, floor, ceiling, and trunc on RR to return\nintegers; yes, I think the corresponding RDF methods should change as\nwell.\n\nCarl\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2899\n\n",
    "created_at": "2008-04-12T16:09:26Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Make RDF round and friends return Integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2899",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @robertwb


```
> Also, round(RR(3.0)) returns an Integer...should RDF behave the same
> > way? (currently round(RDF(3.0)) returns an RDF).

We recently changed round, floor, ceiling, and trunc on RR to return
integers; yes, I think the corresponding RDF methods should change as
well.

Carl
```



Issue created by migration from https://trac.sagemath.org/ticket/2899





---

archive/issue_comments_019928.json:
```json
{
    "body": "The fix for #2898 will fix this.",
    "created_at": "2008-04-13T04:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19928",
    "user": "https://github.com/jasongrout"
}
```

The fix for #2898 will fix this.



---

archive/issue_comments_019929.json:
```json
{
    "body": "Attachment [2899-ncalexan-RIF-floor-ceil-1.patch](tarball://root/attachments/some-uuid/ticket2899/2899-ncalexan-RIF-floor-ceil-1.patch) by @ncalexan created at 2008-08-14 00:38:58\n\nThis makes floor and ceil do what I expect for RIF.  I believe that #2898 does make RDF work.",
    "created_at": "2008-08-14T00:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19929",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2899-ncalexan-RIF-floor-ceil-1.patch](tarball://root/attachments/some-uuid/ticket2899/2899-ncalexan-RIF-floor-ceil-1.patch) by @ncalexan created at 2008-08-14 00:38:58

This makes floor and ceil do what I expect for RIF.  I believe that #2898 does make RDF work.



---

archive/issue_comments_019930.json:
```json
{
    "body": "I just tried to apply this against 3.2, and it fails. It's just a matter of moving the doctests around, I think.",
    "created_at": "2008-11-27T08:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19930",
    "user": "https://github.com/craigcitro"
}
```

I just tried to apply this against 3.2, and it fails. It's just a matter of moving the doctests around, I think.



---

archive/issue_comments_019931.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2009-05-18T21:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19931",
    "user": "https://github.com/robertwb"
}
```

Resolution: worksforme



---

archive/issue_events_003097.json:
```json
{
    "actor": "@robertwb",
    "created_at": "2009-05-18T21:45:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2899#event-3097"
}
```



---

archive/issue_comments_019932.json:
```json
{
    "body": "This appears to have already been fixed. \n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.4.2, Release Date: 2009-05-05                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: a = RDF(3.4)\n\nsage: a.round(), a.floor(), a.ceil()\n (3, 3, 4)\n\n```\n",
    "created_at": "2009-05-18T21:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19932",
    "user": "https://github.com/robertwb"
}
```

This appears to have already been fixed. 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.4.2, Release Date: 2009-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: a = RDF(3.4)

sage: a.round(), a.floor(), a.ceil()
 (3, 3, 4)

```




---

archive/issue_comments_019933.json:
```json
{
    "body": "Did someone add a doctest? Otherwise this should not have been closed.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T21:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19933",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Did someone add a doctest? Otherwise this should not have been closed.

Cheers,

Michael



---

archive/issue_comments_019934.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2009-05-19T04:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19934",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_019935.json:
```json
{
    "body": "Reopening until someone either points to a doctests or post a doctest patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T04:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Reopening until someone either points to a doctests or post a doctest patch.

Cheers,

Michael



---

archive/issue_comments_019936.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-05-19T04:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19936",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003098.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T04:56:59Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2899#event-3098"
}
```



---

archive/issue_comments_019937.json:
```json
{
    "body": "There are doctests for RDF for sure:\n\n\n```\n\n    def round(self):\n        \"\"\"\n        Given real number x, rounds up if fractional part is greater than\n        .5, rounds down if fractional part is less than .5.\n\n        EXAMPLES::\n        \n            sage: RDF(0.49).round()\n            0\n            sage: a=RDF(0.51).round(); a\n            1\n        \"\"\"\n        return Integer(round(self._value))\n\n    def floor(self):\n        \"\"\"\n        Returns the floor of this number\n        \n        EXAMPLES::\n        \n            sage: RDF(2.99).floor()\n            2\n            sage: RDF(2.00).floor()\n            2\n            sage: RDF(-5/2).floor()\n            -3\n        \"\"\"\n        return Integer(math.floor(self._value))\n\n    def ceil(self):\n        \"\"\"\n        Returns the ceiling of this number\n        \n        OUTPUT: integer\n        \n        EXAMPLES::\n        \n            sage: RDF(2.99).ceil()\n            3\n            sage: RDF(2.00).ceil()\n            2\n            sage: RDF(-5/2).ceil()\n            -2\n        \"\"\"\n        return Integer(math.ceil(self._value))\n```\n",
    "created_at": "2009-05-19T16:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19937",
    "user": "https://github.com/ncalexan"
}
```

There are doctests for RDF for sure:


```

    def round(self):
        """
        Given real number x, rounds up if fractional part is greater than
        .5, rounds down if fractional part is less than .5.

        EXAMPLES::
        
            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
        """
        return Integer(round(self._value))

    def floor(self):
        """
        Returns the floor of this number
        
        EXAMPLES::
        
            sage: RDF(2.99).floor()
            2
            sage: RDF(2.00).floor()
            2
            sage: RDF(-5/2).floor()
            -3
        """
        return Integer(math.floor(self._value))

    def ceil(self):
        """
        Returns the ceiling of this number
        
        OUTPUT: integer
        
        EXAMPLES::
        
            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2
        """
        return Integer(math.ceil(self._value))
```




---

archive/issue_comments_019938.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T16:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19938",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019939.json:
```json
{
    "body": "Excellent. Closed as fixed.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T16:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19939",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Excellent. Closed as fixed.

Cheers,

Michael



---

archive/issue_events_003099.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T16:33:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2899#event-3099"
}
```



---

archive/issue_comments_019940.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-05-19T20:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19940",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_019941.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-05-19T20:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19941",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003100.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T20:48:17Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2899#event-3100"
}
```



---

archive/issue_comments_019942.json:
```json
{
    "body": "Wait. There are doctests via Nick's ticket, but that patch has not been merged into the Sage library, but fixed in some other way, i.e. the symbolics switch in 4.0. I assume.\n\nIn that case we might still need doctests, so until this is sorted out I am reopening this again :(\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Wait. There are doctests via Nick's ticket, but that patch has not been merged into the Sage library, but fixed in some other way, i.e. the symbolics switch in 4.0. I assume.

In that case we might still need doctests, so until this is sorted out I am reopening this again :(

Cheers,

Michael



---

archive/issue_comments_019943.json:
```json
{
    "body": "There are doctests.",
    "created_at": "2010-01-16T23:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19943",
    "user": "https://github.com/robertwb"
}
```

There are doctests.



---

archive/issue_events_003101.json:
```json
{
    "actor": "@robertwb",
    "created_at": "2010-01-16T23:47:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2899#event-3101"
}
```



---

archive/issue_comments_019944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-16T23:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2899#issuecomment-19944",
    "user": "https://github.com/robertwb"
}
```

Resolution: fixed
