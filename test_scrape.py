from utils.reddit_scraper import get_user_data

username = "kojied"  # You can change this to test any Reddit user
posts, comments = get_user_data(username)

print("🔹 Sample Posts:")
for p in posts[:3]:
    print(p)
    print("-" * 40)

print("\n🔹 Sample Comments:")
for c in comments[:3]:
    print(c)
    print("-" * 40)
