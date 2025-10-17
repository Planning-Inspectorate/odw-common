import sys
from pipelines.scripts import *


sys.modules[__name__] = sys.modules["pipelines.scripts"]
