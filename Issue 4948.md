# Issue 4948: implement the transfer of Mathematica lists back to Sage

archive/issues_004948.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @jasongrout\n\nMake the following work:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: slist = [1,2,3]\nsage: mathematica(slist) \n{1, 2, 3}\nsage: list(mathematica(slist))\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n| Sage Version 3.2.3, Release Date: 2009-01-05                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mabshoff/.sage/temp/sage/11670/_home_mabshoff__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __len__(self)\n   1345 \n   1346     def __len__(self):\n-> 1347         raise NotImplementedError\n   1348 \n   1349     def __reduce__(self):\n\nNotImplementedError: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4948\n\n",
    "created_at": "2009-01-07T03:55:28Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "implement the transfer of Mathematica lists back to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4948",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

CC:  @jasongrout

Make the following work:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: slist = [1,2,3]
sage: mathematica(slist) 
{1, 2, 3}
sage: list(mathematica(slist))
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mabshoff/.sage/temp/sage/11670/_home_mabshoff__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __len__(self)
   1345 
   1346     def __len__(self):
-> 1347         raise NotImplementedError
   1348 
   1349     def __reduce__(self):

NotImplementedError: 
```


Issue created by migration from https://trac.sagemath.org/ticket/4948





---

archive/issue_comments_037486.json:
```json
{
    "body": "Jason comments:\n\n```\nThese are not the right way to do this, but they seem to give results \nfor right now, at least until someone fixes this:\n\nsage: a=mathematica([1,2,3])\nsage: [a[i] for i in range(1,a.Length()+1)]\n[1, 2, 3]\n\nOr\n\nsage: a=mathematica(slist)\nsage: a._Expect__sage_list\n[1, 2, 3]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-01-07T05:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37486",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason comments:

```
These are not the right way to do this, but they seem to give results 
for right now, at least until someone fixes this:

sage: a=mathematica([1,2,3])
sage: [a[i] for i in range(1,a.Length()+1)]
[1, 2, 3]

Or

sage: a=mathematica(slist)
sage: a._Expect__sage_list
[1, 2, 3]
```


Cheers,

Michael



---

archive/issue_events_011425.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T02:27:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4948#event-11425"
}
```



---

archive/issue_comments_037487.json:
```json
{
    "body": "Attachment [trac-4948-mathematica_lists.patch](tarball://root/attachments/some-uuid/ticket4948/trac-4948-mathematica_lists.patch) by flawrence created at 2009-08-22 05:29:23",
    "created_at": "2009-08-22T05:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37487",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac-4948-mathematica_lists.patch](tarball://root/attachments/some-uuid/ticket4948/trac-4948-mathematica_lists.patch) by flawrence created at 2009-08-22 05:29:23



---

archive/issue_comments_037488.json:
```json
{
    "body": "The patch I just attached does a little more than the scope of this ticket - it also gets mmalist.sage() working, as well as allowing import of floats with exponents (e.g. 4.5e80) from both mathematica and GP (plus it lays the groundwork for importing nonstandard exponent notation from other programs too).",
    "created_at": "2009-08-22T05:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37488",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

The patch I just attached does a little more than the scope of this ticket - it also gets mmalist.sage() working, as well as allowing import of floats with exponents (e.g. 4.5e80) from both mathematica and GP (plus it lays the groundwork for importing nonstandard exponent notation from other programs too).



---

archive/issue_comments_037489.json:
```json
{
    "body": "Great work!   I hope you'll do more to improve the Sage /Mathematica interface.  Thanks!",
    "created_at": "2009-09-14T05:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37489",
    "user": "https://github.com/williamstein"
}
```

Great work!   I hope you'll do more to improve the Sage /Mathematica interface.  Thanks!



---

archive/issue_comments_037490.json:
```json
{
    "body": "What about doctest for this function in `sage/interfaces/expect.py`?\n\n```\n1142\t    def _exponent_symbol(self): \n1143\t        \"\"\" \n1144\t        Return the symbol used to denote *10^ in floats, e.g 'e' in 1.5e6 \n1145\t        \"\"\" \n1146\t        return 'e' \n```\n",
    "created_at": "2009-09-15T19:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

What about doctest for this function in `sage/interfaces/expect.py`?

```
1142	    def _exponent_symbol(self): 
1143	        """ 
1144	        Return the symbol used to denote *10^ in floats, e.g 'e' in 1.5e6 
1145	        """ 
1146	        return 'e' 
```




---

archive/issue_comments_037491.json:
```json
{
    "body": "a further patch adding doctest for generic _exponent_symbol()",
    "created_at": "2009-09-17T02:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37491",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

a further patch adding doctest for generic _exponent_symbol()



---

archive/issue_comments_037492.json:
```json
{
    "body": "Changing component from misc to interfaces.",
    "created_at": "2009-09-17T03:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37492",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing component from misc to interfaces.



---

archive/issue_comments_037493.json:
```json
{
    "body": "Changing assignee from cwitty to @williamstein.",
    "created_at": "2009-09-17T03:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37493",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing assignee from cwitty to @williamstein.



---

archive/issue_comments_037494.json:
```json
{
    "body": "Attachment [trac-4948-mathematica_lists 12660.patch](tarball://root/attachments/some-uuid/ticket4948/trac-4948-mathematica_lists 12660.patch) by flawrence created at 2009-09-17 03:43:40\n\nI added the requested doctest for the generic _exponent_symbol(), a method that is meant to be overloaded by each derived class (i.e. the interface to gp, mathematica, etc).  Since this is meant to be overloaded by each of the interfaces, I didn't use any existing interface in this doctest, as when _exponent_symbol() was overloaded by that interface the doctest would become misleading.  Instead I created a fake interface so that the doctest would always call the correct version of _exponent_symbol.  It's a bit messy but it's the most stable way of doctesting the function that I could think of.\n\nThe approach could be taken to write doctests for the rest of the methods in the Expect class.",
    "created_at": "2009-09-17T03:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37494",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac-4948-mathematica_lists 12660.patch](tarball://root/attachments/some-uuid/ticket4948/trac-4948-mathematica_lists 12660.patch) by flawrence created at 2009-09-17 03:43:40

I added the requested doctest for the generic _exponent_symbol(), a method that is meant to be overloaded by each derived class (i.e. the interface to gp, mathematica, etc).  Since this is meant to be overloaded by each of the interfaces, I didn't use any existing interface in this doctest, as when _exponent_symbol() was overloaded by that interface the doctest would become misleading.  Instead I created a fake interface so that the doctest would always call the correct version of _exponent_symbol.  It's a bit messy but it's the most stable way of doctesting the function that I could think of.

The approach could be taken to write doctests for the rest of the methods in the Expect class.



---

archive/issue_events_011426.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-17T08:24:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4948#event-11426"
}
```



---

archive/issue_comments_037495.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac-4948-mathematica_lists.patch`\n2. `trac-4948-mathematica_lists 12660.patch`",
    "created_at": "2009-09-17T08:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac-4948-mathematica_lists.patch`
2. `trac-4948-mathematica_lists 12660.patch`



---

archive/issue_comments_037496.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-17T08:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_037497.json:
```json
{
    "body": "N.B. the doctests introduced by the above patches fail on 32-bit systems - see #6999.",
    "created_at": "2009-09-23T04:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4948#issuecomment-37497",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

N.B. the doctests introduced by the above patches fail on 32-bit systems - see #6999.
