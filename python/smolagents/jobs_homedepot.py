import helium

helium.start_chrome("https://careers.homedepot.ca/job-search")

# cookie consent
helium.click(helium.Button("OK"))

helium.click("Job Location")
helium.click("ON - Toronto")

