from collections import defaultdict

# Given dictionary
communities = {
    'afghanistan': 0, 'namibia': 2, 'nauru': 2, 'nepal': 2, 'netherlands': 1, 'new zealand': 2, 
    'nicaragua': 2, 'niger': 2, 'nigeria': 2, 'north korea': 2, 'north macedonia': 2, 'norway': 2, 
    'albania': 0, 'algeria': 0, 'andorra': 0, 'angola': 0, 'antigua and barbuda': 0, 'argentina': 0, 
    'armenia': 0, 'australia': 0, 'austria': 0, 'azerbaijan': 0, 'bahamas': 1, 'saint kitts and nevis': 1, 
    'saint lucia': 1, 'saint vincent and the grenadines': 1, 'samoa': 1, 'san marino': 1, 'saudi arabia': 1, 
    'senegal': 1, 'serbia': 1, 'seychelles': 1, 'sierra leone': 1, 'singapore': 1, 'slovakia': 1, 
    'slovenia': 1, 'solomon islands': 1, 'somalia': 1, 'south africa': 1, 'south korea': 1, 
    'south sudan': 1, 'spain': 1, 'sri lanka': 1, 'sudan': 1, 'suriname': 1, 'sweden': 1, 
    'switzerland': 1, 'syria': 1, 'são tomé and príncipe': 1, 'bahrain': 2, 'bangladesh': 10, 
    'haiti': 4, 'honduras': 1, 'hungary': 10, 'barbados': 1, 'belarus': 1, 'belgium': 5, 
    'madagascar': 5, 'malawi': 4, 'malaysia': 5, 'maldives': 1, 'mali': 4, 'malta': 0, 
    'marshall islands': 1, 'mauritania': 0, 'mauritius': 1, 'mexico': 5, 'micronesia': 0, 
    'moldova': 0, 'monaco': 5, 'mongolia': 0, 'montenegro': 5, 'morocco': 5, 'mozambique': 3, 
    'myanmar': 5, 'belize': 3, 'east timor': 3, 'ecuador': 3, 'egypt': 3, 'el salvador': 3, 
    'equatorial guinea': 3, 'eritrea': 3, 'estonia': 3, 'eswatini': 3, 'ethiopia': 3, 'benin': 2, 
    'bhutan': 2, 'bolivia': 0, 'bosnia and herzegovina': 0, 'botswana': 0, 'brazil': 8, 
    'laos': 1, 'latvia': 0, 'lebanon': 2, 'lesotho': 8, 'liberia': 0, 'libya': 0, 'liechtenstein': 2, 
    'lithuania': 8, 'luxembourg': 8, 'brunei': 4, 'iceland': 4, 'india': 4, 'indonesia': 4, 
    'iran': 4, 'iraq': 4, 'ireland': 4, 'israel': 4, 'italy': 4, 'ivory coast': 4, 'bulgaria': 0, 
    'burkina faso': 12, 'oman': 2, 'burundi': 4, 'cambodia': 0, 'cameroon': 2, 'canada': 0, 
    'cape verde': 3, 'central african republic': 11, 'chad': 6, 'chile': 3, 'china': 0, 
    'colombia': 0, 'comoros': 1, 'congo': 11, 'costa rica': 0, 'croatia': 0, 'cuba': 0, 
    'cyprus': 1, 'czechia': 0, 'denmark': 6, 'djibouti': 4, 'dominica': 6, 'dominican republic': 6, 
    'dr congo': 6, 'kazakhstan': 2, 'kenya': 0, 'kiribati': 4, 'kuwait': 9, 'kyrgyzstan': 2, 
    'romania': 0, 'russia': 0, 'rwanda': 0, 'tajikistan': 2, 'tanzania': 0, 'thailand': 6, 
    'togo': 9, 'tonga': 0, 'trinidad and tobago': 9, 'tunisia': 0, 'turkey': 9, 'turkmenistan': 2, 
    'tuvalu': 7, 'fiji': 4, 'finland': 6, 'france': 3, 'gabon': 2, 'gambia': 0, 'georgia': 0, 
    'germany': 13, 'yemen': 2, 'ghana': 0, 'greece': 3, 'grenada': 0, 'guatemala': 0, 
    'guinea': 0, 'guinea-bissau': 7, 'uganda': 7, 'ukraine': 3, 'united arab emirates': 1, 
    'united kingdom': 5, 'united states': 1, 'uruguay': 7, 'uzbekistan': 2, 'guyana': 0, 
    'qatar': 14, 'jamaica': 0, 'japan': 2, 'jordan': 2, 'pakistan': 2, 'palau': 7, 
    'palestine': 3, 'panama': 0, 'papua new guinea': 0, 'paraguay': 16, 'peru': 7, 
    'philippines': 1, 'poland': 6, 'portugal': 8, 'vanuatu': 7, 'vatican city': 15, 
    'venezuela': 0, 'vietnam': 5, 'zambia': 0, 'zimbabwe': 3
}

# Create a dictionary where keys are community numbers and values are sorted lists of countries
sorted_communities = defaultdict(list)
for country, community in communities.items():
    sorted_communities[community].append(country)

# Sort each community's country list alphabetically
for community in sorted_communities:
    sorted_communities[community].sort()

# Print the sorted output
for community, countries in sorted(sorted_communities.items()):
    print(f"{community}: {', '.join(countries)}")
