# Issue 2392: [with patch, needs review] generic univariate polynomial has no discriminant function

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-05 02:00:14

Assignee: mabshoff

CC:  ncalexan

Keywords: univariate polynomial discriminant

As it says: generic univariate polynomial has no discriminant function.


---

Attachment

*Review*:
 * patch looks good, I say apply
 * shall we open a ticket for the mentioned Sage<->PARI issue?


---

Comment by mabshoff created at 2008-03-05 13:28:51

Replying to [comment:1 malb]:
> *Review*:
>  * patch looks good, I say apply
>  * shall we open a ticket for the mentioned Sage<->PARI issue?

Hi malb,

I assume you mean

```
+        Unfortunately SAGE does not handle PARI's variable ordering requirements
+        gracefully, so the following fails:
```

in which case I would suggest that we open a ticket. Is that something that has been discussed before? I do not recall any currently open ticket that mentions pari and variable orderings.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-05 13:29:27

Resolution: fixed


---

Comment by mabshoff created at 2008-03-05 13:29:27

Merged in Sage 2.10.3.rc2


---

Comment by malb created at 2008-03-05 15:29:39

> Hi malb,
> 
> I assume you mean
> {{{
> +        Unfortunately SAGE does not handle PARI's variable ordering requirements
> +        gracefully, so the following fails:
> }}}
> in which case I would suggest that we open a ticket. Is that something that has been discussed before? I do not recall any currently open ticket that mentions pari and variable orderings.

Jup.
