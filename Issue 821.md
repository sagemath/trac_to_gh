# Issue 821: K.fractional_ideal(...)

archive/issues_000821.json:
```json
{
    "body": "Assignee: @williamstein\n\nChange K.ideal to K.fractional_ideal for number fields. \n\n\n```\nOn 10/3/07, Soroosh Yazdani <syazdani@math.berkeley.edu> wrote:\n> \n> I think what you're saying makes sense. Maybe introduce a method\n> fractionalideal, specific to number fields?\n\nIt should be \n\n    K.fractional_ideal(...)\n\nI agree.  I've opened a trac ticket (and accepted it):\n   \n\n> \n> Soroosh\n> On Wed, Oct 03, 2007 at 10:44:49AM -0400, David Harvey wrote:\n> > I find this very confusing:\n> >\n> > sage: F.<a> = QuadraticField(-5)\n> > sage: F.ideal(6)\n> > Fractional ideal (6) of Number Field in a with defining polynomial\n> > x^2 + 5\n> >\n> > sage: QQ.ideal(6)\n> > Principal ideal (1) of Rational Field\n> >\n> > This means that if I write code that can work over an arbitrary\n> > number field, I have to write special cases for Q. I think it's a bad\n> > idea to use the name \"ideal\" for the method that gives an ideal of\n> > the ring of integers. I think we should give this a different name.\n> >\n> > Any thoughts?\n> >\n> > david\n> >\n> >\n> >\n> \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/821\n\n",
    "created_at": "2007-10-04T04:59:48Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "K.fractional_ideal(...)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/821",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Change K.ideal to K.fractional_ideal for number fields. 


```
On 10/3/07, Soroosh Yazdani <syazdani@math.berkeley.edu> wrote:
> 
> I think what you're saying makes sense. Maybe introduce a method
> fractionalideal, specific to number fields?

It should be 

    K.fractional_ideal(...)

I agree.  I've opened a trac ticket (and accepted it):
   

> 
> Soroosh
> On Wed, Oct 03, 2007 at 10:44:49AM -0400, David Harvey wrote:
> > I find this very confusing:
> >
> > sage: F.<a> = QuadraticField(-5)
> > sage: F.ideal(6)
> > Fractional ideal (6) of Number Field in a with defining polynomial
> > x^2 + 5
> >
> > sage: QQ.ideal(6)
> > Principal ideal (1) of Rational Field
> >
> > This means that if I write code that can work over an arbitrary
> > number field, I have to write special cases for Q. I think it's a bad
> > idea to use the name "ideal" for the method that gives an ideal of
> > the ring of integers. I think we should give this a different name.
> >
> > Any thoughts?
> >
> > david
> >
> >
> >
> 

```


Issue created by migration from https://trac.sagemath.org/ticket/821





---

archive/issue_comments_005074.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-04T04:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5074",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005075.json:
```json
{
    "body": "This is much harder than it looks...",
    "created_at": "2007-11-03T15:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5075",
    "user": "https://github.com/williamstein"
}
```

This is much harder than it looks...



---

archive/issue_comments_005076.json:
```json
{
    "body": "I think this has been done already; in sage-2.10.1, number fields have a method .fractional_ideal(), and .ideal() is simply an alias for it.",
    "created_at": "2008-02-17T02:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5076",
    "user": "https://github.com/aghitza"
}
```

I think this has been done already; in sage-2.10.1, number fields have a method .fractional_ideal(), and .ideal() is simply an alias for it.



---

archive/issue_comments_005077.json:
```json
{
    "body": "\n```\n10:47 < mhansen_> wstein: Is #821 fixed?\n10:49 < wstein> mhansen_ -- 821 is not fixed.\n10:49 < wstein> I think it would be trivial to fix.\n10:49 < wstein> I would be ok with just making it so this works:\n10:49 < wstein> sage: QQ.fractional_ideal(6)\n10:50 < wstein> I.e., adding fractional_ideal = ideal in the rational_field.py code.\n10:50 < wstein> Then the ticket could be closed.\n\n```\n",
    "created_at": "2008-02-27T18:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5077",
    "user": "https://github.com/williamstein"
}
```


```
10:47 < mhansen_> wstein: Is #821 fixed?
10:49 < wstein> mhansen_ -- 821 is not fixed.
10:49 < wstein> I think it would be trivial to fix.
10:49 < wstein> I would be ok with just making it so this works:
10:49 < wstein> sage: QQ.fractional_ideal(6)
10:50 < wstein> I.e., adding fractional_ideal = ideal in the rational_field.py code.
10:50 < wstein> Then the ticket could be closed.

```




---

archive/issue_comments_005078.json:
```json
{
    "body": "It might also be good to deprecate the ideal function for a number field completely, since it is confusing that the result is not an ideal of the number field, but a fractional ideal of the ring of integers.  We could fully support ideals of K, but that could be really confusing and bug prone.  The best thing would be to make\n\n```\n def ideal(self, ...):\n```\n\nfor number fields raise a clear exception (ValueError or NotImplementedError) that said \"use fractional_ideal\" instead.",
    "created_at": "2008-02-27T18:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5078",
    "user": "https://github.com/williamstein"
}
```

It might also be good to deprecate the ideal function for a number field completely, since it is confusing that the result is not an ideal of the number field, but a fractional ideal of the ring of integers.  We could fully support ideals of K, but that could be really confusing and bug prone.  The best thing would be to make

```
 def ideal(self, ...):
```

for number fields raise a clear exception (ValueError or NotImplementedError) that said "use fractional_ideal" instead.



---

archive/issue_events_000932.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-20T05:52:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/821#event-932"
}
```



---

archive/issue_comments_005079.json:
```json
{
    "body": "Fixed some time before Sage 3.0.rc0: \n\n```\n[07:00] <mabshoff> wstein: what is your take on #821 ?\n[07:10] <wstein> close #821.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T05:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed some time before Sage 3.0.rc0: 

```
[07:00] <mabshoff> wstein: what is your take on #821 ?
[07:10] <wstein> close #821.
```


Cheers,

Michael



---

archive/issue_comments_005080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T05:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/821#issuecomment-5080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
