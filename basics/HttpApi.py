import requests as req

# Posts requests
postTodosUrl = 'https://jsonplaceholder.typicode.com/posts/'
r = req.post(postTodosUrl, data = {'title':'fooPost', 'body':'bar', 'userId':1})
if r.status_code == 201:
    print(r.text)

postId = r.json()['id']

getTodosUrl = 'https://jsonplaceholder.typicode.com/posts/?'
finalGetTodosUrl = getTodosUrl.replace('?', str(postId))

print("*** " + finalGetTodosUrl +  " ***")

r = req.get(finalGetTodosUrl, allow_redirects=True)
if r.status_code == 200:
    print(r.text)

# Put requests
putTodosUrl = 'https://jsonplaceholder.typicode.com/posts/1'
finalPutTodosUrl = putTodosUrl.replace('?', str(postId))

print("*** " + finalPutTodosUrl +  " ***")

r = req.put(finalPutTodosUrl, data = {'title':'fooPut', 'body':'bar', 'userId':1})
if r.status_code == 200:
    print(r.text)

getTodosUrl = 'https://jsonplaceholder.typicode.com/posts/?'
finalGetTodosUrl = getTodosUrl.replace('?', str(postId))
print("*** " + finalGetTodosUrl +  " ***")

r = req.get(finalGetTodosUrl, allow_redirects=True)
if r.status_code == 200:
    print(r.text)