Cumulative Frequencies README
Author:
  Kristopher Swartzbaugh
  CWID 890939184
  CPSC 535 Adv Algorithms

Project Contents:
  README (this file)
  freq.py (source code)
  input2.txt (input file)
  CumFreqReport (Additional supporting documentation)

Project Summary:
  Given a list of synonyms and individual frequencies, calculate cumulative frequencies of all synonyms

Running in Terminal:
  python3 freq.py

Note: input2.txt should be in same directory


Example Input:
{ ("foot", 5), ("feet", 12), ("day", 3), ("days", 8), ("fear", 2), ("scared", 1), ("long", 12), ("large", 5), ("big", 5), ("was", 4), ("is", 4), ("are", 15)}
{ ("foot", "feet"), ("day","days"), ("fear", "scared"), ("long" ,"big"), ("big" , "large"), ("is", "are"), ("is", "was") }
{ ("tons of", 2), ("large number of", 12), ("mystical", 13), ("magical", 28), ("magic", 5), ("unexplained", 11), ("huge", 2), ("large", 51), ("horses", 25), ("horse", 24), ("large mammal", 24), ("herbivore", 5)}
{ ("herbivore", "horses"), ("horse","large mammal"), ("horses", "large mammal"), ("large number of" ,"huge"), ("tons of" , "large"), ("huge", "large"), ("mystical", "magical") , ("magical","unexplained"), ("magic", "magical")}
{ ("tons of", 2), ("large number of", 12), ("mystical", 13), ("magical", 28), ("magic", 5), ("unexplained", 11), ("huge", 2), ("large", 51), ("horses", 25), ("horse", 24), ("large mammal", 24), ("herbivore", 5), ("large number of", 12)}
{ ("herbivore", "horses"), ("horse","large mammal"), ("horses", "large mammal"), ("large number of" ,"huge"), ("tons of" , "large"), ("huge", "large"), ("mystical", "magical") , ("magical","unexplained"), ("magic", "magical"),  ("horse","large mammal")}


Example Output:
{'feet': 17, 'day': 11, 'fear': 3, 'big': 22, 'are': 23} of size  5
The above is CFfinal
{'herbivore': 78, 'huge': 67, 'magic': 57} of size  3
The above is CFfinal
{'herbivore': 78, 'huge': 67, 'magic': 57} of size  3
The above is CFfinal
