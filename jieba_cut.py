import jieba

f = open('comments.txt')
comments = f.read()
#print(comments)

cut = jieba.cut(comments)

print(cut)
print('  '.join(cut))