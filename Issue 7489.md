# Issue 7489: Integrate GeoGebra into SageNB

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-11-18 22:05:36

Assignee: boothby

CC:  kcrisman

Keywords: geogebra java education teaching interactive

[GeoGebra](http://www.geogebra.org/cms/) is free, interactive program for learning and teaching mathematics.  It can run as an [unsigned](http://www.geogebra.org/en/wiki/index.php/Unsigned_GeoGebra_Applets) Java applet in a capable web browser.  It also has a [JavaScript API](http://www.geogebra.org/en/wiki/index.php/GeoGebra_Applet_Methods).  Some links:

 * [Screenshots](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=72&Itemid=58).
 * [Examples](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=69&Itemid=56), [more (En)](http://www.geogebra.org/en/wiki/index.php/English), [more (Fr)](http://www.geogebra.org/en/wiki/index.php/French).
 * [Documentation](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=75&Itemid=61), [Know How](http://www.geogebra.org/en/wiki/index.php/GeoGebra_Know_How).
 * [Forums](http://www.geogebra.org/forum/).
 * [Wiki](http://www.geogebra.org/en/wiki/index.php/Main_Page).


Given its features, maturity, and popularity, we should consider integrating GeoGebra into [Sage](http://www.sagemath.org/).

See, e.g., [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e791fb1c8665c862/f10f8eb92919ad8f?#f10f8eb92919ad8f).


---

Comment by mpatel created at 2009-11-18 22:06:04

Just creating a ticket.


---

Attachment


---

Comment by mmarco created at 2011-03-04 19:00:00

I send a proof of concept. It is a class called geogebra_applet that can show geogebra applets and (limited, and only working in ideal conditions now) interact with them.

By default it uses the .jar files of the geogebra site, but another ones can be passed as parameters. It can also be passed a ggb as a parameter to be loaded.

If you want to see what it is capable of doing, do the following:

attach('path-to-sageogebra.py')
A=geogebra_applet()
A.show()
A.eval_command('P = (1,1)')


---

Attachment

Now supports multiple applets on a single worksheet


---

Comment by kcrisman created at 2011-04-19 14:09:57

See also [Geogebra's GSOC mention of this idea](http://www.geogebra.org/trac/wiki/Gsoc2010).


---

Comment by kcrisman created at 2011-06-14 03:00:56

Changing keywords from "geogebra java education teaching interactive" to "geogebra java education teaching interactive sd31".


---

Comment by kcrisman created at 2011-10-13 16:24:03

#11489 about using iframe is also probably relevant, particularly the examples showing Geogebra use from within Sage.  This is not the same as this ticket, since those would depend on an internet connection and don't actually put GG in Sage, but it's still worth mentioning here.


---

Comment by dimpase created at 2020-02-16 14:19:53

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-02-16 14:19:53

it can be closed - sagenb is not going to be updated one way or another


---

Comment by dimpase created at 2020-02-16 14:20:04

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-02-16 18:27:03

Resolution: wontfix
