# application-flow

- Main execution –app.py–

  This is the file you must execute.
  It calls a series of functions and other files.
  The main purpose of this file is handling the logger, handling the asset handler and engaging the threads running the trading program.

- Asset handler

  This file contains the piece of code defining the object which will manage the available assets to trade and hand them to the threads.
  It will be important to have this role centralized, so having many threads running at a time could end up with duplicities.

- Logger

  The logger handler is not in a separate file, and it will simply log every thread’s output where it is told to, in a log file. Having this information stored will allow you to debug your code and your strategy, afterwards.

- Trader

  This file contains the code of the object that analyzes the market data and makes decisions.
  Therefore, here relies the most important part of the code, and it is where we will spend most of the time.

- Global variables

  Defined as config, for short, it contains all the configuration parameters of the program, so the programmer does not have to modify values at the code, but rather keep them under the same page.
  It will be imported at the beginning of the execution.
