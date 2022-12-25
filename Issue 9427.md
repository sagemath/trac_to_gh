# Issue 9427: implement fricas integrator

archive/issues_009427.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @hemmecke\n\nKeywords: integrate, fricas\n\nThe attached patch adds the option algorithm=\"fricas\" to the integrate\ncommand.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9427\n\n",
    "created_at": "2010-07-05T08:48:40Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.5",
    "title": "implement fricas integrator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9427",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: @burcin

CC:  @hemmecke

Keywords: integrate, fricas

The attached patch adds the option algorithm="fricas" to the integrate
command.

Issue created by migration from https://trac.sagemath.org/ticket/9427





---

archive/issue_comments_089787.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-05T08:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89787",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089788.json:
```json
{
    "body": "Attachment [trac_9427-fricas-integrate.patch](tarball://root/attachments/some-uuid/ticket9427/trac_9427-fricas-integrate.patch) by whuss created at 2010-07-05 08:51:37",
    "created_at": "2010-07-05T08:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89788",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [trac_9427-fricas-integrate.patch](tarball://root/attachments/some-uuid/ticket9427/trac_9427-fricas-integrate.patch) by whuss created at 2010-07-05 08:51:37



---

archive/issue_comments_089789.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-05T09:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89789",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089790.json:
```json
{
    "body": "This looks great. Thanks for the quick patch!\n\nI have a few minor comments:\n* the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:\n {{{\nsage: infinity._fricas_init_()\n\"%plusInfinity\"\n}}}\n and we can just do af = a._fricas_().\n* Similarly, I suggest moving the code for converting the result back to the `_sage_()` method of the fricas interface.",
    "created_at": "2010-07-05T09:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89790",
    "user": "https://github.com/burcin"
}
```

This looks great. Thanks for the quick patch!

I have a few minor comments:
* the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:
 {{{
sage: infinity._fricas_init_()
"%plusInfinity"
}}}
 and we can just do af = a._fricas_().
* Similarly, I suggest moving the code for converting the result back to the `_sage_()` method of the fricas interface.



---

archive/issue_comments_089791.json:
```json
{
    "body": "Attachment [fricas_infinity.patch](tarball://root/attachments/some-uuid/ticket9427/fricas_infinity.patch) by whuss created at 2010-07-05 15:11:20\n\nReplying to [comment:2 burcin]:\n>  * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:\n>  {{{\n> sage: infinity._fricas_init_()\n> \"%plusInfinity\"\n> }}}\n\nI tried this (see fricas_infinity.patch), but for some reason that I don't understand the output of\n_fricas_init_() changes into something which is not a valid fricas expression.\n\n\n```\nsage: oo._fricas_init_()\n'%plusInfinity'\n```\n\n\nbut\n\n\n```\nsage: oo._fricas_()\n+ infinity\n```\n\n\nI have no idea what is going on here.",
    "created_at": "2010-07-05T15:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89791",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [fricas_infinity.patch](tarball://root/attachments/some-uuid/ticket9427/fricas_infinity.patch) by whuss created at 2010-07-05 15:11:20

Replying to [comment:2 burcin]:
>  * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:
>  {{{
> sage: infinity._fricas_init_()
> "%plusInfinity"
> }}}

I tried this (see fricas_infinity.patch), but for some reason that I don't understand the output of
_fricas_init_() changes into something which is not a valid fricas expression.


```
sage: oo._fricas_init_()
'%plusInfinity'
```


but


```
sage: oo._fricas_()
+ infinity
```


I have no idea what is going on here.



---

archive/issue_comments_089792.json:
```json
{
    "body": "Is \"algorithm\" the most appropiate word here? To me, Fricas, Aximom, Maxima etc are software packages, not algorithms. They implement many differerent algorithms.\n\nI'm not a mathmatician, but certainly my mathematical training would never have suggested that Fricas was an algorithm. \n\nI would have thought something like\n\n\n```\nintegrate(f(x), x, use=\"fricas\") \nintegrate(f(x), x, software=\"fricas\") \nintegrate(f(x), x, method=\"fricas\") \n```\n\n\nwould be better than \n\n\n```\nintegrate(f(x), x, algorithm=\"fricas\") \n```\n\n\nI don't claim any of my choices are optimal, but I think all of them are better than \"algorithm\". \n\nDave",
    "created_at": "2010-07-06T23:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89792",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Is "algorithm" the most appropiate word here? To me, Fricas, Aximom, Maxima etc are software packages, not algorithms. They implement many differerent algorithms.

I'm not a mathmatician, but certainly my mathematical training would never have suggested that Fricas was an algorithm. 

I would have thought something like


```
integrate(f(x), x, use="fricas") 
integrate(f(x), x, software="fricas") 
integrate(f(x), x, method="fricas") 
```


would be better than 


```
integrate(f(x), x, algorithm="fricas") 
```


I don't claim any of my choices are optimal, but I think all of them are better than "algorithm". 

Dave



---

archive/issue_comments_089793.json:
```json
{
    "body": "Replying to [comment:4 drkirkby]:\n\nIf I do\n\n\n```\nsage: search_def('algorithm=')\n```\n\n\nI get **150** results. So the 'algorithm' convention is widely\nused in Sage, I don't think it makes sense to change this\nat this point.",
    "created_at": "2010-07-07T07:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89793",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:4 drkirkby]:

If I do


```
sage: search_def('algorithm=')
```


I get **150** results. So the 'algorithm' convention is widely
used in Sage, I don't think it makes sense to change this
at this point.



---

archive/issue_events_023285.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2011-05-10T17:21:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23285"
}
```



---

archive/issue_comments_089794.json:
```json
{
    "body": "Replying to [comment:3 whuss]:\n> Replying to [comment:2 burcin]:\n> >  * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:\n  {{{\n sage: infinity._fricas_init_()\n \"%plusInfinity\"\n }}}\n> \n> I tried this (see fricas_infinity.patch), but for some reason that I don't understand the output of\n> _fricas_init_() changes into something which is not a valid fricas expression.\n> \n {{{\n sage: oo._fricas_init_()\n '%plusInfinity'\n }}}\n> \n> but\n> \n> {{{\n> sage: oo._fricas_()\n> + infinity\n> }}}\n> \n> I have no idea what is going on here.\n\nThis seems to be how fricas prints `%plusInfinity`. Ralf, can you help us with this?",
    "created_at": "2011-05-10T17:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89794",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:3 whuss]:
> Replying to [comment:2 burcin]:
> >  * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:
  {{{
 sage: infinity._fricas_init_()
 "%plusInfinity"
 }}}
> 
> I tried this (see fricas_infinity.patch), but for some reason that I don't understand the output of
> _fricas_init_() changes into something which is not a valid fricas expression.
> 
 {{{
 sage: oo._fricas_init_()
 '%plusInfinity'
 }}}
> 
> but
> 
> {{{
> sage: oo._fricas_()
> + infinity
> }}}
> 
> I have no idea what is going on here.

This seems to be how fricas prints `%plusInfinity`. Ralf, can you help us with this?



---

archive/issue_comments_089795.json:
```json
{
    "body": "Well, not quite right, as http://axiom-wiki.newsynthesis.org/PerCent shows. I've added\n\n```\n)set output algebra on\n```\n\nin order to also show the ascii output. Otherwise mathaction renders tex output of axiom. These things starting with a percent sign are only used for input. What exactly gets printed depends on the ')set output' settings.",
    "created_at": "2011-05-10T18:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89795",
    "user": "https://github.com/hemmecke"
}
```

Well, not quite right, as http://axiom-wiki.newsynthesis.org/PerCent shows. I've added

```
)set output algebra on
```

in order to also show the ascii output. Otherwise mathaction renders tex output of axiom. These things starting with a percent sign are only used for input. What exactly gets printed depends on the ')set output' settings.



---

archive/issue_comments_089796.json:
```json
{
    "body": "Also look at the exports of OrderedCompletion.\nhttps://github.com/hemmecke/fricas-svn/blob/master/src/algebra/complet.spad.pamphlet#L20\nObviously also 'plusInfinity()' and 'minusInfinity()' could be used as input.\n\nThe output is constructed in\nhttps://github.com/hemmecke/fricas-svn/blob/master/src/algebra/complet.spad.pamphlet#L59\nHow the symbol infinity appears is hidden inside OutputForm and probably deeper.\n\n```\n)set output tex on\n(1) -> plusInfinity()      \n\n   (1)   + infinity\n$$\n+\\infty \n\\leqno(1)\n$$\n\n                                             Type: OrderedCompletion(Integer)\n```\n",
    "created_at": "2011-05-10T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89796",
    "user": "https://github.com/hemmecke"
}
```

Also look at the exports of OrderedCompletion.
https://github.com/hemmecke/fricas-svn/blob/master/src/algebra/complet.spad.pamphlet#L20
Obviously also 'plusInfinity()' and 'minusInfinity()' could be used as input.

The output is constructed in
https://github.com/hemmecke/fricas-svn/blob/master/src/algebra/complet.spad.pamphlet#L59
How the symbol infinity appears is hidden inside OutputForm and probably deeper.

```
)set output tex on
(1) -> plusInfinity()      

   (1)   + infinity
$$
+\infty 
\leqno(1)
$$

                                             Type: OrderedCompletion(Integer)
```




---

archive/issue_comments_089797.json:
```json
{
    "body": "So the ascii output for plusInfinity is \"+ infinity\" and the `_fricas_init_()` method in attachment:fricas_infinity.patch works as intended.\n\nWilfried, will you have time to revise the patch? Note that when #9880 is merged (almost) all symbolics patches will need to be rebased.",
    "created_at": "2011-05-10T18:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89797",
    "user": "https://github.com/burcin"
}
```

So the ascii output for plusInfinity is "+ infinity" and the `_fricas_init_()` method in attachment:fricas_infinity.patch works as intended.

Wilfried, will you have time to revise the patch? Note that when #9880 is merged (almost) all symbolics patches will need to be rebased.



---

archive/issue_events_023286.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23286"
}
```



---

archive/issue_events_023287.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23287"
}
```



---

archive/issue_events_023288.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23288"
}
```



---

archive/issue_events_023289.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23289"
}
```



---

archive/issue_events_023290.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23290"
}
```



---

archive/issue_events_023291.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23291"
}
```



---

archive/issue_events_023292.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23292"
}
```



---

archive/issue_events_023293.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23293"
}
```



---

archive/issue_comments_089798.json:
```json
{
    "body": "Replying to [comment:4 drkirkby]:\n> Is \"algorithm\" the most appropiate word here? To me, Fricas, Aximom, Maxima etc are software packages, not algorithms. They implement many differerent algorithms.\n> \n> I'm not a mathmatician, but certainly my mathematical training would never have suggested that Fricas was an algorithm. \n> \n> I would have thought something like\n> \n> {{{\n> integrate(f(x), x, use=\"fricas\") \n> integrate(f(x), x, software=\"fricas\") \n> integrate(f(x), x, method=\"fricas\") \n> }}}\n> \n> would be better than \n> \n> {{{\n> integrate(f(x), x, algorithm=\"fricas\") \n> }}}\n> \n> I don't claim any of my choices are optimal, but I think all of them are better than \"algorithm\". \n\n+1 for `use`, `software` or `library`\nMoreover, in some situation, when we call the software (fricas, maxima, ...) we might want to feed it with an option `algorithm`.\n\nVincent",
    "created_at": "2014-12-07T12:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89798",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:4 drkirkby]:
> Is "algorithm" the most appropiate word here? To me, Fricas, Aximom, Maxima etc are software packages, not algorithms. They implement many differerent algorithms.
> 
> I'm not a mathmatician, but certainly my mathematical training would never have suggested that Fricas was an algorithm. 
> 
> I would have thought something like
> 
> {{{
> integrate(f(x), x, use="fricas") 
> integrate(f(x), x, software="fricas") 
> integrate(f(x), x, method="fricas") 
> }}}
> 
> would be better than 
> 
> {{{
> integrate(f(x), x, algorithm="fricas") 
> }}}
> 
> I don't claim any of my choices are optimal, but I think all of them are better than "algorithm". 

+1 for `use`, `software` or `library`
Moreover, in some situation, when we call the software (fricas, maxima, ...) we might want to feed it with an option `algorithm`.

Vincent



---

archive/issue_comments_089799.json:
```json
{
    "body": "I have made a git branch with the attached files, rebased on 6.5.b2\n----\nNew commits:",
    "created_at": "2014-12-07T17:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89799",
    "user": "https://github.com/fchapoton"
}
```

I have made a git branch with the attached files, rebased on 6.5.b2
----
New commits:



---

archive/issue_comments_089800.json:
```json
{
    "body": "Replying to [comment:14 vdelecroix]:\n> Moreover, in some situation, when we call the software (fricas, maxima, ...) we might want to feed it with an option `algorithm`.\nFirst I agreed with this, but now I think it would be easy to allow something like `algorithm=fricas-risch`, and this would then be more convenient than `software=fricas,algorithm=risch`. Whereas changing `algorithm` to `software` would be annoying as hell.",
    "created_at": "2015-02-02T09:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89800",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:14 vdelecroix]:
> Moreover, in some situation, when we call the software (fricas, maxima, ...) we might want to feed it with an option `algorithm`.
First I agreed with this, but now I think it would be easy to allow something like `algorithm=fricas-risch`, and this would then be more convenient than `software=fricas,algorithm=risch`. Whereas changing `algorithm` to `software` would be annoying as hell.



---

archive/issue_comments_089801.json:
```json
{
    "body": "Replying to [comment:2 burcin]:\n>  * Similarly, I suggest moving the code for converting the result back to the `_sage_()` method of the fricas interface.\nI know this is how Sympy does it but I think such a decision is up to the Fricas developers.",
    "created_at": "2015-02-02T10:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89801",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:2 burcin]:
>  * Similarly, I suggest moving the code for converting the result back to the `_sage_()` method of the fricas interface.
I know this is how Sympy does it but I think such a decision is up to the Fricas developers.



---

archive/issue_comments_089802.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-02T10:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89802",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089803.json:
```json
{
    "body": "This looks good and tests OK in `symbolic` and `rings`.",
    "created_at": "2015-02-02T10:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89803",
    "user": "https://github.com/rwst"
}
```

This looks good and tests OK in `symbolic` and `rings`.



---

archive/issue_comments_089804.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-02T10:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89804",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089805.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-02T10:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89805",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023294.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-02-03T09:33:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23294"
}
```



---

archive/issue_events_023295.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-02-03T09:33:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "milestone": "sage-6.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23295"
}
```



---

archive/issue_comments_089806.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-02-17T19:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9427#issuecomment-89806",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_023296.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-02-17T19:28:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9427",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9427#event-23296"
}
```
