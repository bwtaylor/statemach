from jinja2 import Environment, PackageLoader

class Template:
  
  def __init__(self,filename):
    self.filename = filename
    env = Environment(loader=PackageLoader('statemach', 'visitors/templates'))
    self.template = env.get_template(filename)
    

  def visit(self, state_machine):
    states = state_machine.states.values()
    print self.template.render(state_machine=state_machine, states=states)
