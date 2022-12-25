# Issue 1556: [with patch] improve readability of unknown username error page

archive/issues_001556.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: notebook\n\nThe current page you get when you try to login to the notebook with an unknown username is incredibly hard to read since it does not even alphabetize usernames.  This patch will alphabetize the list and put each username on a single line. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1556\n\n",
    "created_at": "2007-12-18T02:06:13Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "[with patch] improve readability of unknown username error page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1556",
    "user": "https://github.com/yqiang"
}
```
Assignee: boothby

Keywords: notebook

The current page you get when you try to login to the notebook with an unknown username is incredibly hard to read since it does not even alphabetize usernames.  This patch will alphabetize the list and put each username on a single line. 

Issue created by migration from https://trac.sagemath.org/ticket/1556





---

archive/issue_comments_009893.json:
```json
{
    "body": "Attachment [unknown_username.patch](tarball://root/attachments/some-uuid/ticket1556/unknown_username.patch) by @yqiang created at 2007-12-18 02:06:24",
    "created_at": "2007-12-18T02:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1556#issuecomment-9893",
    "user": "https://github.com/yqiang"
}
```

Attachment [unknown_username.patch](tarball://root/attachments/some-uuid/ticket1556/unknown_username.patch) by @yqiang created at 2007-12-18 02:06:24



---

archive/issue_comments_009894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-21T01:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1556#issuecomment-9894",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_009895.json:
```json
{
    "body": "Merged in 2.9.1 alpha2",
    "created_at": "2007-12-21T01:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1556#issuecomment-9895",
    "user": "https://github.com/rlmill"
}
```

Merged in 2.9.1 alpha2



---

archive/issue_events_001710.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-12-21T01:20:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1556",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1556#event-1710"
}
```



---

archive/issue_comments_009896.json:
```json
{
    "body": "\n```\n- Hide quoted text -\nOn Dec 20, 2007 10:57 PM, William Stein <wstein@gmail.com> wrote:\n> On Dec 20, 2007 6:24 PM, Robert Miller <rlmillster@gmail.com> wrote:\n> >\n> > As pointed out by Michael Abshoff, it seems like an information leak\n> > to list all the usernames on a notebook when you fail to use a valid\n> > one to log in. Thoughts?\n>\n> This exact question comes up about every other week.   Are you talking\n> about a public notebook like sagenb.org or sagenb.com?  If so, then\n> note that *anybody* can make a new account, and once they login\n> with that account, it is trivial for them -- in several different ways -- to get\n> a list of all user names.  If you're talking about a server that you personally\n> run but with no user accounts, then there is just one name, i.e., \"admin\".\n> In both cases, security by obscuring the existing usernames is no security\n> at all.\n>\n> So maybe you are talking about semi-private servers that have a fixed list\n> of accounts and users, like a normal UNIX system say, where potential\n> users cannot sign up for a new account -- only an admin can create accounts.\n> In this case getting a list of users would be a security issue.  But\n> you probably\n> don't mean this since it isn't implemented in sage (yet!).\n\nI should have finished by adding that there is no point at all in\nnot listing usernames in the scenarios in the first paragraph above -- that\nwould just be security by obscurity.  There is a point in not listing\nuser names in paragraph two above.  When Sage actually supports\nwhat is described in paragraph two, then when the notebook is in\nthat mode it shouldn't list usernames.\n\n```\n",
    "created_at": "2007-12-21T06:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1556#issuecomment-9896",
    "user": "https://github.com/williamstein"
}
```


```
- Hide quoted text -
On Dec 20, 2007 10:57 PM, William Stein <wstein@gmail.com> wrote:
> On Dec 20, 2007 6:24 PM, Robert Miller <rlmillster@gmail.com> wrote:
> >
> > As pointed out by Michael Abshoff, it seems like an information leak
> > to list all the usernames on a notebook when you fail to use a valid
> > one to log in. Thoughts?
>
> This exact question comes up about every other week.   Are you talking
> about a public notebook like sagenb.org or sagenb.com?  If so, then
> note that *anybody* can make a new account, and once they login
> with that account, it is trivial for them -- in several different ways -- to get
> a list of all user names.  If you're talking about a server that you personally
> run but with no user accounts, then there is just one name, i.e., "admin".
> In both cases, security by obscuring the existing usernames is no security
> at all.
>
> So maybe you are talking about semi-private servers that have a fixed list
> of accounts and users, like a normal UNIX system say, where potential
> users cannot sign up for a new account -- only an admin can create accounts.
> In this case getting a list of users would be a security issue.  But
> you probably
> don't mean this since it isn't implemented in sage (yet!).

I should have finished by adding that there is no point at all in
not listing usernames in the scenarios in the first paragraph above -- that
would just be security by obscurity.  There is a point in not listing
user names in paragraph two above.  When Sage actually supports
what is described in paragraph two, then when the notebook is in
that mode it shouldn't list usernames.

```

