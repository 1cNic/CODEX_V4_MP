# Индекс БСП

Быстрый индекс по библиотеке `БСП`.

## Как использовать

1. Смотри `*.json`, если нужен машинный поиск по объектам.
2. Смотри раздел `samples_1c`, если нужен компактный живой эталон без всей тяжелой конфигурации.
3. Для подчиненных справочников проверяй поля `owners` и `has_standard_owner`.

## Сводка

- `Catalogs`: 70 объектов
- `Documents`: 11 объектов
- `InformationRegisters`: 183 объектов
- `Reports`: 41 объектов
- `WebServices`: 13 объектов
- `CommonModules`: 523 объектов
- `ChartsOfCharacteristicTypes`: 4 объектов
- `DefinedTypes`: 69 объектов
- `DataProcessors`: 69 объектов
- `DocumentJournals`: 2 объектов
- `Enums`: 95 объектов

## Подчиненные справочники

- `ВариантыОтветовАнкет` -> `ChartOfCharacteristicTypes.ВопросыДляАнкетирования`; standard owner: `True`
- `ВерсииФайлов` -> `Catalog.Файлы`; standard owner: `True`
- `ВопросыШаблонаАнкеты` -> `Catalog.ШаблоныАнкет`; standard owner: `True`
- `ЗакладкиВзаимодействий` -> `Catalog.Пользователи`; standard owner: `True`
- `ЗначенияСвойствОбъектов` -> `ChartOfCharacteristicTypes.ДополнительныеРеквизитыИСведения`; standard owner: `True`
- `ЗначенияСвойствОбъектовИерархия` -> `ChartOfCharacteristicTypes.ДополнительныеРеквизитыИСведения`; standard owner: `True`
- `ПапкиЭлектронныхПисем` -> `Catalog.УчетныеЗаписиЭлектроннойПочты`; standard owner: `True`
- `ПравилаОбработкиЭлектроннойПочты` -> `Catalog.УчетныеЗаписиЭлектроннойПочты`; standard owner: `True`
- `УчетныеЗаписиDSS` -> `Catalog.ЭкземплярыСервераDSS`; standard owner: `True`
- `ШаблоныСообщений` -> `Document.ЭлектронноеПисьмоИсходящее`; standard owner: `True`

## Компактные эталоны

- `subordinate_catalog`: `ВариантыОтветовАнкет` (Catalogs)
- `catalog_with_form`: `Валюты` (Catalogs)
- `document`: `АктОбУничтоженииПерсональныхДанных` (Documents)
- `information_register`: `АдминистративнаяИерархия` (InformationRegisters)
- `report`: `АнализВерсийОбъектов` (Reports)
- `common_module`: `GoogleПереводчик` (CommonModules)
- `chart_of_characteristic_types`: `ВопросыДляАнкетирования` (ChartsOfCharacteristicTypes)
