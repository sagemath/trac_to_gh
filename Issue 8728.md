# Issue 8728: Incorrect integral from Maxima

archive/issues_008728.json:
```json
{
    "body": "Assignee: @burcin\n\nFrom #sage-devel:\n\n```\nBoulemans left the chat room. (Read error: Connection reset by peer)\n[11:58am] Boule joined the chat room.\n[11:58am] Boule: (laptop shutdown due to power supply)\n[11:59am] Boule: e, T, w = var(\"e T w\"); assume(1 = e^2)>0; integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi) should give -2*pi e cos w/(1-e^2)^3/2 instead of 0\n[11:59am] Boule: can someone help?\n[12:00pm] wjp: yeah, sage seems to have some trouble with this integral. You could try http://groups.google.com/group/sage-support since the right people don't seem to be here currently\n[12:00pm] Boule: ok, thanx\n[12:08pm] kcrisman: By the way, I just tried this and get a hang in Maxima.  Can you type the exact commands which lead to an answer of 0?\n[12:08pm] kcrisman: If I plug something (.5, .75) in for e in Maxima in Sage, I do get zero as an output.\n[12:12pm] Boule: don't know maxima, but with numerical values for e and w at wolfram-alfa, it gives something different than 0\n[12:13pm] wjp: *nod* maple gives non-zeros too\n[12:13pm] kcrisman: Can you give the *exact* sequence of commands which yield zero in Sage itself? \n[12:14pm] Boule: e = var('e')\n[12:14pm] Boule: T = var('T')\n[12:14pm] Boule: w = var('w')\n[12:14pm] baali1 joined the chat room.\n[12:14pm] baali left the chat room. (Quit: Leaving.)\n[12:15pm] Boule: assume(1-e^2>0)\n[12:15pm] Boule:  integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)\n[12:15pm] kcrisman: Okay, that's what I thought.\n[12:16pm] kcrisman: Okay, it takes a while but I do get 0.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8728\n\n",
    "created_at": "2010-04-20T16:22:21Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.4",
    "title": "Incorrect integral from Maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8728",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @burcin

From #sage-devel:

```
Boulemans left the chat room. (Read error: Connection reset by peer)
[11:58am] Boule joined the chat room.
[11:58am] Boule: (laptop shutdown due to power supply)
[11:59am] Boule: e, T, w = var("e T w"); assume(1 = e^2)>0; integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi) should give -2*pi e cos w/(1-e^2)^3/2 instead of 0
[11:59am] Boule: can someone help?
[12:00pm] wjp: yeah, sage seems to have some trouble with this integral. You could try http://groups.google.com/group/sage-support since the right people don't seem to be here currently
[12:00pm] Boule: ok, thanx
[12:08pm] kcrisman: By the way, I just tried this and get a hang in Maxima.  Can you type the exact commands which lead to an answer of 0?
[12:08pm] kcrisman: If I plug something (.5, .75) in for e in Maxima in Sage, I do get zero as an output.
[12:12pm] Boule: don't know maxima, but with numerical values for e and w at wolfram-alfa, it gives something different than 0
[12:13pm] wjp: *nod* maple gives non-zeros too
[12:13pm] kcrisman: Can you give the *exact* sequence of commands which yield zero in Sage itself? 
[12:14pm] Boule: e = var('e')
[12:14pm] Boule: T = var('T')
[12:14pm] Boule: w = var('w')
[12:14pm] baali1 joined the chat room.
[12:14pm] baali left the chat room. (Quit: Leaving.)
[12:15pm] Boule: assume(1-e^2>0)
[12:15pm] Boule:  integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)
[12:15pm] kcrisman: Okay, that's what I thought.
[12:16pm] kcrisman: Okay, it takes a while but I do get 0.
```

Issue created by migration from https://trac.sagemath.org/ticket/8728





---

archive/issue_comments_079582.json:
```json
{
    "body": "I wonder if this is another manifestation of this bug:\n\n```\nsage: integrate(sqrt(sin(x)^2+cos(x)^2), x,0,2*pi)\npi\n```",
    "created_at": "2010-04-20T16:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79582",
    "user": "https://github.com/jasongrout"
}
```

I wonder if this is another manifestation of this bug:

```
sage: integrate(sqrt(sin(x)^2+cos(x)^2), x,0,2*pi)
pi
```



---

archive/issue_comments_079583.json:
```json
{
    "body": "#8729 may point to a solution.",
    "created_at": "2010-04-20T16:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79583",
    "user": "https://github.com/jasongrout"
}
```

#8729 may point to a solution.



---

archive/issue_comments_079584.json:
```json
{
    "body": "Hmm, I forgot about this, and it's true it never got implemented, did it?",
    "created_at": "2010-04-20T16:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79584",
    "user": "https://github.com/kcrisman"
}
```

Hmm, I forgot about this, and it's true it never got implemented, did it?



---

archive/issue_comments_079585.json:
```json
{
    "body": "It was fixed about two weeks ago in maxima.  There was a new release of maxima a few days ago---I'm trying to make an spkg right now.",
    "created_at": "2010-04-20T17:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79585",
    "user": "https://github.com/jasongrout"
}
```

It was fixed about two weeks ago in maxima.  There was a new release of maxima a few days ago---I'm trying to make an spkg right now.



---

archive/issue_comments_079586.json:
```json
{
    "body": "Sweet.  I haven't been keeping up on the Maxima list lately, thanks.",
    "created_at": "2010-04-20T17:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79586",
    "user": "https://github.com/kcrisman"
}
```

Sweet.  I haven't been keeping up on the Maxima list lately, thanks.



---

archive/issue_comments_079587.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> I wonder if this is another manifestation of this bug:\n> \n> \n> ```\n> sage: integrate(sqrt(sin(x)^2+cos(x)^2), x,0,2*pi)\n> pi\n> ```\n\n\nI just checked; this ticket isn't the same bug.",
    "created_at": "2010-04-20T19:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79587",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:1 jason]:
> I wonder if this is another manifestation of this bug:
> 
> 
> ```
> sage: integrate(sqrt(sin(x)^2+cos(x)^2), x,0,2*pi)
> pi
> ```


I just checked; this ticket isn't the same bug.



---

archive/issue_comments_079588.json:
```json
{
    "body": "The upgrade to maxima 5.21.1 does not fix this.  After #8731:\n\n```\nsage: e, T, w = var(\"e T w\")    \nsage: assume(1-e^2>0)\nsage: integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)                                           \n0\n```",
    "created_at": "2010-05-13T04:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79588",
    "user": "https://github.com/jasongrout"
}
```

The upgrade to maxima 5.21.1 does not fix this.  After #8731:

```
sage: e, T, w = var("e T w")    
sage: assume(1-e^2>0)
sage: integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)                                           
0
```



---

archive/issue_comments_079589.json:
```json
{
    "body": "Maxima 5.23.2 still has this, and we still haven't reported it. \n\n```\nMaxima 5.23.2 http://maxima.sourceforge.net\nusing Lisp SBCL 1.0.24\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) assume(1-e^2>0);\n                                     2\n(%o1)                              [e  < 1]\n(%i3) integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*%pi);\n(%o3)                                  0\n```\nThis is now Maxima bug 3211975.",
    "created_at": "2011-03-14T20:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79589",
    "user": "https://github.com/kcrisman"
}
```

Maxima 5.23.2 still has this, and we still haven't reported it. 

```
Maxima 5.23.2 http://maxima.sourceforge.net
using Lisp SBCL 1.0.24
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) assume(1-e^2>0);
                                     2
(%o1)                              [e  < 1]
(%i3) integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*%pi);
(%o3)                                  0
```
This is now Maxima bug 3211975.



---

archive/issue_comments_079590.json:
```json
{
    "body": "According to [the bug report](http://sourceforge.net/tracker/?func=detail&aid=3211975&group_id=4933&atid=104933), this is now fixed.  However, some examples may still throw a Lisp error, so we should check out whether that will affect us before saying we're totally fixed when we upgrade.",
    "created_at": "2011-03-30T15:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79590",
    "user": "https://github.com/kcrisman"
}
```

According to [the bug report](http://sourceforge.net/tracker/?func=detail&aid=3211975&group_id=4933&atid=104933), this is now fixed.  However, some examples may still throw a Lisp error, so we should check out whether that will affect us before saying we're totally fixed when we upgrade.



---

archive/issue_comments_079591.json:
```json
{
    "body": "Maxima 5.28 is now out.",
    "created_at": "2012-08-14T01:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79591",
    "user": "https://github.com/kcrisman"
}
```

Maxima 5.28 is now out.



---

archive/issue_comments_079592.json:
```json
{
    "body": "See #13973 where this should (?) be fixed, just need a doctest here?",
    "created_at": "2013-01-20T01:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79592",
    "user": "https://github.com/kcrisman"
}
```

See #13973 where this should (?) be fixed, just need a doctest here?



---

archive/issue_events_021194.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21194"
}
```



---

archive/issue_events_021195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21195"
}
```



---

archive/issue_events_021196.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21196"
}
```



---

archive/issue_events_021197.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21197"
}
```



---

archive/issue_events_021198.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21198"
}
```



---

archive/issue_comments_079593.json:
```json
{
    "body": "In Maxima 5.33.0 (see #13973):\n\n```\n(%i1) assume(e^2<1);\n                                     2\n(%o1)                              [e  < 1]\n(%i2) integrate(cos(w+T)/(1+e*cos(T))^2, T, 0, 2*%pi);\n                      2\nIs abs(e) - sqrt(1 - e ) - 1 positive, negative or zero?\n\nnegative;\n   !          2     !\nIs !sqrt(1 - e ) - 1! - abs(e) positive, negative or zero?\n\nnegative;\n                                             2\n                           2 %pi e sqrt(1 - e ) cos(w)\n(%o2)                    - ---------------------------\n                                   4      2\n                                  e  - 2 e  + 1\n```\nThis appears to be the correct answer.  Note that the answers to both questions are \"negative\" for all *e* with -1 < *e* < 1, so it would be nice if Maxima didn't ask those questions.",
    "created_at": "2014-05-21T20:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79593",
    "user": "https://github.com/pjbruin"
}
```

In Maxima 5.33.0 (see #13973):

```
(%i1) assume(e^2<1);
                                     2
(%o1)                              [e  < 1]
(%i2) integrate(cos(w+T)/(1+e*cos(T))^2, T, 0, 2*%pi);
                      2
Is abs(e) - sqrt(1 - e ) - 1 positive, negative or zero?

negative;
   !          2     !
Is !sqrt(1 - e ) - 1! - abs(e) positive, negative or zero?

negative;
                                             2
                           2 %pi e sqrt(1 - e ) cos(w)
(%o2)                    - ---------------------------
                                   4      2
                                  e  - 2 e  + 1
```
This appears to be the correct answer.  Note that the answers to both questions are "negative" for all *e* with -1 < *e* < 1, so it would be nice if Maxima didn't ask those questions.



---

archive/issue_events_021199.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21199"
}
```



---

archive/issue_events_021200.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21200"
}
```



---

archive/issue_comments_079594.json:
```json
{
    "body": "> In Maxima 5.33.0 (see #13973):\n> This appears to be the correct answer.  Note that the answers to both questions are \"negative\" for all *e* with -1 < *e* < 1, so it would be nice if Maxima didn't ask those questions.\n\nThe thing noted in the message upstream when they closed their ticket\n\n```\nsage: integrate(cos(w+T)/(1+.5*cos(T))^2,T,0,2*pi)\n<boom>\n```\ndoes still happen, but I think that is a different issue tracked elsewhere here (the usual keepfloat thing).\n\nSo... do we have a reasonable test case to add here to confirm this is fixed and close it?",
    "created_at": "2014-10-20T13:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79594",
    "user": "https://github.com/kcrisman"
}
```

> In Maxima 5.33.0 (see #13973):
> This appears to be the correct answer.  Note that the answers to both questions are "negative" for all *e* with -1 < *e* < 1, so it would be nice if Maxima didn't ask those questions.

The thing noted in the message upstream when they closed their ticket

```
sage: integrate(cos(w+T)/(1+.5*cos(T))^2,T,0,2*pi)
<boom>
```
does still happen, but I think that is a different issue tracked elsewhere here (the usual keepfloat thing).

So... do we have a reasonable test case to add here to confirm this is fixed and close it?



---

archive/issue_comments_079595.json:
```json
{
    "body": "Here's the doctest:\n\n```\nsage: assume(1-e^2>0)\nsage: assume(abs(e)-sqrt(1-e^2)-1>0)\nsage: assume(abs(sqrt(1-e^2)-1)-abs(e)>0)\nsage: integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)\n2*pi*sqrt(-e^2 + 1)*e*cos(w)/(e^4 - 2*e^2 + 1)\n```",
    "created_at": "2015-02-01T13:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79595",
    "user": "https://github.com/rwst"
}
```

Here's the doctest:

```
sage: assume(1-e^2>0)
sage: assume(abs(e)-sqrt(1-e^2)-1>0)
sage: assume(abs(sqrt(1-e^2)-1)-abs(e)>0)
sage: integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)
2*pi*sqrt(-e^2 + 1)*e*cos(w)/(e^4 - 2*e^2 + 1)
```



---

archive/issue_comments_079596.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-02-02T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79596",
    "user": "https://github.com/rwst"
}
```

New commits:



---

archive/issue_comments_079597.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-02-02T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79597",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079598.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-02-02T14:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79598",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079599.json:
```json
{
    "body": "Your assumptions are contradictory: the first assumption (`1 - e^2 > 0`) implies the negation of the other two assumptions (see also comment:15).\n\nA fortiori, the other two assumptions (after negating) are actually redundant.  It is annoying that we have to add them; ideally, we would only declare this integral to be \"fixed\" if Maxima did not need the extra two assumptions...",
    "created_at": "2015-02-02T14:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79599",
    "user": "https://github.com/pjbruin"
}
```

Your assumptions are contradictory: the first assumption (`1 - e^2 > 0`) implies the negation of the other two assumptions (see also comment:15).

A fortiori, the other two assumptions (after negating) are actually redundant.  It is annoying that we have to add them; ideally, we would only declare this integral to be "fixed" if Maxima did not need the extra two assumptions...



---

archive/issue_events_021201.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2016-08-05T13:44:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21201"
}
```



---

archive/issue_events_021202.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2016-08-05T13:44:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "milestone": "sage-7.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21202"
}
```



---

archive/issue_comments_079600.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-08-05T13:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79600",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079601.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-08-05T13:44:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79601",
    "user": "https://github.com/rwst"
}
```

New commits:



---

archive/issue_comments_079602.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-05T15:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79602",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021203.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-08-07T20:01:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8728#event-21203"
}
```



---

archive/issue_comments_079603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-08-07T20:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79603",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_079604.json:
```json
{
    "body": "I noticed just now that this ticket has been closed; it seems comment:15 and comment:22 were ignored...",
    "created_at": "2016-08-11T08:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79604",
    "user": "https://github.com/pjbruin"
}
```

I noticed just now that this ticket has been closed; it seems comment:15 and comment:22 were ignored...



---

archive/issue_comments_079605.json:
```json
{
    "body": "That would seem so. I think you are asking for a feature (redundancy of additional assumptions) in Maxima that would warrant a separate ticket. I apologize for not answering earlier.",
    "created_at": "2016-08-11T09:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79605",
    "user": "https://github.com/rwst"
}
```

That would seem so. I think you are asking for a feature (redundancy of additional assumptions) in Maxima that would warrant a separate ticket. I apologize for not answering earlier.



---

archive/issue_comments_079606.json:
```json
{
    "body": "Replying to [comment:28 rws]:\n> I think you are asking for a feature (redundancy of additional assumptions) in Maxima that would warrant a separate ticket.\n\nThat too, but more importantly I meant the fact that the assumptions that are currently made in the doctest are mutually inconsistent:\n\n```\nassume(1-c^2 > 0)\nassume(abs(c) - sqrt(1-c^2) - 1 > 0)\nassume(abs(sqrt(1-c^2)-1) - abs(c) > 0)\n```\nNamely, the first assumption is equivalent to `-1 < c < 1`, and on this domain the functions `abs(c) - sqrt(1-c^2) - 1` and `abs(sqrt(1-c^2)-1) - abs(c)` are strictly negative.\n\nThere is already some functionality for detecting inconsistent assumptions (e.g. `assume(x > 0); assume(x < 0)` raises an error), but it doesn't detect this case.",
    "created_at": "2016-08-11T09:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8728#issuecomment-79606",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:28 rws]:
> I think you are asking for a feature (redundancy of additional assumptions) in Maxima that would warrant a separate ticket.

That too, but more importantly I meant the fact that the assumptions that are currently made in the doctest are mutually inconsistent:

```
assume(1-c^2 > 0)
assume(abs(c) - sqrt(1-c^2) - 1 > 0)
assume(abs(sqrt(1-c^2)-1) - abs(c) > 0)
```
Namely, the first assumption is equivalent to `-1 < c < 1`, and on this domain the functions `abs(c) - sqrt(1-c^2) - 1` and `abs(sqrt(1-c^2)-1) - abs(c)` are strictly negative.

There is already some functionality for detecting inconsistent assumptions (e.g. `assume(x > 0); assume(x < 0)` raises an error), but it doesn't detect this case.
