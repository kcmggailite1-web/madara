from collections import Counter

saraksts = ["sveiki", "labdien", "sveiki", "labdien", "sveiki", "kaijas"
                , "cienījamais", "dzīvot", "cienījamais", "mūsdienu"
                , "mūsdienu", "cienījamais", "kukurūza", "māja"
                , "sveiciens", "dzīvot", "mūsdienu", "dzīvot", "sveiciens", "māja"]

skaititajs = Counter(saraksts)
for vards in skaititajs:
    print(vards)