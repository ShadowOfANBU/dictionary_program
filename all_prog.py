#This Program could be use for generating english word dictionary for dictionary attack.
#Its Developed only for research purposes.
#I am not liable for any kind of damage done from that program, please use wisely.

def first_letter_in_uppercase():
	with open('words_alpha.txt','r') as fp:
		i=1
		for line in fp:
			length=len(line)
			if(length>7 and length<17):
				u=line[0].upper()
				my=line.replace(line[0],u,1)
				with open('Crack3.txt','a') as fw:
					fw.write(my)
				fw.close()	

def first_letter_in_uppercase_with_special_cahracters():
	with open('words_alpha.txt','r') as fp:
		i=1
		for line in fp:
			length=len(line)
			if(length>7 and length<17):
				u=line[0].upper()
				my=line.replace(line[0],u,1)
				my=my.rstrip()
				with open('Crack2.txt','a') as fw:
					data=my+"@"+'\n'
					fw.write(data)
					data=my+"#"+'\n'
					fw.write(data)
					data=my+"$"+'\n'
					fw.write(data)
					data=my+"%"+'\n'
					fw.write(data)
					data=my+"&"+'\n'
					fw.write(data)
					data=my+"*"+'\n'
					fw.write(data)
					data=my+"."+'\n'
					fw.write(data)
					data=my+"!"+'\n'
					fw.write(data)
					data=my+":"+'\n'
					fw.write(data)
					data=my+","+'\n'
					fw.write(data)
					data="@"+my+'\n'
					fw.write(data)
					data="#"+my+'\n'
					fw.write(data)
					data="$"+my+'\n'
					fw.write(data)
					data="%"+my+'\n'
					fw.write(data)
					data="&"+my+'\n'
					fw.write(data)
					data="*"+my+'\n'
					fw.write(data)
					data=":"+my+'\n'
					fw.write(data)
					data="."+my+'\n'
					fw.write(data)
					data=","+my+'\n'
					fw.write(data)
					data="!"+my+'\n'
					fw.write(data)
				fw.close()	

def first_letter_in_uppercase_with_special_characters_and_numbers_upto_two_digits():
	with open('words_alpha.txt','r') as fp:
		i=1
		ult=0
		for line in fp:
			length=len(line)
			if(length>7 and length<17):
				u=line[0].upper()
				my=line.replace(line[0],u,1)
				my=my.rstrip()
				j=0
				with open('Crack1.txt','a') as fw:
					while(j<100):
						data=my+"@"+str(j)+'\n'
						fw.write(data)
						data=my+"*"+str(j)+'\n'
						fw.write(data)
						data=my+":"+str(j)+'\n'
						fw.write(data)	
						data=my+"%"+str(j)+'\n'
						fw.write(data)	
						data=my+"&"+str(j)+'\n'
						fw.write(data)	
						data=my+"#"+str(j)+'\n'
						fw.write(data)	
						data=my+"$"+str(j)+'\n'
						fw.write(data)	
						data=my+"!"+str(j)+'\n'
						fw.write(data)	
						data=my+","+str(j)+'\n'
						fw.write(data)
						data=my+"."+str(j)+'\n'
						fw.write(data)
						data="@"+str(j)+my+'\n'
						fw.write(data)
						data="*"+str(j)+my+'\n'
						fw.write(data)	
						data=":"+str(j)+my+'\n'
						fw.write(data)
						data="%"+str(j)+my+'\n'
						fw.write(data)	
						data="&"+str(j)+my+'\n'
						fw.write(data)	
						data="#"+str(j)+my+'\n'
						fw.write(data)	
						data="$"+str(j)+my+'\n'
						fw.write(data)	
						data="!"+str(j)+my+'\n'
						fw.write(data)	
						data=","+str(j)+my+'\n'
						fw.write(data)
						data="."+str(j)+my+'\n'
						fw.write(data)
						j+=1
				fw.close()	

def first_letter_in_uppercase_and_number_upto_two_digit():
	with open('words_alpha.txt','r') as fp:
		i=1
		ult=0
		for line in fp:
			length=len(line)
			if(length>7 and length<17):
				u=line[0].upper()
				my=line.replace(line[0],u,1)
				my=my.rstrip()
				j=0
				with open('Crack5.txt','a') as fw:
					while(j<100):
						data=my+str(j)+'\n'
						fw.write(data)
						data=my+str(j)+'\n'
						fw.write(data)
						data=my+str(j)+'\n'
						fw.write(data)	
						data=my+str(j)+'\n'
						fw.write(data)	
						data=my+str(j)+'\n'
						fw.write(data)	
						data=my+str(j)+'\n'
						fw.write(data)	
						data=my+str(j)+'\n'
						fw.write(data)	
						data=my+str(j)+'\n'
						fw.write(data)	
						data=my+str(j)+'\n'
						fw.write(data)
						data=my+str(j)+'\n'
						fw.write(data)
						data=str(j)+my+'\n'
						fw.write(data)
						data=str(j)+my+'\n'
						fw.write(data)	
						data=str(j)+my+'\n'
						fw.write(data)
						data=str(j)+my+'\n'
						fw.write(data)	
						data=str(j)+my+'\n'
						fw.write(data)	
						data=str(j)+my+'\n'
						fw.write(data)	
						data=str(j)+my+'\n'
						fw.write(data)	
						data=str(j)+my+'\n'
						fw.write(data)	
						data=str(j)+my+'\n'
						fw.write(data)
						data=str(j)+my+'\n'
						fw.write(data)
						j+=1
				fw.close()	
				
					
# Lookalike Characters: a == @, e == 3, i == !, s == $, o == 0
def use_of_lookalike_character():
	with open('words_alpha.txt','r') as fp:
	
		for mack in fp:
			
			i=0
			with open('Crack4.txt','a') as fw:
				length=len(mack)
				if(length>7 and length<17):
					while(i<len(mack)):
						if(mack[i]=='a'):
							mack=mack.replace(mack[i],'@')
							
							i+=1
						elif(mack[i]=='e'):
							mack=mack.replace(mack[i],'3')
							
							i+=1
						elif(mack[i]=='l'):
							mack=mack.replace(mack[i],'I')
							
							i+=1
						elif(mack[i]=='i'):
							mack=mack.replace(mack[i],'!')
							
							i+=1
						elif(mack[i]=='o'):
							mack=mack.replace(mack[i],'0')
							
							i+=1
						elif(mack[i]=='s'):
							mack=mack.replace(mack[i],'s')
							
							i+=1
						else:
							i+=1
					fw.write(mack)
				fw.close()	

			

		    	
				
				
#Just Remove the # from the below lines and use it of dictionary generation for differenct cases.

#first_letter_in_uppercase()

#first_letter_in_uppercase_with_special_cahracters()

#first_letter_in_uppercase_with_special_characters_and_numbers_upto_two_digits()

#first_letter_in_uppercase_and_number_upto_two_digit()

#use_of_lookalike_character()




