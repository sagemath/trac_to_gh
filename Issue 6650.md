# Issue 6650: semicolon does not hide output in notebook

Issue created by migration from https://trac.sagemath.org/ticket/6650

Original creator: hemmecke

Original creation time: 2009-07-28 21:12:24

Assignee: boothby

while in command-line sage 4.1
1;
(with semicolon) shows no output whereas the same input in a notebook cell will (falsely) output the 1.


---

Comment by was created at 2010-01-19 07:49:29

Actually, I consider this a bug in IPython:

```
bash$ python
Python 2.6.4 (r264:75706, Dec  7 2009, 18:43:55)
[GCC 4.4.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 1;
1
```



---

Comment by acleone created at 2010-01-19 08:40:33

Changing component from notebook to misc.


---

Comment by acleone created at 2010-01-19 08:41:32

Resolution: invalid


---

Comment by was created at 2010-01-19 09:46:14


```
Hi William,

On Mon, Jan 18, 2010 at 11:52 PM, William Stein <wstein@gmail.com> wrote:
>
> SO, now I think this is a bug in *IPython*, not the sage notebook.
> What do you think?

It's by design: one of the few places where early on, I explicitly and
deliberately deviated from default python behavior.

In interactive computing, one often ends up having computations that
are known to produce gigantic output, and it's nice to have a simple
way to say "don't print the result of this computation, just do it".
I just checked and it turns out that matlab works this way too (though
I didn't know that at the time, I hadn't tried matlab then):

>> 1

ans =

    1

>> 1;
>>

I rely on this feature quite often, and I consider it a huge annoyance
of the default python shell that you can not suppress output without
making an assignment.

Cheers,

F
```



---

Comment by was created at 2010-01-19 11:07:53


```
On Tue, Jan 19, 2010 at 2:54 AM, William Stein <> wrote:
> Since IPython has tons and tons of options, maybe one could make this
> another user-customizable option?  If you won't do it, any hints as to
> what would need to be changed?

This could certainly be made an option, please file it so we don't
forget about it:


https://bugs.launchpad.net/ipython

In the meantime, hack out in IPython's prompts.py file around line 530 or so:

           # do not print output if input ends in ';'
           try:
               if self.input_hist[self.prompt_count].endswith(';\n'):
                   return
           except IndexError:
               # some uses of ipshellembed may fail here
               pass

Just remove that block, and the 'feature' will be gone from your
patched version.

Cheers,

f
```



Thanks.   I tried and it seems that site is broken for reporting bugs...  It says:

```
Oops!

Sorry, something just went wrong in Launchpad.

We’ve recorded what happened, and we’ll fix it as soon as possible. Apologies for the inconvenience.

(Error ID: OOPS-1480B921)
```

