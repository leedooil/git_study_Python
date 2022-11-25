# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.loaction = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     def show_detail(self):
#         if self.loaction == "강남":
#             print("강남 아파트 매매 10억 2010년")
#         elif self.loaction == "마포":
#             print("마포 오피스텔 전세 5억 2007년")            
#         elif self.loaction == "송파":
#             print("송파 빌라 월세 500/50 2000년")
            
# h1 = House()                        
# h2 = House()                        
# h3 = House()                        

# h1.show_detail("강남")
# h2.show_detail("마포")
# h3.show_detail("송파")

# 정답
            
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.loaction = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.loaction, self.house_type, self.deal_type\
            , self.price, self.completion_year)
        
houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
    
                                