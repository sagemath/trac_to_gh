# Issue 7362: Make worksheet auto-sync and collaborative editing smarter and more granular

Issue created by migration from https://trac.sagemath.org/ticket/7362

Original creator: mpatel

Original creation time: 2009-10-31 14:43:10

Assignee: boothby

CC:  jason schilly

We ought to make collaborative worksheet editing somewhat more intuitive, even if we stop short (for now) of implementing full-strength [operational transformations](http://en.wikipedia.org/wiki/Operational_transformation) or employing the [Wave Federation Protocol](http://www.waveprotocol.org/).

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/d46ab54616c03b88/df5e0b2e82af4d5a#df5e0b2e82af4d5a).

From [comment:11:ticket:7254 this comment] at #7254:

     The browser and server do not update their `state_number`s if a new cell is added at the end of a sheet, when text cells are added, or cells are deleted. Should we add these to the list, along with the `'delete_all_output'`, `'pretty_print'`, `'system'` worksheet commands? 




---

Comment by mpatel created at 2009-11-06 02:30:25

See [this sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/56cf668a71172b8e/8f1fac23aaca42d3?#8f1fac23aaca42d3), too.


---

Comment by mpatel created at 2009-11-11 18:13:00

Replying to [comment:1 mpatel]:
> See [this sage-notebook thread](http://groups.google.com/group/sage-notebook/browse_thread/thread/56cf668a71172b8e/8f1fac23aaca42d3?#8f1fac23aaca42d3), too.
The links:

 * [MobWrite](http://code.google.com/p/google-mobwrite/) - [theory](http://code.google.com/p/google-mobwrite/wiki/Theory), [client setup](http://code.google.com/p/google-mobwrite/wiki/WebClient), [server setup](http://code.google.com/p/google-mobwrite/wiki/Daemon), [status](http://code.google.com/p/google-mobwrite/wiki/Status).
 * [Cola](http://wiki.eclipse.org/RT_Shared_Editing) - Real-time shared editing in Eclipse - [screencast](http://www.vimeo.com/1195398).

MobWrite seems to be a good option, provided it doesn't overload client and server.  We can call `mobwrite.share` for new input cells and `mobwrite.unshare` for deleted cells.  _If_ MobWrite cannot synchronize arbitrary HTML, perhaps we can `mobwrite.share` a hidden auxiliary cell that holds the escaped HTML of its corresponding output cell.  We can update the output cell's `innerHTML` when MobWrite triggers the auxiliary's `onchange` handler.  Of course, this assumes that we don't run more than one synchronization algorithm at a time.


---

Comment by mpatel created at 2009-11-11 18:13:00

Changing priority from minor to major.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
