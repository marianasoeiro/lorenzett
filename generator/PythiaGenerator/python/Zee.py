__all__ = ["Zee"]

from Gaugi import Logger
from Gaugi.messenger.macros import *
from G4Kernel import treatPropertyValue
from PythiaGenerator.utilities import default_allow_keys

class Zee( Logger ):

  __allow_keys = default_allow_keys

  def __init__( self, name, **kw ): 
    
    Logger.__init__(self)
    import ROOT
    ROOT.gSystem.Load('liblorenzett')
    from ROOT import Zee
    # Create the algorithm
    self.__core = Zee()
    for key, value in kw.items():
      self.setProperty( key,value )

    self.core().initialize()


  def core(self):
    return self.__core

  def run(self):
    self.core().run()
    self.core().finalize()



  def setProperty( self, key, value ):
    if key in self.__allow_keys:
      setattr( self, '__' + key , value )
      self.core().setProperty( key, treatPropertyValue(value) )
    else:
      MSG_FATAL( self, "Property with name %s is not allow for %s object", key, self.__class__.__name__)

 
  def getProperty( self, key ):
    if key in self.__allow_keys:
      return getattr( self, '__' + key )
    else:
      MSG_FATAL( self, "Property with name %s is not allow for %s object", key, self.__class__.__name__)



