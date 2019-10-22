---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---
{% include header.html %}

<div id="comics-list">
{% assign comics = site.data.database.comics | sort: "name" %}
{% include comics_list.html %}
</div>