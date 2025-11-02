def recommend_optimizations(high_cpu, high_mem):
    recs = []
    for _, row in high_cpu.iterrows():
        recs.append(f"⚙️ {row['name']} (PID {row['pid']}) uses {row['cpu_percent']:.1f}% CPU — consider throttling or optimization.")
    for _, row in high_mem.iterrows():
        recs.append(f"🧠 {row['name']} (PID {row['pid']}) uses {row['memory_percent']:.1f}% memory — possible memory leak or inefficiency.")
    if not recs:
        recs.append("✅ System operating efficiently.")
    return recs
