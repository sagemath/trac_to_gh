# Issue 8526: Missing usernames in trac emails

archive/issues_008526.json:
```json
{
    "body": "Assignee: @haraldschilly\n\nCC:  @hivert\n\nIn a number of emails I get from trac, I see lines like this:\n\n```\nChanges (by {'newvalue': u'Fr\\xe9d\\xe9ric Chapoton', 'oldvalue': ''}):\n```\n\nThis should be an actual username instead. The problem seems to appear only when non-ASCII characters are involved.\n\nI'm not sure if this is an actual trac bug or if it's something about our configuration. For this ticket, someone should figure that out, and either file a new bug, fix the trac configuration, or file a bug with trac itself (if that's where the issue is).\n\nThis came up on the following sage-devel thread: \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/060f5430428fd945\n\nIssue created by migration from https://trac.sagemath.org/ticket/8526\n\n",
    "closed_at": "2017-01-21T18:03:11Z",
    "created_at": "2010-03-13T18:10:45Z",
    "labels": [
        "component: website/wiki",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Missing usernames in trac emails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8526",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @haraldschilly

CC:  @hivert

In a number of emails I get from trac, I see lines like this:

```
Changes (by {'newvalue': u'Fr\xe9d\xe9ric Chapoton', 'oldvalue': ''}):
```

This should be an actual username instead. The problem seems to appear only when non-ASCII characters are involved.

I'm not sure if this is an actual trac bug or if it's something about our configuration. For this ticket, someone should figure that out, and either file a new bug, fix the trac configuration, or file a bug with trac itself (if that's where the issue is).

This came up on the following sage-devel thread: 

http://groups.google.com/group/sage-devel/browse_thread/thread/060f5430428fd945

Issue created by migration from https://trac.sagemath.org/ticket/8526





---

archive/issue_events_020500.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-03-04T15:52:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20500"
}
```



---

archive/issue_comments_076925.json:
```json
{
    "body": "Fixed a while ago.",
    "created_at": "2014-03-04T15:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76925",
    "user": "https://github.com/mezzarobba"
}
```

Fixed a while ago.



---

archive/issue_comments_076926.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-04T15:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76926",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076927.json:
```json
{
    "body": "I got this on 4 march 2014:\n\n```\n#11840: sage.symbolic.expression.Expression.collect_common_factors has no\ndocumentation\n-------------------------------------+-------------------------------------\n       Reporter:  mjo                |        Owner:  mvngu\n           Type:  defect             |       Status:  needs_review\n       Priority:  major              |    Milestone:  sage-6.2\n      Component:  documentation      |   Resolution:\n       Keywords:  symbolic,          |    Merged in:\n  beginner                           |    Reviewers:\n        Authors:  Fr\u00e9d\u00e9ric Chapoton  |  Work issues:\nReport Upstream:  N/A                |       Commit:\n         Branch:  u/chapoton/11840   |  06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6\n   Dependencies:                     |     Stopgaps:\n-------------------------------------+-------------------------------------\nChanges (by {'newvalue': u'Fr\\xe9d\\xe9ric Chapoton', 'oldvalue': ''}):\n\n * status:  new => needs_review\n * commit:   => 06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6\n * branch:   => u/chapoton/11840\n * author:   => Fr\u00e9d\u00e9ric Chapoton\n\n\nComment:\n\n Here is a git branch with a little bit more documentation for this method.\n\n I have also taken the opportunity to put raise statement into python3\n format, and to use the trac role to add links to the tickets.\n ----\n New commits:\n ||[http://git.sagemath.org/sage.git/commit/?id=eeeb29316df0b8603bd73367fb6fd527c383692f\n eeeb293]||{{{trac #11840 first step, plus doc python 3 and trac role\n cleanup}}}||\n ||[http://git.sagemath.org/sage.git/commit/?id=06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6\n 06d4fe0]||`trac #11840 details, making sure that tests pass`||\n\n--\nTicket URL: <http://trac.sagemath.org/ticket/11840#comment:4>\nSage <http://www.sagemath.org>\nSage: Creating a Viable Open Source Alternative to Magma, Maple, Mathematica, and MATLAB\n```",
    "created_at": "2014-03-05T15:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76927",
    "user": "https://github.com/jdemeyer"
}
```

I got this on 4 march 2014:

```
#11840: sage.symbolic.expression.Expression.collect_common_factors has no
documentation
-------------------------------------+-------------------------------------
       Reporter:  mjo                |        Owner:  mvngu
           Type:  defect             |       Status:  needs_review
       Priority:  major              |    Milestone:  sage-6.2
      Component:  documentation      |   Resolution:
       Keywords:  symbolic,          |    Merged in:
  beginner                           |    Reviewers:
        Authors:  Frédéric Chapoton  |  Work issues:
Report Upstream:  N/A                |       Commit:
         Branch:  u/chapoton/11840   |  06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6
   Dependencies:                     |     Stopgaps:
-------------------------------------+-------------------------------------
Changes (by {'newvalue': u'Fr\xe9d\xe9ric Chapoton', 'oldvalue': ''}):

 * status:  new => needs_review
 * commit:   => 06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6
 * branch:   => u/chapoton/11840
 * author:   => Frédéric Chapoton


Comment:

 Here is a git branch with a little bit more documentation for this method.

 I have also taken the opportunity to put raise statement into python3
 format, and to use the trac role to add links to the tickets.
 ----
 New commits:
 ||[http://git.sagemath.org/sage.git/commit/?id=eeeb29316df0b8603bd73367fb6fd527c383692f
 eeeb293]||{{{trac #11840 first step, plus doc python 3 and trac role
 cleanup}}}||
 ||[http://git.sagemath.org/sage.git/commit/?id=06d4fe0e2b1c40cbebd4f72ffd171ba9b2389db6
 06d4fe0]||`trac #11840 details, making sure that tests pass`||

--
Ticket URL: <http://trac.sagemath.org/ticket/11840#comment:4>
Sage <http://www.sagemath.org>
Sage: Creating a Viable Open Source Alternative to Magma, Maple, Mathematica, and MATLAB
```



---

archive/issue_comments_076928.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-03-05T15:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76928",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_020501.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-03-05T15:38:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20501"
}
```



---

archive/issue_events_020502.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-03-05T15:38:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20502"
}
```



---

archive/issue_comments_076929.json:
```json
{
    "body": "Also recently:\n\n```\n#15857: change the licenses of schemes/toric/points.py,\nrings/number_field/splitting_field.py, libs/readline.pyx to GPLv2+ (from\nGPLv3+)\n-------------------------------------+-------------------------------------\n       Reporter:  was                |        Owner:\n           Type:  defect             |       Status:  positive_review\n       Priority:  major              |    Milestone:  sage-6.2\n      Component:  misc               |   Resolution:\n       Keywords:                     |    Merged in:\n        Authors:  Julian R\u00fcth        |    Reviewers:  Jeroen Demeyer\nReport Upstream:  N/A                |  Work issues:\n         Branch:                     |       Commit:\n  u/saraedum/ticket/15857            |  9566989f4aedf02479a125943e9c0570db0281e9\n   Dependencies:                     |     Stopgaps:\n-------------------------------------+-------------------------------------\nChanges (by {'newvalue': u'Julian R\\xfcth', 'oldvalue': ''}):\n\n * author:   => Julian R\u00fcth\n\n\nComment:\n\n (sorry)\n\n--\nTicket URL: <http://trac.sagemath.org/ticket/15857#comment:12>\nSage <http://www.sagemath.org>\nSage: Creating a Viable Open Source Alternative to Magma, Maple, Mathematica, and MATLAB\n```",
    "created_at": "2014-03-05T15:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76929",
    "user": "https://github.com/jdemeyer"
}
```

Also recently:

```
#15857: change the licenses of schemes/toric/points.py,
rings/number_field/splitting_field.py, libs/readline.pyx to GPLv2+ (from
GPLv3+)
-------------------------------------+-------------------------------------
       Reporter:  was                |        Owner:
           Type:  defect             |       Status:  positive_review
       Priority:  major              |    Milestone:  sage-6.2
      Component:  misc               |   Resolution:
       Keywords:                     |    Merged in:
        Authors:  Julian Rüth        |    Reviewers:  Jeroen Demeyer
Report Upstream:  N/A                |  Work issues:
         Branch:                     |       Commit:
  u/saraedum/ticket/15857            |  9566989f4aedf02479a125943e9c0570db0281e9
   Dependencies:                     |     Stopgaps:
-------------------------------------+-------------------------------------
Changes (by {'newvalue': u'Julian R\xfcth', 'oldvalue': ''}):

 * author:   => Julian Rüth


Comment:

 (sorry)

--
Ticket URL: <http://trac.sagemath.org/ticket/15857#comment:12>
Sage <http://www.sagemath.org>
Sage: Creating a Viable Open Source Alternative to Magma, Maple, Mathematica, and MATLAB
```



---

archive/issue_events_020503.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20503"
}
```



---

archive/issue_events_020504.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20504"
}
```



---

archive/issue_events_020505.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20505"
}
```



---

archive/issue_events_020506.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20506"
}
```



---

archive/issue_comments_076930.json:
```json
{
    "body": "This ticket appears to be outdated and should be closed.",
    "created_at": "2016-09-25T00:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76930",
    "user": "https://github.com/mkoeppe"
}
```

This ticket appears to be outdated and should be closed.



---

archive/issue_events_020507.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2016-09-25T00:59:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20507"
}
```



---

archive/issue_events_020508.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2016-09-25T00:59:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20508"
}
```



---

archive/issue_comments_076931.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-09-25T00:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76931",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076932.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-09-25T01:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76932",
    "user": "https://github.com/paulmasson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020509.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-01-21T18:03:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8526#event-20509"
}
```



---

archive/issue_comments_076933.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-01-21T18:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8526#issuecomment-76933",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
