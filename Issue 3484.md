# Issue 3484: [with patch, needs review] extend sage_eval (in preparation for sage_input)

Issue created by migration from https://trac.sagemath.org/ticket/3484

Original creator: cwitty

Original creation time: 2008-06-20 08:01:48

Assignee: cwitty

CC:  ncalexan wstein

This patch creates some new functionality in sage_eval: the preparser can be disabled; a sequence of commands can be specified, which will be run before the string is evaluated; and there are new calling conventions that take a tuple instead of a string.

These new calling conventions are useful for the proposed sage_input function (so that `sage_eval(sage_input(...))` works); but the other new functionality is generally useful, so I think it's reasonable to review and apply this patch even though sage_input is not ready for submission.


---

Attachment


---

Comment by mabshoff created at 2008-07-06 10:59:40

I will ping somebody to review this patch and #3485 soon.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 10:59:40

Changing keywords from "" to "editor_mabshoff".


---

Comment by was created at 2008-08-10 05:58:59

REFEREE DISCUSSION (irc log):


```
22:36 < wstein-3764> cwitty -- ping
22:36 < cwitty> Yo.
22:36 < wstein-3764> this gives an error as it should:
22:36 < wstein-3764> sage: sage_eval('z=5', locals=vars)
22:37 < wstein-3764> this doesn't give an error:
22:37 < wstein-3764> sage: sage_eval('z=5', cmd='y=3', locals=vars)
22:37 < wstein-3764> I guess that's ok, but just wanted to get your feedback.
22:37 < wstein-3764> The point is that the expression being evaluated can be a statement 
22:37 < wstein-3764> without error in case of giving the optional cmd.
22:38 < cwitty> Let me look at the code for a minute.
22:39 < wstein-3764> the docstrings for #3484 are really good.
22:40 < cwitty> IMHO it's not worth fixing.  (I'm not sure even how it could be fixed... I guess we could try to parse the 
                expression.)
22:40 < cwitty> Thanks!
22:40 < wstein-3764> OK, i just wanted to check with you.
22:40 < wstein-3764> I'm not that worried about something just accidently working...
22:43 -!- mabshoff [n=michaela@wclient1.irmacs.sfu.ca] has quit [Read error: 104 (Connection reset by peer)]
22:46 < wstein-3764> cwitty -- this sets of an alarm bell for me:
22:46 < wstein-3764> raise SyntaxError, "%s\nError using SAGE to evaluate '%s'"%(msg, cmd_seq if len(cmds) else source) 
22:46 < wstein-3764> Here's why -- many many times I've been bit by error messages that innocently
22:47 < wstein-3764> include a %s in them.   This is for two reasons:
22:47 < wstein-3764> (1) the error message could easily be massive, and (2) [much much worse], an
22:47 < wstein-3764> exception can get raised in the normal course of a computation, and it can
22:48 < wstein-3764> be very bad when the exception takes vastly longer to raise than the whole computation.
22:48 < wstein-3764> cwitty -- ping
22:48 < cwitty> Yes, I'm thinking.
22:49 < wstein-3764> So I prefer to change the message to:
22:49 < wstein-3764> raise SyntaxError
22:49 < wstein-3764> SyntaxError, "invalid syntax"
22:49 < wstein-3764> That's what Python does.
22:50 < cwitty> OK, I guess.
22:50 < wstein-3764> i'll change it.
22:51 < cwitty> I don't think your 2) is an issue in this case, because both %s will be substituting strings.
22:51 < wstein-3764> true.
22:51 < wstein-3764> But changing to "invalid syntax" is perhaps more consistent with python...
22:52 < wstein-3764> Also there is another exception just above in the code and it looks like this:
22:52 < wstein-3764> raise TypeError, "source must be a string." 
22:52 < wstein-3764> It doesn't say what the string is.
22:52 < wstein-3764> or the source.
22:52 < cwitty> If that's what Python does, then probably msg is already "invalid syntax", so we could just skip the whole 
                try/except.
22:53 -!- mabshoff [n=michaela@wclient1.irmacs.sfu.ca] has joined #sage-devel
22:53 < wstein-3764> good point!
22:54 < wstein-3764> can you actually do this and put in a doctest to illustrate it, so I can referee #3485?
22:54 < cwitty> You added that try/except in July 2006.
22:54 < wstein-3764> I know.  It's really my fault.
22:54 < wstein-3764> I'm just trying to trick you into doing something :-)
22:54 < cwitty> Sure, I can do that.
22:55 < wstein-3764> thanks!
```


Positive review when there is a patch that gets rid of that try/except block and adds
a doctest illustrating a syntax error.


---

Attachment

AWESOME.


---

Comment by mabshoff created at 2008-08-10 08:27:04

Resolution: fixed


---

Comment by mabshoff created at 2008-08-10 08:27:04

Merged in Sage 3.1.alpha1
