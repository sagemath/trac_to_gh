# Issue 1659: Add a complex128 method for conversion of symbolic (and other?) expressions to numpy's 128-bit complex type

archive/issues_001659.json:
```json
{
    "body": "Assignee: @robertwb\n\n```\nrishi_: I use scipy very often. To use complex number I have to use the following statement:  sage: a=numpy.complex128(complex(2+3*I)). Is it not possible to avoid 2 conversions?\n[12:29pm] mabshoff: hungry? *ducks*\n[12:29pm] ondrej: mabshoff - like a small dog?\n[12:29pm] mabshoff: yes. a young dog.\n[12:29pm] wstein-1658: We could add a method (2+3*I).complex128().\n[12:29pm] wstein-1658: Want that?\n[12:29pm] wstein-1658: Is I symbolic, by the way?\n[12:29pm] rishi_: yes\n[12:30pm] wstein-1658: Do you want to avoid two conversions because of speed or code cleaness?\n[12:30pm] wstein-1658: Probably clean-ness.\n[12:30pm] rishi_: cleaness\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1659\n\n",
    "closed_at": "2010-08-26T20:16:48Z",
    "created_at": "2008-01-02T19:33:21Z",
    "labels": [
        "component: coercion"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add a complex128 method for conversion of symbolic (and other?) expressions to numpy's 128-bit complex type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1659",
    "user": "https://github.com/williamstein"
}
```
Assignee: @robertwb

```
rishi_: I use scipy very often. To use complex number I have to use the following statement:  sage: a=numpy.complex128(complex(2+3*I)). Is it not possible to avoid 2 conversions?
[12:29pm] mabshoff: hungry? *ducks*
[12:29pm] ondrej: mabshoff - like a small dog?
[12:29pm] mabshoff: yes. a young dog.
[12:29pm] wstein-1658: We could add a method (2+3*I).complex128().
[12:29pm] wstein-1658: Want that?
[12:29pm] wstein-1658: Is I symbolic, by the way?
[12:29pm] rishi_: yes
[12:30pm] wstein-1658: Do you want to avoid two conversions because of speed or code cleaness?
[12:30pm] wstein-1658: Probably clean-ness.
[12:30pm] rishi_: cleaness
```

Issue created by migration from https://trac.sagemath.org/ticket/1659





---

archive/issue_comments_010527.json:
```json
{
    "body": "A temporary workaround (and almost the fix):\n\n```\nsage: import sage.calculus.calculus\nsage: def complex128(self): import numpy; return numpy.complex128(complex(self))\n....: \nsage: sage.calculus.calculus.SymbolicExpression.complex128 = complex128\nsage: \nsage: (3 + 2*I).complex128()\n(3+2j)\n```",
    "created_at": "2008-01-02T19:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1659#issuecomment-10527",
    "user": "https://github.com/williamstein"
}
```

A temporary workaround (and almost the fix):

```
sage: import sage.calculus.calculus
sage: def complex128(self): import numpy; return numpy.complex128(complex(self))
....: 
sage: sage.calculus.calculus.SymbolicExpression.complex128 = complex128
sage: 
sage: (3 + 2*I).complex128()
(3+2j)
```



---

archive/issue_comments_010528.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-08-26T20:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1659#issuecomment-10528",
    "user": "https://github.com/mwhansen"
}
```

Resolution: worksforme



---

archive/issue_events_004090.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-08-26T20:16:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1659",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1659#event-4090"
}
```



---

archive/issue_comments_010529.json:
```json
{
    "body": "This now works:\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: combinat\nsage: import numpy\nsage: a = numpy.complex128(2+3*I); a\n(2+3j)\nsage: type(a)\n<type 'numpy.complex128'>\n```",
    "created_at": "2010-08-26T20:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1659#issuecomment-10529",
    "user": "https://github.com/mwhansen"
}
```

This now works:

```

----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: import numpy
sage: a = numpy.complex128(2+3*I); a
(2+3j)
sage: type(a)
<type 'numpy.complex128'>
```



---

archive/issue_events_004091.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-08-26T20:16:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1659",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1659#event-4091"
}
```
