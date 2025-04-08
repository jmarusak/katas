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

# Rogers
page = context.new_page()
page.goto("https://jobs.rogers.com/search")

# Bell
page = context.new_page()
page.goto("https://jobs.bell.ca/ca/en/search-results")
page.click("text='Category'")
#page.fill("input[placeholder='Search in category']", "Technology")
#page.get_by_label("Technology").check()

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

input("Press Enter to continue...")
context.storage_state(path="jobs.json")
browser.close()
