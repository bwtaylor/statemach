class Display:

  def visit(self, state_machine):
    states = state_machine.states
    for state in states.values():
      print "state: ", state.name
      for transition in state.transitions_out.values():
        print "  transition: ", transition.name, " attributes: ",
        for attribute_or_group in transition.attributes:
          print attribute_or_group.name,
        print
    

