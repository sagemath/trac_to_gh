# Issue 3916: Make a %wiki cell mode for the notebook

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-20 20:36:08

Assignee: boothby

CC:  timothyclemans

Currently it seems that the only way to get nice text between cells is to do a %html cell or to edit the worksheet directly.  Either way, you have to write html code by hand.

It would be nice if there was a %wiki cell mode, like %html, but let you put in wiki markup which would then be converted to HTML to display.

Here are some CREOLE parsers (with examples that convert to html):

[http://creoleparser.googlepages.com/](http://creoleparser.googlepages.com/)

[http://wiki.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python](http://wiki.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python)






---

Comment by jason created at 2008-08-20 20:38:22

Also, see the python section of [http://www.wikicreole.org/wiki/Converters](http://www.wikicreole.org/wiki/Converters)


---

Comment by jason created at 2008-08-20 20:47:10

Other options include Markdown ([http://www.freewisdom.org/projects/python-markdown/](http://www.freewisdom.org/projects/python-markdown/)) or reST ([http://docutils.sourceforge.net/rst.html](http://docutils.sourceforge.net/rst.html)).


---

Attachment


---

Comment by AlexGhitza created at 2009-01-23 02:51:10

Changing type from defect to enhancement.


---

Comment by timdumol created at 2009-12-06 12:35:20

Since we already have text cells, is this still relevant?


---

Comment by was created at 2009-12-09 16:27:17

Resolution: fixed


---

Comment by was created at 2009-12-09 16:27:17

Nope, this isn't relevant.


---

Comment by was created at 2009-12-09 16:27:27

Resolution changed from fixed to invalid


---

Comment by edrex created at 2010-02-04 00:13:42

wait, how do text cells enable me to use markdown syntax?

i'd like to be able to write the in-between text in markdown, run it through sage and markdown, and get a nicely-formatted html page. How could this be accomplished?


---

Comment by Sharpie created at 2010-02-16 01:23:03

Replying to [comment:9 edrex]:
> wait, how do text cells enable me to use markdown syntax?
> 
> i'd like to be able to write the in-between text in markdown, run it through sage and markdown, and get a nicely-formatted html page. How could this be accomplished? 

I agree-- text cells are nice, but I don't want to spend half my day pointing-and-click around to get something formatted.  Markdown allows you to format without breaking the flow of writing.
