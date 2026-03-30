import urllib.request, urllib.error

print("Sending 65 requests to /health (limit: 60/minute)...")
results = {}
for i in range(65):
    try:
        r = urllib.request.urlopen("http://localhost:8000/health")
        code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    results[code] = results.get(code, 0) + 1
    print(f"  [{i+1:02d}] HTTP {code}", "(RATE LIMITED)" if code == 429 else "")

print("\n--- Summary ---")
for code, count in sorted(results.items()):
    label = "(rate limited)" if code == 429 else "(ok)"
    print(f"  HTTP {code}: {count} responses {label}")
