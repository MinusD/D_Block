import traceback
from Task1.Person import Person
from Task1.LogModule import Log


class Doctor(Person):
    def __init__(self, name, surname, age, id_number, speciality):
        Person.__init__(self, name, surname, age)
        self.id_number = id_number
        self.speciality = speciality
        self.patients = {}
        Log('CRE', f'создано Doctor с именем: {name} и LisId: {id_number}')

    def new_patient(self, patient_id, patient_sn):
        self.patients[patient_id] = patient_sn
        Log('INF', f'добавлен пациент с id: {patient_id}  ФИО: {patient_sn} у доктора: {self.name}')

    def del_patient(self, patient_id):
        try:
            self.patients.pop(patient_id)
            Log('INF', f'удален пациент с id: {patient_id} у доктора: {self.name}')
        except:
            print(f"Something wrong! Failed to delete patient with id {patient_id}!")
            Log('ERR', f'не удалось удалить пациент с id: {patient_id} у доктора: {self.name}')

    def all_patient(self):
        print("ID    | Surname N.P.")
        for key, value in self.patients.items():
            print('{: <5}'.format(key), end=" | ")
            print('{: <5}'.format(value))
        Log('PRI', f'распечатан список пациентов доктора: {self.name}')

    def __str__(self):
        Log('PRI', f'распечатана информация о докторе {self.name}')
        return f'ФИ: {self.surname} {self.name}\nВозраст: {self.age}\nНомер удостоверения: {self.id_number}' \
               f'\nСпециальность: {self.speciality}'


if __name__ == '__main__':
    try:
        doc = Doctor("Vova", "Medven", 35, 10, "Proctologist")
        doc.new_patient(1, "Petrov F.E.")
        doc.new_patient(2, "Voronov V.R.")
        doc.new_patient(3, "Repotrov S.P.")
        doc.all_patient()
        doc.del_patient(2)
        doc.del_patient(2)
        doc.all_patient()
        print(doc)
    except AssertionError:
        print("TEST ERROR")
        traceback.print_exc()
    else:
        print("TEST PASSED")
