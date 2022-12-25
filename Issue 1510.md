# Issue 1510: Adding the SimpleJSON module to SAGE

archive/issues_001510.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nI am using JSON objects (http://json.org) as a language neutral way to allow SAGE to communicate with clients.  I have installed SimpleJSON (http://cheeseshop.python.org/pypi/simplejson) on a SAGE server and have it sending 2D plot data to an applet in the notebook.  I would now like to request that SimpleJSON be added to SAGE.\n\nIn order to test SAGE->Applet communications using JSON, perform the following steps:\n\n1) Install SimpleJSON in SAGE.  The user must be able to import SimpleJSON by entering \"import simplejson\" in a cell.\n\n2) Paste the following code into CELL 0 of a new worksheet and execute it in order to launch the applet:\n\n\n```\nhtml('<applet id=\"mathrider\" code=\"org.mathrider.MathRider.class\" width=\"800\" height=\"650\" codebase=\"http://sage.math.washington.edu/home/tkosan/mathrider/\" archive=\"mathrider.jar\" MAYSCRIPT></applet>')\n```\n\n\n3) After the applet launches, select the \"Cell\" tab, paste the following code into the \"Send Cell\" text area, and execute it with <shift><tab>.\n\n\n```\na = MathRider()\na.show(plot(2*x,0,1))\n```\n\n\n4) The code will be sent to SAGE for evaluation and a JSON object which contains the plot data will be returned to the applet.\n\n5) The plot will then be displayed in the \"2DPlot\" tab.\n\nIf you would like to see the data that is returned by the above code, just execute it in a blank cell in the notebook.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1510\n\n",
    "created_at": "2007-12-14T18:15:26Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Adding the SimpleJSON module to SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1510",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkosan"
}
```
Assignee: @williamstein

CC:  @jasongrout

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



Issue created by migration from https://trac.sagemath.org/ticket/1510





---

archive/issue_comments_009645.json:
```json
{
    "body": "Changing assignee from @williamstein to tkosan.",
    "created_at": "2008-01-20T10:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9645",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkosan"
}
```

Changing assignee from @williamstein to tkosan.



---

archive/issue_comments_009646.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T10:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9646",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkosan"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009647.json:
```json
{
    "body": "Spkg can be found here:\n\nhttp://sage.math.washington.edu/home/tkosan/misc/simplejson-1.7.3.spkg\n\nTest with the following code:\n\n\n```\nsage: import simplejson\nsage: simplejson.dumps([int(3),int(4)])\n'[3, 4]'\nsage: simplejson.dumps(['foo', {'bar': ('baz', None, float(1.0), int(2))}])\n'[\"foo\", {\"bar\": [\"baz\", null, 1.0, 2]}]'\n```\n",
    "created_at": "2008-01-20T10:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9647",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkosan"
}
```

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

archive/issue_comments_009648.json:
```json
{
    "body": "The package is relatively small and MIT license, so I would say it's suitable for inclusion. How does it handle Cython classes?",
    "created_at": "2008-01-22T06:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9648",
    "user": "https://github.com/robertwb"
}
```

The package is relatively small and MIT license, so I would say it's suitable for inclusion. How does it handle Cython classes?



---

archive/issue_comments_009649.json:
```json
{
    "body": "I think some sort of general voting and discussion should occur before including any new packages standard in Sage, especially ones that don't cover some very clear mathematical area that is completely unconvered by Sage (e.g., R and PolyBori did address a clear mathematical area).   In particular, it is _critical_ that there be more than one person who really wants the package to go in before we even consider putting it in.    I suggest that:\n1. simplejson be made an optional package,\n2. there be a post to sage-devel to start some discussion about whether this actually belongs in Sage.  That it is is easy to put in Sage (it's pure python) is a plus, but is definitely not enough of an argument (to put it mildly). \n\nRemember, every package that goes into Sage will cause Michael Abshoff, and me, and others headaches at some point, and will add to the horrendous problem we already have with packages getting out of date with upstream. \n\nAlso, perhaps there should be somebody -- probably Ted in this case -- who very clear volunteers to keep the package up to date for the next year, and find somebody to take over if they can't continue. \n\nThe above was quick brainstorming.   It is not meant to be some well thought out procedure, which is something I don't think we have yet.\n\n -- William",
    "created_at": "2008-01-22T07:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9649",
    "user": "https://github.com/williamstein"
}
```

I think some sort of general voting and discussion should occur before including any new packages standard in Sage, especially ones that don't cover some very clear mathematical area that is completely unconvered by Sage (e.g., R and PolyBori did address a clear mathematical area).   In particular, it is _critical_ that there be more than one person who really wants the package to go in before we even consider putting it in.    I suggest that:
1. simplejson be made an optional package,
2. there be a post to sage-devel to start some discussion about whether this actually belongs in Sage.  That it is is easy to put in Sage (it's pure python) is a plus, but is definitely not enough of an argument (to put it mildly). 

Remember, every package that goes into Sage will cause Michael Abshoff, and me, and others headaches at some point, and will add to the horrendous problem we already have with packages getting out of date with upstream. 

Also, perhaps there should be somebody -- probably Ted in this case -- who very clear volunteers to keep the package up to date for the next year, and find somebody to take over if they can't continue. 

The above was quick brainstorming.   It is not meant to be some well thought out procedure, which is something I don't think we have yet.

 -- William



---

archive/issue_comments_009650.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> The package is relatively small and MIT license, so I would say it's suitable for inclusion. How does it handle Cython classes? \n\nAccording to the home page, it should handle them OK. From the webpage:\n\"\"\"\nJSON is built on two structures:\n\n* A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.\n* An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.\n\nThese are universal data structures. Virtually all modern programming languages support them in one form or another. It makes sense that a data format that is interchangable with programming languages also be based on these structures.\n\"\"\"",
    "created_at": "2008-01-22T18:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9650",
    "user": "https://github.com/dfdeshom"
}
```

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

archive/issue_comments_009651.json:
```json
{
    "body": "This doesn't quite answer my question--for pickling one has to implement __reduce__, and I'm wondering if there's a similar mechanism for the JSON package. (Of course, almost anything could be represented, but how much would have to be hand implemented?)",
    "created_at": "2008-01-23T03:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9651",
    "user": "https://github.com/robertwb"
}
```

This doesn't quite answer my question--for pickling one has to implement __reduce__, and I'm wondering if there's a similar mechanism for the JSON package. (Of course, almost anything could be represented, but how much would have to be hand implemented?)



---

archive/issue_comments_009652.json:
```json
{
    "body": "This spkg is relevant due to the patches at #5564.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-27T06:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9652",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This spkg is relevant due to the patches at #5564.

Cheers,

Michael



---

archive/issue_comments_009653.json:
```json
{
    "body": "From #5564, an updated simplejson spkg is at http://sage.math.washington.edu/home/mhansen/simplejson-2.0.9.spkg",
    "created_at": "2009-05-30T07:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9653",
    "user": "https://github.com/jasongrout"
}
```

From #5564, an updated simplejson spkg is at http://sage.math.washington.edu/home/mhansen/simplejson-2.0.9.spkg



---

archive/issue_comments_009654.json:
```json
{
    "body": "I've created an updated updated spkg: http://sage.math.washington.edu/home/drake/simplejson-2.0.9.spkg\n\nThis spkg has the proper Mercurial repo, spkg-install, spkg-check, SPKG.txt, and so on.\n\nI don't know about pickling and so on, except that as it stands, if you do something like `simplejson.dumps(1)`, it fails and says \"TypeError: 1 is not JSON serializable\". I don't know enough to fix the problem or decide whether or not it's an issue.",
    "created_at": "2009-06-02T05:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9654",
    "user": "https://github.com/dandrake"
}
```

I've created an updated updated spkg: http://sage.math.washington.edu/home/drake/simplejson-2.0.9.spkg

This spkg has the proper Mercurial repo, spkg-install, spkg-check, SPKG.txt, and so on.

I don't know about pickling and so on, except that as it stands, if you do something like `simplejson.dumps(1)`, it fails and says "TypeError: 1 is not JSON serializable". I don't know enough to fix the problem or decide whether or not it's an issue.



---

archive/issue_comments_009655.json:
```json
{
    "body": "Changing assignee from tkosan to @williamstein.",
    "created_at": "2009-06-02T05:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9655",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkosan"
}
```

Changing assignee from tkosan to @williamstein.



---

archive/issue_comments_009656.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-06-02T05:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9656",
    "user": "https://trac.sagemath.org/admin/accounts/users/tkosan"
}
```

Changing status from assigned to new.



---

archive/issue_comments_009657.json:
```json
{
    "body": "This could be closed if #6359 gets closed since Python 2.6 comes with a json module.",
    "created_at": "2009-06-20T01:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9657",
    "user": "https://github.com/mwhansen"
}
```

This could be closed if #6359 gets closed since Python 2.6 comes with a json module.



---

archive/issue_comments_009658.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-07-16T21:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9658",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_009659.json:
```json
{
    "body": "Yep, I think we can close this now that we're at Python 2.6.",
    "created_at": "2009-07-16T21:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1510#issuecomment-9659",
    "user": "https://github.com/mwhansen"
}
```

Yep, I think we can close this now that we're at Python 2.6.



---

archive/issue_events_001664.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-07-16T21:05:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1510",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1510#event-1664"
}
```
