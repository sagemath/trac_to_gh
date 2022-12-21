# Issue 1908: Make it so that show plots a list as a grid

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-01-24 03:56:49

Assignee: was

CC:  ekirkman

This patch extends the functionality introduced in #1869 .  It lets you show lists of things as tiled images.  This does take out the default settings for graphs that were set in #1869, though.  Should those be in the system show() command?



```
        sage: show(graphs(3), layout='circular', vertex_size=50, vertex_labels=False, graph_border=True)
        sage: show(list(graphs(3)), layout='circular', vertex_size=50, vertex_labels=False, graph_border=True)
        sage: show(graphs(4), layout='circular', vertex_size=50, vertex_labels=False, graph_border=True)
        sage: show([plot(sin(i*x)) for i in range(30)]) # Two pages of images
        sage: show([sin(i*x) for i in range(2)])
        sage: show([sin(i*x) for i in range(30)], columns=1, rows=10)
```




---

Comment by jason created at 2008-01-24 03:58:08

This should be applied after #1869.


---

Attachment

Updated patch to fix typo in doctests


---

Comment by rlm created at 2008-01-24 16:17:45

Jason,

The whole point of having the graphs_list functionality called from show is to take advantage of the code that is already written. Many hours were put into that code, and the fact that the show function might become bogged down is a good thing - the more things it can handle well, the better. There is no reason to undo all that hard work!


---

Comment by jason created at 2008-01-24 16:29:20

Robert,

I agree that the graphs look very nice with those default parameters and it does look like it took a lot of work to get it to the state it is in now.  Let me see if I can rework my patch to include those defaults automatically.  Is there any other functionality provided in graphs_list that isn't provided for in the attached patch?  My purpose in this patch is to extend the great ideas in the graphs_list function to any sort of list of graphics objects.


---

Comment by rlm created at 2008-01-24 16:42:50

Actually, if you look at `graph_list.py`, you'll notice that the bulk of the work isn't going on in `show_graphs()`, but in `to_graphics_arrays()`, which looks pretty similar to some of the code you wrote. Perhaps this code should be generalized-- note the clever use of `**kwds` here...


---

Comment by jason created at 2008-01-24 19:03:10

Yes, most of what I did was while I was looking at to_graphics_arrays().  Thanks for the tip about **kwds.


---

Attachment

Apply in place of show_list.patch


---

Comment by jason created at 2008-01-24 22:22:18

I think I addressed in show_list-updated.patch the concerns that Robert had with the show() function not having nice defaults for graphs.  I pushed the defaults for a particular object into the class definition, though, instead of having a huge switch statement in show().  That way the defaults are not hardcoded, but could be easily changed on a per-object basis if the user wanted their graphs or other objects plotted a different way than the default (for example, if a user wanted their digraphs to look different from their graphs, or their BundleGraphs to look different from their normal graphs, etc.)

To define some defaults for plotting an object in an array, just assign the class variable object.graphics_array_defaults to a dictionary containing your default options to object.plot().  Any defaults are overridden with explicit keyword arguments to show().



Jason


---

Comment by rlm created at 2008-01-25 10:15:47

I really like the idea of class defaults for list plots being in the classes themselves instead of in functional.py.... Good thinking!


---

Attachment


---

Comment by jason created at 2008-01-26 20:42:33

show_list-updated-ref.patch should be applied after show_list-updated.patch.


---

Comment by jason created at 2008-01-28 19:16:47

Doctest for Robert's addition.


---

Attachment

There are three patches to be applied here, in this order:

  1.  show_list-updated.patch
  2.  show_list-updated-ref.patch
  3. show_list-updated-ref-doctest.patch


---

Comment by mabshoff created at 2008-02-14 18:37:13

Resolution: fixed


---

Comment by mabshoff created at 2008-02-14 18:37:13

Merged the above three patches in Sage 2.10.2.alpha2
