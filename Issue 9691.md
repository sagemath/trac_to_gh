# Issue 9691: Make another Trac search box or button

archive/issues_009691.json:
```json
{
    "body": "Assignee: mvngu, schilly\n\nCC:  embray slelievre\n\nOr something like that.  The problem is that Search at the top gives all tickets, closed or open, with the content, while often one wants just to search open tickets.  Since the only other option is clicking View Tickets, then Custom Query, etc. (notice that even the Search tab doesn't do anything useful different from the Search box), and THEN clicking all the non-'closed' options, we should improve this.  \n\nI'm putting component website/wiki, but only because there isn't a trac component.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9691\n\n",
    "created_at": "2010-08-05T15:11:13Z",
    "labels": [
        "website/wiki",
        "major",
        "enhancement"
    ],
    "title": "Make another Trac search box or button",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9691",
    "user": "kcrisman"
}
```
Assignee: mvngu, schilly

CC:  embray slelievre

Or something like that.  The problem is that Search at the top gives all tickets, closed or open, with the content, while often one wants just to search open tickets.  Since the only other option is clicking View Tickets, then Custom Query, etc. (notice that even the Search tab doesn't do anything useful different from the Search box), and THEN clicking all the non-'closed' options, we should improve this.  

I'm putting component website/wiki, but only because there isn't a trac component.

Issue created by migration from https://trac.sagemath.org/ticket/9691





---

archive/issue_comments_094198.json:
```json
{
    "body": "Changing keywords from \"\" to \"Trac\".",
    "created_at": "2018-08-01T16:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94198",
    "user": "slelievre"
}
```

Changing keywords from "" to "Trac".



---

archive/issue_comments_094199.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-08-03T17:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94199",
    "user": "embray"
}
```

Resolution: wontfix



---

archive/issue_comments_094200.json:
```json
{
    "body": "If somebody really wants this they could open an issue at https://github.com/sagemath/sage_trac_plugin but this is a non-trivial plugin and can be easily achieved with a custom query.",
    "created_at": "2018-08-03T17:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94200",
    "user": "embray"
}
```

If somebody really wants this they could open an issue at https://github.com/sagemath/sage_trac_plugin but this is a non-trivial plugin and can be easily achieved with a custom query.



---

archive/issue_comments_094201.json:
```json
{
    "body": "I think the issue here is making the Trac Query easier to find.\nThe new user easily finds the \"Trac Search\"  but it can take time\nto encounter the Trac Query, and even when one know it exists,\nit's not easy to find it back from the Sage Trac home page.",
    "created_at": "2018-08-04T08:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94201",
    "user": "slelievre"
}
```

I think the issue here is making the Trac Query easier to find.
The new user easily finds the "Trac Search"  but it can take time
to encounter the Trac Query, and even when one know it exists,
it's not easy to find it back from the Sage Trac home page.



---

archive/issue_comments_094202.json:
```json
{
    "body": "Currently, when visiting Sage's Trac, one sees the following at the top:\n\n- first a line with the search box and search button\n\n```\n[ search box ] Search\n```\n\n- then a line like one of the following, depending whether one is logged in:\n\n```\nLogin, GitHub Login, Preferences, Help/Guide, About Trac, API\n```\n\n\n```\nlogged in as <username>, Logout, Preferences, Help/Guide, About Trac, API\n```\n\n- then a line like one of the following, depending whether one is logged in:\n\n```\nWiki, Timeline, Roadmap, View Tickets, Search\n```\n\n\n```\nWiki, Timeline, Roadmap, View Tickets, New Ticket, Search\n```\n\nOne of these lines arguably should point to the Trac Query page.",
    "created_at": "2018-08-06T11:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94202",
    "user": "slelievre"
}
```

Currently, when visiting Sage's Trac, one sees the following at the top:

- first a line with the search box and search button

```
[ search box ] Search
```

- then a line like one of the following, depending whether one is logged in:

```
Login, GitHub Login, Preferences, Help/Guide, About Trac, API
```


```
logged in as <username>, Logout, Preferences, Help/Guide, About Trac, API
```

- then a line like one of the following, depending whether one is logged in:

```
Wiki, Timeline, Roadmap, View Tickets, Search
```


```
Wiki, Timeline, Roadmap, View Tickets, New Ticket, Search
```

One of these lines arguably should point to the Trac Query page.



---

archive/issue_comments_094203.json:
```json
{
    "body": "The [Trac Search page](https://trac.sagemath.org/search) should also\npoint to the [Trac Query page](https://trac.sagemath.org/query).",
    "created_at": "2018-08-06T11:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94203",
    "user": "slelievre"
}
```

The [Trac Search page](https://trac.sagemath.org/search) should also
point to the [Trac Query page](https://trac.sagemath.org/query).



---

archive/issue_comments_094204.json:
```json
{
    "body": "That would still require a small plugin at least.  Without significant motivation I don't think minor UX improvements in Trac are a good use of time unless someone really wants to do it (and would probably be better directed upstream).",
    "created_at": "2018-08-06T14:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9691#issuecomment-94204",
    "user": "embray"
}
```

That would still require a small plugin at least.  Without significant motivation I don't think minor UX improvements in Trac are a good use of time unless someone really wants to do it (and would probably be better directed upstream).
