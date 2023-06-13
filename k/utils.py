import sys
import logging 
import importlib
from pathlib import Path

def load_plug(plug_name):
  path = Path(f"k/plugins/{plug_name}.py")
  name = "k.plugins.{}".format(plug_name)
  spec = importlib.util.spec_from_file_location(name, path)
  load = importlib.util.module_from_spec(spec)
  load.logger = logging.getLogger(plug_name)
  spec.loader.exec_module(load)
  sys.modules["k.plugins."+ plug_name]  = load 
  print("kbot has Imported  " + plug_name)