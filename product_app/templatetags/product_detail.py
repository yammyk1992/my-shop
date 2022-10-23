from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
            <table class="table">
              <tbody>
            """

TABLE_TAIL = """
            </tbody>
               </table>           
            """

TABLE_CONTENT = """
            <tr>
                <td>{name}</td>
                <td>{value}</td>
            </tr>    
                """

PRODUCT_FEATURE = {
    'sport': {
        'Вид спорта': 'kind_of_sport',
        'Материал': 'material',
        'Цвет': 'colour',
        'Страна производства': 'country'
    },
    'tv': {
        'Диагональ': 'diagonal',
        'SMART-TV': 'smart_tv',
        'Дата выпуска модели': 'release',
        'Разрешение': 'resolution'
    },
    'toys': {
        'Возвраст': 'age',
        'Материал': 'material',
        'Дата выпуска модели': 'release',
        'Страна происхождения': 'country',
        'Фирма': 'company'
    },
    'goods': {
        'Название': 'name',
        'Страна происхождения': 'country',
        'Фирма': 'company',
        'Пол': 'sex',
        'Размер': 'size'
    }
}


def get_product_feature(product, model_name):
    table_content = ''
    for name, value in PRODUCT_FEATURE[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_detail(product):
    model_name = product.__class__._meta.model_name
    # превращаем наш тег в полноценный HTML
    return mark_safe(TABLE_HEAD + get_product_feature(product, model_name) + TABLE_TAIL)
