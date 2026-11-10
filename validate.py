#!/usr/bin/env python3
"""Validate analyzer.html math: independent Python recomputation of 3 presets
+ Amendment-3 tax schedule, compared against JSON emitted by the page itself
(analyzer.html?test=1, rendered via headless Chrome --dump-dom)."""
import json, re, subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "file://" + os.path.join(HERE, "analyzer.html") + "?test=1"

# ---------- independent Python model (mirrors the spec, not the JS) ----------
def pmt(rate_pct, n, pv):
    r = rate_pct / 100 / 12
    if r <= 0:
        return pv / n
    return pv * r / (1 - (1 + r) ** -n)

def balance(pv, rate_pct, k):
    r = rate_pct / 100 / 12
    p = pmt(rate_pct, 360, pv)
    if r <= 0:
        return pv * (1 - k / 360)
    return pv * (1 + r) ** k - p * (((1 + r) ** k - 1) / r)

def exemption(a3, year):
    if not a3:
        return 50_000
    if year >= 3:
        return 250_000   # 2028
    if year >= 2:
        return 150_000   # 2027
    return 50_000

def run(s, years):
    cash = s["price"] * s["down"] / 100
    close = s["price"] * s["closePct"] / 100
    L = s["price"] - cash
    M = pmt(s["rate"], 360, L)
    if s["mode"] == "str":
        gross0 = s["adr"] * 365 * s["occ"] / 100
    else:
        gross0 = s["rent"] * 12
    rows, cum = [], 0.0
    for t in range(1, years + 1):
        f = (1 + s["expGrowth"] / 100) ** (t - 1)
        grossT = gross0 * (1 + s["rentGrowth"] / 100) ** (t - 1)
        collected = grossT * (1 - s["vac"] / 100)
        hoa, ins = s["hoa"] * 12 * f, s["ins"] * f
        if s["mode"] == "primary":
            av = s["price"] * (1 + min(3, s["appGrowth"]) / 100) ** (t - 1)
            tax = max(0, av - exemption(s["amendment3"], t)) * s["mills"] / 100
        else:
            av = s["price"] * (1 + s["appGrowth"] / 100) ** (t - 1)
            if s.get("ded15"):
                av *= 0.85
            tax = av * s["mills"] / 100
        repairs = capex = s["price"] * 0.01 * f
        mg = collected * (s["mgmtPct"] / 100 if s["mgmt"] else 0)
        strfee = collected * s.get("strPct", 0) / 100 if s["mode"] == "str" else 0
        tdt = grossT * s.get("tdt", 0) / 100 if s["mode"] == "str" else 0
        permit = s.get("permit", 0) if s["mode"] == "str" else 0
        op = hoa + ins + tax + repairs + mg + strfee + tdt + permit
        noi = collected - op
        debt = 12 * M if t <= 360 else 0
        cf = noi - capex - debt
        cum += cf
        rows.append(dict(year=t, noi=noi, cf=cf, cum=cum,
                         bal=balance(L, s["rate"], min(t * 12, 360)),
                         val=s["price"] * (1 + s["appGrowth"] / 100) ** t, tax=tax))
    # year-1 components (growth factors = 1)
    if s["mode"] == "primary":
        tax1 = max(0, s["price"] - exemption(s["amendment3"], 1)) * s["mills"] / 100
    else:
        av1 = s["price"] * (0.85 if s.get("ded15") else 1)
        tax1 = av1 * s["mills"] / 100
    y1 = rows[0]
    cap = y1["noi"] / s["price"] * 100
    coc = y1["cf"] / (cash + close) * 100
    F = s["hoa"] * 12 + s["ins"] + tax1 + 2 * s["price"] * 0.01 + 12 * M + (s.get("permit", 0) if s["mode"] == "str" else 0)
    if s["mode"] == "str":
        denom = (1 - s["vac"] / 100) * (1 - s.get("strPct", 0) / 100) - s.get("tdt", 0) / 100
        be = F / (365 * s["occ"] / 100 * denom) if denom > 0 else float("nan")  # ADR
    else:
        denom = (1 - s["vac"] / 100) * (1 - (s["mgmtPct"] / 100 if s["mgmt"] else 0))
        be = F / (12 * denom) if denom > 0 else float("nan")
    return dict(cashAtClose=cash + close, pmt=M, y1noi=y1["noi"], y1cf=y1["cf"],
                cap=cap, coc=coc, breakeven=be, tax1=tax1,
                cum5=rows[4]["cum"] if len(rows) >= 5 else None,
                val10=rows[-1]["val"], bal10=rows[-1]["bal"],
                taxes=[r["tax"] for r in rows])

# ---------- presets (must match analyzer.html) ----------
P = {
 "wpb": dict(mode="inv",price=340000,down=20,closePct=3,rate=6.95,hoa=100,ins=4280,mills=1.85,
             rent=1750,rentGrowth=2,appGrowth=3,expGrowth=3,vac=5,mgmt=True,mgmtPct=10,ded15=False,amendment3=False),
 "titus": dict(mode="inv",price=320000,down=20,closePct=3,rate=6.95,hoa=40,ins=4280,mills=1.85,
             rent=1600,rentGrowth=2,appGrowth=2.5,expGrowth=3,vac=5,mgmt=True,mgmtPct=10,ded15=False,amendment3=False),
 "kiss": dict(mode="str",price=475000,down=20,closePct=3,rate=6.95,hoa=110,ins=2400,mills=1.9,
             rent=0,rentGrowth=2,appGrowth=3,expGrowth=3,vac=0,mgmt=False,mgmtPct=0,ded15=False,amendment3=False,
             adr=215,occ=62,strPct=25,tdt=6,permit=1500),
 "vieraA3": dict(mode="primary",price=450000,down=25,closePct=3,rate=6.95,hoa=130,ins=3000,mills=1.85,
             rent=0,rentGrowth=0,appGrowth=3,expGrowth=3,vac=0,mgmt=False,mgmtPct=0,ded15=False,amendment3=True),
}

def main():
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
                          "--virtual-time-budget=4000", "--dump-dom", URL],
                         capture_output=True, text=True, timeout=60).stdout
    m = re.search(r'<div id="testjson">(.*?)</div>', out, re.S)
    if not m:
        print("FAIL: testjson not found in DOM (page JS may have crashed). DOM len:", len(out))
        sys.exit(1)
    js = json.loads(m.group(1).replace("&amp;", "&"))
    fails = 0
    for item in js:
        key = item["preset"]
        yrs = 5 if key == "vieraA3" else 10
        py = run(P[key], yrs)
        checks = []
        for f in ("cashAtClose", "pmt", "tax1"):
            checks.append((f, py[f], item.get(f)))
        if key != "vieraA3":
            for f in ("y1noi", "y1cf", "cap", "coc"):
                checks.append((f, py[f], item.get(f)))
            checks.append(("breakeven", py["breakeven"], item.get("breakeven")))
            checks.append(("cum5", py["cum5"], item.get("cum5")))
        else:
            checks.append(("taxes", py["taxes"], item.get("taxes")))
        for name, a, b in checks:
            if a is None or b is None:
                ok = a == b
            elif isinstance(a, list):
                ok = len(a) == len(b) and all(abs(x - y) < 0.01 for x, y in zip(a, b))
            else:
                ok = abs(a - b) < 0.01
            if not ok:
                fails += 1
                print(f"  MISMATCH {key}.{name}: python={a} js={b}")
            else:
                print(f"  ok  {key}.{name} = {round(a,2) if isinstance(a,(int,float)) else a}")
    print("\nRESULT:", "ALL CHECKS PASS" if fails == 0 else f"{fails} MISMATCHES")
    # sanity print of the numbers for the report
    for k in ("wpb", "titus", "kiss"):
        r = run(P[k], 10)
        print(f"{k}: y1CF/mo={r['y1cf']/12:,.0f} CoC={r['coc']:.2f}% cap={r['cap']:.2f}% breakeven={'ADR ' if k=='kiss' else '$'}{r['breakeven']:,.0f}")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
