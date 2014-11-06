#!/usr/bin/python
import os


stringofnames = os.environ['QUERY_STRING']
namepairs = stringofnames.split('=')


if stringofnames == "":
	page = """
	<!DOCTYPE html>
	<html>
	<head>
		<title></title>
	</head>
		<body>
			<form method="get" action="cgi-bin/hello2.py">
				<label>Enter your name</label>
				<input type="text" name="thename" value="Nothing"></input>			
				<input type="submit"></input>

			</form>
		</body>
	</html>
	"""
	print page
else:
	
	pageheader = """

	<!DOCTYPE html>
	Header

	"""
	formpage = """
	<html>
	<head>
		
		<title></title>

	</head>
		<body>
			<form method="get" action="cgi-bin/hello2.py">
				<label>Enter your name</label>
				<input type="text" name="thename" value="Nothing"></input>			
				<input type="submit"></input>

			</form>
			<h1>Hello, %s</h1>
		</body>
	</html>
	""" % namepairs[1]
	print formpage

