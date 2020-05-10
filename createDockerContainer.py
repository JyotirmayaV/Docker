#!/usr/bin/python3

import subprocess
print ("Content-type:text/html\r\n\r\n")

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 


def displayPage():
	print('''
	<html>
	<head>
		<style>
			table {
			  font-family: arial, sans-serif;
			  border-collapse: collapse;
			  width: 100%;
			}

			td, th {
			  border: 1px solid #dddddd;
			  text-align: left;
			  padding: 8px;
			}
		</style>
	</head>

	<body>

		<center><h1>Create a New Docker Container</h1></center>
		 
		<form action="createDockerContainer.py" method="post">
				<table align="center">
					
					<tr>
						<th>Requirement</th>
						<th>User Input</th>
						<th>Hint to help User</th>'
					</tr>
					<tr>
						<td>Docker Image Name</td>
						<td><input type = "text" placeholder="Enter Image Name" name='imageName' required></td>
						<td>You can search the image name from <a href='https://hub.docker.com'>Docker Images</a></td>
					</tr>

					<tr>
						<td>Docker Container Name</td>
						<td><input type = "text" placeholder="Enter Container Name" name='containerName' required></td>
						<td>
							This name is very Important as it shall only be used to reference this container in future.<br>
							Give the names which have not been used till now.<br>
							<!--For seeing names used, Click here <a href=''>Docker Inspect</a>-->
						</td>
					</tr>

					<tr>
						<td>Docker Network Driver</td>
						<td>
							<input type="radio" name="networkDriver" value="bridge" checked>bridge<br>
  							<input type="radio" name="networkDriver" value="host">host<br>
  							<input type="radio" name="networkDriver" value="null">null
  						</td>
  						<td>
  							The bridge network driver is used to provide you with switch and router access.<br>
  							The host network driver is used to get the IP directly of the base OS.<br>
  							The null network driver is used to create an isolated container devoid of any outer network connection.
  						</td>
  					</tr>

  					<tr>
						<td>Docker Network Name (Optional)</td>
						<td><input type = "text" placeholder="Enter Network Name" name='networkName'></td>
						<td>
							Give a name to your network.<br>
							If no name is provided by you, a default name corresponding to the above selected driver shall be selected.<br>
							Its helpful if you want containers in a specific network.<!--To see all networks cretaed till now, Click here <a href=''>Docker Network Name</a>-->
						</td>
					</tr>

					<tr>
						<td>Port Number (Optional)</td>
						<td><input type = "number" placeholder="Enter Port Number" name='containerPortNumber'></td>
						<td>
							This is used in case of enabling PAT for exposing the OS.
						</td>
					</tr>

					<tr>
						<td>Volume Name (Optional)</td>
						<td><input type = "txt" placeholder="Enter the volume in base OS" name='volume'></td>
						<td>Specify the volume name along with the location of the volume.<br>
						    Useful in case if you have to link the volume to your docker container to directly use files.
						</td>
					</tr>
				</table><br>

				<input type = "submit" value = "Create a new Container" align="center"/>
		</form>

		<p>Thanks to Vimal Daga Sir.</p>
	''')


displayPage()

# Get data from fields
container = "sudo docker run -dit"

imageName = form.getvalue('imageName')

if imageName is not None :

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

	#print(subprocess.getoutput('date'))

	x = subprocess.getoutput(container)

	print(x)

	#print('<pre>',subprocess.getoutput('sudo docker ps -a'),'</pre>')

	#print("man new problem every day annoys me")
