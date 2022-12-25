# Issue 5968: increase doctest coverage of sage/modular/modsym/modular_symbols.py from 0% to 100%

archive/issues_005968.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5968\n\n",
    "created_at": "2009-05-03T03:18:16Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "increase doctest coverage of sage/modular/modsym/modular_symbols.py from 0% to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5968",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @JohnCremona



Issue created by migration from https://trac.sagemath.org/ticket/5968





---

archive/issue_comments_047204.json:
```json
{
    "body": "Attachment [trac_5968.patch](tarball://root/attachments/some-uuid/ticket5968/trac_5968.patch) by @williamstein created at 2009-05-03 05:56:58",
    "created_at": "2009-05-03T05:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47204",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5968.patch](tarball://root/attachments/some-uuid/ticket5968/trac_5968.patch) by @williamstein created at 2009-05-03 05:56:58



---

archive/issue_comments_047205.json:
```json
{
    "body": "Attachment [trac_5968-part2.patch](tarball://root/attachments/some-uuid/ticket5968/trac_5968-part2.patch) by @williamstein created at 2009-05-03 05:58:41",
    "created_at": "2009-05-03T05:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47205",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5968-part2.patch](tarball://root/attachments/some-uuid/ticket5968/trac_5968-part2.patch) by @williamstein created at 2009-05-03 05:58:41



---

archive/issue_comments_047206.json:
```json
{
    "body": "I have one microscopically insignificant quibble: might it not be better to add a couple of minus signs into the `__cmp__` method, changing it to \n\n```\nif not isinstance(other, ModularSymbol):\n    return cmp(type(self), type(other))\nreturn cmp((self.__space,-self.__i,self.__alpha,self.__beta),\n           (other.__space,-other.__i,other.__alpha,other.__beta))\n```\n\n?\n\nThis is somehow the sort order that \"feels most natural\" to me -- so X<sup>2</sup>Y comes before XY<sup>2</sup>. This would then need fewer changes to other files, but of course it means most of the new doctests in your file would need rewriting :-). Also, what is the reasoning behind introducing the space in the `_repr_` method? I would advocate leaving `_repr_` as is unless there is a pressing reason to change it, in order to minimise the likelihood of breaking user code.",
    "created_at": "2009-05-04T09:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47206",
    "user": "https://github.com/loefflerd"
}
```

I have one microscopically insignificant quibble: might it not be better to add a couple of minus signs into the `__cmp__` method, changing it to 

```
if not isinstance(other, ModularSymbol):
    return cmp(type(self), type(other))
return cmp((self.__space,-self.__i,self.__alpha,self.__beta),
           (other.__space,-other.__i,other.__alpha,other.__beta))
```

?

This is somehow the sort order that "feels most natural" to me -- so X<sup>2</sup>Y comes before XY<sup>2</sup>. This would then need fewer changes to other files, but of course it means most of the new doctests in your file would need rewriting :-). Also, what is the reasoning behind introducing the space in the `_repr_` method? I would advocate leaving `_repr_` as is unless there is a pressing reason to change it, in order to minimise the likelihood of breaking user code.



---

archive/issue_comments_047207.json:
```json
{
    "body": "Apply over previous two patches",
    "created_at": "2009-05-04T14:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47207",
    "user": "https://github.com/loefflerd"
}
```

Apply over previous two patches



---

archive/issue_comments_047208.json:
```json
{
    "body": "Attachment [trac_5968-part3.patch](tarball://root/attachments/some-uuid/ticket5968/trac_5968-part3.patch) by @loefflerd created at 2009-05-04 14:42:01\n\nThe new patch above adds the suggested minus sign to give a more \"natural\" sort order, and adjusts the doctests accordingly; I've checked that with this modification all doctests still pass on my machine (32-bit Linux). I take back my comment about the `_repr_` method: all the native Python sequence types print with spaces in, so I agree that a space in modular symbols is better for consistency, and it certainly looks nicer.\n\nIn the process of fixing this I realised that the file `modular_symbols.py` isn't included in the reference manual, so the new patch does that too (and includes some ReST syntax fixes, so the manual page builds correctly and looks nice-ish). \n\nWilliam: I'm happy with your changes, so if you're happy with my subsequent ones, I guess we can call this a positive review.",
    "created_at": "2009-05-04T14:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47208",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5968-part3.patch](tarball://root/attachments/some-uuid/ticket5968/trac_5968-part3.patch) by @loefflerd created at 2009-05-04 14:42:01

The new patch above adds the suggested minus sign to give a more "natural" sort order, and adjusts the doctests accordingly; I've checked that with this modification all doctests still pass on my machine (32-bit Linux). I take back my comment about the `_repr_` method: all the native Python sequence types print with spaces in, so I agree that a space in modular symbols is better for consistency, and it certainly looks nicer.

In the process of fixing this I realised that the file `modular_symbols.py` isn't included in the reference manual, so the new patch does that too (and includes some ReST syntax fixes, so the manual page builds correctly and looks nice-ish). 

William: I'm happy with your changes, so if you're happy with my subsequent ones, I guess we can call this a positive review.



---

archive/issue_comments_047209.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2009-05-10T21:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47209",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_047210.json:
```json
{
    "body": "William: just in case you've forgotten about this ticket, it would be good if you could take a quick glance at the changes I made in my third patch above.\n\nBTW, I'm moving this ticket to component \"modular forms\", which seems to be a better fit for it.",
    "created_at": "2009-05-10T21:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47210",
    "user": "https://github.com/loefflerd"
}
```

William: just in case you've forgotten about this ticket, it would be good if you could take a quick glance at the changes I made in my third patch above.

BTW, I'm moving this ticket to component "modular forms", which seems to be a better fit for it.



---

archive/issue_comments_047211.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2009-05-10T21:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47211",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_047212.json:
```json
{
    "body": "What is the status here? Let's get it into 4.0 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the status here? Let's get it into 4.0 :)

Cheers,

Michael



---

archive/issue_comments_047213.json:
```json
{
    "body": "I'm waiting for was or somebody else to OK my patch (the third one), which just adds a minus sign and changes doctests to match. I've asked John Cremona (cc'ed) to have a look at it if he gets a chance.",
    "created_at": "2009-05-15T14:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47213",
    "user": "https://github.com/loefflerd"
}
```

I'm waiting for was or somebody else to OK my patch (the third one), which just adds a minus sign and changes doctests to match. I've asked John Cremona (cc'ed) to have a look at it if he gets a chance.



---

archive/issue_comments_047214.json:
```json
{
    "body": "I am doing it *now*!",
    "created_at": "2009-05-15T15:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47214",
    "user": "https://github.com/JohnCremona"
}
```

I am doing it *now*!



---

archive/issue_comments_047215.json:
```json
{
    "body": "Review: applied all 3 patches to 3.4.2 with no problem.  All tests in sage/modular and doc/en/bordeaux_2008 pass.  This is on a 64-bit machine.\n\nI did not build the documentation (it takes such ages)  but looking at the docstrings could not see anything wrong.\n\nLet's roll!",
    "created_at": "2009-05-15T15:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47215",
    "user": "https://github.com/JohnCremona"
}
```

Review: applied all 3 patches to 3.4.2 with no problem.  All tests in sage/modular and doc/en/bordeaux_2008 pass.  This is on a 64-bit machine.

I did not build the documentation (it takes such ages)  but looking at the docstrings could not see anything wrong.

Let's roll!



---

archive/issue_comments_047216.json:
```json
{
    "body": "Merged all three patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-16T01:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47216",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047217.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-16T01:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5968#issuecomment-47217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
