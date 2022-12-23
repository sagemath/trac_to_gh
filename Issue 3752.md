# Issue 3752: gap.eval -- oddity in parsing multiline input and comments

Issue created by migration from https://trac.sagemath.org/ticket/3752

Original creator: was

Original creation time: 2008-08-01 01:13:39

Assignee: was


```
On Thu, Jul 31, 2008 at 11:20 AM, Peter <> wrote:
>
> Hi,
>
> I'm trying to use some GAP code in the Sage notebook, and the code has
> many one-line comments in it (starting with #). I switched the
> notebook to gap mode (using the dropdown menu) and then noticed that
> in each cell only commands that appear before the first comment are
> processed by GAP. The same happens in cells that start with %gap.
>
> Can someone perhaps verify this behaviour and/or suggest a fix? (I'm
> using Sage 3.0.5, and the same behaviour seems to occur on
> Sagenb.org.)

Yes, here's an example of this in the sage notebook text form (I made the triple {'s into double for this ticket): 

{{{
Untitled
system:gap


{{id=112|
Print(2 + 2); # add numbers
Print(3 + 3); # add more numbers
///

4
}}
}}}


---

Comment by jipsen created at 2008-08-07 23:32:08

This problem can be fixed by adding the following lines at the start of the 
eval method in the file interfaces/gap.py:


```
        # remove comments, replace newlines by space
        x = "".join([(r[:r.find('#')] if r.find('#')!=-1 else r)+' ' \
                     for r in x.split('\n')])
```


(This still needs to be tested on a variety of GAP input lines.)

I also noticed that if the length of the string processed by GAP is more than ~103 characters, then no output is produced (although the GAP code seems to be evaluated correctly and any functions defined in the code works in subsequent notebook cells).

Here is an example:


```
{{id=112|
%gap
test := function()
return "make a long input string  (delete 1 char to see the output)";
end;
test();
///
}}
```



---

Attachment


---

Comment by mhansen created at 2009-01-23 10:31:52

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-23 10:31:52

Changing assignee from was to mhansen.


---

Comment by malb created at 2009-01-24 07:10:14

I have a performance concern, but this is #5086 now.


---

Comment by mabshoff created at 2009-01-24 19:31:33

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:31:33

Resolution: fixed
