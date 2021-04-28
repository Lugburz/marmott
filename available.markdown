---
layout: main
title: Disponibles
---

{% include header.html %}
{% assign allcomics = site.data.database.comics | where_exp: "item", "item.hide != true" %}
{% assign comics = allcomics | where_exp: "item", "item.owned == true" | sort: "name" %}

Ici c'est toutes les BDs que je mets à disposition. Elles ne sont pas toutes au boulot, me demander au besoin.

<div id="comics-list">
{% include comics_list.html %}
</div>