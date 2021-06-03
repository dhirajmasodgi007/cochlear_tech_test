import json

def main():

    # create a simple JSON array
    #jsonString = '{"key1":"value1","key2":"value2","key3":"value3"}'
    user = open('user.json')
    devices = open('devices.json')
    accounts = open('accounts.json')
    # change the JSON string into a JSON object
    userObject = json.load(user)

    # print the keys and values
    #for key in jsonObject:
    #    value = jsonObject[key]
    #    print("The key and value are ({}) = ({})".format(key, value))

    #pass

    if 'type' not in userObject:
        raise ValueError ("Please pass user type either 'Patient' or 'Doctor'.")
    else:
        userType = userObject['type']
        print("User type found is: " + (userObject['type']))

    if 'userId' not in userObject:
        raise ValueError ("Please pass valid userId.")
    else:
        userId = userObject['userId']
        print("User found is: " + (userId)) 

    # In case of patient login I displayed the devices related to the particular patient.
    if userType == 'Patient':
        # Transform json input to python objects
        #input_dict = json.loads(devices)
        input_dict = json.load(devices)
        # Filter python objects with list comprehensions
        output_dict = [x for x in input_dict if  x['owner'] == userId]
        # Transform python object back into json
        output_json = json.dumps(output_dict)
        # Show json
        print("The list of devices related to: " + userId + "\n" + output_json)


    # In case of doctor login the rules applied are doctor's related clinics patients who gave the consent devices will be displayed. 
    if userType == 'Doctor':
        # Transform json input to python objects
        #input_dict = json.loads(devices)
        input_dict = json.load(accounts)
        clinic_dict = input_dict
        patient_dict = clinic_dict
        devices_dict = json.load(devices)
        # Filter python objects with list comprehensions
        output_dict = [x['clinic'] for x in input_dict if  x['id'] == userId]
        # Transform python object back into json
        output_json = json.dumps(output_dict)
        # Show json
        print("The list of clinics related to: " + userId + "\n" + output_json) 
        patient_list = []
        patient_itr_list = {}
        for clinic in output_dict:
            patient_itr_list =  [patient['id'] for patient in clinic_dict if  (clinic == patient['clinic'] and patient['type'] == 'Patient' and patient['consent'] == True)]
            patient_list =  patient_list + patient_itr_list
        output_json = json.dumps(patient_list)
        # Show json
        print("The list of doctor's patients related to clinics with whom doctor is connected and patient gave the consent are: " + userId + "\n" + output_json)
        device_list = []
        device_itr_list = {}
        for patient in patient_list:
            device_itr_list =  [device['deviceId'] for device in devices_dict if  patient == device['owner']]
            device_list =  device_list + device_itr_list
        output_json = json.dumps(device_list)
        # Show json
        print("The list of devices of doctor's patient with consent is listed " + userId + "\n" + output_json)


if __name__ == '__main__':
    main()