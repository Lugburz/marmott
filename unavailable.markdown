---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: main
---

{% include header.html %}

Ici c'est toutes les BDs qu'on m'a prêté ou que je ne compte pas mettre à disposition pour une raison ou pour une autre.

<div id="comics-list">
{% assign comics = site.data.database.comics | where_exp: "item", "item.owned == false and item.hide != true" | sort: "name" %}
{% include comics_list.html %}
</div>