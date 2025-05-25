from abc import ABC, abstractmethod


class PersonInfo(ABC):
    @abstractmethod
    def get_info_person(self):
        pass

class WorkInfo(ABC):
    @abstractmethod
    def get_info_work(self):
        pass

class SeniorDeveloper(PersonInfo,WorkInfo):

    def get_info_person(self):
        print("Общая информация о сотруднике...")

    def get_info_work(self):
        print("Общая информация о должностной инструкции...")


class Student(PersonInfo):

    def get_info_person(self):
        print("Общая информация о студенте...")
