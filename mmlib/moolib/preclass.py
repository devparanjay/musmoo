import json

def askq():
    print('Please answer the following questions honestly for the best recommendation. These questions are selected based on significant research. The answers are never stored or used beyond the functioning of this app. :)')
    q1 = 'How is your day going?'
    q2 = 'Does your favorite food seem appealing to you right now?'
    q3 = 'How does thinking about your favorite color(s) make you feel at the moment?'
    a1 = str(input(q1))
    a2 = str(input(q2))
    a3 = str(input(q3))
    qas = a1 + '\n' + a2 + '\n' + a3
    return qas

def askqnr(qnr:list):
    print('\nPlease answer the following questions honestly for the best recommendation. These questions are selected based on significant research. The answers are never stored or used beyond the functioning of this app. :)')
    print('The more descriptive your answers, the better recommendations you get.')
    print('''If you don't want to answer all questions, then simply type "skip".''')
    ans = []
    for i in range(len(qnr)):
        print('Question ' + str(i+1) + ':')
        ai = str(input(f'{qnr[i]}'))
        if ai == 'skip':
            break
        else:
            ans.append(ai)
    return ans

def prep_conf(confpath):
    locations = {"DZ":  "Algeria",  "AR":  "Argentina",  "AU":  "Australia",  "AT":  "Austria",  "AZ":  "Azerbaijan",  "BH":  "Bahrain",  "BD":  "Bangladesh",  "BY":  "Belarus",  "BE":  "Belgium",  "BO":  "Bolivia",  "BA":  "Bosnia and Herzegovina",  "BR":  "Brazil",  "BG":  "Bulgaria",  "KH":  "Cambodia",  "CA":  "Canada",  "CL":  "Chile",  "CO":  "Colombia",  "CR":  "Costa Rica",  "HR":  "Croatia",  "CY":  "Cyprus",  "CZ":  "Czechia",  "DK":  "Denmark",  "DO":  "Dominican Republic",  "EC":  "Ecuador",  "EG":  "Egypt",  "SV":  "El Salvador",  "EE":  "Estonia",  "FI":  "Finland",  "FR":  "France",  "GE":  "Georgia",  "DE":  "Germany",  "GH":  "Ghana",  "GR":  "Greece",  "GT":  "Guatemala",  "HN":  "Honduras",  "HK":  "Hong Kong",  "HU":  "Hungary",  "IS":  "Iceland",  "IN":  "India",  "ID":  "Indonesia",  "IQ":  "Iraq",  "IE":  "Ireland",  "IL":  "Israel",  "IT":  "Italy",  "JM":  "Jamaica",  "JP":  "Japan",  "JO":  "Jordan",  "KZ":  "Kazakhstan",  "KE":  "Kenya",  "KW":  "Kuwait",  "LA":  "Laos",  "LV":  "Latvia",  "LB":  "Lebanon",  "LY":  "Libya",  "LI":  "Liechtenstein",  "LT":  "Lithuania",  "LU":  "Luxembourg",  "MY":  "Malaysia",  "MT":  "Malta",  "MX":  "Mexico",  "ME":  "Montenegro",  "MA":  "Morocco",  "NP":  "Nepal",  "NL":  "Netherlands",  "NZ":  "New Zealand",  "NI":  "Nicaragua",  "NG":  "Nigeria",  "MK":  "North Macedonia",  "NO":  "Norway",  "OM":  "Oman",  "PK":  "Pakistan",  "PA":  "Panama",  "PG":  "Papua New Guinea",  "PY":  "Paraguay",  "PE":  "Peru",  "PH":  "Philippines",  "PL":  "Poland",  "PT":  "Portugal",  "PR":  "Puerto Rico",  "QA":  "Qatar",  "RO":  "Romania",  "RU":  "Russia",  "SA":  "Saudi Arabia",  "SN":  "Senegal",  "RS":  "Serbia",  "SG":  "Singapore",  "SK":  "Slovakia",  "SI":  "Slovenia",  "ZA":  "South Africa",  "KR":  "South Korea",  "ES":  "Spain",  "LK":  "Sri Lanka",  "SE":  "Sweden",  "CH":  "Switzerland",  "TW":  "Taiwan",  "TZ":  "Tanzania",  "TH":  "Thailand",  "TN":  "Tunisia",  "TR":  "Turkey",  "UG":  "Uganda",  "UA":  "Ukraine",  "AE":  "United Arab Emirates",  "GB":  "United Kingdom",  "US":  "United States",  "UY":  "Uruguay",  "VE":  "Venezuela",  "VN":  "Vietnam",  "YE":  "Yemen",  "ZW":  "Zimbabwe"}
    languages = {0: 'Arabic', 1: 'African', 2: 'Assamese', 3: 'Odia', 4: 'Bengali', 5: 'Bhojpuri', 6: 'English', 7: 'Gujarati', 8: 'Haryanvi', 9: 'Hindi', 10: 'Kannada', 11: 'Malayalam', 12: 'Marathi', 13: 'Punjabi', 14: 'Tamil', 15: 'Telugu'}
    genres = {0: 'Carnatic Classical', 1: 'Classical', 2: 'Country and Americana', 3: 'Dance and Electronic', 4: 'Decades', 5: 'Devotional', 6: 'Family', 7: 'Folk and Acoustic', 8: 'Ghazal/Sufi', 9: 'Hindustani Classical', 10: 'Hip-Hop', 11: 'Indian Indie', 12: 'Indian Pop', 13: 'Indie and Alternative', 14: 'J-POP', 15: 'Jazz', 16: 'K-Pop'}
    music_moods = {0: 'Chill', 1: 'Commute', 2: 'Energy Boosters', 3: 'Feel-Good', 4: 'Focus', 5: 'Party', 6: 'Romance', 7: 'Sad', 8: 'Sleep', 9: 'Workout'} 

    print("Please choose the location you want the music suggestions to be from below.\n(e.g.: 0)")
    for location in locations:
        print(location, locations.get(location), sep=". ")
    usr_location_inp = input('''Enter a single country code from above: ''').upper()
    usr_location = {}
    usr_location["usr_location"] = {usr_location_inp: locations[usr_location_inp]}
    
    print("Please choose the languages you're comfortable listening to music in by entering comma-separated numbers from below.\n(e.g.: 0, 1, 7)")
    for lang in languages:
        print(lang, languages.get(lang), sep=". ")
    usr_langs_inp = list((str(input('''Enter "," separated numbers from above: ''')).replace(" ","")).split(','))
    usr_langs = {'usr_languages': {}}
    for i in range(len(usr_langs_inp)):
        usr_langs_inp[i] = int(usr_langs_inp[i])
        usr_langs["usr_languages"].update({usr_langs_inp[i]: languages[usr_langs_inp[i]]})

    print("Please choose your favorite music genres by entering comma-separated numbers from below.\n(e.g.: 1, 8)")
    for genre in genres:
        print(genre, genres.get(genre), sep=". ")
    usr_genres_inp = list((str(input('''Enter "," separated numbers from above: ''')).replace(" ","")).split(','))
    usr_genres = {'usr_genres': {}}
    for i in range(len(usr_genres_inp)):
        usr_genres_inp[i] = int(usr_genres_inp[i])
        usr_genres["usr_genres"].update({usr_genres_inp[i]: genres[usr_genres_inp[i]]})

    print("Please choose your favorite music moods by entering comma-separated numbers from below.\n(e.g.: 0, 3, 6)")
    for mood in music_moods:
        print(mood, music_moods.get(mood), sep=". ")
    usr_music_moods_inp = list((str(input('''Enter "," separated numbers from above: ''')).replace(" ","")).split(','))
    usr_music_moods = {'usr_music_moods': {}}
    for i in range(len(usr_music_moods_inp)):
        usr_music_moods_inp[i] = int(usr_music_moods_inp[i])
        usr_music_moods["usr_music_moods"].update({usr_music_moods_inp[i]: music_moods[usr_music_moods_inp[i]]})
    
    print("Do you want your recommendations to be printed here? The recommendations will still be stored in the recommendation folder anyways.")
    usr_printpref = {'usr_printpref': 0}
    usr_printpref_inp = int(input('Enter 0 for False and 1 for True: '))
        
    usr_printpref["usr_printpref"] = usr_printpref_inp
    
    conf_dict = {'usr': {}, 'moo': {}}
    conf_dict['usr'].update(usr_location)
    conf_dict['usr'].update(usr_langs)
    conf_dict['usr'].update(usr_genres)
    conf_dict['usr'].update(usr_music_moods)
    conf_dict["usr"].update(usr_printpref)
    conf_dict["moo"]['locations'] = locations
    conf_dict['moo']['languages'] = languages
    conf_dict['moo']['genres'] = genres
    conf_dict['moo']['music_moods'] = music_moods
    
    with open(confpath, 'w') as conff:
        json.dump(conf_dict, conff)

def prep_qnr(qnrpath):
    with open(qnrpath, 'r') as qnrf:
        return qnrf.readlines()

def prep_data(data, dafi_abs):
    with open(dafi_abs, 'w') as dafi:
        dafi.writelines(data)
        dafi.write('\n'.join(data))

def preclass(qnrpath, confpath, dafipath):
    prep_conf(confpath)
    emot = askqnr(qnr=prep_qnr(qnrpath))
    prep_data(emot, dafipath)
    
if __name__ == '__main__':
    print('preclass')