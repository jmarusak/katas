from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://jobs.rbc.com/ca/en/search-results")

page.click("text='Accept All Cookies'")

page.click("text='Category'")
page.fill("input[placeholder='Search in Category']", "Technology")
page.get_by_label("Technology | Analytics | Research").check()

page.click("text='State / Province'")
page.fill("input[placeholder='Search in State / Province']", "Ontario")
page.get_by_label("Ontario ").check()

page.get_by_label("Sort by").select_option(label="Most recent")

input("Press Enter to continue...")
browser.close()
