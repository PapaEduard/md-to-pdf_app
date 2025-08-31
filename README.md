# Simple converter markdown -> pdf
Простое приложение для конвертации файлов markdown в pdf. В качестве языка программирования используется python. Не предполагает наличия веб-сервера, а значит не слушает никакие порты.
Запускается
```bash
python app.py ./inputs/main.md ./results/file1.pdf
```
## Задачи
1) Написать Dockerfile для формирования среды под приложение\
потребуются deb пакеты `libpango-1.0-0 libharfbuzz-dev libpangoft2-1.0-0` и python пакеты из `requirements.txt`
2) Написать к нему compose.yml для запуска \
потребуется прокинуть через bind mount
- папку `./results` на хосте в папку `/src/results` в контейнере
- папку `./inputs` на хосте в папку `/src/inputs` в контейнере
3) Создать job (pipeline), который будет 
  - собирать docker image для приложения, если в параметрах был поставлен чек-бокс "Build new image"
  - пушить новый image в docker hub
  - обновлять репозиторий из ветки, указанной в параметрах
  - запускать контейнер с command для конвертации файла md, который был передан как параметр сборке (файл должен быть закоммичен в git в директорию `inputs`)
  - сохранять как артефакт в Jenkins итоговый pdf файл
 
<details>
  <summary>спойлер к "запускать контейнер с command для конвертации файла"</summary>
  
  ```bash
  docker run -d  -v ./inputs:/src/inputs -v ./results:/src/results md-to-pdf python app.py ./inputs/main.md ./results/main.pdf
  ```
  
</details>

