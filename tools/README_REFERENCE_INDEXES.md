# Reference Indexes

В проекте собраны легкие индексы и компактные эталоны по двум тяжелым библиотекам:
- `УНФ`
- `БСП`

## Что использовать

- `tools/build_1c_reference_indexes.py`
  Пересобирает индексы и папку `samples_1c`.

- `tools/find_1c_reference.py`
  Быстрый поиск по уже собранным индексам.

- `tools/reference_indexes/`
  Готовые индексы в `json` и краткие сводки в `md`.

- `samples_1c/`
  Компактные живые эталоны: подчиненный справочник, документ, регистр, отчет, HTTP-сервис, общий модуль и т.д.

## Примеры

```powershell
python .\tools\find_1c_reference.py Номенклатура --library unf --section Catalogs
python .\tools\find_1c_reference.py Owner --library unf --section Catalogs --owners-only
python .\tools\find_1c_reference.py Валюты --library bsp
python .\tools\build_1c_reference_indexes.py
```

## Зачем это нужно

Теперь не нужно каждый раз загружать тяжелые `УНФ` и `БСП` в конфигуратор ради примеров.
Достаточно держать их в проекте как библиотеку-источник, а для повседневной работы использовать индекс и `samples_1c`.
