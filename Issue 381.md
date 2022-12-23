# Issue 381: SAGE daemon mode

Issue created by migration from https://trac.sagemath.org/ticket/381

Original creator: was

Original creation time: 2007-05-28 21:14:39

Assignee: was


```
On May 28, 5:11 pm, Marshall Hampton <hampto...@gmail.com> wrote:
> This is more of a unixy process control question but I am applying it
> to sage.
>
> I would like to start a notebook on my office machine while I am at a
> conference.  I tried logging in with ssh, starting the notebook,
> suspending it with ctrl-z, and then putting the suspended process in
> the background with bg.  This didn't really work, although I could
> still restart the notebook server with a browser.  I could figure this
> out eventually but I am hoping someone reading this list already knows
> how to do this.

There are several options:

1) use screen - see www.gnu.org/software/screen/
2) use nohup - see man nohup
3) use disown - see http://www.faqs.org/docs/bashman/bashref_79.html

All have their specific advantages, I would just go with screen.

It might be worthwhile to offer an option for SAGE to demonize itself.

Cheers,
Michael Abshoff
```



---

Comment by was created at 2007-05-28 22:43:58


```


Well, the idea is to detach the running SAGE instance from the shell
to let it run in the background until it is killed or the system is
rebooted.

There is more than one way to do it: For a good C example see
http://www.enderunix.org/docs/eng/daemon.php - for a python example
see http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66012

The python example could be more or less copied (I guess because I am
not a python expert), but it should be done very early in the SAGE
startup as far as I can tell. Writing a little C wrapper that just
does

 i=fork();
 if (i<0) exit(1); /* fork error */
 if (i>0) exit(0); /* parent exits */
 /* child (daemon) continues */
 execv("./sage");

might be easier.
```



---

Comment by mabshoff created at 2007-08-23 11:20:35

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-08-23 11:20:35

Changing status from new to assigned.


---

Comment by klee created at 2010-10-17 04:39:32

Look at #7893 ([http://trac.sagemath.org/sage_trac/ticket/7893](http://trac.sagemath.org/sage_trac/ticket/7893)).

It would be good to incorporate the idea of the example to the script in the previous ticket.


---

Comment by leif created at 2012-12-02 16:06:16

Ping.

The Sage Installation Guide currently lacks this topic.  (There's only a reference from the [online FAQ](http://wiki.sagemath.org/faq#Other_questions) to _this_ ticket.)


---

Comment by leif created at 2012-12-02 16:10:36

Changing keywords from "" to "Sage server background process service".


---

Comment by jdemeyer created at 2013-06-13 12:23:41

What's wrong with nohup? It does exactly what you want, why add a Sage option to emulate nohup?


---

Comment by was created at 2013-06-13 16:49:35

I think nohup doesn't daemonize.  There is a long list of things that should happen when a process is damonized:

     http://en.wikipedia.org/wiki/Daemon_(computing) 

The right way to solve this problem would almost certainly involve including this Python module:  https://pypi.python.org/pypi/python-daemon/


---

Comment by jdemeyer created at 2013-06-13 18:16:40

Replying to [comment:8 was]:
> I think nohup doesn't daemonize.
True, `nohup` itself doesn't daemonize. But normally you would do

```
$ nohup sage -n &
```

It's the `&` at the end which does the "daemonization".

> There is a long list of things that should happen when a process is damonized:
> 
>      http://en.wikipedia.org/wiki/Daemon_(computing) 
This refers to traditional Unix daemons, which would be quite different from a Sage "daemon" started by an ordinary user.

So it's not clear to me what would be needed for a Sage daemon which is not covered by

```
$ nohup sage &
```



---

Comment by was created at 2013-06-13 18:25:14

> This refers to traditional Unix daemons, which would be quite different from a Sage "daemon" started by an ordinary user.

I think traditional daemonization is the right way to solve this problem.  Moreover, it would be a useful step for making it easy to run a sage server as part of the usual system-wide daemons on Unix.


---

Comment by jdemeyer created at 2013-06-13 18:30:26

Replying to [comment:10 was]:
> it would be a useful step for making it easy to run a sage server as part of the usual system-wide daemons on Unix. 
Which is #7893, this ticket seems to be about single-user use.


---

Comment by leif created at 2013-06-13 18:51:27

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 was]:
> > I think nohup doesn't daemonize.
> True, `nohup` itself doesn't daemonize. But normally you would do
> {{{
> $ nohup sage -n &
> }}}
> It's the `&` at the end which does the "daemonization".
> 
> > There is a long list of things that should happen when a process is damonized:
> > 
> >      http://en.wikipedia.org/wiki/Daemon_(computing) 
> This refers to traditional Unix daemons, which would be quite different from a Sage "daemon" started by an ordinary user.
> 
> So it's not clear to me what would be needed for a Sage daemon which is not covered by
> {{{
> $ nohup sage &
> }}}

Well, you'd at least also have to `>/dev/null`.

Inherited file descriptors other than 0, 1 and 2 are left untouched.

`nohup` doesn't change the working directory, nor e.g. modify the umask.

The background process doesn't get adopted by `init` until you logout, and similar process group specific stuff I think.

(...)


---

Comment by klee created at 2016-03-23 04:38:48

Changing status from new to needs_review.


---

Comment by klee created at 2016-03-23 04:38:48

The problem that this ticket deals with is nowadays solved by using the OS tools such as Upstart in Ubuntu for example. So I think there needs no further discussion on this matter.


---

Comment by chapoton created at 2016-04-16 18:35:46

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
