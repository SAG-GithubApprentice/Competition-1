names = ['St. Albans',
        'St. Albans', 
        'St Albans', 
        'St.Ablans',
        "St.albans", 
        "St. Alans", 'S.Albans',
        'St..Albans', 'S.Albnas', 
        'St. Albnas', "St.Al bans", 'St.Algans',
        "Sl.Albans", 'St. Allbans', "St, Albans", 'St. Alban', 'St. Alban']

#Expected output:

#['St Albans', 'St Albans', 'St Albans', 'St Ablans', 
# 'St Albans', 'St Alans', 'S Albans', 'St Albans', 'S Albnas', 
# 'St Albnas', 'St Albans', 'St Algans', 'Sl Albans', 'St Allbans', 'St Albans', 'St Alban', 'St Alban']

new_names = [' '.join(word.capitalize() for word in name.replace("St.Al bans", 'St Albans')
                       .replace('.', ' ').replace(',', ' ').split())for name in names]

print("new names =", new_names)

#Actual output

#new names = ['St Albans', 'St Albans', 'St Albans', 'St Ablans', 
# 'St Albans', 'St Alans', 'S Albans', 'St Albans', 'S Albnas',
# 'St Albnas', 'St Albans', 'St Algans', 'Sl Albans', 'St Allbans', 'St Albans', 'St Alban', 'St Alban']