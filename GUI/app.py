from tkinter import *
from get_request import get_news_by_key

#import JSON
from tkinter.filedialog import asksaveasfile

window = Tk()
window.geometry('900x600')
window.title('Дайте деняк')


t_n1 = StringVar()
text_n1 = StringVar
t_n2 = StringVar()
t_n3 = StringVar()

def check(*args):
    keyword = requ_con.get()
    news = get_news_by_key(keyword)

    print(keyword, type(keyword))
    text_1.delete(1.0, END)
    text_1.insert(1.0, news['text'])
    t_n1.set(news['title'])
    #print(news)


requ = Label(text= 'Введите ключевое слово', master= window)
requ_con = Entry(master = window)

text_1 = Text(height=5,master=window)
label_1 = Label(text= "Новость 1",master= window, textvariable=t_n1)
text_2 = Text(height=5,master=window)
label_2 = Label(text= "Новость 2",master= window, textvariable=t_n2)
text_3 = Text(height=5,master=window)
label_3 = Label(text= "Новость 3",master= window, textvariable=t_n3)
submit = Button(window,text='Запросить новости', command= check).grid(row=3, column=0)



#,command = check

test = 1

#def writeToJSONFile(path, fileName, data):
#        json.dump(data, path)

#path = './'

'''
def check():
    a = Name.get()
    b = test * int(Age.get())
    c = Role.get()
    print(a)
    print(b)
    print(c)
    data = {}
    data['Name'] = a
    data['Age'] = b
    data['Role'] = c
    files = [('JSON File', '*.json')]
    fileName='IOTEDU'
    filepos = asksaveasfile(filetypes = files,defaultextension = json,initialfile='IOTEDU')
    writeToJSONFile(filepos, fileName, data)
'''

text_1.grid(row=0, column=0)
text_2.grid(row=1,column=0)
text_3.grid(row=2,column=0)
label_1.grid(row=0, column=1)
label_2.grid(row=1, column=1)
label_3.grid(row=2, column=1)
requ.grid(row = 5, column= 1)
requ_con.grid(row= 4, column=1)

mainloop()