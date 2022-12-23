# Issue 4919: convert sage.misc.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4919

Original creator: mhansen

Original creation time: 2009-01-01 22:53:45

Assignee: tba




---

Attachment


---

Comment by jhpalmieri created at 2009-01-07 21:29:06

I'm not sure why graphs/graph_generators is included in this patch, but the one change there is minor enough that I can give it a positive review...

attach.py isn't part of the reference manual, it seems to me.  Should it be?  The changes to the source code look fine.

dist.py: looks good.

func_persist.py: looks good.

functional.py: I think lines 428-430 could be deleted, but this is not a big deal.

  lines 943-946: this should be an itemized list (a continuation of the list of inputs)

getusage.py: looks good.

hg.py: as I mentioned in my review of #4902, methods like `__init__` are missing from the html version of the documentation.

  lines 415-419: this should be an itemized list (it's been garbled in the conversion)

  same thing for lines 454-461, 534-537, 690-693, 921-922, 947-949, 970-972

  line 1035: Sage_ROOT should be SAGE_ROOT

latex.py: this is not really an appropriate issue for this ticket, but in the conversion to html and/or pdf, can we remove the word "nodetex" when it appears as a directive in a docstring?

  lines 744-750: these look okay as is, but might look better with each numbered item starting on a new line

log.py: looks good.

misc.py: lines 304-308: should be a list (or two lists, one for input, one for output)

  line 705: need a space between `for` and `"Sage"`

  lines 718-720: could be deleted (just produces a break in the EXAMPLES).  same for lines 723-725, 728-730, 733-735, 739-741, 749-751, 756-758, 844-846, 850-852.

  line 1437: it should say "whether certain integers are >3", but the ">" was omitted.

  line 1453: "positive integer < 100": the "<" was omitted.

  line 1629: "fail in Sage <= 1.3.7.": the "<" was omitted.

  line 1674: Sage_ROOT should be SAGE_ROOT

mrange.py: looks good.

package.py: lines 126-128 should be an itemized list.  same with lines 169-171, 212-214, 256-257

persist.py: looks good.

sage_eval.py: looks good.

trace.py: not part of the reference manual.  looks good anyway.


---

Attachment


---

Comment by jhpalmieri created at 2009-01-11 06:33:26

Great, except you missed (in hg.py):

>   lines 415-419: this should be an itemized list (it's been garbled in the conversion)

(You got the other six instances that I mentioned.)


---

Comment by jhpalmieri created at 2009-01-15 04:26:49

(Oops, I forgot to change the summary when I added my last comment.)


---

Attachment

I still see the problem with lines 415-419 in hg.py: should be an itemized list, not a paragraph.


---

Comment by mabshoff created at 2009-02-24 18:15:18

I am merging #4919 as is. Please move the remaining issues to a new ticket against 3.4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 18:17:09

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 18:17:09

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-02-26 15:24:20

See #5374.


---

Comment by mabshoff created at 2009-02-26 16:18:29

Thanks John.

Cheers,

Michael
