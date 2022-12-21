# Issue 4856: [with patch; needs review] make qasm an optional spkg

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-23 07:45:22

Assignee: mabshoff

See attached spkg.  This came up at 

  http://groups.google.com/group/sage-devel/browse_thread/thread/175e8f515e58d497

It might be a good example of something, so maybe should become an optional spkg...   It's pretty specialized and very small. 


---

Attachment


---

Comment by GeorgSWeber created at 2009-01-02 09:41:20

This ticket needs work in several areas:

* SPKG.txt is not up to current standards, see http://wiki.sagemath.org/spkgTemplate

* spkg-install is not up to current standards, see http://wiki.sagemath.org/SPKG_Audit resp. trac ticket #633 --- adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO

* The spkg-install says:

```
    echo "You must make sure the dvipng program is available on your system."
    echo "You might be able to install the dvipng program listed in the"
    echo "output of 'sage -optional'.  If that doesn't work, just use whatever"
    echo "is offered by your operating system."
    exit 1
```

but in the discussion on sage-devel (link above) it is said:

```
Do not install that dvipng spkg.  You *MUST* install dvipng instead
using whatever method your operating system provides (e.g., rpm, deb,
etc.).  It's a completely standard linux program.  The Sage dvipng
spkg will be deleted soon, since it doesn't make sense for us to be
hosting it.

 -- William 
```


* (optional) the qasm.py would benefit from a doctest, the addition of some kind of example could easily be turned into a working spkg-check script


---

Comment by was created at 2009-01-02 15:42:13

Resolution: wontfix


---

Comment by was created at 2009-01-02 15:42:13

>  adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO

I've always considered that SAGE_LOCAL thing pointless.

Anyway, upon further reflection, and given the lack of response by anybody in the community related to qasm, I think this is way too specialized to be an official optional spkg.  I'm thus closing this ticket.


---

Comment by mabshoff created at 2009-01-02 15:52:54

Replying to [comment:3 was]:
> >  adding a check for SAGE_LOCAL to be non-empty is a blocker IMHO
> 
> I've always considered that SAGE_LOCAL thing pointless.
> 

Not if you run spkg-install from the command line to debug things.

Cheers,

Michael
