# Issue 9471: include matplotlib html5 canvas rendering to sage

archive/issues_009471.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jasongrout\n\nSee http://code.google.com/p/mplh5canvas/\n\nLet's include this in Sage soon.  I just tried it out for fun on my laptop:\n\n  (1) Grab and extract the tarball from here: \n           http://code.google.com/p/mplh5canvas/downloads/list\n     then install it with \"sage -python setup.py install\"\n  \n  (2) Install netifaces:\n     sage -sh\n     easy_install netifaces\n     exit\n\n  (3) In the Sage notebook, or command line, paste something like this:\n\n\n```\nimport matplotlib\nmatplotlib.use('module://mplh5canvas.backend_h5canvas')\nfrom pylab import *\nimport time\n\n\"\"\"Simple static plot, mostly for testing zooming...\n\"\"\"\nclf()\n\ntheta = arange(0,8*pi,0.1)\na=1\nb=.2\n\nfor dt in arange(0,2*pi,pi/2.0):\n\n     x = a*cos( theta+dt )*exp(b*theta)\n     y = a*sin( theta+dt )*exp(b*theta)\n\n     dt = dt+pi/4.0\n\n     x2 = a*cos( theta+dt )*exp(b*theta)\n     y2 = a*sin( theta+dt )*exp(b*theta)\n\n     xf = concatenate( (x,x2[::-1]) )\n     yf = concatenate( (y,y2[::-1]) )\n\n     p1=fill(xf,yf)\n\nshow()\n```\n\nBasically, you can put nearly any example from the matplotlib website before show (and after clf()) and it will \"just work\".\n\nWhat happens above is that a new server is started and the plot displayed in it.  Figuring out how to use our existing twisted server for interaction could be a nontrivial but very import challenge. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9471\n\n",
    "created_at": "2010-07-10T15:13:32Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "include matplotlib html5 canvas rendering to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9471",
    "user": "@williamstein"
}
```
Assignee: jason, was

CC:  @jasongrout

See http://code.google.com/p/mplh5canvas/

Let's include this in Sage soon.  I just tried it out for fun on my laptop:

  (1) Grab and extract the tarball from here: 
           http://code.google.com/p/mplh5canvas/downloads/list
     then install it with "sage -python setup.py install"
  
  (2) Install netifaces:
     sage -sh
     easy_install netifaces
     exit

  (3) In the Sage notebook, or command line, paste something like this:


```
import matplotlib
matplotlib.use('module://mplh5canvas.backend_h5canvas')
from pylab import *
import time

"""Simple static plot, mostly for testing zooming...
"""
clf()

theta = arange(0,8*pi,0.1)
a=1
b=.2

for dt in arange(0,2*pi,pi/2.0):

     x = a*cos( theta+dt )*exp(b*theta)
     y = a*sin( theta+dt )*exp(b*theta)

     dt = dt+pi/4.0

     x2 = a*cos( theta+dt )*exp(b*theta)
     y2 = a*sin( theta+dt )*exp(b*theta)

     xf = concatenate( (x,x2[::-1]) )
     yf = concatenate( (y,y2[::-1]) )

     p1=fill(xf,yf)

show()
```

Basically, you can put nearly any example from the matplotlib website before show (and after clf()) and it will "just work".

What happens above is that a new server is started and the plot displayed in it.  Figuring out how to use our existing twisted server for interaction could be a nontrivial but very import challenge. 


Issue created by migration from https://trac.sagemath.org/ticket/9471


