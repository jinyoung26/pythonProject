# jumsu_list = [90, 100, 25, 35, 40]
#
# for jumsu in jumsu_list:
#     print(jumsu)

class post:
    id = ''
    title = ''
    author = ''
    content = ''

save_post = post()
save_post.id = 'PJY'
save_post.title = 'Django'
save_post.author = '박진영'
save_post.content = '장고 배우는 중'

print(save_post)
print("id:", save_post.id)
print("title:", save_post.title)
print("author:", save_post.author)
print("content:", save_post.content)
