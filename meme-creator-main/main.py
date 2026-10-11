#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

text_top = ''
text_bottom = ''
text_top_y = ''
text_bottom_y = ''
selected_color = ''
#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        text_top = request.form['textTop']
        text_bottom = request.form['textBottom']

        # Задание №3. Получаем расположение текста
        text_top_y = request.form['textTop_y']
        text_bottom_y = request.form['textBottom_y']
        selected_color = request.form['color-selector']


        # Задание №3. Получаем цвет текста
        

        return render_template('index.html', 
                               # отображаем выбранное изображение
                               selected_image=selected_image, 

                               # Задание №2. Отображаем текст
                               text_top = text_top,
                               text_bottom = text_bottom,
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y,
                               selected_color = selected_color

                               # Задание №3. Отображаем цвет 
                               
                               
                               #Задание №3. Отоброжаем расположение текста

                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
