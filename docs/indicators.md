# indicators

## Exponential Moving Average (EMA)

Answers the question: Is the trend clearly defined? If so, is it moving up or down?

This indicator will be used to see the trend of the value. Let’s see what it is:

- We all know what an average is. Take the n numbers, add them up and divide the result by n. We will do the same procedure, but with the close data of the candles of the asset of which we want to calculate the EMA.

- How many values, you will be wondering. The fact is that an EMA calculation is always accompanied by a number. This number indicates the window size, which contains the values of which we will calculate the average. Thus, a window of 1 value will be a lot more susceptible to changes than a window of 50 values.

- Now that we have our window, we start rolling it over all the close values of the day, as if it was a wagon in a roller coaster, moving, calculating averages.

- The word exponential is there to indicate that the averages are somehow weighted, meaning that the values closer to the current moment are given more importance than the others. Which is clever, because we care about what is happening now, to decide our entry.

## Relative Strength Index (RSI)

Answers the question: How hard are people buying or selling?

- It is an oscillator, which means that it is always oscillating within two values, being these 0 and 100.

- The resting point of its oscillation would be 50, where the trend is neither buying neither selling.

- It is thought to have a ceil at 70 and a low end at 30. When surpassing these barriers, it is demonstrated that a rebound is likely to happen. In other words, if the RSI is 75, it has been overbought, and will probably start to switch its trend to be more sold than bought, soon. If the RSI is 10 –far below 30–, it has been oversold, and people may start to buy mode than sell.

## Stochastic (STOCH)

Answers the question: How is the asset price currently, compared to its recent historical range?

Again, it is an oscillator, within 0 and 100.

- As said, it is composed of two curves. The fast one, which will react quicker to the price, and the slow one, which will be used as a reference.

- This index provides us with the specific instant where the price has reached its upper or lower limit –in comparison to the last values, remember–, thus it indicates a change of trend.

- This index also provides us with the proximity to this limit, which means that, even though the curves still haven’t crossed, it is not likely to go much upper –or lower–.

- This indicator admits three configuration parameters, being them the length of the number of samples taken, the softening factor and the average factor for the slow curve.

