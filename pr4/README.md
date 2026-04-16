# Завдання:  
Варіант 16: Застосуйте метод головних компонент для виявлення основних факторів, що
впливають на енергоспоживання. Порівняйте з методами кореляційного аналізу.
Візуалізуйте основні компоненти та їх вплив на енергоспоживання.  

# Реалізація:  
Спочатку відбувається імпорт необхідних бібліотек:  
pandas - робота з таблицями  
PCA - метод головних компонент  
StandardScaler - нормалізація даних  
matplotlib, seaborn - побудова графіків  
numpy - математичні обчислення  

<p align="center"><img width="557" height="152" alt="image" src="https://github.com/user-attachments/assets/c71a0f8b-1096-4dd9-81e2-b351fae7c23a" /></p>  

Наступним кроком відбувається завантаження та розділенння даних на ознаки і ціль. Для коректної роботи PCA відбувається стандартизація без цього PCA працює неправильно, бо ознаки мають різні одиниці виміру. 
Далі відбувається створення об'єкту PCA, який потрібен для перетворення даних у новий простір головних компонент. Виводиться пояснена дисперсія, яка показує, яку частку інформації пояснює кожна компонента.
Вивід графіку накопиченої дисперсії, який показує, скільки компонент достатньо для збереження інформації.  

<p align="center"><img width="763" height="508" alt="image" src="https://github.com/user-attachments/assets/588980b9-c573-44b9-9de6-acc1cd348a3e" /></p>  

Після виводу графіку відбувається зменшення даних до 2 вимірів. Створюється новий датафрейм для об'єднання результатів PCA з цільовою змінною. Наступним кроком відбувається кореляція PCA з цільовою змінною, яка показує, наскільки PC1 і PC2 пов'язані з енерноспоживанням. Для візуалізації відображаться дані у 2д це дає візуальне розуміння залежностей.  

<p align="center"><img width="761" height="392" alt="image" src="https://github.com/user-attachments/assets/21ec5aa2-8f1c-4b14-9ae7-cf91f3c44239" /></p>  

Наступним кроком виводиться матриця компонент, вона показує вагу кожної ознаки в кожній компоненті. Heatmap компонент, візуалізує внесок ознак, що дає легко побачити найважливіші фактори. У циклі виводяться топ фактори. Далі відбувається кореляція матриці, яка обчислює залежності між усіма змінними. Heatmap кореляції, який візуалізує кореляції. В кінці відбувається кореляція з цільовою змінною та вивід результатів.

<p align="center"><img width="869" height="694" alt="image" src="https://github.com/user-attachments/assets/076af723-8415-469d-8d57-390d86c8b1a3" /></p>   

# Результати:
Explained variance ratio: [0.96425348 0.01580867 0.00901458 0.00467854 0.00372207 0.00252267]  
Сума поясненої варіації: 1.0000000000000002  
<p align="center"><img width="970" height="634" alt="image" src="https://github.com/user-attachments/assets/0d61a30a-7ecc-4923-834d-df0730bbbff4" /></p>   
Кореляція PC з energy_consumption:  
PC1                   0.995111  
PC2                  -0.029464  
energy_consumption    1.000000  
Name: energy_consumption, dtype: float64  
<p align="center"><img width="926" height="725" alt="image" src="https://github.com/user-attachments/assets/cc079da3-a18d-4169-a95e-2e83d92d69db" /></p>   

<p align="center"><img width="1243" height="680" alt="image" src="https://github.com/user-attachments/assets/810663e7-2fc1-444e-ab31-8caeb43a0ef9" /></p>   
Топ фактори для PC1:  
num_devices           0.412447  
population_density    0.411661  
industrial_load       0.410380  
working_hours         0.410364  
temperature           0.398982  
humidity             -0.405496  
Name: PC1, dtype: float64  

Топ фактори для PC2:  
temperature           0.907548  
humidity              0.301518  
num_devices          -0.133744  
population_density   -0.138708  
industrial_load      -0.155401  
working_hours        -0.155459  
<p align="center"><img width="1566" height="921" alt="image" src="https://github.com/user-attachments/assets/f06eb85a-a063-43e7-a03e-05ced7ba1069" /></p>   

ПОРІВНЯННЯ:  
Найбільш впливові ознаки за кореляцією:  
energy_consumption    1.000000  
num_devices           0.994679  
industrial_load       0.993289  
population_density    0.985352  
working_hours         0.980488  
Name: energy_consumption, dtype: float64  

Найбільш впливові ознаки за PCA (PC1):  
num_devices           0.412447  
population_density    0.411661  
industrial_load       0.410380  
working_hours         0.410364  
humidity              0.405496  
Name: PC1, dtype: float64  
# Висновок:    
Метод головних компонент показав, що перша компонента (PC1) пояснює 96.43% дисперсії та має дуже сильний зв’язок з енергоспоживанням (0.995), тобто саме вона відображає основні фактори впливу. Найбільш значущими факторами є num_devices, industrial_load, population_density, working_hours, temperature, тоді як humidity має обернений вплив. Результати кореляційного аналізу підтвердили ці висновки, показавши сильні залежності між цими ознаками та енергоспоживанням. Отже, обидва методи дають узгоджені результати, але PCA дозволяє узагальнити вплив факторів в одній головній компоненті.  
