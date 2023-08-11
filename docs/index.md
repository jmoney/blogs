# Blogs

## Dev.To

{% for name, blog in list_blogs('jmoney').items() %}

* [{{ name.replace('-', ' ').title() }}]({{ blog.url }}) - {{ blog.description }}

{% endfor %}
