# Issue 7376: searching published worksheets does not work to just search for username

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-02 17:59:56

Assignee: boothby

CC:  was

It would be really nice if the "Search" function in the upper left of the published worksheet listing also searched for the username (e.g., I could search for "jason3" and get all of my published worksheets).


---

Comment by mpatel created at 2009-11-04 05:30:30

We should also consider supporting more complex queries, e.g., on an "Advanced Search" page.  By the way, according to [codenode-devel](http://groups.google.com/group/codenode-devel/browse_thread/thread/d3ffefa3b09937b6/98bdf00f65441934?#98bdf00f65441934), Codenode uses [Whoosh](http://whoosh.ca/) for full-text search.


---

Comment by mpatel created at 2009-11-12 15:13:23

It seems this will work: 

```diff
diff --git a/sagenb/notebook/worksheet.py b/sagenb/notebook/worksheet.py
--- a/sagenb/notebook/worksheet.py
+++ b/sagenb/notebook/worksheet.py
`@``@` -1973,7 +1973,7 `@``@` class Worksheet(object):
         """
         # Load the worksheet data file from disk.
         filename = self.worksheet_html_filename()
-        r = (self.owner().lower() + ' ' + self.name().lower() + ' '
+        r = (self.publisher().lower() + ' ' + self.name().lower() + ' '
              + open(filename).read().lower())
         # Check that every single word is in the file from disk.
         for W in split_search_string_into_keywords(search):
```



---

Comment by mpatel created at 2009-11-12 15:24:58

But:

```python
sage: from sagenb.notebook.worksheet import split_search_string_into_keywords as ss
sage: ss('hello there')
['hello', 'there']
sage: ss(" foo bar  'modular form' hello there")
['modular form', "'", 'hello', 'there']
```


[Pyparsing](http://pyparsing.wikispaces.com/) is another alternative.  There's a [search query parser](http://pyparsing.wikispaces.com/file/view/searchparser.py) among the [examples](http://pyparsing.wikispaces.com/Examples).  The license appears to be a modified-BSD license.

Should we add modifiers?  For example, the search phrase `"Fourier user:joe` would restrict the search to worksheets published by Joe.  Other possible modifiers: `title`, `text_cell`, `compute_cell`, `dates`, `input`, `output`, `collaborators`, `rating`.


---

Comment by mpatel created at 2009-11-12 15:41:33

Search by publisher. Apply to sagenb repo.


---

Attachment

Alternate version: Search by owner and publisher.  Apply only this patch to sagenb repo.


---

Comment by mpatel created at 2009-11-12 15:50:54

Changing status from new to needs_review.


---

Attachment

Should we do more with this ticket?


---

Comment by was created at 2009-12-09 00:06:20

Nice; this works as advertised.

I like all the discussion above about even more sophisticated searching systems, but of course they shouldn't hold up this ticket getting a... positive review!


---

Comment by was created at 2009-12-09 00:06:20

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 01:12:02

I merged this patch into sagenb-0.4.6.


---

Comment by was created at 2009-12-09 01:12:02

Resolution: fixed
