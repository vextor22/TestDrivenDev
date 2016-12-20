from selenium import webdriver

browser = webdriver.Firefox()

#user navigates to our home page
browser.get('http://127.0.0.1:8000')

#looks at page title
assert 'To-Do' in browser.title

#Enters a todo item straight away (Buy peacock feathers)

#Hits enter, page updates and lists
#1: Buy peacock feathers" as item in to-do list

#still a box to add another item
#enters (Use peacock feathers to make a fly)

#page updates, both items in list

#wonders whether site remembers the list, visits the unique url of list,
#list is still there

#satisfied, user leaves

browser.quit()
