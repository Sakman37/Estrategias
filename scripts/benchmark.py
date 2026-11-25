from pathlib import Path
import sys, time, statistics, csv, json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from router import *
OUT=Path(__file__).resolve().parents[1]/'evidence'; OUT.mkdir(exist_ok=True)
cases=[('fastest',FastestStrategy()),('accessible',AccessibleStrategy()),('balanced',BalancedStrategy())]
r=Router(campus_graph()); rows=[]
for name,st in cases:
 times=[]; result=None
 for _ in range(1000):
  t=time.perf_counter_ns(); result=r.route('Entrada','Laboratorios',st); times.append((time.perf_counter_ns()-t)/1e6)
 rows.append({**result,'runs':len(times),'median_ms':round(statistics.median(times),5),'p95_ms':round(sorted(times)[int(.95*(len(times)-1))],5)})
with (OUT/'benchmark.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
(OUT/'benchmark.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(rows,ensure_ascii=False,indent=2))
