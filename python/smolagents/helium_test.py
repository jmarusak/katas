import helium

driver = helium.start_chrome("https://portal.procomservices.com/jobs?loginType=contractor&lang=en")


helium.click("Search by")
helium.press(helium.TAB)
helium.press(helium.TAB)
helium.press(helium.TAB)
helium.press(helium.TAB)
helium.press(helium.ENTER)
helium.click(helium.Text("Last 24 hours"))

# Wait for dropdown to be available and click to open it
helium.write("Toronto", into="City or Province/State")
helium.click(helium.S("#location"))
helium.click(helium.Text("Toronto"))

helium.click("Search")

driver
