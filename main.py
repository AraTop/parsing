from abc import ABC , abstractmethod
import json
import requests


class Sample(ABC):
   @abstractmethod

   def head_hunter(self):
      pass
   @abstractmethod

   def super_job(self):
      pass
   @abstractmethod

   def HeadHunter_or_SuperJob(self):
      pass

class Search(Sample):
   
   def __init__(self,lang, base) -> None:
      self.lang = lang
      self.base = base

   def head_hunter(self):
      """получить вакансии данного языка програмирования , на платформе HeadHunter """

      payload = {
      'text': f'Программист {self.lang}',
      'area': 1,
      'only_with_salary': True,
      'period': 30,
      }
   
      data = requests.get("https://api.hh.ru/vacancies",params=payload)
      data_json = data.json()
      data_returned = []

      for item in data_json["items"]:
         json_format = {"name":None, "price":None, "employment":None, "alternate_url":None, "requirement":None, "experience":None}

         json_format["name"] = item["name"]

         if item["salary"]["from"] == None:
            json_format["price"] = item["salary"]["to"]
         elif item["salary"]["to"] == None:
            json_format["price"] = item["salary"]["from"]
         else:
            json_format["price"] = item["salary"]["from"] + item["salary"]["to"]

         json_format['employment'] = item["employment"]["name"]
         json_format["alternate_url"] = item["alternate_url"]
         json_format["requirement"] = item["snippet"]["requirement"]
         json_format["experience"] = item["experience"]["name"]
      
         data_returned.append(json_format)

      return data_returned
   
   def super_job(self,api_token):
      """получить вакансии данного языка програмирования , на платформе SuperJob """

      url = 'https://api.superjob.ru/2.0/vacancies/'

      payload = {
         'keyword': f'{self.lang} разработчик',
         'area':1,
         'page': 0, 
         'period': 30}
   
      headers = {
         'X-Api-App-Id': api_token}
   
      response = requests.get(url, params=payload, headers=headers, timeout=10)
      data = response.json()
      data_returned = []

      for item in data["objects"]:
         json_format = {"name":None, "price":None, "employment":None, "alternate_url":None, "requirement":None, "experience":None}

         json_format["name"] = item["profession"]

         if item["payment_from"] == None:
            json_format["price"] = item["payment_to"] 

         elif item["payment_to"]  == None:
            json_format["price"] = item["payment_from"]

         else:
            json_format["price"] = item["payment_from"] + item["payment_to"] 

         json_format['employment'] = item["type_of_work"]["title"]

         json_format["alternate_url"] = item["link"]

         json_format["requirement"] = item["candidat"]
         json_format["experience"] = item["experience"]["title"]
      
         data_returned.append(json_format)

      return data_returned

   def HeadHunter_or_SuperJob(self):
      if self.base == "HeadHunter":
         return "HeadHunter"
      
      elif self.base == "SuperJob":
         return "SuperJob"

class Brain:
   def __init__(self,file,number_list_iteration):
      self.file = file
      self.number = number_list_iteration

   def __gt__(self, other):
      "метод для операции сравнения больше"
      number_iteration = 0
      number_iteration = self.number
   
      number = self.file[self.number]["price"] 

      for item in other:
         return number > item["file"][number_iteration]["price"]

   def __lt__(self,other):
      "метод для операции сравнения меньше"
      number_iteration = 0
      number_iteration = self.number
   
      number = self.file[self.number]["price"]

      for item in other:
         return number < item["file"][number_iteration]["price"]
      
   def __repr__(self) -> str:
      return f"{self.file}"

   def __getitem__(self,key):
      return self.__dict__

class JsonFile:
   def __init__(self,vacancies, name_file):
      self.vacancies = vacancies
      self.name_file = name_file

   def save_to_JSON(self):
      data = {}
      data['vacancies'] = []

      for value in self.vacancies:
         if value == {}:
            continue
         data['vacancies'].append(value)

      with open(self.name_file, 'w' , encoding="utf-8") as f:
         json.dump(data, f, indent=2 , ensure_ascii=False)   