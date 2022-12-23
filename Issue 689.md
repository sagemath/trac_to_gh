# Issue 689: modifying preparse.py to benefit from the Python standard tokenize module

Issue created by migration from https://trac.sagemath.org/ticket/689

Original creator: was

Original creation time: 2007-09-18 15:51:23

Assignee: somebody


```
On 9/18/07, Joel B. Mohler <joel@kiwistrawberry.us> wrote:

    I don't have a strong opinion about the original proposition ... although I
    have spent the last week being thoroughly vexed by python being zero-based
    when all the things I would write on paper about math would index things
    one-based.


One solution to that is to just write things 0-based in your math papers. 
I've been doing that in all the mathematics I write for the last 2 years
or so, and nobody complains.   Consider an $n$-dimensional vector
space with basis $v_0, \ldots, v_{n-1}$. 

    However, I did want to say this about the preparser.  My impression is that it
    is written by doing very manual character/string reading.  I think
    the 'tokenize' module could probably make the code much much cleaner.  It has
    annoying (but understandable) semantics.  Here's an example below.


True.  I've been looking forward to somebody rewriting the preparse(...)
function for a long time.  Much to my surprise nobody has.  I don't think
anybody has even tried, though people have suggested they would try
on a few occasions. I would certainly be happy if it were to happen, though
I'm not going to do it myself, since the current version works perfectly
well, is easy to understand, and I have other things that I have to do.
Also, speeding up the preparser might have little noticeable effect on the
speed of Sage, since all actual work / computation happens after preparsing.
That said, if you do
    sage: search_src('sage_eval')
you'll see 83 places in the Sage library code itself that involve calling
the Sage preparser, and those could be faster. 

Using tokenize as you illustrate below would probably be a simple
intermediate way to rewrite the preparser without going nuts trying
to do something too complicated.  E.g., the preparser currently
has code to find string literals in the input line -- the tokenize module
does the same thing, probably much better.   Also the preparser
has code to parse out valid identifiers, and again the tokenize module
below does that automatically.

I think "modifying preparse.py to benefit from the Python standard tokenize module" would be a good trac enhancement ticket:
  

    --
    Joel

    import tokenize

    # helper class to generate a stream from a string
    class line_token_stream:
        def __init__( self, s ):
            self.line = s

        def __call__( self ):
            if self.line:
                s = self.line
                self.line = None
                return s
            raise StopIteration

    def tokenize_line( s ):
        for t in  tokenize.generate_tokens( line_token_stream( s ) ):
            yield t

    for i in tokenize_line( "func(1+2)" ):
        print i

```

