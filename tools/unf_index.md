# УНФ быстрый индекс

Файл сгенерирован скриптом `tools/index_unf.py`.

## Как использовать

1. Открыть `tools/unf_index.json` для машинного поиска по объектам.
2. Искать по имени объекта, наличию владельцев, форм и модулей.
3. Для подчиненных справочников смотреть поля `owners` и `has_standard_owner`.

## Подчиненные справочники

- `БанковскиеКартыКонтрагентов`
  xml: `УНФ/Catalogs/БанковскиеКартыКонтрагентов.xml`
  owners: `Catalog.ФизическиеЛица`
  standard owner attr: `True`
- `БанковскиеСчета`
  xml: `УНФ/Catalogs/БанковскиеСчета.xml`
  owners: `Catalog.Организации, Catalog.Контрагенты, Catalog.ФизическиеЛица`
  standard owner attr: `True`
- `ВерсииПоставляемыхРасширений`
  xml: `УНФ/Catalogs/ВерсииПоставляемыхРасширений.xml`
  owners: `Catalog.ПоставляемыеРасширения`
  standard owner attr: `True`
- `ВерсииФайлов`
  xml: `УНФ/Catalogs/ВерсииФайлов.xml`
  owners: `Catalog.Файлы`
  standard owner attr: `True`
- `ВидыДеятельностиЕНВД`
  xml: `УНФ/Catalogs/ВидыДеятельностиЕНВД.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `ВидыЦенКонтрагентов`
  xml: `УНФ/Catalogs/ВидыЦенКонтрагентов.xml`
  owners: `Catalog.Контрагенты`
  standard owner attr: `True`
- `ВиртуальныеКаталогиТоваровМагазиновСоцСетей`
  xml: `УНФ/Catalogs/ВиртуальныеКаталогиТоваровМагазиновСоцСетей.xml`
  owners: `ExchangePlan.ИнтеграцияСМагазинамиСоцСетей`
  standard owner attr: `True`
- `ДисконтныеКарты`
  xml: `УНФ/Catalogs/ДисконтныеКарты.xml`
  owners: `Catalog.ВидыДисконтныхКарт`
  standard owner attr: `True`
- `ДоверенностиНалогоплательщика`
  xml: `УНФ/Catalogs/ДоверенностиНалогоплательщика.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `ДоговорыКонтрагентов`
  xml: `УНФ/Catalogs/ДоговорыКонтрагентов.xml`
  owners: `Catalog.Контрагенты, Catalog.Организации`
  standard owner attr: `True`
- `ЕдиницыИзмерения`
  xml: `УНФ/Catalogs/ЕдиницыИзмерения.xml`
  owners: `Catalog.Номенклатура, Catalog.КатегорииНоменклатуры, Catalog.НаборыЕдиницИзмерения`
  standard owner attr: `True`
- `ЗаявленияОбОтзывеМЧДФНС`
  xml: `УНФ/Catalogs/ЗаявленияОбОтзывеМЧДФНС.xml`
  owners: `Catalog.МашиночитаемыеДоверенностиФНС`
  standard owner attr: `True`
- `ЗначенияКатегорийНовостей`
  xml: `УНФ/Catalogs/ЗначенияКатегорийНовостей.xml`
  owners: `ChartOfCharacteristicTypes.КатегорииНовостей`
  standard owner attr: `True`
- `ЗначенияРеквизитовКТРУ`
  xml: `УНФ/Catalogs/ЗначенияРеквизитовКТРУ.xml`
  owners: `ChartOfCharacteristicTypes.РеквизитыКТРУ`
  standard owner attr: `True`
- `ЗначенияСвойствОбъектов`
  xml: `УНФ/Catalogs/ЗначенияСвойствОбъектов.xml`
  owners: `ChartOfCharacteristicTypes.ДополнительныеРеквизитыИСведения`
  standard owner attr: `True`
- `ЗначенияСвойствОбъектовИерархия`
  xml: `УНФ/Catalogs/ЗначенияСвойствОбъектовИерархия.xml`
  owners: `ChartOfCharacteristicTypes.ДополнительныеРеквизитыИСведения`
  standard owner attr: `True`
- `ЗначенияХарактеристикКТРУ`
  xml: `УНФ/Catalogs/ЗначенияХарактеристикКТРУ.xml`
  owners: `Catalog.ХарактеристикиКТРУ`
  standard owner attr: `True`
- `ЗоныТарифыДоставки`
  xml: `УНФ/Catalogs/ЗоныТарифыДоставки.xml`
  owners: `Catalog.СлужбыДоставки`
  standard owner attr: `True`
- `ИнтервалыДоставки`
  xml: `УНФ/Catalogs/ИнтервалыДоставки.xml`
  owners: `Catalog.СлужбыДоставки`
  standard owner attr: `True`
- `КассыККМ`
  xml: `УНФ/Catalogs/КассыККМ.xml`
  owners: `Catalog.Организации, Catalog.СтруктурныеЕдиницы`
  standard owner attr: `True`
- `КолонкиКалендарейСотрудников`
  xml: `УНФ/Catalogs/КолонкиКалендарейСотрудников.xml`
  owners: `Catalog.КалендариСотрудников`
  standard owner attr: `False`
- `КомплектацииНоменклатуры`
  xml: `УНФ/Catalogs/КомплектацииНоменклатуры.xml`
  owners: `Catalog.Номенклатура`
  standard owner attr: `True`
- `КонтактыЛидов`
  xml: `УНФ/Catalogs/КонтактыЛидов.xml`
  owners: `Catalog.Лиды`
  standard owner attr: `True`
- `ЛицензииПоставщиковАлкогольнойПродукции`
  xml: `УНФ/Catalogs/ЛицензииПоставщиковАлкогольнойПродукции.xml`
  owners: `Catalog.Контрагенты`
  standard owner attr: `True`
- `ЛицензионныеКарточкиТранспортныхСредств`
  xml: `УНФ/Catalogs/ЛицензионныеКарточкиТранспортныхСредств.xml`
  owners: `Catalog.ТранспортныеСредства`
  standard owner attr: `True`
- `МашиночитаемыеДоверенностиРаспределенныйРеестр`
  xml: `УНФ/Catalogs/МашиночитаемыеДоверенностиРаспределенныйРеестр.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `НоменклатураПоставщиков`
  xml: `УНФ/Catalogs/НоменклатураПоставщиков.xml`
  owners: `Catalog.Контрагенты`
  standard owner attr: `True`
- `ОснованияУвольненияПользовательские`
  xml: `УНФ/Catalogs/ОснованияУвольненияПользовательские.xml`
  owners: `Catalog.ОснованияУвольнения`
  standard owner attr: `True`
- `ПартииНоменклатуры`
  xml: `УНФ/Catalogs/ПартииНоменклатуры.xml`
  owners: `Catalog.Номенклатура`
  standard owner attr: `True`
- `Патенты`
  xml: `УНФ/Catalogs/Патенты.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `ПодразделенияОрганизаций`
  xml: `УНФ/Catalogs/ПодразделенияОрганизаций.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `ПочтовыеЯщикиУчетныхЗаписей`
  xml: `УНФ/Catalogs/ПочтовыеЯщикиУчетныхЗаписей.xml`
  owners: `Catalog.УчетныеЗаписиЭлектроннойПочты`
  standard owner attr: `True`
- `ПунктыВыдачиЗаказа`
  xml: `УНФ/Catalogs/ПунктыВыдачиЗаказа.xml`
  owners: `Catalog.СлужбыДоставки`
  standard owner attr: `True`
- `РегистрацииВНалоговомОргане`
  xml: `УНФ/Catalogs/РегистрацииВНалоговомОргане.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `РегистрацииВОрганеСтатистики`
  xml: `УНФ/Catalogs/РегистрацииВОрганеСтатистики.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `СамостоятельныеКлассификационныеЕдиницы`
  xml: `УНФ/Catalogs/СамостоятельныеКлассификационныеЕдиницы.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `СерииНоменклатуры`
  xml: `УНФ/Catalogs/СерииНоменклатуры.xml`
  owners: `Catalog.Номенклатура`
  standard owner attr: `True`
- `СкладыСлужбДоставки`
  xml: `УНФ/Catalogs/СкладыСлужбДоставки.xml`
  owners: `Catalog.СлужбыДоставки`
  standard owner attr: `True`
- `Спецификации`
  xml: `УНФ/Catalogs/Спецификации.xml`
  owners: `Catalog.Номенклатура`
  standard owner attr: `True`
- `СпецификацииМП`
  xml: `УНФ/Catalogs/СпецификацииМП.xml`
  owners: `Catalog.ТоварыМП`
  standard owner attr: `True`
- `ТипыПисемОбменСБанками`
  xml: `УНФ/Catalogs/ТипыПисемОбменСБанками.xml`
  owners: `Catalog.НастройкиОбменСБанками`
  standard owner attr: `True`
- `ТорговыеТочки`
  xml: `УНФ/Catalogs/ТорговыеТочки.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `УчетныеЗаписиDSS`
  xml: `УНФ/Catalogs/УчетныеЗаписиDSS.xml`
  owners: `Catalog.ЭкземплярыСервераDSS`
  standard owner attr: `True`
- `ХарактеристикиКТРУ`
  xml: `УНФ/Catalogs/ХарактеристикиКТРУ.xml`
  owners: `Catalog.КТРУ`
  standard owner attr: `True`
- `ХарактеристикиНоменклатуры`
  xml: `УНФ/Catalogs/ХарактеристикиНоменклатуры.xml`
  owners: `Catalog.Номенклатура, Catalog.КатегорииНоменклатуры`
  standard owner attr: `True`
- `ШаблоныНаименований`
  xml: `УНФ/Catalogs/ШаблоныНаименований.xml`
  owners: `Catalog.КатегорииНоменклатуры`
  standard owner attr: `True`
- `ШтатноеРасписание`
  xml: `УНФ/Catalogs/ШтатноеРасписание.xml`
  owners: `Catalog.Организации`
  standard owner attr: `True`
- `Ячейки`
  xml: `УНФ/Catalogs/Ячейки.xml`
  owners: `Catalog.СтруктурныеЕдиницы`
  standard owner attr: `True`

## Разделы

- `Catalogs`: 674 объектов
- `Documents`: 302 объектов
- `AccumulationRegisters`: 126 объектов
- `InformationRegisters`: 1050 объектов
- `Reports`: 344 объектов
- `HTTPServices`: 16 объектов
- `CommonModules`: 2986 объектов
- `ChartsOfCharacteristicTypes`: 9 объектов
- `DefinedTypes`: 551 объектов
