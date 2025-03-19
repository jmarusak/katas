from playwright.sync_api import sync_playwright

# Read URLs from file
with open("workday.txt", "r") as file:
    urls = file.readlines()

# Launch browser
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context(storage_state="workday.json")

# Open URLs
for url in urls:
    # Go to URL if not commented by #
    if not url.startswith("#"):
        page = context.new_page()
        page.goto(url)

input("Press Enter to continue...")
context.storage_state(path="workday.json")
browser.close()
