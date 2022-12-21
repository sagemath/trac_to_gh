# Issue 9691: Make another Trac search box or button

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-08-05 15:11:13

Assignee: mvngu, schilly

CC:  embray slelievre

Or something like that.  The problem is that Search at the top gives all tickets, closed or open, with the content, while often one wants just to search open tickets.  Since the only other option is clicking View Tickets, then Custom Query, etc. (notice that even the Search tab doesn't do anything useful different from the Search box), and THEN clicking all the non-'closed' options, we should improve this.  

I'm putting component website/wiki, but only because there isn't a trac component.


---

Comment by slelievre created at 2018-08-01 16:54:00

Changing keywords from "" to "Trac".


---

Comment by embray created at 2018-08-03 17:25:33

Resolution: wontfix


---

Comment by embray created at 2018-08-03 17:25:33

If somebody really wants this they could open an issue at https://github.com/sagemath/sage_trac_plugin but this is a non-trivial plugin and can be easily achieved with a custom query.


---

Comment by slelievre created at 2018-08-04 08:12:20

I think the issue here is making the Trac Query easier to find.
The new user easily finds the "Trac Search"  but it can take time
to encounter the Trac Query, and even when one know it exists,
it's not easy to find it back from the Sage Trac home page.


---

Comment by slelievre created at 2018-08-06 11:14:27

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

Comment by slelievre created at 2018-08-06 11:16:06

The [Trac Search page](https://trac.sagemath.org/search) should also
point to the [Trac Query page](https://trac.sagemath.org/query).


---

Comment by embray created at 2018-08-06 14:15:37

That would still require a small plugin at least.  Without significant motivation I don't think minor UX improvements in Trac are a good use of time unless someone really wants to do it (and would probably be better directed upstream).
