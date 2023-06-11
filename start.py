from main import Search , Brain , JsonFile, Vacancy


def user_Function():
   # api_key - замепните на свой
   api_key = "v3.r.137576500.e2e95fd182c513c0803ff06264ceec9d568d0b1e.4703138b796b9e79e9efd267b578c0f8a4686e60"

   print("Здравствуй, как ваше имя?")
   name_user = input().title()
   print(f"{name_user}, очень рад знакомству. \nГотовы познакомится с вакансиями? \nEсли да то просто напиши '+' либо 'enter' \nEсли же нет напиши '-' ")
   user_answer = input()
   if user_answer == "+":
      print("ready")     
   elif user_answer == "-":
      print('Приходите в следующий раз')
      return 

   print("\nГде вы хотите искать вакансии \n1 - HeadHunter, \n2 - SuperJob")
   user_input = input()
   if int(user_input) == 1:
      search = Search(input("Какой язык искать: "), "HeadHunter")
         
   elif int(user_input) == 2:
      search = Search(input("Какой язык искать: "), "SuperJob")
         
   if search.HeadHunter_or_SuperJob() == "HeadHunter":
      data = search.head_hunter()
      y = 0
      for value in data:
         print("-------------------------------")
         print(f"Вакансия по счету: {y}")
         print(f"Name: {value['name']}")
         print(f"Price: {value['price']} Руб.")
         print(f"Employment: {value['employment']}")
         print(f"Url: {value['alternate_url']}")
         print(f"Requirement: {value['requirement']}")
         print(f"Experience: {value['experience']}")
         y += 1
   
   elif search.HeadHunter_or_SuperJob() == "SuperJob":
      data = search.super_job(api_key)
      y = 0
      for value in data:
         print("-------------------------------")
         print(f"Вакансия по счету: {y}")
         print(f"Name: {value['name']} Руб.")
         print(f"Price: {value['price']}")
         print(f"Employment: {value['employment']}")
         print(f"Url: {value['alternate_url']}")
         print(f"Requirement: {value['requirement']}")
         print(f"Experience: {value['experience']}")
         y += 1

   def dell_Function(data , user_input):
      y = 0
      for value in data:
         if value == {}:
            print("\nВы уже удаляли данную вакансию")
         elif y == user_input:
            del value['name'] ,
            del value['price'] ,
            del value['employment'] ,
            del value['alternate_url'] ,
            del value['requirement'] ,
            del value['experience']
            print(f"Вакансия под номером {user_input} удалена") 
         y += 1
            
      return data

   while True:
      print("-------------------------------\nХотите удалить из списка какую-то вакансию перед добавлением в Json_File? \nEсли да то просто напишите '+' \nесли же нет '-'")
      user_input = input()
      if user_input == "-":
         break
      elif user_input == "+":
         print("Укажите нумерацию той вакансии которую хотите удалить")
         user_input = input()
         data = dell_Function(data , int(user_input))
      else:
         print("\nНеизвестный знак, выберите среди предложенных")


   while True:
      print("Хотите сравнить вакансии между собой по зарплате? \nЕсли хотите пишите '+' , если не хотите '-' ")
      user_input = input()
      if user_input == "-":
         break
      elif user_input == "+":
         print("Какой язык програмирования?")
         user_input = input()
         data_HeadHunter = Search(user_input , "HeadHunter")
         data_SuperJob = Search(user_input , "SuperJob")

         if data_HeadHunter.HeadHunter_or_SuperJob() == "HeadHunter":
            data_hh = search.head_hunter()
            
         if data_SuperJob.HeadHunter_or_SuperJob() == "SuperJob":
            data_sj = search.super_job(api_key)

         print("Какою нумерацию вакансий хотите сравнить из предложеных")
         print("Нажмите 'Enter' чтоб показать варианты вакансий")
         input()
         y = 0
         for value in data_hh:
            if value == {}:
               continue
            print("\n-------------------------------")
            print(f"Вакансия по счету: {y}")
            print(f"Name: {value['name']} Руб.")
            print(f"Price: {value['price']}")
            print(f"Employment: {value['employment']}")
            print(f"Url: {value['alternate_url']}")
            print(f"Requirement: {value['requirement']}")
            print(f"Experience: {value['experience']}")
            y += 1

         print("\nИз выше перечисленых вакансий выберите нужную указав цифру")

         user_input_number = input()
         vacancy1 = Vacancy(data_hh[int(user_input_number)]["name"] , data_hh[int(user_input_number)]["price"] , data_hh[int(user_input_number)]["alternate_url"] , data_hh[int(user_input_number)]["experience"] , data_hh[int(user_input_number)]["requirement"] , data_hh[int(user_input_number)]["employment"])

         print("Хотите сравнить > или <")

         user_input = input()
         if user_input == ">":
            is_gt = vacancy1.__gt__(data_sj[int(user_input_number)])
            if is_gt == False:
               print("\nЗарплата на HeadHunter под данным номером меньше чем на SuperJob с таким же номером")
            elif is_gt == True:
               print("\nЗарплата на SuperJob под данным номером меньше чем на HeadHunter с таким же номером")

         elif user_input == "<":
            is_lt = vacancy1.__lt__(data_sj[int(user_input_number)])
            if is_lt == True:
                print("\nЗарплата на HeadHunter под данным номером меньше чем на SuperJob с таким же номером")
            elif is_lt == False:
                print("\nЗарплата на SuperJob под данным номером меньше чем на HeadHunter с таким же номером")
               
         else:
            print("\nНеизвестный знак, выберите среди предложенных")
      else:
         print("\nНеизвестный знак, выберите среди предложенных")


   print("\nВот и все, добавляем готовые данные в Json_File")
   print("Придумайте название Json_File")
   print("loading...")
   user_name_file = input()
   
   if user_name_file == "":
      print("Oops... Вы не указали название файла, название будет стандартным")
      user1 = JsonFile(data,"file.json")
      user1.save_to_JSON()
      print("Все готова, Json_File должен появится, спасибо за уделенное время")
      return
      
   user1 = JsonFile(data,user_input)
   user1.save_to_JSON()
   print("Все готова, Json_File должен появится, спасибо за уделенное время")