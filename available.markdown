---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---

{% include header.html %}

Ici c'est toutes les BDs que je mets à disposition. Elles ne sont pas toutes au boulot, me demander au besoin.

<div id="comics-list">
{% assign comics = site.data.database.comics | where_exp: "item", "item.owned == true" | sort: "name" %}
{% include comics_list.html %}
</div>