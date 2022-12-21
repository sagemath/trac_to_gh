# Issue 6973: SVG or other vector graphics editor

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-09-21 01:32:00

Assignee: boothby

CC:  acleone

An interactive vector graphics editor accessible from the Sage notebook or the command-line may have a variety of uses:

 * Drawing diagrams.
 * Annotating images.  See [matplotlib](http://matplotlib.sourceforge.net/contents.html)'s [SVG backend](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/backends/backend_svg.py?view=markup).
 * Manipulating graphs and knots.
 * Animating objects.  See [SMIL](http://en.wikipedia.org/wiki/Synchronized_Multimedia_Integration_Language).
 * Creating a free-form 2D workspace.

Candidates:

 * [SVG-edit](http://code.google.com/p/svg-edit/) - seems very promising; actively developed.
 * [SVG web](http://code.google.com/p/svgweb/) - can render SVG via Flash for IE; actively developed.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/86429406fb3bba17/dd3163cb2a47fa38?#dd3163cb2a47fa38) for some discussion.


---

Comment by mpatel created at 2010-01-28 19:26:52

Hi Alex - Feel free to take this in any direction you think is worthwhile!


---

Comment by kcrisman created at 2014-12-10 19:32:38

Changing component from notebook to interfaces.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from interfaces to interfaces: optional.


---

Comment by chapoton created at 2015-10-08 18:24:31

Some time has passed and nothing happened. Maybe we can now close this as out of topic ?


---

Comment by chapoton created at 2015-10-08 18:24:31

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-10-08 23:32:11

Why?!


---

Comment by chapoton created at 2015-10-09 06:44:09

What do you mean ? Do you agree or disagree with me ?

If somebody wants to edit an SVG file, she can use any existing SVG editor. I do not
see why sage should provide such an editor. Do we aim to replace every single software around ? Has this anything to do with mathematics ?


---

Comment by vdelecroix created at 2015-10-09 09:19:34

"Manipulating graphs and knots" is mostly being something that we want in Sage... isn't it?


---

Comment by jmantysalo created at 2015-10-09 09:51:19

At least I would like to have a digraph editor, just like we now have for undirected graphs. Maybe an option to it?


---

Comment by embray created at 2018-08-14 17:33:23

It seems there are at least some valid use cases, e.g. for graphical notebook widgets for objects in Sage (something which is actively being explored).

I don't know that there's necessarily a case within that for editing arbitrary SVG graphics, though I don't think there'd much case to be made for this outside the context of a notebook widget (anything beyond that is maybe too complicated...)


---

Comment by chapoton created at 2018-11-30 20:49:32

Changing status from needs_review to needs_info.
