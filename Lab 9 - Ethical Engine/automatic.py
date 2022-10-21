from audit import audit, log_scenario



def automatic_decision(scenario):
    Pas_tod_count = 0
    Pas_ad_count = 0
    Pas_eld_count = 0
    Pas_preg_count = 0
    Pas_pet_count = 0
    Pas_doc_count = 0
    Pas_ceo_count = 0
    Pas_crim_count = 0

    Ped_tod_count = 0
    Ped_ad_count = 0
    Ped_eld_count = 0
    Ped_preg_count = 0
    Ped_pet_count = 0
    Ped_doc_count = 0
    Ped_ceo_count = 0
    Ped_crim_count = 0

    for i in scenario.passengers:
        if (i.age == "baby" or i.age == "child"):
            Pas_tod_count += 1
        if (i.pregnant == True):
            Pas_preg_count += 1
        if (i.age == "adult"):
            Pas_ad_count += 1
        if (i.age == "elderly" ):
            Pas_eld_count += 1
        if (i.charType == "animal"):
            Pas_pet_count += 1
        if (i.profession == "doctor"):
            Pas_doc_count += 1
        if (i.profession == "CEO"):
            Pas_ceo_count += 1
        if (i.profession == "criminal"):
            Pas_crim_count += 1

    for j in scenario.pedestrians:
        if (j.age == "baby" or i.age == "child"):
            Ped_tod_count += 1
        if (j.pregnant == True):
            Ped_preg_count += 1
        if (j.age == "elderly" ):
            Ped_eld_count += 1
        if (j.age == "adult" ):
            Ped_ad_count += 1
        if (j.charType == "animal"):
            Ped_pet_count += 1
        if (j.profession == "doctor"):
            Ped_doc_count += 1
        if (j.profession == "CEO"):
            Ped_ceo_count += 1
        if (j.profession == "criminal"):
            Ped_crim_count += 1

    if (Pas_tod_count > Ped_tod_count):
        return "passengers"
    elif (Pas_tod_count < Ped_tod_count): # Prioritize Children
        return "pedestrians"
    elif (Pas_preg_count > Ped_preg_count): # Then Prioritize the pregnant
        return "passengers"
    elif (Pas_preg_count < Ped_preg_count):
        return "pedestrians"
    elif (Pas_doc_count > Ped_doc_count): # Then Prioritize the Doctors
        return "passengers"
    elif (Pas_doc_count < Ped_doc_count):
        return "pedestrians"
    elif (Pas_ceo_count > Ped_ceo_count): # Then Prioritize CEOs for economy
        return "passengers"
    elif (Pas_ceo_count < Ped_ceo_count):
        return "pedestrians"
    elif (Pas_ad_count > Ped_ad_count):  # The Adults
        return "passengers"
    elif (Pas_ad_count < Ped_ad_count):
        return "pedestrians"
    elif (Pas_eld_count > Ped_eld_count):
        return "passengers"
    elif (Pas_eld_count < Ped_eld_count):
        return "pedestrians"
    elif (Pas_crim_count > Ped_crim_count): # Then, whichever has least # of criminals
        return "pedestrians"
    elif (Pas_crim_count < Ped_crim_count):
        return "passengers"
    elif (Pas_pet_count > Ped_pet_count): # Then Prioritize Pets
        return "passengers"
    elif (Pas_pet_count < Ped_pet_count):
        return "pedestrians"

    return "passengers" #Otherwise, default to passengers first

if __name__ == '__main__':
    audit(automatic_decision, 10000, seed=8675309)
