# Issue 487: problem with the is_principal method for fractional ideals in a number field.

archive/issues_000487.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe Problem has been reported by Kevin McGown at http://groups.google.com/group/sage-forum/t/a8a6efc565e36339\n\nIn SAGE 2.8 it seems there is a problem with the is_principal method\nfor fractional ideals in a number field.  In the code below I create\nthe same ideal in two different ways and obtain two different answers\nfrom is_principal (True and False). \n\n\n```\nsage: K = QuadraticField(-119,'a')\nsage: P2 = K.ideal([2]).factor()[0][0]\nsage: I = P2^5\nsage: a = K.0\nsage: J = K.ideal([1/2*a+3/2])\nsage: I==J\nTrue\nsage: I.is_principal()\nFalse\nsage: J.is_principal()\nTrue\n```\n\n\nKevin also suggested a fix:\n\n```\nI believe the problem is with the following line in the is_principal()\nmethod:\n\nif len (self.gens()) <= 1:\n\nInstead it should read:\n\nif len (self.gens_reduced()) <= 1:\n\nNot 100% sure, but I thought I would bring it to your attention.\n\n- Kevin\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/487\n\n",
    "created_at": "2007-08-24T05:29:07Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "problem with the is_principal method for fractional ideals in a number field.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/487",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

The Problem has been reported by Kevin McGown at http://groups.google.com/group/sage-forum/t/a8a6efc565e36339

In SAGE 2.8 it seems there is a problem with the is_principal method
for fractional ideals in a number field.  In the code below I create
the same ideal in two different ways and obtain two different answers
from is_principal (True and False). 


```
sage: K = QuadraticField(-119,'a')
sage: P2 = K.ideal([2]).factor()[0][0]
sage: I = P2^5
sage: a = K.0
sage: J = K.ideal([1/2*a+3/2])
sage: I==J
True
sage: I.is_principal()
False
sage: J.is_principal()
True
```


Kevin also suggested a fix:

```
I believe the problem is with the following line in the is_principal()
method:

if len (self.gens()) <= 1:

Instead it should read:

if len (self.gens_reduced()) <= 1:

Not 100% sure, but I thought I would bring it to your attention.

- Kevin
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/487





---

archive/issue_comments_002420.json:
```json
{
    "body": "Another suggestion from Kevin:\n\n```\nHello everyone,\n\nI think my fix above was incorrect.  The relevant file is:\n/sage-2.8.2-i386-Darwin/local/lib/python2.5/site-packages/sage/rings/\nnumber_field/number_field_ideal.py\n\nI think the problem is with the following line:\nself.__is_principal = (len(v[0]) == 0) ## i.e., v[0] is the zero\nvector\n\nThis above code gets 1 for the length of the zero vector.  I replaced\nit with this line:\nself.__is_principal = (v[0] == \"[0]~\")\n\nI don't know if this is the best way to do it, but it seemed to fix\nthe problem for me.\n\n- Kevin \n```\n",
    "created_at": "2007-08-27T07:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/487#issuecomment-2420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another suggestion from Kevin:

```
Hello everyone,

I think my fix above was incorrect.  The relevant file is:
/sage-2.8.2-i386-Darwin/local/lib/python2.5/site-packages/sage/rings/
number_field/number_field_ideal.py

I think the problem is with the following line:
self.__is_principal = (len(v[0]) == 0) ## i.e., v[0] is the zero
vector

This above code gets 1 for the length of the zero vector.  I replaced
it with this line:
self.__is_principal = (v[0] == "[0]~")

I don't know if this is the best way to do it, but it seemed to fix
the problem for me.

- Kevin 
```




---

archive/issue_events_000518.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-06T09:19:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/487",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/487#event-518"
}
```



---

archive/issue_comments_002421.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T09:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/487#issuecomment-2421",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002422.json:
```json
{
    "body": "The actual fix was a bit more complicated than described above, though the above was very helpful.\nThis is definitely fixed in sage > 2.8.3.5.",
    "created_at": "2007-09-06T09:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/487#issuecomment-2422",
    "user": "https://github.com/williamstein"
}
```

The actual fix was a bit more complicated than described above, though the above was very helpful.
This is definitely fixed in sage > 2.8.3.5.
