def get_list_more_6_characters(file):

    from xml.etree import ElementTree as ET
    import re
    import string
    translator = str.maketrans('.,', '.,', string.punctuation)

    tree = ET.parse(file)
    channel = tree.find('channel')

    raw_list = []
    for item in channel.findall('item'):
        nodes = ['title', 'description']
        for j in nodes:
            my_text = item.find(j).text  # got access to text of description
            tagless_my_text = re.sub(r'\<[^>]*\>', '', my_text)  # clean from inside tags
            formated_my_text = tagless_my_text.translate(translator)  # clean from punctuation
            word_list = formated_my_text.split()
            for word in word_list:
                if len(word) > 6:
                    raw_list.append(word)
    return raw_list


def common_words(raw_list):

    from collections import Counter

    raw_dict = Counter(raw_list) #dict {'word':number of times}
    word_list = raw_dict.most_common(10)
    raw_common_list = []
    for i in word_list:
        for j in i:
            raw_common_list.append(j)
    common_list = raw_common_list[::2]
    return common_list


def main():
    file_list = ['newsafr.xml', 'newscy.xml', 'newsfr.xml', 'newsit.xml']
    for file in file_list:
        func_2 = get_list_more_6_characters(file)
        func_3 = common_words(func_2)
        print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле {0}: {1}'.format(file, ', '.join(func_3)))


main()




