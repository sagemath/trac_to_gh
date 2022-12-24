# Issue 6928: Upgrade the Trac spkg to 0.11.5

archive/issues_006928.json:
```json
{
    "body": "Assignee: tbd\n\n[Trac](http://trac.edgewall.org/) is a problem tracker for software projects.  For example, see here.\n\nThe latest available Trac spkg is [old](http://www.sagemath.org/packages/optional/).  Version [0.11.5](http://trac.edgewall.org/browser/tags/trac-0.11.5/RELEASE) may include several new features, either [built-in](http://trac.edgewall.org/wiki/TracGuide) or  [added-on](http://trac.edgewall.org/wiki/PluginList) ([more plug-ins](http://trac-hacks.org/)).  Moreover, we can use the spkg to test potential improvements to [Sage trac](http://trac.sagemath.org/sage_trac).\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/257b1e92d98c40d7/724cc866319332a0?#724cc866319332a0) for a discussion of requested features and potentially useful plug-ins.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6928\n\n",
    "created_at": "2009-09-13T04:15:00Z",
    "labels": [
        "packages: optional",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Upgrade the Trac spkg to 0.11.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6928",
    "user": "mpatel"
}
```
Assignee: tbd

[Trac](http://trac.edgewall.org/) is a problem tracker for software projects.  For example, see here.

The latest available Trac spkg is [old](http://www.sagemath.org/packages/optional/).  Version [0.11.5](http://trac.edgewall.org/browser/tags/trac-0.11.5/RELEASE) may include several new features, either [built-in](http://trac.edgewall.org/wiki/TracGuide) or  [added-on](http://trac.edgewall.org/wiki/PluginList) ([more plug-ins](http://trac-hacks.org/)).  Moreover, we can use the spkg to test potential improvements to [Sage trac](http://trac.sagemath.org/sage_trac).

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/257b1e92d98c40d7/724cc866319332a0?#724cc866319332a0) for a discussion of requested features and potentially useful plug-ins.

Issue created by migration from https://trac.sagemath.org/ticket/6928





---

archive/issue_comments_057257.json:
```json
{
    "body": "Get plugins [here](http://trac.edgewall.org/wiki/PluginList) and [here](http://trac-hacks.org/).\n\n* [TracMercurial](http://trac.edgewall.org/wiki/TracMercurial) - Repository browser with diffs and some support for queues.\n* [AnnouncerPlugin](http://trac-hacks.org/wiki/AnnouncerPlugin) - Custom notifications for the user.\n* [TracTicketDepgraphPlugin](http://trac-hacks.org/wiki/TracTicketDepgraphPlugin) - Ticket dependency graphs.\n* [TicketBackLinksMacro](http://trac-hacks.org/wiki/TicketBackLinksMacro) - Pages linking to a ticket.  TODO: Tickets-to-ticket links.\n* [TicketChangePlugin](http://trac-hacks.org/wiki/TicketChangePlugin) - Owner-editable comments.\n* [WikiTableMacro](http://trac-hacks.org/wiki/WikiTableMacro) - Embedded SQL query results.\n\nTrac [database schema](http://trac.edgewall.org/wiki/TracDev/DatabaseSchema).",
    "created_at": "2009-09-19T15:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57257",
    "user": "mpatel"
}
```

Get plugins [here](http://trac.edgewall.org/wiki/PluginList) and [here](http://trac-hacks.org/).

* [TracMercurial](http://trac.edgewall.org/wiki/TracMercurial) - Repository browser with diffs and some support for queues.
* [AnnouncerPlugin](http://trac-hacks.org/wiki/AnnouncerPlugin) - Custom notifications for the user.
* [TracTicketDepgraphPlugin](http://trac-hacks.org/wiki/TracTicketDepgraphPlugin) - Ticket dependency graphs.
* [TicketBackLinksMacro](http://trac-hacks.org/wiki/TicketBackLinksMacro) - Pages linking to a ticket.  TODO: Tickets-to-ticket links.
* [TicketChangePlugin](http://trac-hacks.org/wiki/TicketChangePlugin) - Owner-editable comments.
* [WikiTableMacro](http://trac-hacks.org/wiki/WikiTableMacro) - Embedded SQL query results.

Trac [database schema](http://trac.edgewall.org/wiki/TracDev/DatabaseSchema).



---

archive/issue_comments_057258.json:
```json
{
    "body": "See [TracPlugins](http://trac.edgewall.org/wiki/TracPlugins) for ways to sample plug-ins.  Here's one way, roughly:\n\n* Download `plugin.zip` from a plug-in's page.\n* `unzip plugin.zip`\n* `cd plugin/` \n* `cd 0.11/` (if necessary; `0.11` here matches the Trac version)\n* `chmod u+rw,go+r -R *` (if necessary)\n* `sage -python bdist_egg`\n* `cp dist/plugin-ver-py2.6.egg $SAGE_ROOT/local/lib/python/site-packages/sage_trac/plugins`\n* Restart the Trac server in sage.\n\nNote: Plug-ins installed in this way --- directly to a project's `plugins` directory --- are automatically enabled, but the plug-in may still require configuration in `sage_trac/conf/trac.ini`.  See the plug-in's home page for details.",
    "created_at": "2009-09-20T22:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57258",
    "user": "mpatel"
}
```

See [TracPlugins](http://trac.edgewall.org/wiki/TracPlugins) for ways to sample plug-ins.  Here's one way, roughly:

* Download `plugin.zip` from a plug-in's page.
* `unzip plugin.zip`
* `cd plugin/` 
* `cd 0.11/` (if necessary; `0.11` here matches the Trac version)
* `chmod u+rw,go+r -R *` (if necessary)
* `sage -python bdist_egg`
* `cp dist/plugin-ver-py2.6.egg $SAGE_ROOT/local/lib/python/site-packages/sage_trac/plugins`
* Restart the Trac server in sage.

Note: Plug-ins installed in this way --- directly to a project's `plugins` directory --- are automatically enabled, but the plug-in may still require configuration in `sage_trac/conf/trac.ini`.  See the plug-in's home page for details.



---

archive/issue_comments_057259.json:
```json
{
    "body": "Should we modify `server.trac.trac.trac_create_instance()` to use the Mercurial plug-in by default?  We would need to overwrite `conf/trac.ini`.  Triple-quote it?  Add a keyword option to `trac()`?",
    "created_at": "2009-09-20T22:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57259",
    "user": "mpatel"
}
```

Should we modify `server.trac.trac.trac_create_instance()` to use the Mercurial plug-in by default?  We would need to overwrite `conf/trac.ini`.  Triple-quote it?  Add a keyword option to `trac()`?



---

archive/issue_comments_057260.json:
```json
{
    "body": "Apply with spkg.",
    "created_at": "2009-09-22T08:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57260",
    "user": "mpatel"
}
```

Apply with spkg.



---

archive/issue_comments_057261.json:
```json
{
    "body": "Attachment [trac_6928-trac_spkg.patch](tarball://root/attachments/some-uuid/ticket6928/trac_6928-trac_spkg.patch) by mpatel created at 2009-09-22 08:48:32",
    "created_at": "2009-09-22T08:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57261",
    "user": "mpatel"
}
```

Attachment [trac_6928-trac_spkg.patch](tarball://root/attachments/some-uuid/ticket6928/trac_6928-trac_spkg.patch) by mpatel created at 2009-09-22 08:48:32



---

archive/issue_comments_057262.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Should we modify `server.trac.trac.trac_create_instance()` to use the Mercurial plug-in by default?  We would need to overwrite `conf/trac.ini`.  Triple-quote it?  Add a keyword option to `trac()`?\nThe [attachment:trac_6928-trac_spkg.patch patch] adds an `easy_setup` option that enables the webadmin and Mercurial plugins when creating a new Trac project.",
    "created_at": "2009-09-22T08:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57262",
    "user": "mpatel"
}
```

Replying to [comment:4 mpatel]:
> Should we modify `server.trac.trac.trac_create_instance()` to use the Mercurial plug-in by default?  We would need to overwrite `conf/trac.ini`.  Triple-quote it?  Add a keyword option to `trac()`?
The [attachment:trac_6928-trac_spkg.patch patch] adds an `easy_setup` option that enables the webadmin and Mercurial plugins when creating a new Trac project.



---

archive/issue_comments_057263.json:
```json
{
    "body": "Merges fine, doctests work well, and the package installs and works. Nice job. Postive review.",
    "created_at": "2009-09-22T15:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57263",
    "user": "timdumol"
}
```

Merges fine, doctests work well, and the package installs and works. Nice job. Postive review.



---

archive/issue_comments_057264.json:
```json
{
    "body": "More worthy(?) [plug-ins](http://trac-hacks.org/):\n\n* [AccountManagerPlugin](http://trac-hacks.org/wiki/AccountManagerPlugin) - Alternative authentication, forgotten password recovery, email registration, etc.\n* [GraphvizPlugin](http://trac-hacks.org/wiki/GraphvizPlugin) - Inline graphs.\n* [MasterTicketsPlugin](http://trac-hacks.org/wiki/MasterTicketsPlugin) - Adds \"blocks\" and \"is blocked by\" ticket fields.\n* [RecaptchaRegisterPlugin](http://trac-hacks.org/wiki/RecaptchaRegisterPlugin).\n* [TicketDeletePlugin](http://trac-hacks.org/wiki/TicketDeletePlugin) - For the privileged.\n* [TicketChartsMacro](http://trac-hacks.org/wiki/TicketChartsMacro) - Uses [Open Flash Charts](http://teethgrinder.co.uk/open-flash-chart-2/).\n* [TicketStatsMacro](http://trac-hacks.org/wiki/TicketStatsMacro) - Time charts of new, closed, total tickets.\n* [TracWysiwygPlugin](http://trac-hacks.org/wiki/TracWysiwygPlugin) - Supports tables.",
    "created_at": "2009-09-23T11:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57264",
    "user": "mpatel"
}
```

More worthy(?) [plug-ins](http://trac-hacks.org/):

* [AccountManagerPlugin](http://trac-hacks.org/wiki/AccountManagerPlugin) - Alternative authentication, forgotten password recovery, email registration, etc.
* [GraphvizPlugin](http://trac-hacks.org/wiki/GraphvizPlugin) - Inline graphs.
* [MasterTicketsPlugin](http://trac-hacks.org/wiki/MasterTicketsPlugin) - Adds "blocks" and "is blocked by" ticket fields.
* [RecaptchaRegisterPlugin](http://trac-hacks.org/wiki/RecaptchaRegisterPlugin).
* [TicketDeletePlugin](http://trac-hacks.org/wiki/TicketDeletePlugin) - For the privileged.
* [TicketChartsMacro](http://trac-hacks.org/wiki/TicketChartsMacro) - Uses [Open Flash Charts](http://teethgrinder.co.uk/open-flash-chart-2/).
* [TicketStatsMacro](http://trac-hacks.org/wiki/TicketStatsMacro) - Time charts of new, closed, total tickets.
* [TracWysiwygPlugin](http://trac-hacks.org/wiki/TracWysiwygPlugin) - Supports tables.



---

archive/issue_comments_057265.json:
```json
{
    "body": "Replying to [comment:7 timdumol]:\n> Merges fine, doctests work well, and the package installs and works. Nice job. Postive review.\nThanks!  In case there's interest...  There's a Sage Trac Labs demo with more than a few installed plug-ins at\n\n* http://sage.math.washington.edu/home/mpatel/trac_labs/\n\nSee [README_config](http://sage.math.washington.edu/home/mpatel/trac_labs/README_config) for setup information.",
    "created_at": "2009-09-23T11:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57265",
    "user": "mpatel"
}
```

Replying to [comment:7 timdumol]:
> Merges fine, doctests work well, and the package installs and works. Nice job. Postive review.
Thanks!  In case there's interest...  There's a Sage Trac Labs demo with more than a few installed plug-ins at

* http://sage.math.washington.edu/home/mpatel/trac_labs/

See [README_config](http://sage.math.washington.edu/home/mpatel/trac_labs/README_config) for setup information.



---

archive/issue_comments_057266.json:
```json
{
    "body": "Just a clarification:  The spkg above includes Genshi, which it installs before installing Trac.  As far as I can tell, a network connection is not required.  Of course, if it's useful on its own, perhaps as an alternative to Jinja, I/we can make a dedicated Genshi spkg.",
    "created_at": "2009-09-23T23:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57266",
    "user": "mpatel"
}
```

Just a clarification:  The spkg above includes Genshi, which it installs before installing Trac.  As far as I can tell, a network connection is not required.  Of course, if it's useful on its own, perhaps as an alternative to Jinja, I/we can make a dedicated Genshi spkg.



---

archive/issue_comments_057267.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57267",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_057268.json:
```json
{
    "body": "I put the spkg in the optional spkg repo and applied the patch in sage-4.2.alpha0.",
    "created_at": "2009-10-15T05:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57268",
    "user": "mhansen"
}
```

I put the spkg in the optional spkg repo and applied the patch in sage-4.2.alpha0.



---

archive/issue_comments_057269.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n> Thanks!  In case there's interest...  There's a Sage Trac Labs demo with more than a few installed plug-ins at\n>  * http://sage.math.washington.edu/home/mpatel/trac_labs/\nMoved to http://sage.math.washington.edu/home/mpatel/projects/traclabs",
    "created_at": "2009-10-16T10:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6928#issuecomment-57269",
    "user": "mpatel"
}
```

Replying to [comment:9 mpatel]:
> Thanks!  In case there's interest...  There's a Sage Trac Labs demo with more than a few installed plug-ins at
>  * http://sage.math.washington.edu/home/mpatel/trac_labs/
Moved to http://sage.math.washington.edu/home/mpatel/projects/traclabs
