#!/usr/bin/python3

import time
import subprocess as sb
print ("Content-type:text/html\r\n\r\n")

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage('operationsForm') 

# Get data from fields


def displayPage():

	#the starting tags
	print('''
	<html>
		
		<head>
			<title>
				My Docker World
			</title>
		</head>

		<body>

			<!--<center><img src='docker.png' alt='Docker Logo'/>-->

			<center><h2>Welcome to Your One Stop GUI Based Docker Management System</h2></center>
			
			<pre>
			<form action = 'index.py' name = 'operationsForm'>

			''')

	docker_containers = sb.getoutput('sudo docker ps -a')
		
	docker_containers = docker_containers + "\n"	
	
	length = len(docker_containers)

	start_index = 0

	end_index = docker_containers.find('\n')   #Because docker ps -a uses '\n' for next line of information display
	
	#print('first find : ',end_index,'..',docker_containers[end_index],'@')	
	
	print('      ',docker_containers[start_index:end_index] )   #printing the heading

	#start_index = end_index + 1 #skipped '\n'

	#print('start_index : ',start_index,'..',docker_containers[start_index],'@')

	docker_containers =  docker_containers[ end_index + 1 : length ] 
	
	length = len(docker_containers)
	
	#print("-----------------------------")
	#print(docker_containers)
	#print("-------------------------------")

	f = 1
	
	#start_index = 0	
	#print('next start_index : ',start_index,'..',docker_containers[start_index],'@')
	

	'''for i in repr(docker_containers):
		print(i)'''
	end_index = docker_containers.find('\n')
	#print('second find end_index : ',end_index)

	while True  :   
		#because at end when '\n' will not be found start_index will become 0 as start_index = end_index + 1 = -1 + 1 = 0
		
		#print(start_index," - ",end_index)	
		#print("***",docker_containers[start_index],"***")
		#print("###",docker_containers[start_index],"###")	

		print('''<br><input type="radio" name="containerID" value="{}"  {}>'''.format(docker_containers[ start_index : docker_containers.find(' ')] ,'checked' if f == 1 else ' ' ) ,end='')
		                
		print(docker_containers[ start_index : end_index ] )
		
		docker_containers =  docker_containers[ end_index + 1: length ] 
		
		start_index = 0
		end_index = docker_containers.find('\n')
		length = len(docker_containers)
		#print('new end index : ',end_index)
		
		#print()
		
		if end_index == -1 or end_index >= length :
			#print(' end_index : ',end_index)
			#print(' length : ',length,'good bye')
			break
		f = 2 #was only for selecting one docker container initially in case user forgets to select the docker conatiner for operation to perform on

		'''if f>=7 :
			print(start_index," - ",end_index," - ",length)
			break'''
	#The operation to be performed radio buttons
	print('''<h4>Select Operation to perform on the Selected Container</h4>
		<!--<input type = 'radio' name = 'operation' value = 'execute'>Execute command on Container--><input type = 'radio' name = 'operation' value = 'inspect'>Inspect Container	<!--<input type = 'radio' name = 'operation' value = 'createImage'>Create Container Image-->	<input type = 'radio' name = 'operation' value = 'delete'>Delete Container	
		<h4>Or Select Operation to perform on the Docker Engine</h4>
		<!--<input type = 'radio' name = 'operation' value='ymlOperation'>Use Infrastructure as a code--><input type = 'radio' name = 'operation' value = 'createNew'>Create a New Container	<input type = 'radio' name = 'operation' value = 'deleteAll'>Delete all Containers
		<br><input type = 'submit' value = 'Perform my selected Operation'> 
		
		
			</form>''')

	



def execute():
	print("You selected to execute command")
	'''#print(name = 'commandsForm'><h5>Enter command to execute<br></h5>
	#	<button type = 'submit' value = 'Execute Command'>
		)
	print(sb.getoutput('sudo ./execute.py'))
	#cform = cgi.FieldStorage('commandsForm')
	#command = cform.getvalue('command')
	#while command is None:
	#	time.sleep(1)
	#print('command :',command)
	#output = sb.getoutput(command)
	#print(output)'''
	#print("Set-Cookie:ContainerID = {};\r\n".format(operationForm.getvalue('containerID'))
	#print("Set-Cookie:Domain = execute.py'\r\n")
	#print("Content-type
	cmd = "window.localStorage.setItem(\"ContainerID\",{});".format(form.getvalue('containerID'))
	print(cmd)
	print('<script>{}</script>'.format(cmd))
	print('''<script>
		window.location.href = \"execute.py\";
	</script>''')
	
def inspect():
	operation=None
	print("I am here in inspect")
	print(sb.getoutput('sudo docker container inspect {}'.format(form.getvalue('containerID'))))

def createImage():
	print("I am here in create Image")

def delete():
	operation = None
	print("Option to Perform : Delete Selected Container\n")
	print("Deleting ..........\n")
	print(sb.getoutput('sudo docker rm -f {}'.format(form.getvalue('containerID'))))
	print("Selected Container successfully deleted.\n")

def deleteAll():
	operation=None
	print("Deleting all containers.......")
	print(sb.getoutput('sudo docker container rm -f $(sudo docker container ls -a -q)'))

def createNew():
	operation=None
	print("I am here in createNew")
	print('''<script>window.location.href = 'createDockerContainer.py';</script>''')

#operation = ''
displayPage()
operation = form.getvalue('operation')
if operation is not None:
	print('*',operation,'*')
	if operation == 'execute' :
		execute()
		#print('''<script>window.location.href = 'execute.py';</script>''')	
	elif operation == 'inspect' :
		inspect()
	elif operation == 'createImage' :
		createImage()
	elif operation == "delete" :
		print('i am going to call delete\n')
		delete()
	elif operation == "deleteAll":
		deleteAll()
	elif operation == "createNew":
		createNew()
	#operation = None
	#print('operation:',operation)
	print('Kindly refresh the Page to show you the changes.') #getting back the page with all the modifications
	#print('''<script>window.location.href = 'index.py';</script>''')

'''container = "sudo docker run -dit"

imageName = form.getvalue('imageName')

containerName = form.getvalue('containerName')

networkDriver = form.getvalue('networkDriver')

networkName = form.getvalue('networkName')

containerPortNumber = form.getvalue('containerPortNumber')

volume = form.getvalue('volume')


container = container + " --name " + str(containerName)    

if networkName is not None:
    mynetwork = "docker network create --drive " + str(networkDriver) + " " + str(networkName)
    container = container + " --network " + str(networkName)

if containerPortNumber is not None:
    container = container + " --p " + str(containerPortNumber) + ":80"

if volume is not None:
    container = container + " -v /lw:" + str(volume)

container = container + " "+str(imageName)

#print(subprocess.run('date'))

#print(container)

#subprocess.run(container,shell=True)

#print('success')
#print(subprocess.run('docker ps -a',shell=True))

#print(imageName," ",containerName," ",networkDriver," ",networkName," ",containerPortNumber," ",volume);
#print('erroring')

print(subprocess.getoutput('date'))

x = subprocess.getoutput(container)

print(x)'''
#the closing tags			

print('''
		</pre>
		</body>
	</html>
		
		''')

'''print('<pre>',subprocess.getoutput('sudo docker ps -a'),'</pre>')

print("man new problem every day annoys me")'''
