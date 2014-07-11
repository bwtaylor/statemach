class RangeConstraint:
 def __init__(self,min,max):
   self.min = min
   self.max = max
 def validate(self,value):
   return value >= self.min and value <= self.max

class Enumeration:
  def __init__(self, values_dictionary):
    self.values_dictionary = values_dictionary
  def validate(self,value):
    values_dictionary.has_key(value)
