<<<<<<< HEAD
import random

recipes = ["된장찌개", "김치볶음밥", "떡볶이", "불고기", "비빔밥", "라면"]

print("오늘 뭐 먹지?")
print("👉 추천 메뉴:", random.choice(recipes))
=======
recipes = {
    "된장찌개": ["된장", "두부", "호박", "양파"],
    "김치볶음밥": ["김치", "밥", "대파", "계란"],
    "떡볶이": ["떡", "고추장", "어묵", "양파"],
    "불고기": ["소고기", "간장", "설탕", "참기름"],
    "비빔밥": ["밥", "나물", "고추장", "계란"],
    "라면": ["라면", "계란", "파"]
}

print("오늘 뭐 먹지?")
for dish, ingredients in recipes.items():
    print(f"\n📌 {dish}")
    print("  필요 재료:", ", ".join(ingredients))
>>>>>>> feature/shopping-list
