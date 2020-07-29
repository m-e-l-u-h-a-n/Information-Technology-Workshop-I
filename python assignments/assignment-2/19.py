import sys
import textwrap
module_names=', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_names))