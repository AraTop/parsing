from main import Search

class Vacancy:
  def __init__(self, title , salary , url , experience , requirement , employment):
   self.title = title
   self.salary = salary
   self.url = url
   self.experience = experience 
   self.requirement = requirement
   self.employment = employment

  def __gt__(self, other):
      "метод для операции сравнения больше"
      
      return self.salary > other["price"]

  
  def __lt__(self,other):
      "метод для операции сравнения меньше"
      
      return self.salary < other["price"]
  
  def __str__(self):
      return f"{self.title}"
  


search = Search('Python','HeadHunter')
if search.HeadHunter_or_SuperJob() == "HeadHunter":
   y = 0
   data = search.head_hunter()
   vacancy = Vacancy(data[y]["name"] , data[y]["price"] , data[y]["alternate_url"] , data[y]["experience"] , data[y]["requirement"] , data[y]["employment"])
   print(vacancy.__gt__(data[2]))
   print(data[2]["price"]) # 50000
   print(data[0]["price"]) # 80000


   user = input()
   number_1 = 1
   number_2 = 2
   if user != number_1:
      print("sdfsdf")
   else:
      print("fsdfsd")
