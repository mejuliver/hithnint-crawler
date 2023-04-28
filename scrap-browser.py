from selenium import webdriver 
from selenium.webdriver.common.by import By 
 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
url = "https://www.brownsfashion.com/ph/shopping/elleme-buttoned-coat-dress-16754486" 
 
options = webdriver.ChromeOptions() 
options.headless = True 

temporary_pokemons_data = [];
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
	driver.get(url) 	
 
	print("Page URL:", driver.current_url) 
	print("Page Title:", driver.title) 
	
 
	# parent_elements = driver.find_elements(By.XPATH, "//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']") 
	
	test_data = driver.page_source
	
	with open('page.html', 'wb') as html_file:
		html_file.write(test_data.encode())


# 	for parent_element in parent_elements: 
# 		pokemon_name = parent_element.find_element(By.XPATH, ".//h2") 
# 		pokemon_link = parent_element.get_attribute("href") 
# 		pokemon_price = parent_element.find_element(By.XPATH, ".//span") 
 
# 		temporary_pokemons_data.append({ 
# 			"name": pokemon_name.text, 
# 			"link": pokemon_link, 
# 			"price": pokemon_price.text 
# 		})
		
# print(temporary_pokemons_data)
 