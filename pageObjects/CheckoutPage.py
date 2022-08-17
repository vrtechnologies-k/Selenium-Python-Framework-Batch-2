from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    searchKeyword = (By.CLASS_NAME,'search-keyword')

    def getKeyword(self):
        return self.driver.find_element(*CheckoutPage.searchKeyword)

    vegTables = (By.CSS_SELECTOR,'.products .product')

    def getvegTables(self):
        return self.driver.find_elements(*CheckoutPage.vegTables)

    buttons = (By.XPATH,'//div[@class="product"]/div/button')

    def getButtons(self):
        return self.driver.find_elements(*CheckoutPage.buttons)

    vegName = (By.XPATH,'parent::div/parent::div/h4')

    def getvegName(self):
        return self.driver.find_element(*CheckoutPage.vegName)

    cartIcon = (By.CLASS_NAME,'cart-icon')

    def getcartIcon(self):
        return self.driver.find_element(*CheckoutPage.cartIcon)

    checkout = (By.XPATH,"//button[contains(.,'PROCEED TO CHECKOUT')]")

    def getcheckOut(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    productName = (By.CSS_SELECTOR,'.product-name')

    def getproductName(self):
        return self.driver.find_elements(*CheckoutPage.productName)

    productPrice = (By.XPATH,"//table[@id='productCartTables']/tbody/tr/td[5]")

    def getproductPrices(self):
        return self.driver.find_elements(*CheckoutPage.productPrice)

    totalAmount = (By.CSS_SELECTOR,'.totAmt')

    def gettotalAmount(self):
        return self.driver.find_element(*CheckoutPage.totalAmount)

    promoCode = (By.CLASS_NAME,'promoCode')

    def getpromoCode(self):
        return self.driver.find_element(*CheckoutPage.promoCode)

    promoButton = (By.CLASS_NAME, 'promoBtn')

    def getpromoButton(self):
        return self.driver.find_element(*CheckoutPage.promoButton)

    discountAmount = (By.CLASS_NAME, 'discountAmt')

    def getdiscountAmount(self):
        return self.driver.find_element(*CheckoutPage.discountAmount)

    promoInfo = (By.CLASS_NAME, 'promoInfo')

    def getpromoInfo(self):
        return self.driver.find_element(*CheckoutPage.promoInfo)

    placeOrder  = (By.XPATH,"//button[contains(.,'Place Order')]")

    def getplaceOrder(self):
        return self.driver.find_element(*CheckoutPage.placeOrder)
