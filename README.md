# TicTacToe
Early attempt at applying machine learning to the problem of teaching a tic tac toe board. 
Done by implementing a decision tree which updates after each game on whether the move sequence it chose led to a win, loss, or draw. The bot will first look to defend against any immediate threat of there being
three in a row by the opponent. 
If no threat is found, it will turn to the decison tree as to its best posible move. 

After the player quits out of the session, the results of th games will be updated and saved to the pickle file for the next time the program is opened. 
