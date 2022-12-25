# Issue 3548: [with patch, positive review] bug in Permutation creation from a string

archive/issues_003548.json:
```json
{
    "body": "Assignee: joyner\n\nThis sucks:\n\n```\nsage: Permutation( '(4,5)' )\nIndexError: list assignment index out of range\n```\n\nSee below for more details. \n\n```\nOn Thu, Jul 3, 2008 at 10:50 AM, John Cremona <> wrote:\n>\n> I would still say that this is a bug, since the following does work:\n> sage: Permutation('(1)(2)(3)(4,5)')\n> [1, 2, 3, 5, 4]\n> and the docstring says the Permutation can be given a string in cycle\n> notation, and 1-cycles are usually omitted.  Looking at the code\n> (Permutation??) the error is in the call to from_cycles where the\n> first parameter n is computed as the sum of the lengths of the cycles\n> input instead of the maximum integer input.\n>\n> John Cremona\n>\n> 2008/7/3 Pierre <>:\n>>\n>> hi all,\n>>\n>> I'm confused with the cycle notation for permutations (bug ?)\n>> While the following works:\n>>\n>> sage: Permutation( '(1,2)' )\n>>\n>> the following yields an error:\n>>\n>> sage: Permutation( '(4,5)' )\n>> IndexError: list assignment index out of range\n>>\n>> What's confusing is that if you go:\n>>\n>> sage: x= Permutation( (4,5) )\n>> sage: s= x.cycle_string(); s\n>> '(4,5)'\n>>\n>> I'm trying to build a dictionnary whose keys are permutations; since\n>> the keys have to be hashable, i'm relying on the cycle_string()\n>> strings. But the above issue prevents me from recovering a permutation\n>> from its string !\n>>\n>> Is there a way around this ?\n>>\n>> thanks\n>> pierre\n\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3548\n\n",
    "closed_at": "2008-07-05T22:44:00Z",
    "created_at": "2008-07-04T00:25:45Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, positive review] bug in Permutation creation from a string",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3548",
    "user": "https://github.com/williamstein"
}
```
Assignee: joyner

This sucks:

```
sage: Permutation( '(4,5)' )
IndexError: list assignment index out of range
```

See below for more details. 

```
On Thu, Jul 3, 2008 at 10:50 AM, John Cremona <> wrote:
>
> I would still say that this is a bug, since the following does work:
> sage: Permutation('(1)(2)(3)(4,5)')
> [1, 2, 3, 5, 4]
> and the docstring says the Permutation can be given a string in cycle
> notation, and 1-cycles are usually omitted.  Looking at the code
> (Permutation??) the error is in the call to from_cycles where the
> first parameter n is computed as the sum of the lengths of the cycles
> input instead of the maximum integer input.
>
> John Cremona
>
> 2008/7/3 Pierre <>:
>>
>> hi all,
>>
>> I'm confused with the cycle notation for permutations (bug ?)
>> While the following works:
>>
>> sage: Permutation( '(1,2)' )
>>
>> the following yields an error:
>>
>> sage: Permutation( '(4,5)' )
>> IndexError: list assignment index out of range
>>
>> What's confusing is that if you go:
>>
>> sage: x= Permutation( (4,5) )
>> sage: s= x.cycle_string(); s
>> '(4,5)'
>>
>> I'm trying to build a dictionnary whose keys are permutations; since
>> the keys have to be hashable, i'm relying on the cycle_string()
>> strings. But the above issue prevents me from recovering a permutation
>> from its string !
>>
>> Is there a way around this ?
>>
>> thanks
>> pierre


```

Issue created by migration from https://trac.sagemath.org/ticket/3548





---

archive/issue_comments_025047.json:
```json
{
    "body": "Attachment [sage-trac3548.patch](tarball://root/attachments/some-uuid/ticket3548/sage-trac3548.patch) by @JohnCremona created at 2008-07-04 22:09:15",
    "created_at": "2008-07-04T22:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3548#issuecomment-25047",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-trac3548.patch](tarball://root/attachments/some-uuid/ticket3548/sage-trac3548.patch) by @JohnCremona created at 2008-07-04 22:09:15



---

archive/issue_comments_025048.json:
```json
{
    "body": "The attached patch (based on 3.0.4.alpha0) fixes this and adds some relevant doctests.\n\n```\nsage: p = Permutation( '(4,5)' ); p\n[1, 2, 3, 5, 4]\nsage: p2 = Permutation( '(4,5)(10)' ); p2\n[1, 2, 3, 5, 4, 6, 7, 8, 9, 10]\n```",
    "created_at": "2008-07-04T22:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3548#issuecomment-25048",
    "user": "https://github.com/JohnCremona"
}
```

The attached patch (based on 3.0.4.alpha0) fixes this and adds some relevant doctests.

```
sage: p = Permutation( '(4,5)' ); p
[1, 2, 3, 5, 4]
sage: p2 = Permutation( '(4,5)(10)' ); p2
[1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
```



---

archive/issue_comments_025049.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-05T19:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3548#issuecomment-25049",
    "user": "https://github.com/rlmill"
}
```

+1



---

archive/issue_comments_025050.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-05T22:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3548#issuecomment-25050",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_025051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-05T22:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3548#issuecomment-25051",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008128.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-05T22:44:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3548",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3548#event-8128"
}
```
