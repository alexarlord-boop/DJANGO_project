# {'title': '',
#  'description': '',
#  'coords': '',
#  'type': '',
#  'user_skill': '',
#  'enviroment_chars': '',
#  'extreme': ''}

all_activities = [{'title': 'Туутари-Парк',
                   'description': 'На сегодняшний день Туутари-Парк - современный горнолыжный комплекс площадью 50 гектар, с 6 освещенными трассами длиной от 400 до 600 метров и перепадом высот от 60 до 80 метров.',
                   'coords': '59.693254, 30.178091',
                   'type': 's_mount',
                   'user_skill': '0',
                   'enviroment_chars': '1',
                   'extreme': '0'},

                  {'title': 'Горнолыжный курорт Архыз',
                   'description': 'Расположенный в живописнейшем районе Карачаево-Черкесской республики, рядом с одноименным селом, всесезонный горнолыжный курорт является буквально местом притяжения туристов.',
                   'coords': '43.543728, 41.181608',
                   'type': 's_mount',
                   'user_skill': '0',
                   'enviroment_chars': '0',
                   'extreme': '0'},

                  {'title': 'Абзаково',
                   'description': 'Славится своей уникальной природой, головокружительным горным воздухом, вкупе с умопомрачительными пейзажами.',
                   'coords': '53.798092, 58.614875',
                   'type': 's_mount',
                   'user_skill': '0',
                   'enviroment_chars': '1',
                   'extreme': '0'},

                  {'title': 'Шерегеш',
                   'description': 'Курорт со стремительно развивающейся инфраструктурой, ежегодно завоевывающий новых поклонников, чрезвычайно популярный среди жителей Сибири',
                   'coords': '52.953390, 87.955999',
                   'type': 's_mount',
                   'user_skill': '0',
                   'enviroment_chars': '1',
                   'extreme': '0'},

                  {'title': 'Горный Воздух',
                   'description': 'С годами популярность курорта только растет и постепенно от всесоюзных соревнований и кубков, «Горный Ветер» дорастает до международных.',
                   'coords': '46.950439, 142.801174',
                   'type': 's_mount',
                   'user_skill': '1',
                   'enviroment_chars': '2',
                   'extreme': '1'},

                  {'title': 'Superbank, Gold Coast',
                   'description': 'Considered to be a “surfer’s paradise,” Gold Coast is known for its 70 km of beaches and four epic point breaks including the Superbank, which is considered one of the world’s finest breaks.',
                   'coords': '-28.001431, 153.363484',
                   'type': 'on_water',
                   'user_skill': '0',
                   'enviroment_chars': '2',
                   'extreme': '0'},

                  {'title': 'Sanya, Hainan',
                   'description': 'China is not exactly known for its beaches or surfing, but a gigantic island on its southern tip offers untouched tropical beaches with consistent, un-crowded waves.',
                   'coords': '18.292447, 109.444089',
                   'type': 'on_water',
                   'user_skill': '0',
                   'enviroment_chars': '2',
                   'extreme': '0'},

                  {'title': 'Tofino, Vancouver Island',
                   'description': 'This is the surfing capital of Canada that offers fun, picturesque breaks on the west coast of the island.',
                   'coords': '49.114048, -125.893811',
                   'type': 'on_water',
                   'user_skill': '1',
                   'enviroment_chars': '0',
                   'extreme': '2'},
                  ]
#
# def add_activities_to_db(list_of_activities):
#     for act in list_of_activities:
#         new_activity = Activity(title=act['title'], description=act['description'],
#                                 coords=act['coords'], type=act['type'],
#                                 user_skill=act['user_skill'], enviroment_chars=act['enviroment_chars'],
#                                 extreme=act['extreme'])
#
#         # new_activity.title = act['title']
#         # new_activity.description = act['description']
#         # new_activity.coords = act['coords']
#         # new_activity.type = act['type']
#         # new_activity.user_skill = act['user_skill']
#         # new_activity.enviroment_chars = act['enviroment_chars']
#         # new_activity.extreme = act['extreme']
#
#         new_activity.save()
#
#
# def add_one_activity_to_db(activitiy):
#     new_activity = Activity(title=activitiy['title'], description=activitiy['description'],
#                             coords=activitiy['coords'], type=activitiy['type'],
#                             user_skill=activitiy['user_skill'], enviroment_chars=activitiy['enviroment_chars'],
#                             extreme=activitiy['extreme'])
#     new_activity.save()