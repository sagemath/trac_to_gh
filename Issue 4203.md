# Issue 4203: Make a suboption decorator to complement #4201

Issue created by migration from https://trac.sagemath.org/ticket/4203

Original creator: jason

Original creation time: 2008-09-26 22:45:34

Assignee: mhansen

CC:  anakha


```
[17:06] <mhansen> Yeah -- suboption should take a prefix, defaults, and then return something like an arrow_options dict.
[17:07] <mhansen> @suboption('arrow', color='red', line='+')
[17:07] <jason-> okay, yeah, even better.
[17:07] <mhansen> And that would pick up things like arrow_color='blue'.
[17:07] <jason-> then I don't have to type the dictionary explicitly
[17:09] <mhansen> I think doing something like that might be a good idea.  It'd at least be a nice consistent way to handle all of these options.
```


The idea is that we'd like to get a bunch of options to pass on to, say, an arrow_drawing routine.  It'd be really nice if we could rename the suboptions too, so the original arrow_color argument could be returned as the rgbcolor element of the arrow_options dict.



---

Comment by jason created at 2008-09-26 22:48:23

Use case:


```
@suboption('arrow', color='red', line_style='+')
@options(vertices=True, edge_labels=True)
def plot_graph():
    draw vertices
    for each edge:
        draw_arrow(**arrow_options)
    draw edge labels
```

so the plot_graph function has options arrow_color and arrow_line_style, but inside the function, it just sees an arrow_options dictionary populated from these.


---

Comment by mhansen created at 2008-10-23 16:29:28

Changing status from new to assigned.


---

Comment by mhansen created at 2008-10-23 16:29:28

I put up an initial implementation of this.


---

Comment by jason created at 2008-10-23 17:23:33

Very nice.  Positive review.

Eventually, we ought to present a nice documentation interface to the user of the combined effect of the suboptions, the options and the rename_keyword decorators.  In other words, some automated way of getting exactly everything that a person can do to a function.  But that should be another trac ticket. 

All doctests in plot/*.py pass with this patch.


---

Comment by anakha created at 2008-10-23 19:19:43

I got this with a quick test.


```
sage: @suboptions('test')
def f(**kwds):
....:     print kwds
....:     
sage: f(test_size=2)
{'test_options': {'ize': 2}}
```


str.lstrip removes all characters given from the front of the string:


```
sage: 'baba_baca'.lstrip('ab_')
'ca'
```



---

Attachment

I put up a new patch which addresses that issue.


---

Comment by anakha created at 2008-10-23 21:00:31

Very nice.  It's all good now.


---

Comment by jason created at 2008-10-23 23:15:45

I guess my one last comment is to compute len(self.name) outside of the inner loop, but if it doesn't get changed, I'm not going to cry.


---

Comment by mabshoff created at 2008-10-25 21:22:41

Resolution: fixed


---

Comment by mabshoff created at 2008-10-25 21:22:41

Merged in Sage 3.2.alpha1
