def function(noun):
  determiner = "a"
  if noun[0] == "a" or noun[0] == "e" or noun[0] == "i" or noun[0] == "o" or noun[0] == "u":
    determiner = "an"
  return determiner