#Care hospital wants to know the medical speciality visited by the maximum number of patients.
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>0:
        speciality=medical_speciality['P']
    elif E>0:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_speciality={'P':'Pediatrics','O':'orthopedics','E':'ENT'}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)