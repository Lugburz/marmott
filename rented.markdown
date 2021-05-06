---
layout: main
title: Empruntés
---

{% include header.html %}
{% assign allcomics = site.data.database.comics | where_exp: "item", "item.hide != true" %}
{% assign comics = allcomics | where_exp: "item", "item.rented_by != null" | sort_natural: "name" %}

Ce qu'on m'a emprunté.

<div id="comics-list">
{% include comics_list.html %}
</div>