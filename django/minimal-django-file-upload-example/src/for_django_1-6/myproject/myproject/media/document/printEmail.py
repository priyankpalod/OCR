flag = "0"   # to check if found the domain (1 => found)
flag2 = "0"  # to check if we were in a email block (1=>yes) or we have a seperate email (0 => seperate email)
emails = []
emails_printed = []
directory = "/var/www/html/OCR++/django/minimal-django-file-upload-example/src/for_django_1-6/myproject/myproject/media/documents/"
filetoRead = directory + "input_mail_parse.txt"
outfile = open(directory + "input_Allmails.txt",'w')
#outfile = open("/users/user/Desktop/Palod/Allmails.txt",'a')
#outfile.write("<?" + filetoRead.split("_mail_parse.txt")[0] + "?>\n")
with open(filetoRead,'r') as f:
    for line in f:
        abc = line.split()

        if len(abc) >= 1:  # if not a blank line

	        if abc[1] == "1":   #output column
			if abc[0].find('{')!=-1 or abc[0].find('[')!=-1:
			    flag2 = "1"
			if abc[0].find('}')==-1 and abc[0].find(']')==-1:
	        	    emails.append((((abc[0].strip('{')).strip('[')).strip(',')))
			if abc[0].find("}")!=-1:
			    domain = str(abc[0].split('}')[len(abc[0].split('}'))-1])
			    for email in ((((abc[0].strip('{')).strip('[')).strip(',')).split('}')[0]).split(','):	#done since there may
			    	emails.append(email)									#not be spaces b/w ,
	        	    flag = "1"
			    flag2 = "0"
			if abc[0].find("]")!=-1:
			    domain = str(abc[0].split(']')[len(abc[0].split(']'))-1])
			    for email in ((((abc[0].strip('{')).strip('[')).strip(',')).split(']')[0]).split(','):
			    	emails.append(email)
	        	    flag = "1"
			    flag2 = "0"
			if flag == "0" and flag2 == "0" and abc[0].lower().find("permissions@acm.")==-1 and abc[0] not in emails_printed:
			    emails_printed.append(abc[0])
			    outfile.write("\n<email>\n\t" + ((((abc[0].strip(',')).strip('.')).strip(')')).strip(',')).strip(';') + "\n</email>\n")
			if flag == "1":
			    for usernames in emails:
				if usernames == "":
				    continue
				usernames += domain
				usernames = ((usernames.strip('.')).strip(',')).strip(')')
				if usernames not in emails_printed:
				        emails_printed.append(usernames)
				        outfile.write("\n<email>\n\t" + usernames + "\n</email>\n")
			    flag = "0"
	        else:
	        	if abc[0] != "0":
	        		flag = "0"
				del emails[:]

outfile.close()
