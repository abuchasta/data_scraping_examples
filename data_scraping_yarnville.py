from selenium import webdriver
import gspread

gc = gspread.oauth()
sh = gc.open('data scraping')
worksheet = sh.sheet1

link = "https://www.yarnville.com.ua/product-category/ispie-raffia/matt"
browser = webdriver.Chrome()

try:
    browser.get(link)
    
    title_elements = browser.find_elements_by_css_selector("h2.woocommerce-loop-product__title")
    i = 2
    for element in title_elements:
        title = element.text
        worksheet.update_cell(i, 1, title)
        i = i + 1
        
    price_elements = browser.find_elements_by_css_selector("span.price")
    j = 2    
    for element in price_elements:    
        price = element.text
        worksheet.update_cell(j, 2, price)
        j = j + 1
           
finally:
    browser.quit()