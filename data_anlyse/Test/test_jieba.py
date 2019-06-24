import jieba
import jieba.analyse
import jieba.posseg


#### 停用词 
stopwords = [line.strip() for line in open('data/stop_words.txt', 'r', encoding='utf-8').readlines()] 

#### 加载自定义词典
jieba.load_userdict("userdict.txt")
jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
jieba.del_word('自定义词')


##### 词性标注
raw_data="习近平强调，人类对自然规律的认知没有止境，防灾减灾、抗灾救灾是人类生存发展的永恒课题。科学认识致灾规律，有效减轻灾害风险，实现人与自然和谐共处，需要国际社会共同努力。中国将坚持以人民为中心的发展理念，坚持以防为主、防灾抗灾救灾相结合，全面提升综合防灾能力，为人民生命财产安全提供坚实保障。希望各位代表围绕本次研讨会“与地震风险共处”的主题，踊跃参与，集思广益，为促进减灾国际合作、降低自然灾害风险、构建人类命运共同体作出积极贡献"
seg_list=jieba.cut(raw_data,cut_all=True)
print("/".join(seg_list))

words=jieba.posseg.cut(raw_data)
for word,flag in words:
    print('%s %s' %(word,flag))



######关键字提取 

# 字符串前面加u表示使用unicode编码
content = u'中国特色社会主义是我们党领导的伟大事业，全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想，为全面推进党的建设新的伟大工程进一步指明了方向。'

# 第一个参数：待提取关键词的文本
# 第二个参数：返回关键词的数量，重要性从高到低排序
# 第三个参数：是否同时返回每个关键词的权重
# 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print(str(item[0])+''+str(item[1]))
# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
# 即仅提取地名、名词、动名词、动词
keywords = jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print(str(item[0])+' '+str(item[1]))


