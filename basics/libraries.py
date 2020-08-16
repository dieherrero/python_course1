import re 

string = "HELLO ma freind."
print string
new = re.sub('[A-M]','Z', string) #first arguement: remove characters inside [], subbing in the second arguement, ^ means exception i.e. [^0-9] removes everything except numbers.
print new
















