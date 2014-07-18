import jinja2 as j
import os, errno

import visitors.visitor as v
import state_machinery.state_mach as sm

class Template(v.Visitor):
  
  def __init__(self,filename):
    self.filename = filename
    loader = j.PackageLoader('statemach', 'visitors/templates')
    self.environment = j.Environment(loader=loader)
    
  def _mkdir_p(self,path):
    try:
      os.makedirs(path)
    except OSError as x:
      if x.errno == errno.EEXIST and os.path.isdir(path):
        pass
      else: raise 
      
  def use_filter(self, name, function):
    self.environment.filters[name] = function
    

  def visit(self, state_machine):
    self.template = self.environment.get_template(self.filename)
    output = self.template.render(
      state_machine = state_machine, 
      states = state_machine.states.values(),
      transitions = state_machine.transitions.values(),
      attribute_groups = state_machine.attribute_group_list(),
      actors = state_machine.actors)
    self.path='output/'+state_machine.service+'/'+state_machine.resource
    self._mkdir_p(self.path)
    outfile =open(self.path+'/'+self.filename, 'w+')
    print >>outfile, output


class TemplateAndCommand(Template):
    
    def __init__(self,filename,command_template):
      Template.__init__(self,filename)
      self.command_template = command_template
      
    def visit(self, state_machine):
      Template.visit(self,state_machine)
      system_command = self.command_template.format(path=self.path)
      os.system(system_command)
