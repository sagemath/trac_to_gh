# Issue 1321: [graphs] an interactive graph editor

Issue created by migration from https://trac.sagemath.org/ticket/1321

Original creator: jason

Original creation time: 2007-11-28 20:09:51

Assignee: mhansen

CC:  boothby rlm rbeezer

Keywords: graphs

This is most likely a big project.

From Chris Godsil's wishlist (replies by Jason Grout and Robert Miller, in that order).


```
>>> A graph editor. This would allow graphs to be constructed and edited by
>>> pointing and clicking. It should be able to output ps/pdf files. We
>>> want to
>>> be able to save the current state in machine readable form, and to be able
>>> to input graphs in this form. This means we will have drawings as explicit
>>> objects. (Thus it would be easy to write programs to generate drawings.)
>>> If we have a graph displayed in the editor, we should be able to access it
>>> from sage/python, and compute parameters there. So I would like to be able
>>> to adjust the graph with the mouse, or from sage.
>>> Some people will want to be able to use arbitrarily complicated curves
>>> for the edges, and to place all sorts of text around the drawing. This
>>> will
>>> lead to something like xfig rewritten in sage.
>> Indeed, this does sound like a very ambitious project. We might look at
>> incorporating other graph editors. There are a few written in Java that
>> might be useful. As it is, though, do we have any GUI things we can work
>> with other than Java (like the recent interactive 3d plots) or some sort
>> of AJAX trickery? We may be able to do something with javascript
>> draggable objects here, using jquery or some other javascript GUI
>> library. It seems like at one point someone mentioned another javascript
>> library for drawing on a web page.
> Sean Howe wrote a javascript editor, and that is lurking in my email
> somewhere. I think it was decided against for reasons of notebook
> security, and in favor of the new Java3d stuff. The problem is that
> interactive GUIs is a difficult problem for anything in Sage. Also,
> nothing has been written for the Java3d stuff yet. The problem with a
> lot of graph visualizers and editors already written is that most of
> them aren't very high quality, and there are so many low quality
> ones...

```



---

Comment by jason created at 2007-11-30 16:18:57

This project looks really interesting:

http://graphexploration.cond.org/index.html

An interactive graph editor written in Java.


---

Comment by rlm created at 2007-12-17 15:22:45

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:22:45

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:22:45

Changing component from combinatorics to graph theory.


---

Comment by rkirov created at 2009-08-03 22:42:50

copy from the sage-devel group:

I have been sitting on this code for too long, so I think it would fit
in Sage's philosophy to release early, to include it in the next
version of Sage. Here is my current version:

http://www.math.uiuc.edu/~rkirov2/sage/graph_editor.zip

it contains a diff patch for Sage devel and two files which need to go
"$SAGE_ROOT/local/notebook/javascript/graph_editor" (create that
folder). Sage/local is not under mercurial so I can't add it to the
patch.

now to get the graph editor just type (in notebook):

sage: G = graphs.PetersenGraph()
sage: graph_editor(G)

comments:
1) Update button is really ungraceful but i couldn't figure out how to
send the data behind the scene to the Sage server (as the server so
far is made to communicate only with the cells). So now it just dumps
the data in the cell it was called and leaves it to the user to
execute the update.

2)The graph_editor opens in an iframe, so if you grad a node out of
the whole frame, it stops tracking it (this can be probably fixed with
some major JS hack). However, now it detects you left the iframe and
returns the vertex to its original position.

3) This works only for simple graphs for now.

any suggestions, comments, especially code corrections are welcome 

Rado


---

Comment by mpatel created at 2009-08-04 03:19:10

A minor suggestion:  Please try transposing the last two lines of `mouseReleased()` to, e.g.,

```
    dragged_node = null;
    last_click_time = millis();
    redraw();
    }
  if(!LIVE) noLoop();
}

class Edge {
```

I think this will solve the problem of "high" CPU use after
 * Turning on the live feature.
 * Turning off the live feature.
 * Clicking on the canvas to add a new node.


---

Comment by rkirov created at 2009-08-06 18:13:28

thanks for catching the bug. The new version is attached as "mpatel" (its was supposed to be "mpatel's bug fix" but i hit enter). Apparently you cant edit once you send it.


---

Comment by rlm created at 2009-08-26 18:11:34

I've made the patches and files themselves available. This will make review/discussion easier.

On top of a fresh copy of Sage-4.1.1, I:

1. Applied the patch to the library. There was a rejected hunk, which I fixed, and posted the modified patch as `trac_1321-graph_editor-rebased-4.1.1.patch`. (Since the original patch was not an `hg` patch, my name got put on the patch when I exported it. We'll need to fix this so that Rado gets proper credit.)

2. Copied the html and js files to `$SAGE_ROOT/local/notebook/javascript/graph_editor`, after creating this directory.

3. Rebuilt Sage and tried it out.

REFEREE COMMENTS:

1. This only works from within the notebook, if you run it on a command line it just spits out some HTML. The variable `EMBEDDED_MODE` is used to tell whether this is the case or not. We should do something more intelligent for the command line case.

2. When you update, it always defines the graph `G`, even if that was not the graph you were actually using. You can get Python to tell you the variable name used somehow, but at the moment I forget.

3. Also, when you update, it defines the graph as capital `G`, and then sets the position of lowercase `g`. This gives an error when it is actually evaluated.

4. Finally, the js file seems particularly averse to whitespace. This looks like the result of some obfuscation program or something... Can I suggest we format it a little better?

5. Instead of `graph_editor(G)`, we should probably organize it as `G.edit()` or `G.graph_editor()` or something like that.

6. I really like this, and I want to see it merged ASAP!!!


---

Comment by rkirov created at 2009-09-04 03:22:45

Thanks for reviewing my editor. Sorry for the late reply, I totally forgot to look at Trac and was waiting on google group thread. I will try to fix the small bugs this weekend and if I have time rewrite some of the js code in pure js, instead of the processing.js fake-java.

>1. This only works from within the notebook, if you run it on a command line it just spits out some HTML. The variable EMBEDDED_MODE is used to tell whether this is the case or not. We should do something more intelligent for the command line case.

This should be easy to fix.

>2. When you update, it always defines the graph G, even if that was not the graph you were actually using. You can get Python to tell you the variable name used somehow, but at the moment I forget.

I couldn't figure how to do that either, not sure if it is even posible. Probably will try my luck with Stackoverflow.

>3. Also, when you update, it defines the graph as capital G, and then sets the position of lowercase g. This gives an error when it is actually evaluated.

That is an easy fix

>4. Finally, the js file seems particularly averse to whitespace. This looks like the result of some obfuscation program or something... Can I suggest we format it a little better?

The js file is not writen by me. Its processing.js with on line modification by me, it lacks whitespace because its should load faster that way, and it is not intended to be further modified (think of it as a graphics library).

>5. Instead of graph_editor(G), we should probably organize it as G.edit() or G.graph_editor() or something like that.

Shouldn't be hard, have to see which file to edit.

>6. I really like this, and I want to see it merged ASAP!!! 

Awesome, that makes two of us. Btw, thanks for fixing my patch. I am still struggling with hg.

Rado


---

Comment by rkirov created at 2009-09-21 04:55:41

ok, attached is the new version.

1) Polished update button, which is now a save button. There is a text cell where the user can enter the name they want to give to the graph. Save is done automatically when button is clicked (no more shift+enter necessary)

2) Turned off the sliders for the live, there is some kind of bug with jqueryui in SAGE. Not sure what, but they were not terribly useful.

3) The processing JS code is moved over to pure JS (instead of the bizarre parsed java). Also now it has its own separate file "graphed.js".

The new patch should be ran on top of the old one.

Rado


---

Comment by mpatel created at 2009-09-21 05:35:03

Replying to [comment:9 rkirov]:
> 2) Turned off the sliders for the live, there is some kind of bug with jqueryui in SAGE. Not sure what, but they were not terribly useful.
For what it's worth, #5447 will upgrade jQuery UI.


---

Comment by jason created at 2009-09-22 17:06:18

rbeezer: I'm leaving this for you on review day :).


---

Comment by rbeezer created at 2009-09-23 07:22:38

This looks stable and useful enough now to be merged with one change.

Most all of Robert Miller's comments have been addressed favorably.  I'm of two minds about `G.edit()` versus `graph_editor(G)`, its the latter now.

There needs to be a limit on the size of a graph, so that is one needed addition.

You probably want to create one final set of patches and files, with clear directions on where each goes, the current state is a bit confusing.  Start patch files with  `trac_1321_xxx` and end with `.patch`

Positive review once a size limit goes in.  This will be a really, really nice addition!

Rob


---

Comment by rlm created at 2009-09-24 16:04:03

Replying to [comment:13 rbeezer]:
> I'm of two minds about `G.edit()` versus `graph_editor(G)`, its the latter now.

`G.edit()` should exist, and just call `graph_editor(G)`.


---

Comment by rbeezer created at 2009-09-24 16:53:53

Replying to [comment:14 rlm]:
> Replying to [comment:13 rbeezer]:
> > I'm of two minds about `G.edit()` versus `graph_editor(G)`, its the latter now.
> 
> `G.edit()` should exist, and just call `graph_editor(G)`.
> 
Yes, both can/should be there.  The call `graph_editor()` is nice because it provides a two-vertex graph with a single edge.  Somebody using this the first time then has something to fiddle with, without even knowing anything about instantiating a `Graph` object.  So I prefer the object-oriented version, but think this is a place where the plain command is beneficial.


---

Comment by mpatel created at 2009-11-16 19:10:29

I can work on merging

<h1 style="font-size: 10.0em;"><span style="color: red;">g</span><span style="color: orange;">r</span><span style="color: yellow;">a</span><span style="color: green;">p</span><span style="color: blue;">h</span><span style="color: #4B0082;">E</span><span style="color: violet;">d</span></h1>

into SageNB.  Are the four most recent attachments the key files?

(Yes, that was unnecessary.)


---

Comment by rbeezer created at 2009-11-16 19:35:47

Replying to [comment:16 mpatel]:

> (Yes, that was unnecessary.)

But quite refreshing, all the same.  ;-) Thanks for working on this one!  Hopefully Rado can comment on its readieness.

Rob


---

Comment by was created at 2009-11-17 01:28:30

What is "graphEd"???


---

Comment by rbeezer created at 2009-11-17 01:56:29

Replying to [comment:18 was]:
> What is "graphEd"???

Rado's Javascript window that allows you to click to make vertices, edges, drag them around, etc, then ship them off to a Sage Graph instance for further exploration with the layout from the window intact.  It seemed really usable last time I got it going, but with notebook changes, it might require mpatel to get it incorporated properly.


---

Comment by rkirov created at 2009-11-24 02:53:44

I will try to upgrade Sage to the newest version this week and try to see how the does the graph editor (or graphEd as it has been dubbed :) behave with respect to the new NB. The old version was working fine and I put in rob's recommendations, but then sage updated before I can submit the patch. 

Mpatel expect email from me to get some info on how does the new NB works these days and maybe collaborate on getting this finally in Sage. Funny how the main code has been written for 6 months now but dealling with the notebook and learning HG to make patches is taking me forever.

Rado


---

Attachment

Rado's graph editor.  Apply this patch to the *sagenb* repo.  Apply this patch only.


---

Comment by mpatel created at 2009-11-24 04:43:09

I've attached patches to the [attachment:trac_1321-sage_graphed.patch sage] and [attachment:trac_1321-sagenb_graphed.patch sagenb] repositories that should enable the graph editor in 4.3.alpha0.  The sagenb patch "depends" on the sagenb patches at #3895 and #7495 --- the latter precede the #1321 patch in my queue and also modify `twist.py`.

Unfortunately, this is about as far as I have time now and in the near future to take this.  But please verify that it works and feel free to make any changes and suggestions!  Some possibilities:

 * Finish the docstrings in `graph_editor.py`.  Actually, this is a necessity.

 * Add an option to make "Save" send the [position] data to the server but not populate the input cell?

 * Use [JSON](http://json.org/js.html) to pass common graph data structures between the browser and Sage?  For example,

```
import json
g_json = json.dumps(g.networkx_graph().adj)
print g_json
gg = Graph(json.loads(g_json))
```

We could then use `JSON.parse` in the browser to reconstitute a graph, retaining loops, directed edges, labels, etc., and similarly for colorings, etc.  (`JSON.stringify` would work in the opposite direction.)


---

Comment by mpatel created at 2009-11-24 05:13:02

Update: The [attachment:trac_1321-sagenb_graphed.patch sagenb patch] works for me when I apply it to SageNB 0.4.4, in the absence of #3895 and #7495.  The patch may also work with SageNB 0.4.3, which is part of Sage 4.3.alpha0.  But it may be best to [get the latest](http://nb.sagemath.org/).


---

Comment by mpatel created at 2009-11-24 05:38:11

[attachment:trac_1321-sage_graphed_v2.patch Version 2 of the sage library patch], which replaces first version, fixes the docstrings.


---

Comment by rbeezer created at 2009-11-24 05:53:01

Replying to [comment:20 rkirov]:
> learning HG to make patches is taking me forever.

Hi Rado,

I'll send you some stuff by email about creating patches, etc.

Rob


---

Comment by mpatel created at 2009-11-24 07:14:10

Adds two keyword options.  See the comment.  Version 3 of the sage repo patch.  This replaces previous versions.


---

Comment by mpatel created at 2009-11-24 07:28:14

Changing status from needs_work to needs_review.


---

Attachment

Version 3, somewhat experimental:

 * Adds a keyword option `graph_name` (the default is `None`).  By default, the function attempts to guess the name of the graph.  But it can be useful to be explicit.

 * Adds a keyword option `replace_input` (the default is `True`).  If this is `False`, clicking "Save" quietly evaluates the current cell with the updated `Graph`, but it preserves the cell's input (as of when "Save" was clicked).  Currently, we do this by temporarily replacing the input, evaluating the cell, restoring the input, resaving the input, and resizing the cell.  We definitely need a more direct way to do this (even more direct than calling `async_request(worksheet_command('eval'),...)`).

An example:

```
g5 = graphs.TetrahedralGraph()
graph_editor(g5, replace_input=False, graph_name='g5_mod')
```

After clicking "Save", we can evaluate, e.g.,

```
show(g5_mod)
```

in another cell.


---

Comment by rlm created at 2009-12-19 21:28:08

To apply the notebook repo patch, do I just untar the spkg, apply it there, and re-pkg/install sagenb?

Also, does anyone mind if I clean up the patches on this ticket? It's just `trac_1321-sagenb_graphed.patch` and `trac_1321-sage_graphed_v3.patch` now, right?


---

Comment by mpatel created at 2009-12-20 02:03:52

Replying to [comment:28 rlm]:
> To apply the notebook repo patch, do I just untar the spkg, apply it there, and re-pkg/install sagenb?

Yes.

> Also, does anyone mind if I clean up the patches on this ticket?

Feel free!  Thanks!

> It's just `trac_1321-sagenb_graphed.patch` and `trac_1321-sage_graphed_v3.patch` now, right?

Yes.


---

Comment by was created at 2009-12-20 03:14:30

Replying to [comment:29 mpatel]:
> Replying to [comment:28 rlm]:
> > To apply the notebook repo patch, do I just untar the spkg, apply it there, and re-pkg/install sagenb?
> 
> Yes.

In the src directory type

```
    sage -python setup.py develop
```



---

Comment by rkirov created at 2009-12-31 20:12:21

mpatel asked me to mention the changes I made to processing.min.js (which is why it is called processing.editor.min.js). Basically, the only one is that I made the mouse events be attached to the whole document, so that now one can drag vertices outside the canvas (for the erasing maneuver).

attach(curElement,"mousemove",function(e)... ----> attach(document,"mousemove",function(e)...

I will try to add directed graph functionality next (currently stuck at compiling sage4.3 and applying the patches).


---

Comment by rlm created at 2010-01-02 16:48:26

Bravo, very nice!

Please make directed functionality a new ticket, because I think this deserves a positive review.


---

Comment by rlm created at 2010-01-02 16:48:26

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:52:53

I've merged the Sage library patch.  Now the patch for the notebook needs to be merged.


---

Comment by was created at 2010-01-04 06:50:33

Resolution: fixed


---

Comment by was created at 2010-01-04 06:50:33

w00t!!!

merged into sagenb-0.4.8.


---

Comment by rbeezer created at 2010-01-04 08:26:19

Replying to [comment:34 was]:
> w00t!!!

I'll second that sentiment!

Thanks to Rado, Mitesh and everybody else for their work on this one.
