#Write a Python Program to create a product class  declare the states of the class as ProductName,ProductId,Price,GST,
#MfgDate,Expdate.
#create 5 objects intitalise it using parameterized constructor and access the elements of using instance method and declare
#mutator methods as set product name,product price for all 6 prperties and change the values of their properties 
#using mutator methods and print it
class Product():
    def __init__(self,Product_name,Product_ID,Price,GST,Mfg_Date,Exp_Date):
        self.Name = Product_name
        self.ID = Product_ID
        self.Price = Price
        self.GST = GST
        self.Mfg_Date = Mfg_Date
        self.Exp_Date = Exp_Date
    def set_Price(self):
        self.Price = '67,000'
    def DisplayDetails(self):
        print(f"Product Name: {self.Name}")
        print(f"Product ID:   {self.ID}")
        print(f"Price:        {self.Price}")
        print(f"GST:          {self.GST}")
        print(f"Mfg_Date:     {self.Mfg_Date}")
        print(f"Exp_date:     {self.Exp_Date}")
M1=Product('Kawasaki','KD5654','2,00,000','15%','23_09_2024','01_01_2099')
M1.DisplayDetails()
M1.set_Price()
M1.DisplayDetails()