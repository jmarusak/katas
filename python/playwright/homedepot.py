from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

#context = browser.new_context()
context = browser.new_context(storage_state="homedepot.json")

page = context.new_page()
page.goto("https://careers.homedepot.ca/job-search")

page.select_option(".jobSearchFilters.careerAreaFilter", index=0)

input("Press Enter to continue...")
context.storage_state(path="homedepot.json")
browser.close()
