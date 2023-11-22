from django.shortcuts import render
from django.http import HttpResponse

import requests
from django.http import JsonResponse

import string
from string import digits

import json

from arabicstopwords.stopwords_lexicon import stopwords_lexicon 
import qalsadi.lemmatizer 


from .form import ContactForm, SoundForm


def read(request):
    pass


def search_word_level(w, level_1, level_2, level_3, level_4, level_5):
    if w in level_1:
        return 1
    elif w in level_2:
        return 2
    elif w in level_3:
        return 3
    elif w in level_4: 
        return 4
    elif w in level_5:
        return 5
    else:
        return 0


def index(request):

    with open("read/json/level_1.json", 'r') as f:
        level_1 = json.load(f)
    with open("read/json/level_2.json", 'r') as f:
        level_2 = json.load(f)
    with open("read/json/level_3.json", 'r') as f:
        level_3 = json.load(f)
    with open("read/json/level_4.json", 'r') as f:
        level_4 = json.load(f)
    with open("read/json/level_5.json", 'r') as f:
        level_5 = json.load(f)


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():        
            text = form.cleaned_data['message']
            print("from POST", text)


            ## Do all the processing ##

            # 1. clean text from numbers and punctuations
            text = text.translate(str.maketrans("","", string.punctuation))
            text = text.translate(str.maketrans('', '', '؛،?؟ً.'))
            
            text = text.translate(str.maketrans('', '', digits))
            text = text.translate(str.maketrans('', '', '١٢٣٤٥٦٧٨٩٠'))

            # to list
            text_lst= list(text.split(" "))

            # 2. remove stopwords

            #lexicon = stopwords_lexicon()
            #processed_text_lst = [t for t in text_lst if not lexicon.is_stop(t)]


            # 3. filter words 
            #func_words = ['من', 'إلى', 'عن', 'على', 'حتى', 'رب', 'مذ', 'منذ', 'خلا', 'عدا', 'حاشا', 'وارب', 'يا', 'أيا',
            #            'هيا', 'إن', 'أن', 'لكن', 'كأن', 'لعل', 'ليت', 'إلا', 'غير', 'سوى', 'خلا', 'عدا', 'حاشا', 'لم',
            #            'لن', 'سوف', 'أبو', 'أخو', 'حمو', 'ذو', 'فو', 'كاد', 'كرب', 'أوشك', 'عسى', 'حرى', 'شرع', 'أنشأ',
            #            'أخذ', 'بدأ', 'هب', 'طفق', 'جعل', 'كان', 'أصبح', 'أمسى', 'أضحى', 'ظل', 'بات', 'صار', 'ليس',
            #            'مازال', 'مابرح', 'ماانفك', 'مافتئ', 'مادام', 'بل', 'لكن', 'أو', 'لا', 'ثم', 'أم', 'لو',
            #                'لولا', 'مهما', 'اين', 'متى', 'كيفما', 'حيثما', 'أنى', 'أيان', 'أي', 'إذما', 'كلما', 'أنا',
            #                'نحن', 'إياي', 'إيانا', 'أنت', 'أنتما', 'أنتم', 'أنتن', 'إياك', 'إياكما', 'إياكم', 'إياكن', 'هو',
            #                'هي', 'هما', 'هن', 'هم', 'إياه', 'إياها', 'إياهما', 'إياهم', 'إياهن', 'هل', 'متى', 'أين', 'ما',
            #                'كيف', 'كم', 'لماذا', 'ماذا', 'منذ', 'الذي', 'التي', 'اللذان', 'اللتان', 'اللاتي', 'الذين', 'ذا',
            #                'هذا', 'هذه', 'هذان', 'هاتان', 'هؤلاء', 'هنا', 'هناك', 'هنالك', 'ذي', 'أولاء', 'إولى', 'ثمة', 'هذين',
            #                'هاتين', 'ذاك', 'ذاكما', 'ذاكم', 'ذاكن', 'ذيك', 'ذيكما', 'ذيكن', 'تيك', 'تيكن', 'تيكما', 'ذانك', 'آس',
            #                'بري', 'إجاص', 'افوكادو', 'أكي', 'اكي', 'دنيا', 'أناناس', 'باذنجان', 'ببايا', 'برتقال', 'بطيخ', 'أحمر',
            #                'بلوط', 'بندق', 'بوملي', 'تفاح', 'تمر', 'تمر', 'هندي', 'فاكهة', 'التنين', 'توت', 'تين', 'تين', 'شوكي',
            #                'جوافة', 'جوز', 'جوز', 'الهند', 'خيار', 'دراق', 'رامبوتان', 'رمان', 'زعرور', 'زيتون', 'سفرجل', 'شمام',
            #                'صبار', 'حبوب', 'الصنوبر', 'طماطم', 'عليق', 'عناب', 'عنب', 'عنبية', 'فاكهة', 'الخبز', 'فراولة', 'فستق',
            #                'قرع', 'قشطة', 'كاجو', 'كاكاو', 'كاكي', 'كرز', 'كريفون', 'الكشمش', 'الأسود', 'كمكوات', 'كوسة', 'كيوي',
            #                'لوز', 'لوز', 'استوائي', 'لونجان', 'ليتشي', 'ليمون', 'مانجو', 'مشمش', 'موز', 'نبق', 'أبيض', 'أصفر', 'أحمر',
            #                'وردي', 'أزرق', 'رمادي', 'أسود', 'برتقالي', 'أخضر', 'بنفسجي', 'أرجواني', 'بني', 'نيلي', 'فضي', 'ذهبي']

            #processed_text_lst = [t for t in processed_text_lst if t not in func_words]

            
            # remove empty text
            text_lst = list(filter(None, text_lst))


            # remove duplicates
            #processed_text_lst = list(set(processed_text_lst)) 
            

            # lemmetization 


            lemmer = qalsadi.lemmatizer.Lemmatizer()
            lemma_text_lst = lemmer.lemmatize_text(text, return_pos=True)

            #for i, word in enumerate(processed_text_lst):
            #    if word[1] == 'stopword':

            print("Length of text List", len(text_lst))
            print(text_lst)

            print("Length of lem text", len(lemma_text_lst))
            print(lemma_text_lst)



            #print('processed_text_lst', processed_text_lst)

            # Connect to API
            word_data_lst = []
            #not_found_words_lst = [] #processed_text_lst.copy()
            for i, word_to_search in enumerate(text_lst):
                url = 'https://siwar.ksaa.gov.sa/api/alriyadh/exact-search?query='+lemma_text_lst[i][0]
                headers = {'accept': 'application/json', 'apikey': '89a50cce-f3d3-44bc-adf2-981628c30643'}
                response = requests.get(url, headers=headers, verify=False)  
                if response.ok:
                    
                    data = response.json() 
                    #print("from json", data)
                    if data != []:

                        level = search_word_level(lemma_text_lst[i][0], level_1, level_2, level_3, level_4, level_5)
                        #print(word_to_search, level)
                        word_data ={
                                'original_word': word_to_search,
                                'found': True,
                                'difficulty_level': level,
                                'word_info':[],
                                'lemma': lemma_text_lst[i][0],
                                'pos':lemma_text_lst[i][1],
                                #lemma

                            }


                        same_word_list = []
                        for d in data: 
                            
                            if d['pos'] in ['N', 'NC', 'NA', 'NL', 'NT','NM', 'NG','NF','NO','NI']:
                                pos ='name'
                            elif d['pos'] in ['V', 'VI', 'VT']:
                                pos ='verb'
                            elif d['pos'] in ['A', 'AR', 'AS', 'AO', 'AP', 'AA']:
                                pos = 'adj'
                            elif d['pos'] in ['P', 'PP', 'PD', 'PR']:
                                pos = 'pron'
                            else:
                                pos = 'other'


                            
                            word_info ={
                                'nonDiacriticsWord': d['nonDiacriticsLemma'],
                                'word': d['lemma']['formRepresentations'][0]['form'],
                                'morph_pattern': d['morphologicalPatterns'],
                                'pos': pos,
                                'difficulty_level': level,
                                #'arabic_meaning': d['senses'][0]['definition']['textRepresentations'][0]['form'],
                                #'english_translation': d['senses'][0]['translations'][0]['form'],
                                #'usage_level': d['extras']['senseDetails'][0]['usageLevel'],
                                #'theme': d['extras']['senseDetails'][0]['theme']
                            }

                            if d['senses'] != []:
                                word_info["arabic_meaning"] = d['senses'][0]['definition']['textRepresentations'][0]['form']
                            
                            if d['senses'] != []:
                                word_info["english_translation"] = d['senses'][0]['translations'][0]['form']


                            word_data['word_info'].append(word_info)
                        #word_data_lst.append(same_word_list)
                    else:
                        #not_found_words_lst.append(word_to_search)
                        #print("Not found in API", not_found_words_lst)
                        word_data ={
                                'original_word': word_to_search,
                                'found': False,
                                'difficulty_level': 0,
                                'word_info':[]

                            }
                    print(word_data)
                    word_data_lst.append(word_data)

            #not_found_words_lst.extend(func_words)

            return render(request, "read/index.html", context = {'form': form, 'originalText':text_lst, 'wordList':word_data_lst})
      
    form = ContactForm()
    return render(request, "read/index.html", {'form': form})
        
