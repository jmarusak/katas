from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context(storage_state="jobs.json")

# Procom
page = context.new_page()
page.goto("https://portal.procomservices.com/jobs?loginType=contractor&lang=en")
page.fill("input[placeholder='City or Province/State']", "Ontario")
page.locator("text=Ontario >> nth=0").click()
page.press("input[type='text']", "Enter")

# SiSystems
page = context.new_page()
page.goto("https://www.sisystems.com/search/?location=5&expertise=1,4")

# Randstad
page = context.new_page()
page.goto("https://www.randstad.ca/jobs/q-analyst/ontario/toronto/")
page.get_by_label("sort:").select_option(label="date")

# emergiTEL
page = context.new_page()
page.goto("https://emergitel.catsone.com/careers/7701-General?title%5B0%5D=analyst")

# Akkodis
page = context.new_page()
page.goto("https://www.akkodis.com/en-ca/careers/job-results?q=")

input("Press Enter to continue...")
context.storage_state(path="jobs.json")
browser.close()
