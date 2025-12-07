import importlib
import pkgutil
import sys
import inspect
from pathlib import Path

DAYS_PACKAGE = 'days'

def discover_and_run():
    results = []
    package = importlib.import_module(DAYS_PACKAGE)
    package_path = Path(package.__file__).parent

    for finder, name, ispkg in pkgutil.iter_modules([str(package_path)]):
        if name.startswith('day'):
            modname = f"{DAYS_PACKAGE}.{name}"
            try:
                mod = importlib.import_module(modname)
                if hasattr(mod, 'main') and inspect.isfunction(mod.main):
                    print(f"Running {modname}...")
                    out = mod.main()
                    results.append((name, out))
                else:
                    print(f"Skipping {modname}: no main() function")
            except Exception as e:
                print(f"Error running {modname}: {e}")
                results.append((name, e))
    return results

if __name__ == '__main__':
    res = discover_and_run()
    print('\nSummary:')
    for name, out in res:
        print(f"{name}: {out}")
