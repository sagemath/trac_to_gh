# Issue 1510: Adding the SimpleJSON module to SAGE

Issue created by migration from https://trac.sagemath.org/ticket/1510

Original creator: tkosan

Original creation time: 2007-12-14 18:15:26

Assignee: was

CC:  jason

I am using JSON objects (http://json.org) as a language neutral way to allow SAGE to communicate with clients.  I have installed SimpleJSON (http://cheeseshop.python.org/pypi/simplejson) on a SAGE server and have it sending 2D plot data to an applet in the notebook.  I would now like to request that SimpleJSON be added to SAGE.

In order to test SAGE->Applet communications using JSON, perform the following steps:

1) Install SimpleJSON in SAGE.  The user must be able to import SimpleJSON by entering "import simplejson" in a cell.

2) Paste the following code into CELL 0 of a new worksheet and execute it in order to launch the applet:


```
html('<applet id="mathrider" code="org.mathrider.MathRider.class" width="800" height="650" codebase="http://sage.math.washington.edu/home/tkosan/mathrider/" archive="mathrider.jar" MAYSCRIPT></applet>')
```


3) After the applet launches, select the "Cell" tab, paste the following code into the "Send Cell" text area, and execute it with <shift><tab>.


```
a = MathRider()
a.show(plot(2*x,0,1))
```


4) The code will be sent to SAGE for evaluation and a JSON object which contains the plot data will be returned to the applet.

5) The plot will then be displayed in the "2DPlot" tab.

If you would like to see the data that is returned by the above code, just execute it in a blank cell in the notebook.




---

Comment by tkosan created at 2008-01-20 10:41:43

Changing assignee from was to tkosan.


---

Comment by tkosan created at 2008-01-20 10:41:43

Changing status from new to assigned.


---

Comment by tkosan created at 2008-01-20 10:41:43

Spkg can be found here:

http://sage.math.washington.edu/home/tkosan/misc/simplejson-1.7.3.spkg

Test with the following code:


```
sage: import simplejson
sage: simplejson.dumps([int(3),int(4)])
'[3, 4]'
sage: simplejson.dumps(['foo', {'bar': ('baz', None, float(1.0), int(2))}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
```



---

Comment by robertwb created at 2008-01-22 06:39:53

The package is relatively small and MIT license, so I would say it's suitable for inclusion. How does it handle Cython classes?


---

Comment by was created at 2008-01-22 07:51:04

I think some sort of general voting and discussion should occur before including any new packages standard in Sage, especially ones that don't cover some very clear mathematical area that is completely unconvered by Sage (e.g., R and PolyBori did address a clear mathematical area).   In particular, it is _critical_ that there be more than one person who really wants the package to go in before we even consider putting it in.    I suggest that:
  1. simplejson be made an optional package,
  2. there be a post to sage-devel to start some discussion about whether this actually belongs in Sage.  That it is is easy to put in Sage (it's pure python) is a plus, but is definitely not enough of an argument (to put it mildly). 

Remember, every package that goes into Sage will cause Michael Abshoff, and me, and others headaches at some point, and will add to the horrendous problem we already have with packages getting out of date with upstream. 

Also, perhaps there should be somebody -- probably Ted in this case -- who very clear volunteers to keep the package up to date for the next year, and find somebody to take over if they can't continue. 

The above was quick brainstorming.   It is not meant to be some well thought out procedure, which is something I don't think we have yet.

 -- William


---

Comment by dfdeshom created at 2008-01-22 18:29:03

Replying to [comment:3 robertwb]:
> The package is relatively small and MIT license, so I would say it's suitable for inclusion. How does it handle Cython classes? 

According to the home page, it should handle them OK. From the webpage:
"""
JSON is built on two structures:

    * A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
    * An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

These are universal data structures. Virtually all modern programming languages support them in one form or another. It makes sense that a data format that is interchangable with programming languages also be based on these structures.
"""


---

Comment by robertwb created at 2008-01-23 03:47:58

This doesn't quite answer my question--for pickling one has to implement __reduce__, and I'm wondering if there's a similar mechanism for the JSON package. (Of course, almost anything could be represented, but how much would have to be hand implemented?)


---

Comment by mabshoff created at 2009-03-27 06:59:30

This spkg is relevant due to the patches at #5564.

Cheers,

Michael


---

Comment by jason created at 2009-05-30 07:18:56

From #5564, an updated simplejson spkg is at http://sage.math.washington.edu/home/mhansen/simplejson-2.0.9.spkg


---

Comment by ddrake created at 2009-06-02 05:33:01

I've created an updated updated spkg: http://sage.math.washington.edu/home/drake/simplejson-2.0.9.spkg

This spkg has the proper Mercurial repo, spkg-install, spkg-check, SPKG.txt, and so on.

I don't know about pickling and so on, except that as it stands, if you do something like `simplejson.dumps(1)`, it fails and says "TypeError: 1 is not JSON serializable". I don't know enough to fix the problem or decide whether or not it's an issue.


---

Comment by tkosan created at 2009-06-02 05:48:38

Changing assignee from tkosan to was.


---

Comment by tkosan created at 2009-06-02 05:48:38

Changing status from assigned to new.


---

Comment by mhansen created at 2009-06-20 01:49:42

This could be closed if #6359 gets closed since Python 2.6 comes with a json module.


---

Comment by mhansen created at 2009-07-16 21:05:06

Resolution: invalid


---

Comment by mhansen created at 2009-07-16 21:05:06

Yep, I think we can close this now that we're at Python 2.6.
