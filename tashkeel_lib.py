# Tashkeel library for main constants, dictionaries, functions frequently used in the tashkeel prediction module

# all diacritics except shaddah
basic_diacritics = ['َ',
             'ً',
             'ُ',
             'ٌ',
             'ِ',
             'ٍ',
             'ْ']

# all diacritics including shaddah
diacritics = ['َ',
             'ً',
             'ُ',
             'ٌ',
             'ِ',
             'ٍ',
             'ْ',
             'ّ']
# all diacritics including combination like shaddah - damma
full_diacritics = [
'z',
'َ',
'ُ',
'ِ',
'ً',
'ٌ',
'ٍ',
'ّ',
'َّ',
'ًّ',
'ُّ',
'ٌّ',
'ِّ',
'ٍّ',
'ْ',
'ّْ']

# clean raw text and unify new lines
def clean_text(p_text):
  raw_text = p_text
  raw_text = raw_text.replace("!","")
  raw_text = raw_text.replace('"',"")
  raw_text = raw_text.replace("(","")
  raw_text = raw_text.replace(")","")
  raw_text = raw_text.replace("-","")
  raw_text = raw_text.replace(".","")  
  raw_text = raw_text.replace(":","")
  raw_text = raw_text.replace("«","")
  raw_text = raw_text.replace("»","")
  raw_text = raw_text.replace("؟","")
  raw_text = raw_text.replace("0","")
  raw_text = raw_text.replace("1","")
  raw_text = raw_text.replace("2","")
  raw_text = raw_text.replace("3","")
  raw_text = raw_text.replace("4","")
  raw_text = raw_text.replace("5","")
  raw_text = raw_text.replace("6","")
  raw_text = raw_text.replace("7","")
  raw_text = raw_text.replace("8","")
  raw_text = raw_text.replace("9","")
  raw_text = raw_text.replace("z","")
  raw_text = raw_text.replace("ٌٍ","")
  raw_text = raw_text.replace("ٌٍ","")
  raw_text = raw_text.replace("ٍْ","")
  raw_text = raw_text.replace("ٍّ","")
  raw_text = raw_text.replace("ًٌ","")
  raw_text = raw_text.replace("ٌْ","")
  raw_text = raw_text.replace("    "," ")
  raw_text = raw_text.replace("   "," ")
  raw_text = raw_text.replace("  "," ")
  raw_text = raw_text.replace("  "," ")
  raw_text = raw_text.replace("  "," ")
  raw_text = raw_text.replace("\u200d","")
  raw_text = raw_text.replace("،","")
  raw_text = raw_text.replace("\n ","\n")
  raw_text = raw_text.replace(" \n","\n")
  raw_text = raw_text.replace("\n\n","\n")
  raw_text = raw_text.replace("\n\n","\n")
  raw_text = raw_text.replace("\n"," \n ")
  
  return raw_text;


# clean bayt from all punctuation and diacritics
def clean_bayt(t_bayt):
    t_bayt = t_bayt.replace("!","")
    t_bayt = t_bayt.replace('"',"")
    t_bayt = t_bayt.replace("(","")
    t_bayt = t_bayt.replace(")","")
    t_bayt = t_bayt.replace("-","")
    t_bayt = t_bayt.replace(".","")
    t_bayt = t_bayt.replace(":","")
    t_bayt = t_bayt.replace("«","")
    t_bayt = t_bayt.replace("»","")
    t_bayt = t_bayt.replace("؟","")
    t_bayt = t_bayt.replace("0","")
    t_bayt = t_bayt.replace("1","")
    t_bayt = t_bayt.replace("2","")
    t_bayt = t_bayt.replace("3","")
    t_bayt = t_bayt.replace("4","")
    t_bayt = t_bayt.replace("5","")
    t_bayt = t_bayt.replace("6","")
    t_bayt = t_bayt.replace("7","")
    t_bayt = t_bayt.replace("8","")
    t_bayt = t_bayt.replace("9","")
    t_bayt = t_bayt.replace("َ","")
    t_bayt = t_bayt.replace("ٌ","")
    t_bayt = t_bayt.replace("ُ","")
    t_bayt = t_bayt.replace("ً","")
    t_bayt = t_bayt.replace("ٍ","")
    t_bayt = t_bayt.replace("ِ","")
    t_bayt = t_bayt.replace("ْ","")
    t_bayt = t_bayt.replace("ّ","")
    t_bayt = t_bayt.replace("\u200d","")
    t_bayt = t_bayt.replace("،","")
    t_bayt = t_bayt.replace("\n\n","\n")
    t_bayt = t_bayt.replace("    "," ")
    t_bayt = t_bayt.replace("   "," ")
    t_bayt = t_bayt.replace("  "," ")
    t_bayt = t_bayt.replace("  "," ")
    t_bayt = t_bayt.replace("  "," ")
    t_bayt = t_bayt + '\n            '

    return t_bayt