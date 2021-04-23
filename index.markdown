---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---
{% include header.html %}
{% assign allcomics = site.data.database.comics | where_exp: "item", "item.hide != true" %}
{% assign comics = allcomics | sort: "name" %}

<div id="comics-list">
{% include comics_list.html %}
</div>