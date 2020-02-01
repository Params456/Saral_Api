# import requests,json

# a=requests.get("http://saral.navgurukul.org/api/courses")
# print(a)

# with open("params.json","w") as b:
# 	c=json.dump(a.text,b)
# 	c=json.loads(a.text)
# 	# print(c)
# 	# print(type(c)
# 	d=c["availableCourses"]
# 	e=int(input("enter the no"))
# 	f=1
# 	g={}
# 	for i in range(len(d)):
# 		g[f]=d[i]["id"]
# 		f+=1
# 	# print(g)
# 	while True:
# 		for h in g:
# 			if e==h:
# 				print(g[h])

# 				i=requests.get("http://saral.navgurukul.org/api/courses/"+str(g[h])+"/exercises")
# 				# print(i)
# 				j=json.loads(i.text)
# 				k=j["data"]
# 				for z in range(len(k)):
# 					print(k[z]["name"])

					
# 				print("next Id = n , previous Id = p ,again this Id = a ")
# 				l=input("Enter what are you going to do: ")

# 				if l=="n":
# 					e+=1
# 				elif l=="p":
# 					e-=1
# 				if l=="a":
# 					e=e
