---
layout: main
title: Indisponibles
---

{% include header.html %}
{% assign allcomics = site.data.database.comics | where_exp: "item", "item.hide != true" %}
{% assign comics = allcomics | where_exp: "item", "item.owned == false" | sort: "name" %}

Ici c'est toutes les BDs qu'on m'a prêté ou que je ne compte pas mettre à disposition pour une raison ou pour une autre.

<div id="comics-list">
{% include comics_list.html %}
</div>