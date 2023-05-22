import requests 
response=requests.post("https://graph.facebook.com/102480044787664/photos?url=https://technologynews24x7.com/wp-content/uploads/2020/07/python-for-web-development-1068x601.jpg &message=My First Post on Facebook By Python Code&access_token=EAACbD57lMNYBABRK9KzOR1OpMsXoMjmMMZANIBet9CORupvGFO6T1psAgf2tXZARgPV0JOazjclPbwX2k1hIHpvAfPkbVM92XIbtXLZC4r5hlPZAX3RcQECGcErmPbFEkkaUtJpc9wlvyk7hY4nHw2KrewPXzrtU0yWLx8xjiJKwL6zHCPSxj6yvzPyeZB5ahFhaX5xxMqdfchdSneiZCMZCtgwik8TwhgZD")
print(response.json())

