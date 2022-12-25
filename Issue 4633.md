# Issue 4633: fix additional "Fortran-style" names and a coercion

archive/issues_004633.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: axiom\n\nIn order to run the the comparison of integration results between FriCAS and Maxima, it is also necessary to make some simple additions to the 'axiom.py' interface:\n\n```\nwspage@debian:~/sage-3.1.4/devel/sage-main/sage/interfaces$ hg diff\ndiff -r ed3f78f99d2a sage/interfaces/axiom.py\n--- a/sage/interfaces/axiom.py  Tue Nov 25 23:45:43 2008 -0500\n+++ b/sage/interfaces/axiom.py  Wed Nov 26 19:43:59 2008 -0500\n@@ -729,7 +729,10 @@\n        s = P.eval('unparse(%s::InputForm)'%self._name)\n        if 'translation error' in s or 'Cannot convert' in s:\n            raise NotImplementedError\n-        s = multiple_replace({'\\r\\n':'', # fix stupid Fortran-ish\n+        s = multiple_replace({'\\r\\n':'', # fix stupid Fortran-ish\n+                              'DLOG(':'log(',\n+                              'DEXP(':'exp(',\n+                              '::(':'', ',Symbol)':'',\n                              'DSIN(':'sin(',\n                              'DCOS(':'cos(',\n                              'DTAN(':'tan(',\n\n```\n\n---\n\nIntegration produce some additional \"Fortran-style\" names and a\ncoercion that have to be translated before the input form can be\nprocessed by Sage.\n\nWith this change we can do:\n\n```\n  test_int = integrand.integrate(x)\n  fricas_int = axiom.integrate(integrand,x).sage()\n  fricas_cmp = (test_int.simplify_full()-fricas_int.simplify_full()).simplify_full()\n  if (fricas_cmp == 0):\n      print \"FriCAS agrees with Maxima.\"\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4633\n\n",
    "created_at": "2008-11-27T01:42:53Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix additional \"Fortran-style\" names and a coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4633",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```
Assignee: @williamstein

Keywords: axiom

In order to run the the comparison of integration results between FriCAS and Maxima, it is also necessary to make some simple additions to the 'axiom.py' interface:

```
wspage@debian:~/sage-3.1.4/devel/sage-main/sage/interfaces$ hg diff
diff -r ed3f78f99d2a sage/interfaces/axiom.py
--- a/sage/interfaces/axiom.py  Tue Nov 25 23:45:43 2008 -0500
+++ b/sage/interfaces/axiom.py  Wed Nov 26 19:43:59 2008 -0500
@@ -729,7 +729,10 @@
        s = P.eval('unparse(%s::InputForm)'%self._name)
        if 'translation error' in s or 'Cannot convert' in s:
            raise NotImplementedError
-        s = multiple_replace({'\r\n':'', # fix stupid Fortran-ish
+        s = multiple_replace({'\r\n':'', # fix stupid Fortran-ish
+                              'DLOG(':'log(',
+                              'DEXP(':'exp(',
+                              '::(':'', ',Symbol)':'',
                              'DSIN(':'sin(',
                              'DCOS(':'cos(',
                              'DTAN(':'tan(',

```

---

Integration produce some additional "Fortran-style" names and a
coercion that have to be translated before the input form can be
processed by Sage.

With this change we can do:

```
  test_int = integrand.integrate(x)
  fricas_int = axiom.integrate(integrand,x).sage()
  fricas_cmp = (test_int.simplify_full()-fricas_int.simplify_full()).simplify_full()
  if (fricas_cmp == 0):
      print "FriCAS agrees with Maxima."

```


Issue created by migration from https://trac.sagemath.org/ticket/4633





---

archive/issue_comments_034758.json:
```json
{
    "body": "Hi Bill,\n\nplease attach a proper hg patch. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T01:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Bill,

please attach a proper hg patch. 

Cheers,

Michael



---

archive/issue_comments_034759.json:
```json
{
    "body": "Attachment [fortanish.patch](tarball://root/attachments/some-uuid/ticket4633/fortanish.patch) by bpage created at 2008-11-27 01:46:11\n\npatch file",
    "created_at": "2008-11-27T01:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34759",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Attachment [fortanish.patch](tarball://root/attachments/some-uuid/ticket4633/fortanish.patch) by bpage created at 2008-11-27 01:46:11

patch file



---

archive/issue_comments_034760.json:
```json
{
    "body": "Sorry. What is a \"hg patch\"?",
    "created_at": "2008-11-27T01:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34760",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Sorry. What is a "hg patch"?



---

archive/issue_comments_034761.json:
```json
{
    "body": "Replying to [comment:2 bpage]:\n> Sorry. What is a \"hg patch\"?\n\n\nA mercurial patch. hg is the chemical symbol for mercurial, so that is why the mercurial binary is called hg. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T01:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 bpage]:
> Sorry. What is a "hg patch"?


A mercurial patch. hg is the chemical symbol for mercurial, so that is why the mercurial binary is called hg. 

Cheers,

Michael



---

archive/issue_comments_034762.json:
```json
{
    "body": "Further note: The new release of FriCAS-1.0.4 which is not yet available as a Sage spkg no longer produces this \"Fortranish\" functions names.",
    "created_at": "2008-11-27T01:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34762",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Further note: The new release of FriCAS-1.0.4 which is not yet available as a Sage spkg no longer produces this "Fortranish" functions names.



---

archive/issue_comments_034763.json:
```json
{
    "body": "> A mercurial patch. hg is the chemical symbol for mercurial, so that is why the mercurial binary is called hg. \n\n\n:~) I meant, how do I create a \"hg patch\" if not by \"hg diff\"?",
    "created_at": "2008-11-27T01:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34763",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

> A mercurial patch. hg is the chemical symbol for mercurial, so that is why the mercurial binary is called hg. 


:~) I meant, how do I create a "hg patch" if not by "hg diff"?



---

archive/issue_comments_034764.json:
```json
{
    "body": "Hi Bill,\n\n* Check in your changes: hg commit\n* export the last commit: hg export tip > trac_4633.patch\n* attach patch to this ticket\n* prepend \"[with patch, needs review] to summary line\n* wait for review \n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T02:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Bill,

* Check in your changes: hg commit
* export the last commit: hg export tip > trac_4633.patch
* attach patch to this ticket
* prepend "[with patch, needs review] to summary line
* wait for review 

Cheers,

Michael



---

archive/issue_comments_034765.json:
```json
{
    "body": "Attachment [trac_4633.patch](tarball://root/attachments/some-uuid/ticket4633/trac_4633.patch) by bpage created at 2008-11-27 05:05:01\n\n[with patch, needs review] Better?",
    "created_at": "2008-11-27T05:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34765",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Attachment [trac_4633.patch](tarball://root/attachments/some-uuid/ticket4633/trac_4633.patch) by bpage created at 2008-11-27 05:05:01

[with patch, needs review] Better?



---

archive/issue_comments_034766.json:
```json
{
    "body": "Is there a specific procedure for installing (and testing) these kinds of patches? That is, how do I get Sage to know that the code has been updated? This kind of thing would be nice on a wiki page for new developers. Or have I just missed it?",
    "created_at": "2008-11-30T21:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34766",
    "user": "https://github.com/tjl"
}
```

Is there a specific procedure for installing (and testing) these kinds of patches? That is, how do I get Sage to know that the code has been updated? This kind of thing would be nice on a wiki page for new developers. Or have I just missed it?



---

archive/issue_comments_034767.json:
```json
{
    "body": "Replying to [comment:7 tjlahey]:\n> Is there a specific procedure for installing (and testing) these kinds of patches? That is, how do I get Sage to know that the code has been updated? This kind of thing would be nice on a wiki page for new developers. Or have I just missed it?\n\n\nThis is what I do:\n\n0. Pretest, e.g. try: axiom(1/log(x)).sage()\n\n```\n    NotImplementedError\n```\n1. Click on the link to that patch: \"trac_4633.patch\"\n2. Click on the link to \"original format\"\n3. Save the patch file somewhere, e.g. ~/trac_4633.patch\n4. cd sage*/devel/sage-main\n5. apply the patch: patch -p1 < ~/trac_4633.patch\n6. re-build sage: sage -br\n7. test, e.g. try: axiom(1/log(x)).sage()\n\n```\n    1/log(x)\n```\n\nI guess that in a more complete patch I should have added some tests like this to the doc tests. This just seemed too simple.",
    "created_at": "2008-12-01T03:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34767",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Replying to [comment:7 tjlahey]:
> Is there a specific procedure for installing (and testing) these kinds of patches? That is, how do I get Sage to know that the code has been updated? This kind of thing would be nice on a wiki page for new developers. Or have I just missed it?


This is what I do:

0. Pretest, e.g. try: axiom(1/log(x)).sage()

```
    NotImplementedError
```
1. Click on the link to that patch: "trac_4633.patch"
2. Click on the link to "original format"
3. Save the patch file somewhere, e.g. ~/trac_4633.patch
4. cd sage*/devel/sage-main
5. apply the patch: patch -p1 < ~/trac_4633.patch
6. re-build sage: sage -br
7. test, e.g. try: axiom(1/log(x)).sage()

```
    1/log(x)
```

I guess that in a more complete patch I should have added some tests like this to the doc tests. This just seemed too simple.



---

archive/issue_comments_034768.json:
```json
{
    "body": "Replying to [comment:8 bpage]:\n\nIt doesn't want to apply. In my version of sage/interfaces/axiom.py, I don't have:\n\n```\n         s = P.eval('unparse(%s::InputForm)'%self._name) \n         if 'translation error' in s or 'Cannot convert' in s: \n             raise NotImplementedError\n```\nso I get a rejection when I attempt to apply the patch. I'm using Sage 3.2.",
    "created_at": "2008-12-02T23:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34768",
    "user": "https://github.com/tjl"
}
```

Replying to [comment:8 bpage]:

It doesn't want to apply. In my version of sage/interfaces/axiom.py, I don't have:

```
         s = P.eval('unparse(%s::InputForm)'%self._name) 
         if 'translation error' in s or 'Cannot convert' in s: 
             raise NotImplementedError
```
so I get a rejection when I attempt to apply the patch. I'm using Sage 3.2.



---

archive/issue_comments_034769.json:
```json
{
    "body": "This is probably on top of #4036, which itself needs to be slightly rebased.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T23:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is probably on top of #4036, which itself needs to be slightly rebased.

Cheers,

Michael



---

archive/issue_comments_034770.json:
```json
{
    "body": "Replying to [comment:10 mabshoff]:\n> This is probably on top of #4036, which itself needs to be slightly rebased.\n\n\nCorrect. What is the proper procedure to follow in this case?",
    "created_at": "2008-12-03T00:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34770",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Replying to [comment:10 mabshoff]:
> This is probably on top of #4036, which itself needs to be slightly rebased.


Correct. What is the proper procedure to follow in this case?



---

archive/issue_comments_034771.json:
```json
{
    "body": "Hi Bill,\n\nJust mention it on the ticket and/or change the summary line like I just did.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T00:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Bill,

Just mention it on the ticket and/or change the summary line like I just did.

Cheers,

Michael



---

archive/issue_comments_034772.json:
```json
{
    "body": "Please add a doctest that illustrates what you're fixing and mark it \"#optional - fricas\".    The doctest could also include your integration example.\n\nThanks!!",
    "created_at": "2008-12-06T22:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34772",
    "user": "https://github.com/williamstein"
}
```

Please add a doctest that illustrates what you're fixing and mark it "#optional - fricas".    The doctest could also include your integration example.

Thanks!!



---

archive/issue_events_010561.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10561"
}
```



---

archive/issue_events_010562.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10562"
}
```



---

archive/issue_events_010563.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10563"
}
```



---

archive/issue_events_010564.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10564"
}
```



---

archive/issue_events_010565.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10565"
}
```



---

archive/issue_comments_034773.json:
```json
{
    "body": "According to http://trac.sagemath.org/ticket/4633#comment:4, this is no longer needed in recent versions of FriCAS. Sage is now using FriCAS 1.0.9 (#9354).\n\nSo maybe this can be closed ?",
    "created_at": "2014-07-19T12:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34773",
    "user": "https://github.com/fchapoton"
}
```

According to http://trac.sagemath.org/ticket/4633#comment:4, this is no longer needed in recent versions of FriCAS. Sage is now using FriCAS 1.0.9 (#9354).

So maybe this can be closed ?



---

archive/issue_events_010566.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2014-07-19T12:31:28Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10566"
}
```



---

archive/issue_events_010567.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2014-07-19T12:31:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10567"
}
```



---

archive/issue_comments_034774.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-07-19T12:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34774",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_034775.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-16T11:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34775",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034776.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-10-27T16:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4633#issuecomment-34776",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_010568.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-10-27T16:26:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4633",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4633#event-10568"
}
```
