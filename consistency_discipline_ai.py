print("🧠 AI Consistency & Discipline Analyzer \n")

days = int(input("Enter number of days to analyze: "))

completion_rates = []
focus_levels = []

for i in range(days):
    planned = int(input(f"\nDay {i+1} tasks planned: "))
    completed = int(input(f"Day {i+1} tasks completed: "))
    focus = int(input(f"Day {i+1} focus level (1–5): "))

    rate = (completed / planned) * 100 if planned > 0 else 0
    completion_rates.append(rate)
    focus_levels.append(focus)

avg_completion = sum(completion_rates) / days
avg_focus = sum(focus_levels) / days

print("\n📊 CONSISTENCY ANALYSIS")
print(f"Average task completion: {avg_completion:.1f}%")
print(f"Average focus level: {avg_focus:.1f} / 5")

print("\n🧠 Discipline Assessment")

if avg_completion >= 85 and avg_focus >= 4:
    print("💪 Strong discipline and consistency")
elif avg_completion >= 65:
    print("⚠️ Moderate consistency. Improve daily discipline.")
else:
    print("🚨 Poor consistency. Risk of burnout or demotivation.")

print("\n🧭 AI Discipline Advice")

if avg_completion < 70:
    print("• Reduce task overload")
    print("• Focus on completing fewer tasks well")
if avg_focus < 3:
    print("• Improve focus environment")
if avg_completion >= 85:
    print("• Maintain this routine and scale gradually")
