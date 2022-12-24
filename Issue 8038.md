# Issue 8038: email address validator does not accept + in addresses

archive/issues_008038.json:
```json
{
    "body": "Assignee: was\n\nCC:  acleone timdumol\n\nWhen a user is signing up for a notebook account, the email address field does not accept + in the address, even though such addresses are valid -- Gmail, for example, does this. If your account is foo`@`gmail.com, then foo+whatever`@`gmail.com automatically gets delivered to you.\n\nTesting with Gmail, things like \"foo++\", \"foo+bar+\" and so on all are accepted. We need to update the regular expression in sagenb/notebook/twist.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8038\n\n",
    "created_at": "2010-01-22T07:07:08Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "email address validator does not accept + in addresses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8038",
    "user": "ddrake"
}
```
Assignee: was

CC:  acleone timdumol

When a user is signing up for a notebook account, the email address field does not accept + in the address, even though such addresses are valid -- Gmail, for example, does this. If your account is foo`@`gmail.com, then foo+whatever`@`gmail.com automatically gets delivered to you.

Testing with Gmail, things like "foo++", "foo+bar+" and so on all are accepted. We need to update the regular expression in sagenb/notebook/twist.py.

Issue created by migration from https://trac.sagemath.org/ticket/8038





---

archive/issue_comments_070217.json:
```json
{
    "body": "Attachment [trac_8038.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038.patch) by ddrake created at 2010-01-22 07:32:03\n\nPatch up, please review. I tested this in a separate script, as I don't know how to run doctests for the notebook. But it's just running a regexp test on a string, so It Should Work.\n\nOne issue is that we are still rejecting a lot of valid email addresses: http://tools.ietf.org/html/rfc3696#section-3. But we are accepting some invalid addresses, since we're not checking for maximum length, or two consective periods, or beginning with a period, or...\n\nPersonally, coming up a regexp that exactly captures the RFC's requirements is a rabbit hole I don't want to go down, but if anyone else wants to try, feel free to upload a patch!",
    "created_at": "2010-01-22T07:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70217",
    "user": "ddrake"
}
```

Attachment [trac_8038.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038.patch) by ddrake created at 2010-01-22 07:32:03

Patch up, please review. I tested this in a separate script, as I don't know how to run doctests for the notebook. But it's just running a regexp test on a string, so It Should Work.

One issue is that we are still rejecting a lot of valid email addresses: http://tools.ietf.org/html/rfc3696#section-3. But we are accepting some invalid addresses, since we're not checking for maximum length, or two consective periods, or beginning with a period, or...

Personally, coming up a regexp that exactly captures the RFC's requirements is a rabbit hole I don't want to go down, but if anyone else wants to try, feel free to upload a patch!



---

archive/issue_comments_070218.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-22T07:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70218",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070219.json:
```json
{
    "body": "Oh, and things will get especially fun when Unicode is allowed in email addresses! http://en.wikipedia.org/wiki/E-mail_address#Internationalization\n\nI have no idea what to do when someone puts in \"\u7532\u6590`@`\u9ed2\u5ddd.\u65e5\u672c\"!",
    "created_at": "2010-01-22T07:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70219",
    "user": "ddrake"
}
```

Oh, and things will get especially fun when Unicode is allowed in email addresses! http://en.wikipedia.org/wiki/E-mail_address#Internationalization

I have no idea what to do when someone puts in "甲斐`@`黒川.日本"!



---

archive/issue_comments_070220.json:
```json
{
    "body": "To doctest all SageNB files, run `sage -t -sagenb`.  To test `twist.py`, run `sage -t -force_lib twist.py`.  The other options (`-verbose`, etc.) and parallel testing should also work.",
    "created_at": "2010-01-23T06:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70220",
    "user": "mpatel"
}
```

To doctest all SageNB files, run `sage -t -sagenb`.  To test `twist.py`, run `sage -t -force_lib twist.py`.  The other options (`-verbose`, etc.) and parallel testing should also work.



---

archive/issue_comments_070221.json:
```json
{
    "body": "[These](http://www.dominicsayers.com/isemail/) [sites](http://fightingforalostcause.net/misc/2006/compare-email-regex.php) have test results for several increasingly complex validators.\n\nIt seems the main remaining sources of false negatives in `is_valid_email` are\n\n* Other special characters not in quoted strings: `!def!xyz%abc`@`example.com`\n\n* IP addresses:  `first.last`@`[12.34.56.78]`, `first.last`@`[IPv6:1111:2222:3333::4444:5555:6666]`\n\n* Quoted strings:  `first.\"mid\\dle\".\"l`@`st name\"`@`example.com`  (`\\` can escape anything but must escape something)\n\n* Top-level-domains (TLDs) of any length:  `+`@`b.c`\n\n* Comments, possibly nested:  `a(a(b(c],d(e(f],],g],h(i],j],`@`example.com`",
    "created_at": "2010-01-23T14:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70221",
    "user": "mpatel"
}
```

[These](http://www.dominicsayers.com/isemail/) [sites](http://fightingforalostcause.net/misc/2006/compare-email-regex.php) have test results for several increasingly complex validators.

It seems the main remaining sources of false negatives in `is_valid_email` are

* Other special characters not in quoted strings: `!def!xyz%abc`@`example.com`

* IP addresses:  `first.last`@`[12.34.56.78]`, `first.last`@`[IPv6:1111:2222:3333::4444:5555:6666]`

* Quoted strings:  `first."mid\dle"."l`@`st name"`@`example.com`  (`\` can escape anything but must escape something)

* Top-level-domains (TLDs) of any length:  `+`@`b.c`

* Comments, possibly nested:  `a(a(b(c],d(e(f],],g],h(i],j],`@`example.com`



---

archive/issue_comments_070222.json:
```json
{
    "body": "Attachment [trac_8038-email_plus_addressing.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038-email_plus_addressing.patch) by mpatel created at 2010-01-23 19:47:46\n\nUnquoted local-parts, no `..`, short domains.  Replaces previous.",
    "created_at": "2010-01-23T19:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70222",
    "user": "mpatel"
}
```

Attachment [trac_8038-email_plus_addressing.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038-email_plus_addressing.patch) by mpatel created at 2010-01-23 19:47:46

Unquoted local-parts, no `..`, short domains.  Replaces previous.



---

archive/issue_comments_070223.json:
```json
{
    "body": "With luck, someone will write a freely-licensed, full-strength, and Pythonic validator that we can `import`.",
    "created_at": "2010-01-23T19:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70223",
    "user": "mpatel"
}
```

With luck, someone will write a freely-licensed, full-strength, and Pythonic validator that we can `import`.



---

archive/issue_comments_070224.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> With luck, someone will write a freely-licensed, full-strength, and Pythonic validator that we can `import`.\n\nYou'd think such a thing would exist. It would also be nice to have a corpus of validation tests -- you download a pair of big lists (one list of crazy but valid addresses, another of plausible but invalid addresses). But anyway.\n\nYour regexp seems pretty good. I'm a bit confused about\n\n```\n%(unquoted)s+(\\.%(unquoted)s+)*\n```\n\nthough. Doesn't that simply match one or more \"unquoted\" characters? The first bit matches one or more, then the second bit matches zero or more -- so altogether that's one or more. Right? I'm not a regexp wizard by any means.\n\nAlso, the RFC (3696) says that the local part has a maximum of 64 characters and the domain part a max of 255 characters, so maybe we could toss in something like this:\n\n```\nif re_valid_email.match(email) is None:\n    return False\nlengths = map(len, email.split('@'))\nif lengths[0] > 64 or lengths[1] > 255:\n    return False\nreturn True\n```\n\nThoughts?\n\nOh, and thanks for telling me how to doctest notebook stuff.",
    "created_at": "2010-01-24T02:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70224",
    "user": "ddrake"
}
```

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

archive/issue_comments_070225.json:
```json
{
    "body": "Replying to [comment:6 ddrake]:\n> Replying to [comment:5 mpatel]:\n> Your regexp seems pretty good. I'm a bit confused about\n> {{{\n> %(unquoted)s+(\\.%(unquoted)s+)*\n> }}}\n> though. Doesn't that simply match one or more \"unquoted\" characters? The first bit matches one or more, then the second bit matches zero or more -- so altogether that's one or more. Right? I'm not a regexp wizard by any means.\n\nI'm far from regexpert, myself.  I think the first part, `%(unquoted)s+`, matches one or more unquoted characters (e.g., `$uper`), but the rest of the line above matches zero or more blocks (e.g., `.duper+foo`), each of which begins with a period and ends with a string of at least one unquoted character.\n\n> Also, the RFC (3696) says that the local part has a maximum of 64 characters and the domain part a max of 255 characters, so maybe we could toss in something like this:\n> {{{\n> if re_valid_email.match(email) is None:\n>     return False\n> lengths = map(len, email.split('`@`'))\n> if lengths[0] > 64 or lengths[1] > 255:\n>     return False\n> return True\n> }}}\n> Thoughts?\n\nIf we later enable quoted local-parts (e.g., `\"foo`@`bar\"`@`barfoo.com`), we'll need to modify this test.  But for now, we simply reject them, so it's no problem.\n\nRFC 3696's [erratum 1003](http://www.rfc-editor.org/errata_search.php?rfc=3696) and [RFC 5321](http://tools.ietf.org/html/rfc5321#section-4.5.3.1) also give a *total* upper bound of 256 characters (the `sup` may be 254).  What if we just check that `7 < len(email) < 255`?  I assume we can tolerate the [few] false positives that get through --- the confirmation message would not arrive at a truly invalid address.",
    "created_at": "2010-01-24T04:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70225",
    "user": "mpatel"
}
```

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

RFC 3696's [erratum 1003](http://www.rfc-editor.org/errata_search.php?rfc=3696) and [RFC 5321](http://tools.ietf.org/html/rfc5321#section-4.5.3.1) also give a *total* upper bound of 256 characters (the `sup` may be 254).  What if we just check that `7 < len(email) < 255`?  I assume we can tolerate the [few] false positives that get through --- the confirmation message would not arrive at a truly invalid address.



---

archive/issue_comments_070226.json:
```json
{
    "body": "More tests.  Replaces previous.",
    "created_at": "2010-01-24T04:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70226",
    "user": "mpatel"
}
```

More tests.  Replaces previous.



---

archive/issue_comments_070227.json:
```json
{
    "body": "Attachment [trac_8038-email_plus_addressing_v2.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038-email_plus_addressing_v2.patch) by ddrake created at 2010-01-24 05:41:44\n\nThanks for the explanation about the period (\"`\\.`\"). I see that you are preventing two periods in a row.\n\nYour changes look good. I applied the most recent patch and it passes doctests. Somehow I feel like a reviewer now, although I filed this ticket, so I think we need someone else to review it!",
    "created_at": "2010-01-24T05:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70227",
    "user": "ddrake"
}
```

Attachment [trac_8038-email_plus_addressing_v2.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038-email_plus_addressing_v2.patch) by ddrake created at 2010-01-24 05:41:44

Thanks for the explanation about the period ("`\.`"). I see that you are preventing two periods in a row.

Your changes look good. I applied the most recent patch and it passes doctests. Somehow I feel like a reviewer now, although I filed this ticket, so I think we need someone else to review it!



---

archive/issue_comments_070228.json:
```json
{
    "body": "V2 applies cleanly to #8051 (SageNB 0.7) + #7784 + #5712 + #6069.",
    "created_at": "2010-01-25T04:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70228",
    "user": "mpatel"
}
```

V2 applies cleanly to #8051 (SageNB 0.7) + #7784 + #5712 + #6069.



---

archive/issue_comments_070229.json:
```json
{
    "body": "There has been discussion before about having a user also be able to specify a pattern for email addresses (or even just a domain).\u00a0 Is there any way to incorporate a user-specified regexp for validation as well into this patch?\u00a0 Maybe a form on the Notebook Settings page (right under the \"Require e-mail for account registration\") that allows me to put, for example, \n\n*`@`drake.edu\n\nas a regexp validation that is run after this validation.\u00a0 If my validation doesn't pass (i.e., someone doesn't have a drake.edu email address), I don't want the account to register.",
    "created_at": "2010-01-27T02:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70229",
    "user": "jason"
}
```

There has been discussion before about having a user also be able to specify a pattern for email addresses (or even just a domain).  Is there any way to incorporate a user-specified regexp for validation as well into this patch?  Maybe a form on the Notebook Settings page (right under the "Require e-mail for account registration") that allows me to put, for example, 

*`@`drake.edu

as a regexp validation that is run after this validation.  If my validation doesn't pass (i.e., someone doesn't have a drake.edu email address), I don't want the account to register.



---

archive/issue_comments_070230.json:
```json
{
    "body": "Replying to [comment:10 jason]:\n> There has been discussion before about having a user also be able to specify a pattern for email addresses (or even just a domain).\n\nFor reference, this feature request is #7629.",
    "created_at": "2010-01-27T03:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70230",
    "user": "ddrake"
}
```

Replying to [comment:10 jason]:
> There has been discussion before about having a user also be able to specify a pattern for email addresses (or even just a domain).

For reference, this feature request is #7629.



---

archive/issue_comments_070231.json:
```json
{
    "body": "Changing assignee from was to ddrake.",
    "created_at": "2010-01-27T03:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70231",
    "user": "ddrake"
}
```

Changing assignee from was to ddrake.



---

archive/issue_comments_070232.json:
```json
{
    "body": "Attachment [trac_8038-email_plus_addressing_v3.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038-email_plus_addressing_v3.patch) by mpatel created at 2010-01-27 12:13:17\n\nAdd custom test from notebook settings.  Replaces previous.",
    "created_at": "2010-01-27T12:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70232",
    "user": "mpatel"
}
```

Attachment [trac_8038-email_plus_addressing_v3.patch](tarball://root/attachments/some-uuid/ticket8038/trac_8038-email_plus_addressing_v3.patch) by mpatel created at 2010-01-27 12:13:17

Add custom test from notebook settings.  Replaces previous.



---

archive/issue_comments_070233.json:
```json
{
    "body": "V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`",
    "created_at": "2010-01-27T12:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70233",
    "user": "mpatel"
}
```

V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`



---

archive/issue_comments_070234.json:
```json
{
    "body": "If you have a spare moment, please suggest ways administrators might wish to configure #8055.",
    "created_at": "2010-01-27T12:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70234",
    "user": "mpatel"
}
```

If you have a spare moment, please suggest ways administrators might wish to configure #8055.



---

archive/issue_comments_070235.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`\n\nV3 is nice work, but I would prefer that for this ticket, we stick to the issue at hand -- fixing up the email address validator to accept most commonly-seen addresses. I think adding in Jason's request should be done at #7629 on top of this ticket. Can you split off the V3 changes and put them in a patch on that ticket?",
    "created_at": "2010-01-27T13:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70235",
    "user": "ddrake"
}
```

Replying to [comment:12 mpatel]:
> V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`

V3 is nice work, but I would prefer that for this ticket, we stick to the issue at hand -- fixing up the email address validator to accept most commonly-seen addresses. I think adding in Jason's request should be done at #7629 on top of this ticket. Can you split off the V3 changes and put them in a patch on that ticket?



---

archive/issue_comments_070236.json:
```json
{
    "body": "Replying to [comment:14 ddrake]:\n\n> Replying to [comment:12 mpatel]:\n> > V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`\n> V3 is nice work, but I would prefer that for this ticket, we stick to the issue at hand -- fixing up the email address validator to accept most commonly-seen addresses. I think adding in Jason's request should be done at #7629 on top of this ticket. Can you split off the V3 changes and put them in a patch on that ticket?\n\nThat sounds reasonable.  Sorry for causing more work!",
    "created_at": "2010-01-27T14:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70236",
    "user": "jason"
}
```

Replying to [comment:14 ddrake]:

> Replying to [comment:12 mpatel]:
> > V3 is a first take on the additional, custom test.  Example:  `.*`@`drake.edu$`
> V3 is nice work, but I would prefer that for this ticket, we stick to the issue at hand -- fixing up the email address validator to accept most commonly-seen addresses. I think adding in Jason's request should be done at #7629 on top of this ticket. Can you split off the V3 changes and put them in a patch on that ticket?

That sounds reasonable.  Sorry for causing more work!



---

archive/issue_comments_070237.json:
```json
{
    "body": "Sounds good.  Can someone please review V2?",
    "created_at": "2010-01-28T04:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70237",
    "user": "mpatel"
}
```

Sounds good.  Can someone please review V2?



---

archive/issue_comments_070238.json:
```json
{
    "body": "**Note to reviewers:** Please review V2, as V3 - V2 is now at #7629.",
    "created_at": "2010-01-28T06:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70238",
    "user": "mpatel"
}
```

**Note to reviewers:** Please review V2, as V3 - V2 is now at #7629.



---

archive/issue_comments_070239.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-19T08:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70239",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070240.json:
```json
{
    "body": "This works well enough. It's not overly complex like this:\n\n\n```\n\n(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n\n```\n\n\nwhich still does not cover the new IPv6 addresses (c.f. http://snipplr.com/view/20981/rfc-2822-email-validation/). Doctests pass, LGTM.",
    "created_at": "2010-03-19T08:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70240",
    "user": "timdumol"
}
```

This works well enough. It's not overly complex like this:


```

(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

```


which still does not cover the new IPv6 addresses (c.f. http://snipplr.com/view/20981/rfc-2822-email-validation/). Doctests pass, LGTM.



---

archive/issue_comments_070241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8038#issuecomment-70241",
    "user": "timdumol"
}
```

Resolution: fixed
