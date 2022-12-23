# Issue 4497: Implement the function log10

archive/issues_004497.json:
```json
{
    "body": "Assignee: somebody\n\n\"very useful for those who use a lot logarithmic scale\" - Ronan Paix\u00e3o\n\nIssue created by migration from https://trac.sagemath.org/ticket/4497\n\n",
    "created_at": "2008-11-11T23:19:57Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "Implement the function log10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4497",
    "user": "TimothyClemans"
}
```
Assignee: somebody

"very useful for those who use a lot logarithmic scale" - Ronan Paixão

Issue created by migration from https://trac.sagemath.org/ticket/4497





---

archive/issue_comments_033261.json:
```json
{
    "body": "Why this ticket? We already have\n\n```\nsage: log_b?\nType:\t\tfunction\nBase Class:\t<type 'function'>\nString Form:\t<function log at 0x29b33f0>\nNamespace:\tInteractive\nFile:\t\t/Users/michaelabshoff/Desktop/sage-3.1.3.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py\nDefinition:\tlog_b(x, b=None)\nDocstring:\n    \n        Return the log of x to the base b.  The default base is e.\n    \n        INPUT:\n            x -- number\n            b -- base (default: None, which means natural log)\n            \n        OUTPUT:\n            number\n    \n        NOTE: In Magma, the order of arguments is reversed from in\n        SAGE, i.e., the base is given first.  We use the opposite\n        ordering, so the base can be viewed as an optional second\n        argument.\n```\n\nOne could obviously implement log10, but why pollute the global namespace even more?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-12T14:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4497#issuecomment-33261",
    "user": "mabshoff"
}
```

Why this ticket? We already have

```
sage: log_b?
Type:		function
Base Class:	<type 'function'>
String Form:	<function log at 0x29b33f0>
Namespace:	Interactive
File:		/Users/michaelabshoff/Desktop/sage-3.1.3.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py
Definition:	log_b(x, b=None)
Docstring:
    
        Return the log of x to the base b.  The default base is e.
    
        INPUT:
            x -- number
            b -- base (default: None, which means natural log)
            
        OUTPUT:
            number
    
        NOTE: In Magma, the order of arguments is reversed from in
        SAGE, i.e., the base is given first.  We use the opposite
        ordering, so the base can be viewed as an optional second
        argument.
```

One could obviously implement log10, but why pollute the global namespace even more?

Cheers,

Michael



---

archive/issue_comments_033262.json:
```json
{
    "body": "Pari, Maple, and Mathematica all don't do this.   We should not do this in Sage either. It is trivial to implement in terms of existing functions.",
    "created_at": "2008-11-12T17:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4497#issuecomment-33262",
    "user": "was"
}
```

Pari, Maple, and Mathematica all don't do this.   We should not do this in Sage either. It is trivial to implement in terms of existing functions.



---

archive/issue_comments_033263.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-11-12T17:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4497#issuecomment-33263",
    "user": "was"
}
```

Resolution: invalid
