"""Compile and run every lesson solution; exit non-zero on any failure."""
import glob, os, py_compile, subprocess, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = 0
for f in sorted(glob.glob(os.path.join(root, "lessons", "*", "*.py"))):
    py_compile.compile(f, doraise=True)
    if os.path.basename(f) == "solution.py":
        r = subprocess.run([sys.executable, f], cwd=os.path.dirname(f), capture_output=True, text=True, timeout=120, input="")
        print(("PASS " if r.returncode == 0 else "FAIL ") + os.path.relpath(f, root))
        if r.returncode:
            bad += 1
            print(r.stderr[-800:])
print("failures:", bad)
sys.exit(1 if bad else 0)
