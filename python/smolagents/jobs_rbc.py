import helium

helium.start_chrome("https://jobs.rbc.com/ca/en/search-results")

# cookie consent
helium.click(helium.Button("Accept All Cookies"))

helium.write("Data Scientist", into="Search by Keyword")
helium.click(helium.Button("Search"))
