# Issue 1768: get emails from any trac change on a certain component

Issue created by migration from https://trac.sagemath.org/ticket/1768

Original creator: rlm

Original creation time: 2008-01-14 00:44:56

Assignee: was

CC:  cc kcrisman embray slelievre

For example, I don't own a certain component, but I am still passionate enough about it to want to know whenever anything happens in it. Right now, "Settings" is only name and e-mail...


---

Comment by mpatel created at 2010-01-16 20:13:56

The [AnnouncerPlugin](http://trac-hacks.org/wiki/AnnouncerPlugin) seems promising.


---

Comment by slelievre created at 2018-08-01 16:52:45

Changing keywords from "" to "Trac".


---

Comment by embray created at 2018-08-03 17:23:51

Resolution: wontfix


---

Comment by embray created at 2018-08-03 17:23:51

1. I don't think Trac-related issues should have tickets here, ironically.  Most stuff related to the Sage Trac plugin is tracked at https://github.com/sagemath/sage_trac_plugin
2. I don't think there's a way out of-the-box to "subscribe" to specific components like this via e-mail; it would probably require a small plugin and I'm not sufficiently motivated to work on Trac plugins that aren't directly related to improving the overall workflow and/or migrating/integrating with GitLab/GitHub.
3. As it is you can create a custom query for whatever criteria you want and subscribe to it as an RSS feed: https://trac.sagemath.org/query?status=new&component=algebra&format=rss&col=id&col=summary&col=component&col=type&col=status&col=priority&col=milestone&order=priority
