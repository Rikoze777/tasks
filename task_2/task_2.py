from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, lit


def get_product_category_pairs(spark, products_df, categories_df):
    # Создаем датафрейм связей продуктов и категорий
    product_category_links = products_df.join(
        broadcast(categories_df),
        products_df["category_id"] == categories_df["id"],
        "left_outer",
    )

    # Выбираем необходимые колонки, указывая датафрейм для каждого столбца
    product_category_pairs = product_category_links.select(
        products_df["name"].alias("Имя продукта"),
        categories_df["name"].alias("Имя категории"),
    )

    # Получаем продукты без категорий и добавляем столбец 'Имя категории' с null значениями
    products_without_categories = product_category_links.filter(
        categories_df["name"].isNull()
    ).select(
        products_df["name"].alias("Имя продукта"), lit(None).alias("Имя категории")
    )

    # Объединяем результаты с одинаковым количеством столбцов
    result = product_category_pairs.union(products_without_categories).distinct()

    return result


spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

milk_products = spark.createDataFrame(
    [
        (1, "Молоко", 1),
        (2, "Сыр", 2),
        (3, "Йогурт", 3),
        (4, "Творог", None),  # Продукт без категории
    ],
    ["id", "name", "category_id"],
)

meat_products = spark.createDataFrame(
    [
        (1, "Говядина", 4),
        (2, "Свинина", 5),
        (3, "Курица", 6),
        (4, "Индейка", None),  # Продукт без категории
    ],
    ["id", "name", "category_id"],
)

categories = spark.createDataFrame(
    [
        (1, "Молочные продукты"),
        (2, "Сыры"),
        (3, "Йогурты"),
        (4, "Мясо говядины"),
        (5, "Мясо свинины"),
        (6, "Мясо птицы"),
    ],
    ["id", "name"],
)

# Вызов метода для молочной продукции
result_df_milk = get_product_category_pairs(spark, milk_products, categories)
print("Молочная продукция:")
result_df_milk.show()

# Вызов метода для мясной продукции
result_df_meat = get_product_category_pairs(spark, meat_products, categories)
print("Мясная продукция:")
result_df_meat.show()
