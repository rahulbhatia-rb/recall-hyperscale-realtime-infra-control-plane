import json,sys
from gate import evaluate
with open(sys.argv[1]) as f: r=evaluate(json.load(f))
if r['allowed']:
    print('READY'); raise SystemExit(0)
print('BLOCKED')
for x in r['findings']: print('- '+x)
raise SystemExit(1)
