# Завдання   
Варіант16: Побудова моделі для класифікації з використанням Random Forest:
Реалізувати класифікацію за допомогою алгоритму Random Forest,
використовуючи дані про соціо-економічні показники.

# Опис Random forest  
Random forest - це ансамблевий алгоритм класифікації та регресії   

Даний метод машинного навчання будує множину дерев рішень і об'єднує їх результати для підвищення точності та стабільності прогнозу.  

# Опис програмної реалізації  

Імпорт бібліотек:  
pandas - для роботи з таблицями (DataFrame)  
train_test_split - розділення даних на навчальні та тестові  
RandomForestClassifier - модель Random Forest для класифікації  
LabelEncoder - перетворення текстових даних у числа  

<p align="center"><img width="532" height="113" alt="image" src="https://github.com/user-attachments/assets/d183df1d-b512-4dff-af9e-8194ec246db9" /></p>  

Створюється об'єкт людини, для якої у подальшому буде передбачено дохід та перетворюється у датафрейм.

<p align="center"><img width="556" height="443" alt="image" src="https://github.com/user-attachments/assets/a1d13b60-512e-44db-96e4-6b57710e5bba" /></p>  

Наступним кроком розглядається датасет, доступний за посиланням https://archive.ics.uci.edu/dataset/2/adult. Він містить соціально-економічні дані про людей, зокрема вік, освіту, зайнятість та інші характеристики, а також інформацію про рівень їхнього доходу.  

<p align="center"><img width="924" height="191" alt="image" src="https://github.com/user-attachments/assets/2875e0d1-2de0-4c3d-90e8-1fc8545cadaa" /></p>  

Так як багато параметрів мають строковий тип, відбувається їх перетворення за допомогою LabelEncoder в числовий тип.  

<p align="center"><img width="576" height="193" alt="image" src="https://github.com/user-attachments/assets/ec07f610-0f94-41c0-8460-0a467d61e58d" /></p>

Наступним кроком відбувається поділ на ознаки та цільову змінну. Цільовою змінною є дохід.  

<p align="center"><img width="373" height="68" alt="image" src="https://github.com/user-attachments/assets/ee5dd251-5e90-49a1-97ea-77fd406f5f59" /></p>

Після розбиття даних створюється модель з максимальною глибиною дерева 20 та з випадковістю 0, після чого відбувається її навчання. Дані діляться так 80% для навчання та 20% для тестування моделі. Вивід точності. 

<p align="center"><img width="879" height="144" alt="image" src="https://github.com/user-attachments/assets/6072b91c-132d-4cd0-ba09-c1feec41c2b7" /></p>

В кінці дані об'єкта людини переводяться у той самий формат, що й навчальні та відбувається прогнозування після чого виводиться зпрогнозований дохід.  

<p align="center"><img width="720" height="216" alt="image" src="https://github.com/user-attachments/assets/4164ed5c-5e03-45e0-a614-93a1f0e1863b" /></p>
 

# Результат
Точність моделі: 86.58%  
Прогноз: >50K  
