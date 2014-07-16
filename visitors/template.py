from jinja2 import Environment, PackageLoader
import os, errno

class Template:
  
  def __init__(self,filename):
    self.filename = filename
    env = Environment(loader=PackageLoader('statemach', 'visitors/templates'))
    self.template = env.get_template(filename)
    
  def mkdir_p(self,path):
    try:
      os.makedirs(path)
    except OSError as x:
      if x.errno == errno.EEXIST and os.path.isdir(path):
        pass
      else: raise 

  def visit(self, state_machine):
    output = self.template.render(
      state_machine=state_machine, 
      states=state_machine.states.values(),
      transitions=state_machine.transitions.values()
    )
    path='output/'+state_machine.resource
    self.mkdir_p(path)
    outfile =open(path+'/'+self.filename, 'w+')
    print >>outfile, output
    
      
