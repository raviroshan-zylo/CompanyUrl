from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.get("https://www.google.com/search?ei=YqCbW4nrAZGA8QXbuomYBg&q=python+testing&oq=python+testing&gs_l=psy-ab.3..0i20i263k1l2j0l8.3025.5857.0.6030.15.13.0.0.0.0.384.1887.0j1j5j1.8.0....0...1c.1.64.psy-ab..7.8.2176.6..35i39k1j0i67k1.292.Ho7iK9kBVMk")


uinput = input("Paste the company names")
newlist = list(uinput.split(","))


#time.sleep(7)

for x in newlist:   
    dr.find_element_by_id("lst-ib").clear()
    k = dr.find_element_by_id("lst-ib").send_keys(x)
    dr.find_element_by_name("btnG").click()
    var = dr.find_element_by_tag_name("cite").text
    var1 = var.replace("https://","")
    var2 = var1.replace("http://","")
    var3 = var2.replace("www.","")
    print ("www."+ var3[0:var3.find("/")])
    dr.find_element_by_id("lst-ib").clear()

