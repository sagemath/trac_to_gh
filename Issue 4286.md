# Issue 4286: [with patch, needs review] minor improvements to old integer code

archive/issues_004286.json:
```json
{
    "body": "Assignee: somebody\n\njust cleaning up some cruft\n\nIssue created by migration from https://trac.sagemath.org/ticket/4286\n\n",
    "created_at": "2008-10-14T19:49:00Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] minor improvements to old integer code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4286",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

just cleaning up some cruft

Issue created by migration from https://trac.sagemath.org/ticket/4286





---

archive/issue_comments_031310.json:
```json
{
    "body": "Tired as I am, I only write down some remarks from \"pure reading\":\n\n1. The (new) lines 3636 and 3682 (\"return v[0]\") should perhaps be:\n\n   return as_Integer(v[0])\n\ni.e. with the explicit (eventual) conversion of v[0] to a Sage integer. Probably that is done by the compiler implicitly. But anyway, the code would display even more visibly its intention what it is doing.\n\n2. I'm unsure whether the macro \"PY_TYPE_CHECK\" is allowed to be used inside _sig_on / _sig_off. And even if it is for the time being, a future change of that macro using some more pythonics might bombastically break the new code this patch brings --- at runtime. (It's implicitly used in lines 3639, 3641, 3685, 3687 inside \"as_Integer\".)\n\n3. The line 3523 (\"if mpz_cmp_ui(m.value, 1) == 0:\"). If I was a puricist, I'd say it should be replaced by the four lines:\n   \n   _sig_on\n   r = mpz_cmp_ui(m.value, 1)\n   _sig_off\n   if r == 0:\n\nThus this \"external\" function call to GMP is wrapped by _sig_on/_sig_off, too.\n(The variable r is destroyed in the very next line anyway.)",
    "created_at": "2008-10-14T22:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4286#issuecomment-31310",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Tired as I am, I only write down some remarks from "pure reading":

1. The (new) lines 3636 and 3682 ("return v[0]") should perhaps be:

   return as_Integer(v[0])

i.e. with the explicit (eventual) conversion of v[0] to a Sage integer. Probably that is done by the compiler implicitly. But anyway, the code would display even more visibly its intention what it is doing.

2. I'm unsure whether the macro "PY_TYPE_CHECK" is allowed to be used inside _sig_on / _sig_off. And even if it is for the time being, a future change of that macro using some more pythonics might bombastically break the new code this patch brings --- at runtime. (It's implicitly used in lines 3639, 3641, 3685, 3687 inside "as_Integer".)

3. The line 3523 ("if mpz_cmp_ui(m.value, 1) == 0:"). If I was a puricist, I'd say it should be replaced by the four lines:
   
   _sig_on
   r = mpz_cmp_ui(m.value, 1)
   _sig_off
   if r == 0:

Thus this "external" function call to GMP is wrapped by _sig_on/_sig_off, too.
(The variable r is destroyed in the very next line anyway.)



---

archive/issue_comments_031311.json:
```json
{
    "body": "Attachment [4286-integer-cruft.patch](tarball://root/attachments/some-uuid/ticket4286/4286-integer-cruft.patch) by @robertwb created at 2008-10-15 11:14:54\n\nThanks for looking at this. I've attached a new patch that should address your comments. The type checking has been pulled out of the main loop which addresses 1 and 2, which was actually an issue in the old code as well. (Note that isinstance will be a fast typecheck in the next release of Cython). \n\nAs for (3), there is no reason to put _sig_on/_sig_of around mpz_cmp_ui. These signal handlers are used for long-running code (where one wants to be able to intercept control-C) or code that might raise other signals/abort. mpz_cmp_ui is not such a function (in fact, it's a simple macro).",
    "created_at": "2008-10-15T11:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4286#issuecomment-31311",
    "user": "https://github.com/robertwb"
}
```

Attachment [4286-integer-cruft.patch](tarball://root/attachments/some-uuid/ticket4286/4286-integer-cruft.patch) by @robertwb created at 2008-10-15 11:14:54

Thanks for looking at this. I've attached a new patch that should address your comments. The type checking has been pulled out of the main loop which addresses 1 and 2, which was actually an issue in the old code as well. (Note that isinstance will be a fast typecheck in the next release of Cython). 

As for (3), there is no reason to put _sig_on/_sig_of around mpz_cmp_ui. These signal handlers are used for long-running code (where one wants to be able to intercept control-C) or code that might raise other signals/abort. mpz_cmp_ui is not such a function (in fact, it's a simple macro).



---

archive/issue_comments_031312.json:
```json
{
    "body": "Thanks for cleaning up this old code.\n\nThe following very minor issues do certainly not prevent me from giving this patch \"as is\" a positive review, but I thought I should write them down nevertheless:\n\n4. By the patch file, only \"def LCM_list\" becomes \"cpdef LCM_list\". One might also change \"def GCD_list\" into \"cpdef GCD_list\", at least for 3.1.3.rc0 (which is the youngest version I currently have and where this is otherwise not the case), if only for consistency. (I do not know enough about the difference between \"def\" and \"cpdef\" yet, but I do trust you there.)\n\n\n5. Again for consistency (or beauty?) only, one could make the two lines 2129/2130\n\n```\ncdef Integer z\nz = PY_NEW(Integer)\n```\n\ninto the one line\n\n```\ncdef Integer z = <Integer>PY_NEW(Integer)\n```\n\n(And again I do not enough about using \"<Integer>\" or not as a type qualifier, but yet again I trust you there.)",
    "created_at": "2008-10-16T20:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4286#issuecomment-31312",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Thanks for cleaning up this old code.

The following very minor issues do certainly not prevent me from giving this patch "as is" a positive review, but I thought I should write them down nevertheless:

4. By the patch file, only "def LCM_list" becomes "cpdef LCM_list". One might also change "def GCD_list" into "cpdef GCD_list", at least for 3.1.3.rc0 (which is the youngest version I currently have and where this is otherwise not the case), if only for consistency. (I do not know enough about the difference between "def" and "cpdef" yet, but I do trust you there.)


5. Again for consistency (or beauty?) only, one could make the two lines 2129/2130

```
cdef Integer z
z = PY_NEW(Integer)
```

into the one line

```
cdef Integer z = <Integer>PY_NEW(Integer)
```

(And again I do not enough about using "<Integer>" or not as a type qualifier, but yet again I trust you there.)



---

archive/issue_events_004530.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-18T20:32:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4286#event-4530"
}
```



---

archive/issue_comments_031313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T20:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4286#issuecomment-31313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031314.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T20:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4286#issuecomment-31314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha0



---

archive/issue_comments_031315.json:
```json
{
    "body": "Remark: This patch introduced a bug:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage.rings.integer.GCD_list([2,2,3])\n2\n```\n\n\nThe problem is in line 3654 of integer.pyx where there is a\nmissing ==0 so the break occurs immediately where it shouldn't.\n\nThis will be fixed in a patch at #3118, so there is no need to reopen this ticket.",
    "created_at": "2008-10-22T12:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4286#issuecomment-31315",
    "user": "https://github.com/JohnCremona"
}
```

Remark: This patch introduced a bug:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage.rings.integer.GCD_list([2,2,3])
2
```


The problem is in line 3654 of integer.pyx where there is a
missing ==0 so the break occurs immediately where it shouldn't.

This will be fixed in a patch at #3118, so there is no need to reopen this ticket.
