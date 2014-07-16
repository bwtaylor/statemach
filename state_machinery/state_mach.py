import collections as c

def _cat(x,y):
  xlist = x if isinstance(x, c.Iterable) else [x]
  ylist = y if isinstance(y, c.Iterable) else [y]
  return xlist + ylist


class State:  
  """A state is one of the enumerated nodes within
  the state machine.
  """
  
  def __init__(self,name,description):
    self.name = name
    self.description = description
    self.transitions_out = {}
    self.transitions_in = {}
    self.attributes = []
    
  def transition_out(self,transition):
    self.transitions_out[transition.name]=transition
  
  def transition_in(self,transition):
    self.transitions_in[transition.name]=transition
 
 
class Attribute:
  
  def __init__(self,name,type,description=""):
    self.name = name
    self._valid_types = ["string","int"]
    self.type = type
    self.description = description
    self.constraints = []
  
  def constraint(self, constraint):
    self.constraints.append(constraint)
  
  def validate(self,value):
    return not [constraint for constraint in self.constraints if not constraint.validate(value) ]
  
  
class AttributeGroup:
  def __init__(self,name,attributes):
    self.name=name
    self.attributes=attributes
    self.constraints = []
  def constraint(self, constraint):
    self.constraints.append(constraint)
    
    
class Transition:
  def __init__(self,name,from_state,to_state,attributes=[],actor="user"):
    self.name=name
    self.from_state=from_state
    self.to_state=to_state
    self.attributes=_cat([],attributes)  
    self.actor=actor
    from_state.transition_out(self)
    to_state.transition_in(self)


class StateMachine:
  
  def __init__(self,service,resource,version,description):
    self.service = service
    self.resource = resource
    self.version = version
    self.description = description
    self.states = {}
    self.state("start","The starting state")
    self.state("end", "The terminal end state")
    self.transitions = {}
    
  def state(self,name,description):
    # todo: handle updates to existing states
    state = State(name,description)
    self.states[name] = state
    return state
    
  def add_states(self,namelist):
    return [self.state(name) for name in namelist]
    
  def transition(self,name,from_name,to_name,attributes=[],actor="user"):
    from_state = self.states[from_name]
    to_state = self.states[to_name]
    self.transitions[name] = Transition(name,from_state,to_state,attributes,actor)
  
  def accept_visitor(self,visitor):
    self.visitor = visitor
  
  def visit(self):
    self.visitor.visit(self)
  
  def do(self,visitor):
    self.accept_visitor(visitor)
    self.visit()
    


