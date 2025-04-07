from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context(storage_state="jobs.json")

# Home Depot
page = context.new_page()
page.goto("https://careers.homedepot.ca/job-search")
page.select_option(".jobSearchFilters.careerAreaFilter", index=0)

# Tangerine Bank
page = context.new_page()
page.goto("https://jobs.scotiabank.com/Tangerine/go/Tangerine/2407617/?locale=en_US")
# If you see a cookie banner, click "Accept All"
if page.query_selector("text='Accept All'"):
    page.click("text='Accept All'")

# RBC
page = context.new_page()
page.goto("https://jobs.rbc.com/ca/en/search-results")
page.click("text='Category'")
page.fill("input[placeholder='Search in Category']", "Technology")
page.get_by_label("Technology | Analytics | Research").check()
#page.click("text='State / Province'")
#page.fill("input[placeholder='Search in State / Province']", "Ontario")
#page.get_by_label("Ontario (").check()
page.get_by_label("Sort by").select_option(label="Most recent")

# Rogers
page = context.new_page()
page.goto("https://jobs.rogers.com/search")

# Procom
page = context.new_page()
page.goto("https://portal.procomservices.com/jobs?loginType=contractor&lang=en")
page.fill("input[placeholder='City or Province/State']", "Ontario")
page.locator("text=Ontario >> nth=0").click()
page.press("input[type='text']", "Enter")

# Akkodis
#page = context.new_page()
#page.goto("https://www.akkodis.com/en-ca/careers/job-results?q=")

# Randstad
page = context.new_page()
page.goto("https://www.randstad.ca/jobs/q-data/s-technologies/ontario/contract/")
page.get_by_label("sort:").select_option(label="date")

# Bell
page = context.new_page()
page.goto("https://jobs.bell.ca/ca/en/search-results")
page.click("text='Category'")
#page.fill("input[placeholder='Search in category']", "Technology")
#page.get_by_label("Technology").check()

input("Press Enter to continue...")
context.storage_state(path="jobs.json")
browser.close()
