---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---

{% include header.html %}

Par auteur.

<div id="comics-list">
{% assign comics = site.data.database.comics | sort: "author" %}
{% include comics_list.html %}
</div>