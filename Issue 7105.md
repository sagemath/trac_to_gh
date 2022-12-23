# Issue 7105: change search_doc and search_src so the links are opened in a new tab/window

Issue created by migration from https://trac.sagemath.org/ticket/7105

Original creator: was

Original creation time: 2009-10-04 05:36:58

Assignee: boothby

One way would be to add target="_new" right before href="...". 

The justification for this change is that currently after looking at the docs one hits the backbutton which results in a corrupted view of the worksheet (for now). 


---

Comment by jhpalmieri created at 2009-10-04 16:14:17

I think another way would be to save the search results to a file -- `format_search_as_html` may already put things in the right format -- and open that file using 

```
  from sage.misc.viewer import browser
  import os
  url = .. file name ...
  os.system(browser() + " " + url)
```



---

Comment by was created at 2009-10-04 19:05:28

Possibly good idea.  I did something like this with "help(foo)", where it creates a link to a page that opens in a new browser.


---

Comment by jhpalmieri created at 2011-03-25 22:53:53

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2011-03-25 22:53:53

Here's a patch.


---

Attachment


---

Comment by jhpalmieri created at 2011-03-25 22:55:41

By the way, according to [this link](http://thedesignspace.net/MT2archives/000316.html), `target="_blank"` is preferable to `target="_new"`.  This fits with my experience, also.


---

Comment by kcrisman created at 2011-03-28 18:38:25

Oh, this is a great idea.  I'll try to review it soon if no one else does.


---

Comment by jhpalmieri created at 2011-03-28 18:45:15

It only took a year and half to implement.  Since the main part of the patch is the addition of 16 characters (the rest is modification to doctests), that's about one character per month...


---

Comment by kcrisman created at 2011-03-29 20:03:23

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-03-29 20:03:23

Okay, this looks okay and works.  Definitely an improvement - I had never used the search much in the notebook because it just gave a list of files.

I have to say, I really don't like that it gives you the file.  Getting the whole plot/plot.py isn't very useful!  I mean, you can do a text search, but the command-line experience is much better than that.


---

Comment by jhpalmieri created at 2011-03-29 20:59:18

Replying to [comment:7 kcrisman]:
> I have to say, I really don't like that it gives you the file.  Getting the whole plot/plot.py isn't very useful!  I mean, you can do a text search, but the command-line experience is much better than that.

I'm trying to think of what else we could do.  If you do "search_src", it opens up the source code, but there are no tags or any other way to navigate the resulting page.  Maybe we could highlight the search terms somehow?  This probably requires some javascript, about which I know basically nothing.  If you do "search_doc", it opens up the html documentation, which has tags, and maybe we could jump to the tag nearest the first instance of the search terms.  Another option for search_doc would be to defer to Sphinx's search, which highlights code and jumps to some instance (not necessarily the first, maybe the best match?).


---

Comment by kcrisman created at 2011-03-29 21:11:10

I don't know why it can't literally return the output of search_src in the command line. Maybe because that's piped into less?

Well, in any case this is another ticket. No point turning this into the next ticket to nowhere.


---

Comment by jhpalmieri created at 2011-03-29 21:37:32

Replying to [comment:9 kcrisman]:
> I don't know why it can't literally return the output of search_src in the command line. Maybe because that's piped into less?

No, the command `_format_search_as_html` deliberately ignores multiple matches in the same file, along with the line numbers and the line containing each match -- it just uses the file name.  The extra information is there, but it's discarded.  I wonder if there's a good way to present it.  Figure out a way to use javascript to open up a Python file to a specified line, and then give one link for each matching line?  Also keep the current version as a more compact option?

> Well, in any case this is another ticket. No point turning this into the next ticket to nowhere.

I agree, I'm just brainstorming.


---

Comment by jdemeyer created at 2011-04-13 07:42:23

Resolution: fixed
