# Индекс УНФ

Быстрый индекс по библиотеке `УНФ`.

## Как использовать

1. Смотри `*.json`, если нужен машинный поиск по объектам.
2. Смотри раздел `samples_1c`, если нужен компактный живой эталон без всей тяжелой конфигурации.
3. Для подчиненных справочников проверяй поля `owners` и `has_standard_owner`.

## Сводка

- `Catalogs`: 674 объектов
- `Documents`: 302 объектов
- `AccumulationRegisters`: 126 объектов
- `InformationRegisters`: 1050 объектов
- `Reports`: 344 объектов
- `HTTPServices`: 16 объектов
- `WebServices`: 18 объектов
- `CommonModules`: 2986 объектов
- `ChartsOfCharacteristicTypes`: 9 объектов
- `DefinedTypes`: 551 объектов
- `DataProcessors`: 324 объектов
- `DocumentJournals`: 46 объектов
- `Enums`: 1067 объектов

## Подчиненные справочники

- `БанковскиеКартыКонтрагентов` -> `Catalog.ФизическиеЛица`; standard owner: `True`
- `БанковскиеСчета` -> `Catalog.Организации, Catalog.Контрагенты, Catalog.ФизическиеЛица`; standard owner: `True`
- `ВерсииПоставляемыхРасширений` -> `Catalog.ПоставляемыеРасширения`; standard owner: `True`
- `ВерсииФайлов` -> `Catalog.Файлы`; standard owner: `True`
- `ВидыДеятельностиЕНВД` -> `Catalog.Организации`; standard owner: `True`
- `ВидыЦенКонтрагентов` -> `Catalog.Контрагенты`; standard owner: `True`
- `ВиртуальныеКаталогиТоваровМагазиновСоцСетей` -> `ExchangePlan.ИнтеграцияСМагазинамиСоцСетей`; standard owner: `True`
- `ДисконтныеКарты` -> `Catalog.ВидыДисконтныхКарт`; standard owner: `True`
- `ДоверенностиНалогоплательщика` -> `Catalog.Организации`; standard owner: `True`
- `ДоговорыКонтрагентов` -> `Catalog.Контрагенты, Catalog.Организации`; standard owner: `True`
- `ЕдиницыИзмерения` -> `Catalog.Номенклатура, Catalog.КатегорииНоменклатуры, Catalog.НаборыЕдиницИзмерения`; standard owner: `True`
- `ЗаявленияОбОтзывеМЧДФНС` -> `Catalog.МашиночитаемыеДоверенностиФНС`; standard owner: `True`
- `ЗначенияКатегорийНовостей` -> `ChartOfCharacteristicTypes.КатегорииНовостей`; standard owner: `True`
- `ЗначенияРеквизитовКТРУ` -> `ChartOfCharacteristicTypes.РеквизитыКТРУ`; standard owner: `True`
- `ЗначенияСвойствОбъектов` -> `ChartOfCharacteristicTypes.ДополнительныеРеквизитыИСведения`; standard owner: `True`
- `ЗначенияСвойствОбъектовИерархия` -> `ChartOfCharacteristicTypes.ДополнительныеРеквизитыИСведения`; standard owner: `True`
- `ЗначенияХарактеристикКТРУ` -> `Catalog.ХарактеристикиКТРУ`; standard owner: `True`
- `ЗоныТарифыДоставки` -> `Catalog.СлужбыДоставки`; standard owner: `True`
- `ИнтервалыДоставки` -> `Catalog.СлужбыДоставки`; standard owner: `True`
- `КассыККМ` -> `Catalog.Организации, Catalog.СтруктурныеЕдиницы`; standard owner: `True`
- `КолонкиКалендарейСотрудников` -> `Catalog.КалендариСотрудников`; standard owner: `False`
- `КомплектацииНоменклатуры` -> `Catalog.Номенклатура`; standard owner: `True`
- `КонтактыЛидов` -> `Catalog.Лиды`; standard owner: `True`
- `ЛицензииПоставщиковАлкогольнойПродукции` -> `Catalog.Контрагенты`; standard owner: `True`
- `ЛицензионныеКарточкиТранспортныхСредств` -> `Catalog.ТранспортныеСредства`; standard owner: `True`

## Компактные эталоны

- `subordinate_catalog`: `БанковскиеКартыКонтрагентов` (Catalogs)
- `catalog_with_form`: `АвтоматическиеСкидки` (Catalogs)
- `document`: `АвансовыйОтчет` (Documents)
- `accumulation_register`: `АвансовыеПлатежиИностранцевПоНДФЛ` (AccumulationRegisters)
- `information_register`: `АбонентыЭДО` (InformationRegisters)
- `report`: `ABCXYZАнализПродаж` (Reports)
- `http_service`: `Chatbot` (HTTPServices)
- `common_module`: `GoogleПереводчик` (CommonModules)
- `chart_of_characteristic_types`: `АналитикаДоходовИРасходов` (ChartsOfCharacteristicTypes)
