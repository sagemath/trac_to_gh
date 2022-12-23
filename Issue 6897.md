# Issue 6897: Migrate Notebook to Django

Issue created by migration from https://trac.sagemath.org/ticket/6897

Original creator: timdumol

Original creation time: 2009-09-06 03:18:54

Assignee: boothby

CC:  rkirov mhansen

Moving Notebook to Django will abstract the server and  user authentication, and give us a free admin interface, as well as a large support codebase.

1On Aug 31, 11:20 pm, William Stein <wst...`@`gmail.com> wrote:
> <SNIP>
> 
> I'm not at all convinced that using twisted in any way (web or web2) is a
> good idea for the Sage notebook.   I plan to revisit this in late
> September.    The first thing I plan to do is consider switching from
> twisted to Django, as is done in codenode -- seehttp://codenode.org/--
> hopefully, even sharing code with that project.   Of course, twisted could
> still get used at a certain level behind the scenes, but the Sage notebook
> would then no longer explicitly use it.
> 
> So if you want to help as you describe above, perhaps you could accelerate
> this.  This involves:
> 
>   (1) getting familiar with Django, if you don't already know it.
> 
>   (2) reading through the current codenode codebase
> 
>   (3) then formulating a plan to replace server/notebook/twist.py with
> something based either directly on Django, or possibly using codenode in
> some way.
> 
> The above is what I would do, but if you do it first that would be
> spectacular.
> 
> William


---

Comment by timdumol created at 2009-09-09 13:16:52

Changing assignee from boothby to timdumol.


---

Comment by timdumol created at 2009-09-09 13:16:52

Changing status from new to assigned.


---

Comment by mpatel created at 2009-09-11 02:07:05

A naive question:  Does Django support asynchronous responses?


---

Comment by timdumol created at 2009-09-11 10:42:06

If you mean AJAX (pull), then yes, Django supports AJAX. If you mean Comet (push) though, then no, as far as I can tell. From what I know, Comet can only be done with event-based servers (e.g., Twisted, Orbited). We can, however, let Twisted deal with async responses, while Django can deal with everything else -- as is done in Codenode. We still get the benefits of a pluggable database architecture, user authentication, url routing, etc.


---

Comment by timdumol created at 2009-09-11 14:29:27

Preliminary work at http://github.com/TimDumol/sage-notebook-django-branch/tree/master


---

Comment by mpatel created at 2009-09-11 14:56:47

Thanks very much for the explanation.  I'm not familiar with Python web frameworks, so I don't have a strong opinion about what's best for Sage.  I'm definitely not arguing against migrating to Django.

My interest stems from #6855, which I'd like to implement with [Comet](http://en.wikipedia.org/wiki/Comet_%28programming%29), if possible.  I think I'll take a closer look at [Twisted's](http://twistedmatrix.com/projects/core/documentation/howto/async.html) [deferreds](http://twistedmatrix.com/projects/web/documentation/howto/index.html).  Is [this](http://popcnt.org/2007/12/asynchronous-django-responses-comet-yes.html) possibly relevant?

By the way, what are your thoughts about [FirePython](http://firepython.binaryage.com/)?  I think we can use the middleware part to send [logging](http://docs.python.org/library/logging.html) information to the browser.  As far as I'm aware, Sage does not yet use Python's logging module, although #6187 uses it in the doc builder.  Having a ["unified" logging facility](http://groups.google.com/group/sage-devel/browse_thread/thread/5a17a7244380405e/dcb25d3b5b775a69?#dcb25d3b5b775a69) in the Sage library could be useful.

By another way, it appears there's a new, event-based server from Facebook called [Tornado](http://www.tornadoweb.org/).  I'm not sure yet why they didn't use Twisted.


---

Comment by timdumol created at 2009-09-11 15:38:30

I'm not too experienced in async programming, so I'm afraid I can't answer your question regarding deferreds. There is an abundance of tutorials on using [Orbited](http://orbited.org) for comet, but none that I see for Twisted. Code will be needed for the client in Javascript (I believe there are libraries for this), and for the server. Orbited can provide both -- although that will mean adding another package to Sage. It may be worth looking into it. [Here's](http://anirudhsanjeev.org/tutorialhow-to-django-comet-orbited-stomp-morbidq-jsio/) an example on using Twisted, Django and Orbited together.

FirePython looks great! It will be *very* handy. It seems to be easy to add once the Django work is done too.

The reasons for creating Tornado instead of Twisted are outlined [here](http://bret.appspot.com.sharedcopy.com/entry/b49e738e301cf669416324f53a34febd.html) in the comments. The developers found Twisted's web support messy.


---

Comment by mpatel created at 2009-09-11 16:25:13

Thanks again.  I'll try to investigate.

Can the migration subsume or simplify some of the tasks listed on the [Sage Usability page](http://wiki.sagemath.org/SageUsability)?  If so, please feel free to add comments.  I think your input would be greatly appreciated.


---

Comment by timdumol created at 2009-09-12 09:25:36

Django migration should help with the ff. issues:

 * Streamlined deployment - account management, fewer bugs, etc.

 * [Captcha](http://en.wikipedia.org/wiki/Captcha) for notebook sign-up - [reCAPTCHA](http://recaptcha.net/).

 * LDAP Authentication.

 * Add users as admins. (fprimex)

 * User groups.

 * See http://routes.groovie.org/ to handle URLS (which is basically all twist.py is doing a lot of).
   *Well, Django has its own url router.*


---

Comment by timdumol created at 2009-09-16 14:45:39

Apparently, we need the Twisted-trunk to run on Django. Twisted-trunk has some fixes that make it possible to use Django that have not been included in Twisted 8.2.0. Notably, POST requests don't seem to get passed on to Django in 8.2.0. I have uploaded spkg's at http://drop.io/trac_6897_reqs that are needed to run this. Jinja 2 is also reuired (which should not be a problem, since I expect #6586 to be merged in before this gets done).

[Codenode](http://codenode.org) also includes the Twisted-trunk in its package.


---

Comment by was created at 2009-11-18 09:39:23

Doesn't Twisted.web2 officially support WSGI?  That was my naive understanding, though I haven't tested it.   This is a good sign:

```
sage: import twisted.web2.wsgi
sage: help(twisted.web2.wsgi)
    class WSGIResource(__builtin__.object)
     |  A web2 Resource which wraps the given WSGI application callable.
     |  
     |  The WSGI application will be called in a separate thread (using
     |  the reactor threadpool) whenever a request for this resource or
     |  any lower part of the url hierarchy is received.
     |  
     |  Methods defined here:
```



---

Comment by timdumol created at 2009-11-18 13:36:02

As far as I know, yes, Twisted.web2 does support WSGI. I have only used Twisted.web, though. I was/am under the impression that Twisted.web2 is not supported upstream anymore, and thus we should avoid using it.


---

Comment by timdumol created at 2009-11-29 07:45:18

Twisted 9.0 has finally been released, which means that WSGI is now supported by Twisted.web.


---

Comment by was created at 2009-12-10 01:22:14

Replying to [comment:13 timdumol]:
> As far as I know, yes, Twisted.web2 does support WSGI. I have only used Twisted.web, though. I was/am under the impression that Twisted.web2 is not supported upstream anymore, and thus we should avoid using it.

True.  We should port the notebook back from Twisted.web2 to Twisted.web.  This will be some significant work but it should get done.


---

Comment by jason created at 2010-10-13 02:52:02

Another point about performance of python options: http://nichol.as/asynchronous-servers-in-python


---

Comment by jason created at 2011-03-18 23:00:26

This seems like a relevant ticket to the move to a flask-based notebook.  Well, at least the title is relevant, even if most of the content is outdated now.


---

Comment by mboratko created at 2011-11-15 22:02:26

Was a decision made here regarding which python middleware to go with? Was flask decided on elsewhere (could you point me to where if that is the case)?


---

Comment by jason created at 2011-11-15 22:11:18

We are using flask in the "new" notebook server.  This decision was made at least by Jan 2011; I don't know of a specific place to point you, but there have been lots of discussions on the sage-notebook mailing list about it.  I think this ticket should be closed as it isn't helpful at all at this point.  The ticket is too vague.  I'm not sure who the release manager is right now, though, so I don't know who to CC.


---

Comment by was created at 2011-11-15 22:33:16

Jeroeon is the current release manager.


---

Comment by jdemeyer created at 2013-05-16 07:46:11

Resolution: invalid
