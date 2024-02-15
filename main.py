import csv

#extract data from csv
def load_data(filename):
    mylist = []
    with open(filename) as numbers:
        numbers_data = csv.reader(numbers,delimiter=',')
        next(numbers_data) #skip header
        for row in numbers_data:
            mylist.append(row)
        return mylist    

#### Only Chagnge here every transfer ######
#You change here in order to channge the source.
new_list = load_data('test.csv')
emoji = '🐧'





#for 2 numbers
def create_file(name,phone1,phone2):
    name = emoji+name
    phone2 = phone2.replace('-','')
    sample_text = "BEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8:;%s;;;\nFN;CHARSET=UTF-8:%s\nSOUND;X-IRMC-N:;;;;\nTEL;CELL:%s\nTEL;CELL:%s\nEMAIL;HOME:\nADR;HOME:\nX-CLASS:PUBLIC\nX-REDUCTION:\nX-NO:\nX-DCM-HMN-MODE:\nEND:VCARD\n" %(name,name,phone1,phone2)
    file = open("My_new_VCF.vcf","a",encoding="utf-8")
    file.write(sample_text)
    file.close()

# if only one number
def create_file_onenum(name,phone1):
    name = emoji+name
    phone1 = phone1.replace('-','')
    sample_text = "BEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8:;%s;;;\nFN;CHARSET=UTF-8:%s\nSOUND;X-IRMC-N:;;;;\nTEL;CELL:%s\nEMAIL;HOME:\nADR;HOME:\nX-CLASS:PUBLIC\nX-REDUCTION:\nX-NO:\nX-DCM-HMN-MODE:\nEND:VCARD\n" %(name,name,phone1)
    file = open("My_new_VCF.vcf","a",encoding="utf-8")
    file.write(sample_text)
    file.close()


for row in new_list:
    print(row)
    if len(row)==2:
        create_file_onenum(row[0],row[1])
    else:
        create_file(row[0],row[1],row[2])
