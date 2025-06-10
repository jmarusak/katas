from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context(storage_state="storage.json")

# Procom
page = context.new_page()
page.goto("https://portal.procomservices.com/jobs?loginType=contractor&lang=en")
page.fill("input[placeholder='City or Province/State']", "Ontario")
page.locator("text=Ontario >> nth=0").click()
page.press("input[type='text']", "Enter")

# SiSystems
page = context.new_page()
#page.goto("https://www.sisystems.com/search/?location=5&expertise=1,4")
page.goto("https://www.sisystems.com/search/?location=5")

# Akkodis
page = context.new_page()
page.goto("https://www.akkodis.com/en-ca/careers/job-results?q=")

# DoorDash
page = context.new_page()
page.goto("https://careersatdoordash.com/job-search/?keyword=&location=Toronto&spage=1")

input("Press Enter to continue...")
context.storage_state(path="storage.json")
browser.close()
