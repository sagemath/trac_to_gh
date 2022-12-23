# Issue 3346: [with patch; not ready for review] finance -- add a very very basic first little tiny amount of quantitative finance functionality to sage

Issue created by migration from https://trac.sagemath.org/ticket/3346

Original creator: was

Original creation time: 2008-06-01 01:22:16

Assignee: was

Just add something.  Nothing much.  Probably this will get deleted anyways once there is a grand plan.  But something like this is needed to get some momentum.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by jkantor created at 2008-06-04 07:16:47

This is very cool. I'm going to give this a positive review, but I have a bunch of suggestions and comments. Most of these are not critical.

1. the historical function doesn't seem to work with ETFs which have ticker symbols but are not stocks. In particular for the ticker symbol USO it gives an error, though getting the current value works. I'm not sure if google gets the data differently? Probably they should both work or neither?

2. The allowed syntax for specifying dates is not documented (unless I missed it).


3. The documentation for the historical doesn't say what fields it displays are (open, high, low, current, volume). It is documented in the date class, but it might be good to be explicit.



4. Unless I missed it there is no function to automatically construct a time series out of historical data, this seems like it would be nice. 
It would also be nice to be able to get other historical parameters (P/E). 
It would also be nice to be able to grab historical data between two specified dates. Also what happens when you plug in holidays, weekends, etc, I guess its just what google does but it should probably be specified.


4. The MarkovMultiFractal needs more documentation.  I want to point out that it is not a standardized model for financial returns (garch is much more widely used), so documentation is important. In particular intuitively what do the different parameters control. Especially since the parameters are kind of misleading as sigma is not the volatility as one would expect a priori. There is a paper cited in the source, but the function needs more documentation. Also, its kind of important that the MarkovMultiFractal is supposed to be modeling the returns and actually the log returns (difference of the log of the prices). So simply saying that yen_usd is equal to this process isn't a very illustrative example. 

5. Its obviously a lot of work but some sort of maximum likelihood parameter fitting would make this much more useful, I see from the source that this was planned and then commented out. I'm not suggesting this needs to be done I just want to emphasize the estimation of parameters is what makes this actually useful.


6. If we are including this markov multi fractal there should probably be a garch model at some point, which is what this markov multi fractal is supposed to improve on.


7. I would put forth the idea that time series should be its own category, or maybe in numerical or statistics (is there a statistics category). After all time series arise everywhere (biology, physics, etc) not just in finance. There are quite a few things it would be nice for the time series to have (arma models at very least) but those aren't relevant to reviewing the patch.


---

Comment by mabshoff created at 2008-06-08 23:33:30

Resolution: fixed


---

Comment by mabshoff created at 2008-06-08 23:33:30

Merged all six patches in Sage 3.0.3.alpha2. The points raised will be adressed in follow up tickets.
