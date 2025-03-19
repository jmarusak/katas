from playwright.sync_api import sync_playwright

urls = [
"https://careers.atb.com/careers?location=Calgary%2C%20AB%2C%20Canada&pid=1125899907081849&domain=atb.com&sort_by=new&location_distance_km=5&triggerGoButton=true",
"https://careers.atb.com/careers?location=Edmonton%2C%20AB%2C%20Canada&pid=1125899907081849&domain=atb.com&sort_by=new&location_distance_km=5&triggerGoButton=true"
]

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

context = browser.new_context()

for url in urls:
    page = context.new_page()
    page.goto(url)
    page.click("text='Advanced options'")
    page.click("text='Risk, Audit & Compliance'")

input("Press Enter to continue...")
browser.close()
