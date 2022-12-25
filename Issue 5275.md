# Issue 5275: One-by-one declaration of morphisms to the coercion mechanism

archive/issues_005275.json:
```json
{
    "body": "Assignee: @robertwb\n\nWould it be possible to add the following functionality (with whatever\nappropriate syntax):\n\n\tdeclare_conversion(source, target, morphism)\n\nwhich would add the morphism from source to target to the conversion\nlist (and probably similarly for coercions). Having some restrictions\non it (like making sure it's called before any coercion/conversion is\nattempted) is no problem.\n\nThis functionality will make it possible for each category to\nautomatically declare the relevant morphisms, independently of the other\ncategories (like if A is in Algebras(K), then this category will\ndeclare the morphism from K to A).\n\nThanks in advance!\n\t\t\t\t\tNicolas\n\nIssue created by migration from https://trac.sagemath.org/ticket/5275\n\n",
    "created_at": "2009-02-14T18:16:50Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "One-by-one declaration of morphisms to the coercion mechanism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5275",
    "user": "https://github.com/nthiery"
}
```
Assignee: @robertwb

Would it be possible to add the following functionality (with whatever
appropriate syntax):

	declare_conversion(source, target, morphism)

which would add the morphism from source to target to the conversion
list (and probably similarly for coercions). Having some restrictions
on it (like making sure it's called before any coercion/conversion is
attempted) is no problem.

This functionality will make it possible for each category to
automatically declare the relevant morphisms, independently of the other
categories (like if A is in Algebras(K), then this category will
declare the morphism from K to A).

Thanks in advance!
					Nicolas

Issue created by migration from https://trac.sagemath.org/ticket/5275





---

archive/issue_comments_040407.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-02-14T18:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5275#issuecomment-40407",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_040408.json:
```json
{
    "body": "Nicolas,\n\nif you have a wish and you ask whether it is possible or not to do you should wait for the answer before opening a ticket. In that case you should also assign it to the wishlist milestone unless someone tells you that he is working on it.\n\nObviously is you are a nice guy and you meant \"I would like the following to be implemented\" then opening the ticket is ok :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T20:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5275#issuecomment-40408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nicolas,

if you have a wish and you ask whether it is possible or not to do you should wait for the answer before opening a ticket. In that case you should also assign it to the wishlist milestone unless someone tells you that he is working on it.

Obviously is you are a nice guy and you meant "I would like the following to be implemented" then opening the ticket is ok :)

Cheers,

Michael



---

archive/issue_events_012253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T20:19:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5275",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5275#event-12253"
}
```



---

archive/issue_comments_040409.json:
```json
{
    "body": "This is certainly possible (I bet I could do it rather quickly). \n\nDiscussion at http://groups.google.com/group/sage-devel/browse_thread/thread/7136f15aab6f6644?hl=en",
    "created_at": "2009-02-14T23:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5275#issuecomment-40409",
    "user": "https://github.com/robertwb"
}
```

This is certainly possible (I bet I could do it rather quickly). 

Discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/7136f15aab6f6644?hl=en
