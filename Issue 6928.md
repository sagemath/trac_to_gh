# Issue 6928: Upgrade the Trac spkg to 0.11.5

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-09-13 04:15:00

Assignee: tbd

[Trac](http://trac.edgewall.org/) is a problem tracker for software projects.  For example, see here.

The latest available Trac spkg is [old](http://www.sagemath.org/packages/optional/).  Version [0.11.5](http://trac.edgewall.org/browser/tags/trac-0.11.5/RELEASE) may include several new features, either [built-in](http://trac.edgewall.org/wiki/TracGuide) or  [added-on](http://trac.edgewall.org/wiki/PluginList) ([more plug-ins](http://trac-hacks.org/)).  Moreover, we can use the spkg to test potential improvements to [Sage trac](http://trac.sagemath.org/sage_trac).

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/257b1e92d98c40d7/724cc866319332a0?#724cc866319332a0) for a discussion of requested features and potentially useful plug-ins.


---

Comment by mpatel created at 2009-09-19 15:37:49

Get plugins [here](http://trac.edgewall.org/wiki/PluginList) and [here](http://trac-hacks.org/).

 * [TracMercurial](http://trac.edgewall.org/wiki/TracMercurial) - Repository browser with diffs and some support for queues.
 * [AnnouncerPlugin](http://trac-hacks.org/wiki/AnnouncerPlugin) - Custom notifications for the user.
 * [TracTicketDepgraphPlugin](http://trac-hacks.org/wiki/TracTicketDepgraphPlugin) - Ticket dependency graphs.
 * [TicketBackLinksMacro](http://trac-hacks.org/wiki/TicketBackLinksMacro) - Pages linking to a ticket.  TODO: Tickets-to-ticket links.
 * [TicketChangePlugin](http://trac-hacks.org/wiki/TicketChangePlugin) - Owner-editable comments.
 * [WikiTableMacro](http://trac-hacks.org/wiki/WikiTableMacro) - Embedded SQL query results.

Trac [database schema](http://trac.edgewall.org/wiki/TracDev/DatabaseSchema).


---

Comment by mpatel created at 2009-09-20 22:01:23

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

Comment by mpatel created at 2009-09-20 22:21:27

Should we modify `server.trac.trac.trac_create_instance()` to use the Mercurial plug-in by default?  We would need to overwrite `conf/trac.ini`.  Triple-quote it?  Add a keyword option to `trac()`?


---

Comment by mpatel created at 2009-09-22 08:35:09

Apply with spkg.


---

Attachment


---

Comment by mpatel created at 2009-09-22 08:51:53

Replying to [comment:4 mpatel]:
> Should we modify `server.trac.trac.trac_create_instance()` to use the Mercurial plug-in by default?  We would need to overwrite `conf/trac.ini`.  Triple-quote it?  Add a keyword option to `trac()`?
The [attachment:trac_6928-trac_spkg.patch patch] adds an `easy_setup` option that enables the webadmin and Mercurial plugins when creating a new Trac project.


---

Comment by timdumol created at 2009-09-22 15:06:55

Merges fine, doctests work well, and the package installs and works. Nice job. Postive review.


---

Comment by mpatel created at 2009-09-23 11:42:12

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

Comment by mpatel created at 2009-09-23 11:48:47

Replying to [comment:7 timdumol]:
> Merges fine, doctests work well, and the package installs and works. Nice job. Postive review.
Thanks!  In case there's interest...  There's a Sage Trac Labs demo with more than a few installed plug-ins at

 * http://sage.math.washington.edu/home/mpatel/trac_labs/

See [README_config](http://sage.math.washington.edu/home/mpatel/trac_labs/README_config) for setup information.


---

Comment by mpatel created at 2009-09-23 23:19:22

Just a clarification:  The spkg above includes Genshi, which it installs before installing Trac.  As far as I can tell, a network connection is not required.  Of course, if it's useful on its own, perhaps as an alternative to Jinja, I/we can make a dedicated Genshi spkg.


---

Comment by mhansen created at 2009-10-15 05:16:48

Resolution: fixed


---

Comment by mhansen created at 2009-10-15 05:16:48

I put the spkg in the optional spkg repo and applied the patch in sage-4.2.alpha0.


---

Comment by mpatel created at 2009-10-16 10:51:48

Replying to [comment:9 mpatel]:
> Thanks!  In case there's interest...  There's a Sage Trac Labs demo with more than a few installed plug-ins at
>  * http://sage.math.washington.edu/home/mpatel/trac_labs/
Moved to http://sage.math.washington.edu/home/mpatel/projects/traclabs
