#Импорт
from flask import Flask, render_template, request



#pip install playsound3
app = Flask(__name__)

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 


#Первая страница
@app.route('/')
def main():      
    return render_template('main.html')


#Вторая страница
@app.route('/1')
def causes():
    return render_template(
                            'causes.html', 
                           
                           )

#Третья страница
@app.route('/2')
def aftermaths():
    return render_template(
                            'aftermaths.html',                           
                                                       
                           )

#Расчет
@app.route('/3')
def solutions():
    return render_template('solutions.html', 
                            
                        )
#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    mail = request.form['mail']
    address = request.form['address']
    date = request.form['date']
    with open('form.txt', 'a',) as f:
        f.write(name + '\
    ')
    with open('form.txt', 'a',) as f:
        f.write(mail + '\
    ')
    with open('form.txt', 'a',) as f:
        f.write(address + '\
    ')
    with open('form.txt', 'a',) as f:
        f.write(date + '\
    ')   
    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           mail = mail,
                           address = address,
                           date = date
                           )

app.run(debug=True)