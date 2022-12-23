# Issue 8038: email address validator does not accept + in addresses

Issue created by migration from https://trac.sagemath.org/ticket/8038

Original creator: ddrake

Original creation time: 2010-01-22 07:07:08

Assignee: was

CC:  acleone timdumol

When a user is signing up for a notebook account, the email address field does not accept + in the address, even though such addresses are valid -- Gmail, for example, does this. If your account is foo`@`gmail.com, then foo+whatever`@`gmail.com automatically gets delivered to you.

Testing with Gmail, things like "foo++", "foo+bar+" and so on all are accepted. We need to update the regular expression in sagenb/notebook/twist.py.


---

Attachment

Patch up, please review. I tested this in a separate script, as I don't know how to run doctests for the notebook. But it's just running a regexp test on a string, so It Should Work.

One issue is that we are still rejecting a lot of valid email addresses: http://tools.ietf.org/html/rfc3696#section-3. But we are accepting some invalid addresses, since we're not checking for maximum length, or two consective periods, or beginning with a period, or...

Personally, coming up a regexp that exactly captures the RFC's requirements is a rabbit hole I don't want to go down, but if anyone else wants to try, feel free to upload a patch!


---

Comment by ddrake created at 2010-01-22 07:32:03

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-01-22 07:35:28

Oh, and things will get especially fun when Unicode is allowed in email addresses! http://en.wikipedia.org/wiki/E-mail_address#Internationalization

I have no idea what to do when someone puts in "甲斐`@`黒川.日本"!


---

Comment by mpatel created at 2010-01-23 06:23:15

To doctest all SageNB files, run `sage -t -sagenb`.  To test `twist.py`, run `sage -t -force_lib twist.py`.  The other options (`-verbose`, etc.) and parallel testing should also work.


---

Comment by mpatel created at 2010-01-23 14:11:25

[These](http://www.dominicsayers.com/isemail/) [sites](http://fightingforalostcause.net/misc/2006/compare-email-regex.php) have test results for several increasingly complex validators.

It seems the main remaining sources of false negatives in `is_valid_email` are

 * Other special characters not in quoted strings: `!def!xyz%abc`@`example.com`

 * IP addresses:  `first.last`@`[12.34.56.78]`, `first.last`@`[IPv6:1111:2222:3333::4444:5555:6666]`

 * Quoted strings:  `first."mid\dle"."l`@`st name"`@`example.com`  (`\` can escape anything but must escape something)

 * Top-level-domains (TLDs) of any length:  `+`@`b.c`

 * Comments, possibly nested:  `a(a(b(c],d(e(f],],g],h(i],j],`@`example.com`


---

Attachment

Unquoted local-parts, no `..`, short domains.  Replaces previous.


---

Comment by mpatel created at 2010-01-23 19:54:45

With luck, someone will write a freely-licensed, full-strength, and Pythonic validator that we can `import`.


---

Comment by ddrake created at 2010-01-24 02:43:38

Replying to [comment:5 mpatel]:
> With luck, someone will write a freely-licensed, full-strength, and Pythonic validator that we can `import`.

You'd think such a thing would exist. It would also be nice to have a corpus of validation tests -- you download a pair of big lists (one list of crazy but valid addresses, another of plausible but invalid addresses). But anyway.

Your regexp seems pretty good. I'm a bit confused about

```
%(unquoted)s+(\.%(unquoted)s+)*
```

though. Doesn't that simply match one or more "unquoted" characters? The first bit matches one or more, then the second bit matches zero or more -- so altogether that's one or more. Right? I'm not a regexp wizard by any means.

Also, the RFC (3696) says that the local part has a maximum of 64 characters and the domain part a max of 255 characters, so maybe we could toss in something like this:

```
if re_valid_email.match(email) is None:
    return False
lengths = map(len, email.split('@'))
if lengths[0] > 64 or lengths[1] > 255:
    return False
return True
```

Thoughts?

Oh, and thanks for telling me how to doctest notebook stuff.


---

Comment by mpatel created at 2010-01-24 04:13:27

Replying to [comment:6 ddrake]:
> Replying to [comment:5 mpatel]:
> Your regexp seems pretty good. I'm a bit confused about
> {{{
> %(unquoted)s+(\.%(unquoted)s+)*
> }}}
> though. Doesn't that simply match one or more "unquoted" characters? The first bit matches one or more, then the second bit matches zero or more -- so altogether that's one or more. Right? I'm not a regexp wizard by any means.

I'm far from regexpert, myself.  I think the first part, `%(unquoted)s+`, matches one or more unquoted characters (e.g., `$uper`), but the rest of the line above matches zero or more blocks (e.g., `.duper+foo`), each of which begins with a period and ends with a string of at least one unquoted character.

> Also, the RFC (3696) says that the local part has a maximum of 64 characters and the domain part a max of 255 characters, so maybe we could toss in something like this:
> {{{
> if re_valid_email.match(email) is None:
>     return False
> lengths = map(len, email.split('`@`'))
> if lengths[0] > 64 or lengths[1] > 255:
>     return False
> return True
> }}}
> Thoughts?

If we later enable quoted local-parts (e.g., `"foo`@`bar"`@`barfoo.com`), we'll need to modify this test.  But for now, we simply reject them, so it's no problem.

RFC 3696's [erratum 1003](http://www.rfc-editor.org/errata_search.php?rfc=3696) and [RFC 5321](http://tools.ietf.org/html/rfc5321#section-4.5.3.1) also give a _total_ upper bound of 256 characters (the `sup` may be 254).  What if we just check that `7 < len(email) < 255`?  I assume we can tolerate the [few] false positives that get through --- the confirmation message would not arrive at a truly invalid address.


---

Comment by mpatel created at 2010-01-24 04:27:30

More tests.  Replaces previous.


---

Attachment

Thanks for the explanation about the period ("`\.`"). I see that you are preventing two periods in a row.

Your changes look good. I applied the most recent patch and it passes doctests. Somehow I feel like a reviewer now, although I filed this ticket, so I think we need someone else to review it!


---

Comment by mpatel created at 2010-01-25 04:47:42

V2 applies cleanly to #8051 (SageNB 0.7) + #7784 + #5712 + #6069.


---

Comment by jason created at 2010-01-27 02:03:12

There has been discussion before about having a user also be able to specify a pattern for email addresses (or even just a domain).  Is there any way to incorporate a user-specified regexp for validation as well into this patch?  Maybe a form on the Notebook Settings page (right under the "Require e-mail for account registration") that allows me to put, for example, 

*`@`drake.edu

as a regexp validation that is run after this validation.  If my validation doesn't pass (i.e., someone doesn't have a drake.edu email address), I don't want the account to register.


---

Comment by ddrake created at 2010-01-27 03:23:29

Replying to [comment:10 jason]:
> There has been discussion before about having a user also be able to specify a pattern for email addresses (or even just a domain).

For reference, this feature request is #7629.


---

Comment by ddrake created at 2010-01-27 03:23:29

Changing assignee from was to ddrake.


---

Attachment

Add custom test from notebook settings.  Replaces previous.


---

Comment by mpatel created at 2010-01-27 12:16:02

V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`


---

Comment by mpatel created at 2010-01-27 12:19:31

If you have a spare moment, please suggest ways administrators might wish to configure #8055.


---

Comment by ddrake created at 2010-01-27 13:32:51

Replying to [comment:12 mpatel]:
> V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`

V3 is nice work, but I would prefer that for this ticket, we stick to the issue at hand -- fixing up the email address validator to accept most commonly-seen addresses. I think adding in Jason's request should be done at #7629 on top of this ticket. Can you split off the V3 changes and put them in a patch on that ticket?


---

Comment by jason created at 2010-01-27 14:29:32

Replying to [comment:14 ddrake]:

> Replying to [comment:12 mpatel]:
> > V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`
> V3 is nice work, but I would prefer that for this ticket, we stick to the issue at hand -- fixing up the email address validator to accept most commonly-seen addresses. I think adding in Jason's request should be done at #7629 on top of this ticket. Can you split off the V3 changes and put them in a patch on that ticket?

That sounds reasonable.  Sorry for causing more work!


---

Comment by mpatel created at 2010-01-28 04:21:24

Sounds good.  Can someone please review V2?


---

Comment by mpatel created at 2010-01-28 06:30:30

*Note to reviewers:* Please review V2, as V3 - V2 is now at #7629.


---

Comment by timdumol created at 2010-03-19 08:47:28

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-03-19 08:47:28

This works well enough. It's not overly complex like this:


```

(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

```


which still does not cover the new IPv6 addresses (c.f. http://snipplr.com/view/20981/rfc-2822-email-validation/). Doctests pass, LGTM.


---

Comment by timdumol created at 2010-05-04 04:44:23

Resolution: fixed
