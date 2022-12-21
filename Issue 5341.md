# Issue 5341: jsmath broken on wiki

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-02-22 20:41:16

Assignee: boothby

CC:  wstein

Apache thinks that the static pages for the wiki should still be handled by moinmoin. E.g.,

http://wiki.sagemath.org/moin_static171/jsmath/jsMath.js

The help pages say that an `Alias` directive should be placed in the config before `ScriptAlias`:

http://moinmo.in/HelpOnInstalling/ApacheOnLinux#Configure_Apache



```
<mabs|4666> Yep, make it an issue for all wikis.
<mabs|4666> or at least mpir, l-functions and sage
```





---

Comment by mabshoff created at 2009-03-01 02:28:18

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by rlm created at 2009-03-07 03:06:26

This is due to a bad simlink:
`jsmath -> ../../../../data/extcode/notebook/javascript/jsmath/`
in
`$SAGE_LOCAL/share/moin/htdocs`

Changing this in `spkg-install` to
`jsmath -> ../../../../data/extcode/javascript/jsmath/`
fixes the problem.

The updated spkg can be found at #3693.


---

Comment by rlm created at 2009-03-07 03:12:46

In order to fix this issue for existing wiki's, you'll also need to change `moin_static171` to `moin_static172` in

`data/plugin/parser/jsmath.py`

within the sage_wiki directory, after upgrading the spkg.


---

Comment by burcin created at 2009-06-13 17:21:05

jsmath is loaded for the sage wiki now. However, the version of jsmath on the wiki is v3.3d, while Sage 4.0.1 comes with v3.6b. This seems to be the latest version available on the jsMath web site as well.

It would be great if the version of the jsMath on the wiki as well as the plugin, etc. configuration matched that of the main Sage distribution.


---

Comment by was created at 2009-06-14 11:07:43

I've upgraded the jsmath install and restarted the wiki.  Note that the wiki is running from sage-3.3, since the latest version of sage has an *ANCIENT* version of moinmoin installed into it.

Please check and verify that the new jsmath is working, then close this ticket.


---

Comment by burcin created at 2009-06-15 10:15:19

The jsmath version on the wiki is still v3.3d, not v3.6b, so I don't see any change after the jsmath ugrade.

Since the jsmath on the wiki is working atm, this ticket can be closed. The old version doesn't matter so much.

It would be nice if the wiki allowed previewing math input, but that should be a separate ticket.

I don't have the right to close tickets on trac, feel free to close this.


---

Comment by was created at 2009-06-15 13:36:35

> I don't have the right to close tickets on trac, feel free to close this. 

Do you think it is a good/bad thing that suddenly most users do not have the ability to change the status of tickets?  This was a change mabshoff made a few weeks ago without discussion.


---

Comment by was created at 2009-06-15 13:36:35

Resolution: fixed
