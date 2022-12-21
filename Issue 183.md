# Issue 183: Regenerating files that hardcode the install PATH -- hangs forever during the install

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-12-16 01:31:05

Assignee: was

{{{On Fri, 15 Dec 2006 17:03:48 -0800, Luis Finotti <luis.finotti`@`gmail.com> wrote:

>
> On 12/15/06, Kate Minola <kate01123`@`gmail.com> wrote:
>>
>> When I try to build sage-1.5.0.2 on my
>> x86_64-Linux box, it gets to
>>
>> sage-spkg sage-1.5.0.2
>>
>> does some processing, then reports
>>
>> " Regenerating files that hardcode the install PATH (please wait a few
>> seconds)..."
>>
>> and then hangs (for a reason I have not yet been able to figure
>> out).  I am using make-3.81.
>
> I had the same problem with my installation (from scratch) in my AMD
> XP system...  (also make 3.81).  Then, after waiting a couple of hours
> and killing it, sage runs, but many tests from "make test" fail.

Maybe you need to type "make" again to finish the install?  The problem
is happening midway through the install, not at the end.  
It is completely uneccessary to " Regenerating files that hardcode the
install PATH (please wait a few seconds)..." during the build, so
I an make sure this doesn't happen during the build.  If one ever
gets a hang after build when this happens, that would be a serious 
problem.  Does it for you, i.e., after finishing the install by typing
"make" again, if you move the entire install directory, then run SAGE,
does the above message only appear for a few seconds, then SAGE starts
up?

William
}}}


---

Comment by was created at 2007-01-09 18:14:47

This is fixed for sage-1.6


---

Comment by was created at 2007-01-09 18:14:47

Resolution: fixed
