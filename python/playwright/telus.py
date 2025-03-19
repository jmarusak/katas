from playwright.sync_api import sync_playwright

urls = [
"https://careers.telus.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_department=Data+Science&optionsFacetsDD_customfield5=&optionsFacetsDD_customfield1=&optionsFacetsDD_customfield2=",
"https://careers.telus.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_department=Engineering+%26+Development&optionsFacetsDD_customfield5=&optionsFacetsDD_customfield1=&optionsFacetsDD_customfield2=",
"https://careers.telus.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_department=Marketing&optionsFacetsDD_customfield5=&optionsFacetsDD_customfield1=&optionsFacetsDD_customfield2="
]

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)

context = browser.new_context()

for url in urls:
    page = context.new_page()
    page.goto(url)
    # Accept cookies only on the first page
    if url == urls[0]:
        page.click("text='Accept'")

input("Press Enter to continue...")
browser.close()
