# Issue 4831: More number field ideal utilities

archive/issues_004831.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @loefflerd m.t.aranes@warwick.ac.uk\n\nKeywords: number fields, orders, ideals\n\nThis follows on from #4536:\n\n1. New invertible_residues() iterator for iterating though only the invertible residues modulo an integral ideal.\n2. New function like pari's add_to_1 so that A.add_to_1(B) return a in A such that 1-a is in B.  (The name of this might change before we upload a patch).\n\nPatch to follows later today.\n\nJohn Cremona and Maite Aranes\n\nIssue created by migration from https://trac.sagemath.org/ticket/4831\n\n",
    "created_at": "2008-12-19T12:31:40Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "More number field ideal utilities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4831",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  @loefflerd m.t.aranes@warwick.ac.uk

Keywords: number fields, orders, ideals

This follows on from #4536:

1. New invertible_residues() iterator for iterating though only the invertible residues modulo an integral ideal.
2. New function like pari's add_to_1 so that A.add_to_1(B) return a in A such that 1-a is in B.  (The name of this might change before we upload a patch).

Patch to follows later today.

John Cremona and Maite Aranes

Issue created by migration from https://trac.sagemath.org/ticket/4831





---

archive/issue_comments_036545.json:
```json
{
    "body": "Attachment [trac-4831.patch](tarball://root/attachments/some-uuid/ticket4831/trac-4831.patch) by @JohnCremona created at 2008-12-19 16:39:11",
    "created_at": "2008-12-19T16:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36545",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-4831.patch](tarball://root/attachments/some-uuid/ticket4831/trac-4831.patch) by @JohnCremona created at 2008-12-19 16:39:11



---

archive/issue_comments_036546.json:
```json
{
    "body": "The attached file (based on 3.2.2) adds three functions, the ones mentioned in the description (with the second one called `element_1_mod()` as we could not think of a better name) and a 3rd one which is a version for integral ideas of the `prime_to_m_part()` function for integers.  the second and third of these were written by Maite Aranes.",
    "created_at": "2008-12-19T16:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36546",
    "user": "https://github.com/JohnCremona"
}
```

The attached file (based on 3.2.2) adds three functions, the ones mentioned in the description (with the second one called `element_1_mod()` as we could not think of a better name) and a 3rd one which is a version for integral ideas of the `prime_to_m_part()` function for integers.  the second and third of these were written by Maite Aranes.



---

archive/issue_comments_036547.json:
```json
{
    "body": "John,\n\nwe will probably not merge an aweful lot of patches into 3.3 before all the ReST patches go in.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-20T14:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John,

we will probably not merge an aweful lot of patches into 3.3 before all the ReST patches go in.

Cheers,

Michael



---

archive/issue_comments_036548.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> John,\n> \n> we will probably not merge an aweful lot of patches into 3.3 before all the ReST patches go in.\n> \n\nThat's fine, I knew that and meant to put 3.4 on it.\n\n> Cheers,\n> \n> Michael",
    "created_at": "2008-12-20T16:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36548",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 mabshoff]:
> John,
> 
> we will probably not merge an aweful lot of patches into 3.3 before all the ReST patches go in.
> 

That's fine, I knew that and meant to put 3.4 on it.

> Cheers,
> 
> Michael



---

archive/issue_comments_036549.json:
```json
{
    "body": "Patch applies fine under 3.2.3; all tests in sage/rings/number_field pass; code looks fine and is very clearly laid out; and some experimentation with various random absolute number fields works fine. (I tried to test it for relative number fields, but they are currently so broken that I didn't succeed in even creating the objects to test it on.)\n\nI like the element_1_mod function, but there is a natural generalisation: given ideals I, J which are not assumed coprime, one might want a function that expresses a given element of I + J as a sum of elements of I and J. But if anyone really wants this we can have a separate ticket for it.\n\nMy one reservation is that the docstrings will need tweaking for compatibility with the new ReST system. Other than that I think this is fine to go in.\n\nDavid",
    "created_at": "2009-01-15T12:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36549",
    "user": "https://github.com/loefflerd"
}
```

Patch applies fine under 3.2.3; all tests in sage/rings/number_field pass; code looks fine and is very clearly laid out; and some experimentation with various random absolute number fields works fine. (I tried to test it for relative number fields, but they are currently so broken that I didn't succeed in even creating the objects to test it on.)

I like the element_1_mod function, but there is a natural generalisation: given ideals I, J which are not assumed coprime, one might want a function that expresses a given element of I + J as a sum of elements of I and J. But if anyone really wants this we can have a separate ticket for it.

My one reservation is that the docstrings will need tweaking for compatibility with the new ReST system. Other than that I think this is fine to go in.

David



---

archive/issue_comments_036550.json:
```json
{
    "body": "I agree that the more general function David suggests is useful, and it is also very easy to write:  set D=I+J, write 1=x+y with x in I/D, y in J/D using the function here, then for any d in D we have d=(dx)+(dy) with the factors in I,J.\n\nOn the other hand implementing this directly using the method we already use would perhaps be more efficient.  So let's not hold this up for that.\n\nOn the docstring comment -- yes, and the same is true for very many patches in there now!",
    "created_at": "2009-01-15T12:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36550",
    "user": "https://github.com/JohnCremona"
}
```

I agree that the more general function David suggests is useful, and it is also very easy to write:  set D=I+J, write 1=x+y with x in I/D, y in J/D using the function here, then for any d in D we have d=(dx)+(dy) with the factors in I,J.

On the other hand implementing this directly using the method we already use would perhaps be more efficient.  So let's not hold this up for that.

On the docstring comment -- yes, and the same is true for very many patches in there now!



---

archive/issue_comments_036551.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n\n> On the docstring comment -- yes, and the same is true for very many patches in there now!\n\nThe patches for the ReST transition will be rebased post Sage 3.3.x, so no need to worry about that now. One of the goals of SD 12 is to get every patch that is ready into 3.3.x (where x probably is equal to 1).\n\nCheers,\n\nMichael",
    "created_at": "2009-01-15T12:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36551",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 cremona]:

> On the docstring comment -- yes, and the same is true for very many patches in there now!

The patches for the ReST transition will be rebased post Sage 3.3.x, so no need to worry about that now. One of the goals of SD 12 is to get every patch that is ready into 3.3.x (where x probably is equal to 1).

Cheers,

Michael



---

archive/issue_events_005077.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-19T01:34:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4831#event-5077"
}
```



---

archive/issue_comments_036552.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T01:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36552",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036553.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T01:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4831#issuecomment-36553",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
