import re

print("🔥 ANAM KA AI CODE ROASTER PRO 🔥")
print("Apna Python code paste karo. Main batati hun kitne paani me ho 😎")
print("Code khatam karne ke baad nayi line me sirf 'DONE' likhna\n")

lines = []
while True:
    line = input()
    if line.strip().upper() == "DONE":
        break
    lines.append(line)

code = "\n".join(lines)
line_count = len(lines)

if line_count == 0:
    print("AI: Bhai khali page roast karun? Code to likho pehle 😂")
    exit()

score = 100
roasts = []
tips = []

# Roasting Logic
if line_count < 5:
    roasts.append("5 lines se kam? Ye code hai ya tweet?")
    score -= 20

if "import" not in code:
    roasts.append("Library use nahi ki. Cycle pe Formula 1 jeetni hai?")
    score -= 10
    tips.append("import random, datetime waghera use karo")

if code.count("print(") > line_count // 2:
    roasts.append("Har line me print? Console ko radio banaya hua hai")
    score -= 15

if "def " not in code and line_count > 10:
    roasts.append("10+ lines aur ek bhi function nahi? Andaaz-e-bayan ghalat hai")
    score -= 15
    tips.append("Code ko functions me break karo: def main(): ...")

if "while True:" in code and "break" not in code:
    roasts.append("while True bina break? Infinite loop = laptop ka janaza 😭")
    score -= 25

if re.search(r"except\s*:", code):
    roasts.append("Bare 'except:'? Sab errors chupa rahi ho. Chor nahi, coder bano")
    score -= 10
    tips.append("except Exception as e: use karo")

if "==" in code and "if" not in code:
    roasts.append("== likha hai lekin if nahi. Ye comparison kisse kar rahe ho?")

# Good things
if "# " in code:
    roasts.append("Comments likhe hain! Chalo kuch to akal hai ✅")
    score += 5

if "for" in code or "while" in code:
    score += 5

# Final Grade
score = max(0, score)
if score >= 90:
    grade = "S-Tier Coder 👑"
elif score >= 70:
    grade = "A-Grade Dev 💪"
elif score >= 50:
    grade = "Pass ho, par mehnat karo 📚"
else:
    grade = "Tutorial dekh ke aao pehle 🥲"

print("\n" + "="*50)
print(f"📊 ANAM KE AI KA REPORT 📊")
print(f"Lines of Code: {line_count}")
print(f"AI Score: {score}/100")
print(f"Grade: {grade}")
print("="*50)

print("\n🔥 ROAST SESSION 🔥")
if roasts:
    for i, roast in enumerate(roasts, 1):
        print(f"{i}. {roast}")
else:
    print("Ya Allah! Perfect code. Roast karne ko kuch nahi mila 😭")

if tips:
    print("\n💡 ANAM KI TIPS 💡")
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")

print(f"\nAnam says: Code karte raho, ek din Google me job pakki 🚀")
